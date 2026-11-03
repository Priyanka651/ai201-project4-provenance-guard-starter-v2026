# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. _"The
detector is accurate"_ is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. _"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"_ is a criterion.

Under each, write a sentence or two on **why that target**. _"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"_ is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area            | A question it could answer                                    |
| --------------- | ------------------------------------------------------------- |
| False positives | How often may a human's writing get called AI?                |
| Score spread    | How far apart should clearly-AI and clearly-human text score? |
| Label coverage  | Is every one of your three labels actually reachable?         |
| The appeal path | Does an appeal always change status and always get recorded?  |
| Bad input       | What happens when `text` is missing, empty, or enormous?      |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---

## 1.

## 1. False Positive Rate

Across all three trials, the system should incorrectly label no more than 1 out of 10 human-written texts as high-confidence AI-generated.

**Why this target:**

I chose this target because falsely accusing a human writer of using AI can affect their trust and reputation. I want my system to minimize false accusations while still detecting AI-generated content.

---

## 2.

## 2. Score Spread

Across all three trials, the average combined score for clearly AI-generated texts should be at least 0.30 higher than the average combined score for clearly human-written texts.

**Why this target:**

I chose 0.30 because I want my system to show a clear difference between AI-generated and human-written content. This difference will help me understand whether combining both signals improves the detection results.

---

## 3. Label Coverage

Across all three trials, the system should successfully produce all 3 labels: high-confidence AI, high-confidence human, and unsure. Each label must be reachable with at least one test input in every trial.

**Why this target:**

I chose this target because my system should not always predict AI or human. Sometimes the result may be uncertain, so the system should provide an unsure label instead of making a wrong prediction.

---

## 4.

## 4. Appeal Path

Across all three trials, 100% of valid appeals (10 out of 10) should be successfully recorded in the audit log, and each appeal should change the content status to under_review.

**Why this target:**

I chose 100% because every writer should have a chance to challenge an incorrect prediction. If an appeal is lost or not recorded, the writer may not get a fair review. I want my system to handle every valid appeal reliably.

---

## 5. Bad Input Handling

Across all three trials, the system should correctly handle 10 out of 10 invalid requests, including missing text, empty text, incorrect data types, and text exceeding 10,000 characters. Each invalid request should return an appropriate HTTP error (400 or 413) without crashing the server.

**Why this target:**

I chose this target because users may accidentally submit empty, missing, or very large text. My system should handle these situations safely and return clear error messages instead of crashing.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
