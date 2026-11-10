# Provenance Guard

Provenance Guard is a Flask-based web service that analyzes writing and estimates whether it shows patterns associated with AI-generated or human-written text.

The system uses two different signals, combines their scores, provides a readable prediction, and allows writers to appeal a decision.

**How to run this project:** See [RUNNING.md](RUNNING.md).

## What This Does

When a user submits text, the service follows these steps:

1. The user sends text and a creator ID to the `/submit` endpoint.

2. The Flask application validates the input.

3. `detector.py` uses a local GPT-2 model to calculate a model signal.

4. `stylometry.py` analyzes sentence length variation, vocabulary diversity, and punctuation density.

5. `scoring.py` combines both signals into one score.

6. The score is converted into a human-readable label: `human`, `unsure`, or `ai`.

7. The response is returned to the user, and the decision is saved in the audit log.

Writers can challenge a result using the `/appeal` endpoint. Their appeal is recorded with an `under_review` status.
---
## Signals and Scoring

### Signal one — the model signal

**What it measures:**

The model signal uses a local GPT-2 language model to measure how predictable the submitted text is. It converts the model's perplexity measurement into a score between 0 and 1.

**Why that might differ between human and AI writing:**

AI-generated text can follow predictable language patterns because language models generate text by predicting likely next tokens. Human writing may contain more unexpected word choices and sentence structures.

**What it can't see:**

This signal cannot reliably identify who actually wrote the text. Formal or predictable human writing may receive an AI-like score, while unusual or edited AI-generated writing may receive a lower score. It also cannot verify authorship or understand the circumstances in which the text was written.

### Signal two — the style signal

**What it measures:**

The style signal measures three writing characteristics:

- **Sentence length spread:** Measures how much sentence lengths vary.

- **Type-token ratio:** Measures unique words compared with total words.

- **Punctuation density:** Measures punctuation marks relative to text length.

The three measurements are converted into AI-oriented scores and combined using these weights:

- Sentence length spread: 40%

- Vocabulary diversity: 30%

- Punctuation density: 30%

**Why that might differ between human and AI writing:**

AI-generated writing may contain more consistent sentence lengths and repeated vocabulary patterns. Human writing can have more variation in sentence structure and punctuation.

**What it can't see:**

The style signal does not understand the meaning of the text or identify its author. Small edits, punctuation changes, sentence splitting, and vocabulary changes can affect the score. Short texts can also produce misleading results.

### The combining rule

**The rule:**

The model signal receives 60% weight, and the style signal receives 40% weight.

If the two signals strongly disagree, the combined score is reduced by 0.10. This is intended to reduce overconfident AI accusations when the evidence is inconsistent.

**The numbers:**

```python

combined_score = 0.60 * model_score + 0.40 * style_score

if abs(model_score - style_score) >= 0.40:

    combined_score -= 0.10

```

The final score is restricted to the range 0–1.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:**

I tested a model score of 0.90 and a style score of 0.10.

Without the disagreement penalty, the weighted score would be 0.58. Because the signals strongly disagree, the system subtracts 0.10.

The final combined score becomes **0.48**, producing an `unsure` prediction.

This approach avoids making a confident accusation when the two signals provide conflicting evidence.

**Calibration observations:**

| Writing sample                 | Style score |

| ------------------------------ | ----------: |

| AI-like writing                |      0.6396 |

| Casual human writing           |      0.4497 |

| Plain human writing            |      0.5855 |

| Lightly edited AI-like writing |      0.4642 |

These were illustrative writing samples rather than a verified authorship dataset.

The plain human sample received a relatively high score, showing a false-positive risk. The edited AI-like sample received a lower score than the original AI-like sample, showing how easily writing changes can affect the style signal.
---
## Label Variants

| Label                 | Score range               | The exact text a reader sees                                                                                                              |

| --------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |

| High-confidence human | 0.00–0.35                 | This writing appears more consistent with human writing, but we cannot determine authorship with certainty.                               |

| Unsure                | Above 0.35 and below 0.65 | We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone. |

| High-confidence AI    | 0.65–1.00                 | This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.                             |

**Why I worded the "unsure" one this way:**

I wanted the message to be fair and respectful to writers. An uncertain score should not make someone feel falsely accused of using AI. The label clearly explains that the system cannot confidently determine authorship and that no conclusion should be drawn from the result alone.
---
## Sample Run

### A submission

**Request:**

```powershell

$body = @{

    text = "Artificial intelligence is transforming modern industries. It improves efficiency and increases productivity."

    creator_id = "user123"

} | ConvertTo-Json -Compress

Invoke-RestMethod -Uri "http://127.0.0.1:5000/submit" -Method POST -ContentType "application/json" -Body $body

```

**Actual response:**

```json

{

  "confidence": 0.5547,

  "content_id": "e7e6af7d-9968-48dd-b397-b33605d6175e",

  "guess": "unsure",

  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",

  "model_score": 0.4822,

  "style_score": 0.6634

}

```

The system returned `unsure` because the combined score was between the human and AI thresholds.

### An appeal

**Request:**

```powershell

$body = @{

    content_id = "e7e6af7d-9968-48dd-b397-b33605d6175e"

    reasoning = "I wrote this text myself. Please review the AI detection result."

} | ConvertTo-Json -Compress

Invoke-RestMethod -Uri "http://127.0.0.1:5000/appeal" -Method POST -ContentType "application/json" -Body $body

```

**Expected response structure (appeal request was tested):**

```json

{

  "content_id": "e7e6af7d-9968-48dd-b397-b33605d6175e",

  "status": "under_review",

  "message": "Your appeal has been submitted for review."

}

```

### What the log shows afterwards

**Request:**

```powershell

Invoke-RestMethod -Uri "http://127.0.0.1:5000/log?limit=2" -Method GET | ConvertTo-Json -Depth 5

```

**Actual audit log entries:**

```json

{

  "count": 2,

  "entries": [

    {

      "combined_score": 0.5547,

      "content_id": "e7e6af7d-9968-48dd-b397-b33605d6175e",

      "creator_id": "user123",

      "guess": "unsure",

      "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",

      "model_score": 0.4822,

      "status": "decided",

      "style_score": 0.6634,

      "timestamp": "2026-11-03T03:53:51+00:00"

    },

    {

      "content_id": "e7e6af7d-9968-48dd-b397-b33605d6175e",

      "creator_id": "user123",

      "event": "appeal",

      "reasoning": "I wrote this text myself. Please review the AI detection result.",

      "status": "under_review",

      "timestamp": "2026-11-03T03:55:33+00:00"

    }

  ]

}

```

The audit log preserves the original decision and adds the appeal as a separate entry. This provides a history of the submission and its review request.
---
## How I Used AI

### Moment 1 — Implementing the Flask API

**What I asked for:**

I asked ChatGPT to help me understand the Flask starter code and implement the `/submit` endpoint step by step.

**What came back:**

ChatGPT explained how to accept JSON input, validate user submissions, generate unique content IDs, call the local AI detector, and return a JSON response.

**What I changed:**

I integrated the code into my existing Flask application, fixed indentation and route errors, and tested the endpoint using PowerShell. I also connected the audit logging functionality and verified that submissions were saved.

### Moment 2 — Stylometry, Scoring, and Appeals

**What I asked for:**

I asked ChatGPT for help implementing sentence length spread, type-token ratio, punctuation density, combined scoring, and the appeal endpoint.

**What came back:**

ChatGPT provided Python implementations, explanations, and testing commands. It also helped me create readable prediction labels and handle disagreements between the two detection signals.

**What I changed:**

I added the functions to my project, tested different writing samples, integrated both signals into the Flask API, and verified the combined scores. I implemented appeal handling and confirmed that appeal requests were recorded in the audit log.
---
## Unit 8 — Testing and Improvements

## Rate Limiting

**My limits:** 10 requests per minute, 200 requests per day.

**Why those numbers and not others:**

I chose 10 requests per minute because a normal writer may submit their work several times while making changes, but they are unlikely to need more than 10 submissions in one minute. The daily limit of 200 allows regular use while restricting scripts that repeatedly submit variations to discover the detection thresholds.

**What a caller counts as:**

The rate limiter prefers a provided creator ID and otherwise falls back to the caller IP address. This is a basic abuse-control mechanism; identities can be rotated and shared IPs may still affect users without creator IDs.

**The run of status codes when I pushed past it:**

Command:

```bash

python run_attacks.py --flood 15

```

Actual output:

```text

200 200 200 200 200 200 200 200 200 200 429 429 429 429 429

```

10 requests succeeded, and 5 requests were rate limited.

The results were saved in `results/flood_2026-11-09_2055.md`.

**Audit logging verification:**

I checked the `/log` endpoint and confirmed that all five rejected requests were recorded with `event: rejected`, `reason: rate_limited`, and `status: rejected`.

\

## Attack Run — Before

The baseline staff attack suite ran **56 cases**. Full per-case inputs and raw outcomes are in `results/attack_run_2026-11-09_2109_before.md`. The runner left 56 cases for manual HELD/BROKE assessment; HTTP success alone does not prove that an attack succeeded.

| Group | Observed outcomes | Interpretation |
|---|---|---|
| EV01–EV10 | 1 `human`, 7 `unsure`, 2 `ai` | Potential evasion; assess each against its expected behavior |
| FP01–FP08 | 6 `ai`, 2 `unsure` | Potential false positives; FP02–FP07 warrant review |
| PI01–PI06 | 1 `human`, 5 `unsure` | No demonstrated execution of injected instructions |
| MF01–MF08 | MF02 returned HTTP 500; MF08 returned 413 | Short-text crash exposed |
| RQ01–RQ12 | All HTTP 400 | Invalid requests rejected |
| FL01_01–FL01_12 | First 10 HTTP 200, final 2 HTTP 429 | Rate limiting triggered |

**Ten audit log entries from the run:** The ten exact JSON records still need to be selected and pasted from `logs/audit.jsonl` or `results/audit_extract.json`. No fabricated entries are included. The audit log should include the original decision and rejection records for representative attacks.

**Single worst outcome:** MF02 sent a one-character input and received HTTP 500. A user should receive a clear validation error, not a server failure. Potential false-positive classifications are also important because the consequences for legitimate writers can be serious.

## Run Log and Verdicts

Baseline evidence: `results/run_2026-11-09_2216_before.md`. After-change evidence: `results/run_2026-11-09_2243_after.md`. The baseline did not exercise Criterion 4; the after-change runner did.

| Criterion | Target | After trial 1 | After trial 2 | After trial 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human false positives | No more than 1/10 high-confidence AI false positives | 6/10 `ai` | 6/10 `ai` | 6/10 `ai` | **Not established** — sample authorship unverified |
| 2. Score separation | Mean AI score at least 0.30 above mean human score | `ai, human, ai` | Same | Same | **Not established** — numeric group comparison missing |
| 3. Label coverage | `human`, `unsure`, and `ai` all reachable | `unsure, ai, ai` | Same | Same | **MISSED** |
| 4. Appeal logging | 10/10 appeals recorded `under_review` | 10/10 | 10/10 | 10/10 | **MET** |
| 5. Invalid inputs | 10/10 HTTP 400 or 413 without crashes | 10/10 | 10/10 | 10/10 | **MET** |

**Real output from one trial:** `run_eval.py::main`, after evaluation, Criterion 5. This is an abbreviated extraction of the recorded HTTP statuses (the complete JSON is in the report):

```json
[400, 400, 400, 400, 413, 400, 400, 400, 400, 400]
```

**Diagnoses:**

- **Criterion 1 / FP02–FP07:** The model and stylometry signals, their weighted combination, and the 0.65 AI threshold can classify structured writing as AI-like. Without verified authorship, the evaluation cannot quantify a true false-positive rate.
- **Criterion 2:** The evaluation scenario lacks verified AI/human groups and a calculation of their mean combined scores. Label outputs alone cannot establish a 0.30 score gap.
- **Criterion 3:** The selected inputs produced only `unsure` and `ai`. The combined-score distribution and label mapping did not reach the `human` threshold on this set; this does not prove the `human` branch is unreachable for every possible input.
- **Criterion 4:** The evaluation runner now submits content, appeals the returned content ID, and checks the `under_review` audit entry. All ten passed in each after trial.
- **Criterion 5:** All ten malformed requests were rejected with HTTP 400 or 413 in each after trial.
- **MF02:** A one-character input reached `detector.model_signal`, which raised an unhandled `ValueError`; the `/submit` route returned HTTP 500.
- **Evasion/prompt injection:** Classification outputs alone are insufficient to assign defensible HELD/BROKE verdicts or infer that injected instructions executed. The individual cases still require manual review.

## The Improvement

**What I changed:** In `app.py`, I caught `ValueError` from `detector.model_signal(text)`, logged the rejected short-text request, and returned HTTP 400 instead of an uncaught HTTP 500.

**Which diagnosis pointed at it:** The MF02 attack demonstrated missing error handling between the model-signal stage and the Flask route.

### Attack Run — After

The same 56 attacks were rerun. Full report: `results/attack_run_2026-11-09_2226_after.md`.

| Check | Before | After |
|---|---|---|
| MF02, one-character input | HTTP 500 | **HTTP 400** |
| RQ01–RQ12 | All HTTP 400 | All HTTP 400 |
| FL01_11–FL01_12 | HTTP 429 | HTTP 429 |
| FP02–FP07 | Classified `ai` | Still classified `ai` |

**Did it help?** Yes, the observed crash became a controlled rejection. The fix was deliberately narrow: it did not resolve the potential false-positive cases or the missing `human` label in the evaluation scenario. The after-run report also left all 56 attack verdicts for manual review rather than auto-marking them HELD or BROKE.

## What's Still Broken

The evaluation has not established a reliable false-positive rate or score separation without verified-authorship samples. Several potential human-writing false positives remain, and the label-coverage scenario still fails to produce `human`. Evasion and prompt-injection cases require manual outcome-by-outcome assessment. For a future iteration I would collect provenance-verified writing, calculate score distributions for each group, revisit thresholds using held-out data, and expand adversarial testing.

**The trade I'd make if this ran for real:** I would favor `unsure` over a confident AI accusation when evidence is ambiguous, even if that lets more AI-generated text avoid a definitive label. Writers bear the cost of false accusations, so any production use should include an accessible human appeal process.

## Remaining submission evidence

The following items should be completed before claiming the Unit 8 rubric is fully satisfied: (1) paste ten real audit log JSON entries; (2) review the 56 attacks individually and record HELD/BROKE with explanations; (3) verify authorship and compute Criterion 1 and 2 metrics; and (4) confirm the required commit count and repository submission. Failed criteria are reported openly rather than presented as passing.
