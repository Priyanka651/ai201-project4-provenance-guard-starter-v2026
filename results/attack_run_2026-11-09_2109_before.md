# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 21:09
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `342e5291-f4f6-433b-8dd3-321c6e4dd0e5` | human | 0.258 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `746ad093-9b96-42c0-934c-1bd0cf4d59e1` | unsure | 0.568 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `34727a9e-a2eb-4129-93eb-ce740b848a48` | unsure | 0.633 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `2c865794-b26d-425f-aeeb-464a6d2bb685` | unsure | 0.624 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `3b75fdbc-af9d-4b85-80cc-251e8174209f` | unsure | 0.413 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0d1a9f9d-0942-4078-b616-44f87dd4cd9a` | unsure | 0.557 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `eda02777-a8c9-4590-89fe-d5e1bf362189` | unsure | 0.635 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `8ad2b6b1-75dd-4bbe-93cf-a8baefa9b198` | unsure | 0.367 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c83e94d6-7aac-48ae-9ab0-5ed3cc8f4e60` | ai | 0.655 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c70f8785-fbfb-499b-89c3-7d1f9400e965` | ai | 0.899 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `a85ec2cd-9805-49cf-b6b7-73e560125f1b` | unsure | 0.620 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `f8017e06-56b9-45d5-9688-a607ff279a1f` | ai | 0.714 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `8d7e822a-1a23-46d3-9c93-63eaabed978d` | ai | 0.743 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `39600c86-0cc0-47d5-97c7-ea8951d488ef` | ai | 0.744 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `20cb0b8a-2e1e-40be-8f77-69bf38efefda` | ai | 0.757 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `097c1ddf-eed3-4243-96c8-0e095727da82` | ai | 0.770 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `ffa691eb-1113-432c-bc7b-d9b9b59d5b2c` | ai | 0.785 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `1728de47-2185-4a4d-bf8f-57806f3d9623` | unsure | 0.358 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ae938f07-ea3a-47bd-9e90-94cd29215c7c` | unsure | 0.489 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `88790395-84a0-4da4-9f1a-4c1914e9d8f9` | human | 0.325 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `e6a7816f-a5db-4126-8635-ddac2aaa3d67` | unsure | 0.596 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `5d9faf24-3fb1-4dc9-8b1e-8d91851f2e40` | unsure | 0.536 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `5bc67046-1fa3-4f7c-85c6-ad238b3ae55d` | unsure | 0.583 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `2f5e79bc-1b93-4ac3-8892-f476af3727f8` | unsure | 0.586 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `eb59cd26-3f2a-452e-89f7-065de46f0eac` | human | 0.180 |  |
| MF04 | malformed | text is only punctuation | 200 | `d89aeee3-68a3-4700-b13a-5e0cf4152c2e` | human | 0.107 |  |
| MF05 | malformed | text is a very long single word | 200 | `1ac47cdf-ecca-42a8-a6ec-7d39569016f7` | ai | 0.879 |  |
| MF06 | malformed | text is emoji only | 200 | `9b123a43-9b84-48b8-8162-3de70a4ac662` | ai | 0.698 |  |
| MF07 | malformed | text is right-to-left script | 200 | `3e61ac73-7407-4e7d-aa7b-7bb1f1deadea` | unsure | 0.644 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `636fe43c-8b62-4f62-938f-36ee3eb8f3ef` | human | 0.183 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1410577c-dc8c-4e59-b6f6-1ede472aec5e` | human | 0.183 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `32727203-588c-4e38-93d9-a5726e7339aa` | human | 0.183 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `94419da8-516f-4148-9240-0351484fa766` | human | 0.183 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `56bfaa91-380f-462e-ae09-2b1c82256982` | human | 0.183 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `af1f1a62-0b10-4242-9a20-b6299b102a28` | human | 0.183 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1e64a0d5-b543-4906-a98b-f40ea084008b` | human | 0.183 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b70eb73c-fbbf-4057-85f0-5ab814fcbaad` | human | 0.183 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `57d74e00-23bd-4e99-8d56-4e322992c251` | human | 0.183 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a9525196-5028-44d7-9c90-1a20520087ec` | human | 0.183 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "342e5291-f4f6-433b-8dd3-321c6e4dd0e5",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.2581,
  "model_score": 0.1635,
  "style_score": 0.65,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "746ad093-9b96-42c0-934c-1bd0cf4d59e1",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5683,
  "model_score": 0.5943,
  "style_score": 0.5294,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "34727a9e-a2eb-4129-93eb-ce740b848a48",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.6333,
  "model_score": 0.6662,
  "style_score": 0.584,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "2c865794-b26d-425f-aeeb-464a6d2bb685",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6239,
  "model_score": 0.6114,
  "style_score": 0.6427,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "3b75fdbc-af9d-4b85-80cc-251e8174209f",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.4134,
  "model_score": 0.3212,
  "style_score": 0.5517,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "0d1a9f9d-0942-4078-b616-44f87dd4cd9a",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5568,
  "model_score": 0.5727,
  "style_score": 0.533,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "eda02777-a8c9-4590-89fe-d5e1bf362189",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6354,
  "model_score": 0.5862,
  "style_score": 0.7092,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "8ad2b6b1-75dd-4bbe-93cf-a8baefa9b198",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3672,
  "model_score": 0.2452,
  "style_score": 0.5502,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c83e94d6-7aac-48ae-9ab0-5ed3cc8f4e60",
  "creator_id": "attacker_EV09",
  "guess": "ai",
  "confidence": 0.655,
  "model_score": 0.7042,
  "style_score": 0.5813,
  "label": "This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c70f8785-fbfb-499b-89c3-7d1f9400e965",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8994,
  "model_score": 0.9792,
  "style_score": 0.7798,
  "label": "This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "a85ec2cd-9805-49cf-b6b7-73e560125f1b",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6199,
  "model_score": 0.6175,
  "style_score": 0.6236,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "f8017e06-56b9-45d5-9688-a607ff279a1f",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7135,
  "model_score": 0.7387,
  "style_score": 0.6758,
  "label": "This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "8d7e822a-1a23-46d3-9c93-63eaabed978d",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7434,
  "model_score": 0.8051,
  "style_score": 0.6509,
  "label": "This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "39600c86-0cc0-47d5-97c7-ea8951d488ef",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7435,
  "model_score": 0.8329,
  "style_score": 0.6094,
  "label": "This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "20cb0b8a-2e1e-40be-8f77-69bf38efefda",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.757,
  "model_score": 0.8005,
  "style_score": 0.6917,
  "label": "This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "097c1ddf-eed3-4243-96c8-0e095727da82",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7702,
  "model_score": 0.8814,
  "style_score": 0.6034,
  "label": "This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "ffa691eb-1113-432c-bc7b-d9b9b59d5b2c",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.785,
  "model_score": 0.8816,
  "style_score": 0.64,
  "label": "This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "1728de47-2185-4a4d-bf8f-57806f3d9623",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3584,
  "model_score": 0.3223,
  "style_score": 0.4125,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "ae938f07-ea3a-47bd-9e90-94cd29215c7c",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4893,
  "model_score": 0.4625,
  "style_score": 0.5294,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "88790395-84a0-4da4-9f1a-4c1914e9d8f9",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.325,
  "model_score": 0.2044,
  "style_score": 0.5059,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "e6a7816f-a5db-4126-8635-ddac2aaa3d67",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.596,
  "model_score": 0.5943,
  "style_score": 0.5985,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "5d9faf24-3fb1-4dc9-8b1e-8d91851f2e40",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5364,
  "model_score": 0.4998,
  "style_score": 0.5912,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "5bc67046-1fa3-4f7c-85c6-ad238b3ae55d",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5829,
  "model_score": 0.6401,
  "style_score": 0.4972,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "2f5e79bc-1b93-4ac3-8892-f476af3727f8",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5859,
  "model_score": 0.5583,
  "style_score": 0.6273,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "eb59cd26-3f2a-452e-89f7-065de46f0eac",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.18,
  "model_score": 0.0,
  "style_score": 0.7,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "d89aeee3-68a3-4700-b13a-5e0cf4152c2e",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.1067,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "1ac47cdf-ecca-42a8-a6ec-7d39569016f7",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8786,
  "model_score": 0.9976,
  "style_score": 0.7,
  "label": "This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "9b123a43-9b84-48b8-8162-3de70a4ac662",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.6981,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This writing shows patterns associated with AI-generated text, but this result is not proof that AI was used.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "3e61ac73-7407-4e7d-aa7b-7bb1f1deadea",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.6438,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We cannot confidently determine whether this writing was created by a person or AI. No conclusion should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "636fe43c-8b62-4f62-938f-36ee3eb8f3ef",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1827,
  "model_score": 0.0287,
  "style_score": 0.6636,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "1410577c-dc8c-4e59-b6f6-1ede472aec5e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1827,
  "model_score": 0.0287,
  "style_score": 0.6636,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "32727203-588c-4e38-93d9-a5726e7339aa",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1827,
  "model_score": 0.0287,
  "style_score": 0.6636,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "94419da8-516f-4148-9240-0351484fa766",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1827,
  "model_score": 0.0287,
  "style_score": 0.6636,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "56bfaa91-380f-462e-ae09-2b1c82256982",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1827,
  "model_score": 0.0287,
  "style_score": 0.6636,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "af1f1a62-0b10-4242-9a20-b6299b102a28",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1827,
  "model_score": 0.0287,
  "style_score": 0.6636,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "1e64a0d5-b543-4906-a98b-f40ea084008b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1827,
  "model_score": 0.0287,
  "style_score": 0.6636,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "b70eb73c-fbbf-4057-85f0-5ab814fcbaad",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1827,
  "model_score": 0.0287,
  "style_score": 0.6636,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "57d74e00-23bd-4e99-8d56-4e322992c251",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1827,
  "model_score": 0.0287,
  "style_score": 0.6636,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "a9525196-5028-44d7-9c90-1a20520087ec",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1827,
  "model_score": 0.0287,
  "style_score": 0.6636,
  "label": "This writing appears more consistent with human writing, but we cannot determine authorship with certainty.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
