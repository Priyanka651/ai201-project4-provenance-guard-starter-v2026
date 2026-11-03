# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

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

| Writing sample                 | Style score |
| ------------------------------ | ----------: |
| AI-like writing                |      0.6396 |
| Casual human writing           |      0.4497 |
| Plain human writing            |      0.5855 |
| Lightly edited AI-like writing |      0.4642 |

These were illustrative writing samples rather than a verified authorship dataset.

The plain human sample received a relatively high score, showing a false-positive risk. The edited AI-like sample received a lower score than the original AI-like sample, showing how easily writing changes can affect the style signal.

---

## Label Variants

| Label                 | Score range               | The exact text a reader sees                                                                                                              |
| --------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| High-confidence human | 0.00–0.35                 | This writing appears more consistent with human writing, but we cannot determine authorship with certainty.                               |
| Unsure                | Above 0.35 and below 0.65 | We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone. |
| High-confidence AI    | 0.65–1.00                 | This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.                             |

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

The following sections remain to be completed in Unit 8:

- Rate Limiting
- Attack Run — Before
- Run Log and Verdicts
- The Improvement
- Attack Run — After
- What's Still Broken

These sections will be completed using actual attack results, evaluation runs, and documented improvements.

---

**Repository:** https://github.com/Priyanka651/ai201-project4-provenance-guard-starter-v2026

**How to run this project:** [RUNNING.md](RUNNING.md)

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** **_ per minute, _** per day

**Why those numbers and not others:**

<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ------- |
| 1.        |        |       |       |       |         |
| 2.        |        |       |       |       |         |
| 3.        |        |       |       |       |         |
| 4.        |        |       |       |       |         |
| 5.        |        |       |       |       |         |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
