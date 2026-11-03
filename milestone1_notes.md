# Milestone 1: Understanding the Submission Flow

## 1. Submission Flow

1. User submits text and creator_id through POST /submit.
2. The system receives the text in app.py.
3. detector.py analyzes the text using a local AI model.
4. stylometry.py analyzes writing patterns such as sentence length, vocabulary, and punctuation.
5. scoring.py combines both signals to calculate a confidence score.
6. The system generates a label: AI-generated, human-written, or unsure.
7. audit.py saves the decision, and the API returns the result with a unique content_id.

## 2. Two Signals and Their Limitations

### Signal 1: AI Detector (detector.py)

- Uses a local AI model to analyze text.
- Measures how predictable the writing is.
- AI-generated text may follow predictable patterns.
- Limitation: Formal or structured human writing may also look AI-generated.

### Signal 2: Stylometry (stylometry.py)

- Analyzes writing style and patterns.
- Measures sentence length variation, vocabulary diversity, and punctuation.
- Human writing may have more variation in style.
- Limitation: AI can imitate human writing patterns, making detection difficult.

## 3. False Positive Scenario

1. A human writer submits their original writing.
2. The system incorrectly predicts that the text is AI-generated.
3. The writer receives a high AI score, such as 0.92.
4. The system displays a high-confidence AI label.
5. The writer disagrees with the prediction.
6. The writer submits an appeal with their content_id and reasoning.
7. The system records the appeal and changes the status to under_review.

## 4. API Endpoints

### Endpoint 1: POST /submit

Purpose: Accept user text and analyze whether it is AI-generated or human-written.

Input:

```json
{
  "text": "This is my first poem.",
  "creator_id": "user123"
}
```

Example Output:

```json
{
  "content_id": "abc123",
  "guess": "AI",
  "confidence": 0.92,
  "label": "This text is likely AI-generated.",
  "model_score": 0.9,
  "style_score": 0.94
}
```

### Endpoint 2: POST /appeal

Purpose: Allow writers to request a review if they disagree with the prediction.

Input:

```json
{
  "content_id": "abc123",
  "reasoning": "I wrote this poem myself."
}
```

Example Output:

```json
{
  "content_id": "abc123",
  "status": "under_review",
  "message": "Your appeal has been recorded."
}
```
