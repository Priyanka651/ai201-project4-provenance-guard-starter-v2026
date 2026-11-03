
"""
Combine the model signal and style signal into one score.

Higher score = more AI-like writing.

Scoring rule:
- 60% model signal
- 40% style signal
- If signals disagree strongly, reduce the combined score
  to avoid overconfident AI accusations.

This is a heuristic, not proof of AI authorship.
"""

import config


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Combine two signals into a score between 0 and 1.

    Model signal weight: 0.60
    Style signal weight: 0.40

    A disagreement penalty reduces false-positive risk.
    """

    model_score = max(0.0, min(1.0, float(model_score)))
    style_score = max(0.0, min(1.0, float(style_score)))

    # Weighted average
    combined_score = (
        0.60 * model_score
        + 0.40 * style_score
    )

    # Strong disagreement between signals
    disagreement = abs(model_score - style_score)

    if disagreement >= 0.40:
        combined_score -= 0.10

    # Keep score between 0 and 1
    combined_score = max(0.0, min(1.0, combined_score))

    return round(combined_score, 4)


def score_to_label(score: float) -> tuple[str, str]:
    """
    Convert the combined score into a readable label.

    Uses thresholds from config.py.
    """

    if score >= config.AI_THRESHOLD:
        return (
            "ai",
            "This writing shows patterns associated with AI-generated text, "
            "but this result is not proof that AI was used."
        )

    if score <= config.HUMAN_THRESHOLD:
        return (
            "human",
            "This writing appears more consistent with human writing, "
            "but we cannot determine authorship with certainty."
        )

    return (
        "unsure",
        "We cannot confidently determine whether this writing was created "
        "by a person or AI. No conclusion should be drawn from this result alone."
    )


def label_ranges() -> list[tuple[str, str]]:
    """
    Return the score ranges for all three labels.
    """

    return [
        (
            "high-confidence human",
            f"0.00 – {config.HUMAN_THRESHOLD:.2f}"
        ),
        (
            "unsure",
            f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"
        ),
        (
            "high-confidence AI",
            f"{config.AI_THRESHOLD:.2f} – 1.00"
        ),
    ]


if __name__ == "__main__":
    print("Testing combined scoring...\n")

    test_cases = [
        ("AI-like", 0.90, 0.80),
        ("Human-like", 0.20, 0.30),
        ("Unsure", 0.50, 0.50),
        ("Disagreement", 0.90, 0.10),
    ]

    for name, model_score, style_score in test_cases:
        combined = combine_signals(model_score, style_score)
        guess, label = score_to_label(combined)

        print(f"Test: {name}")
        print(f"Model Score: {model_score}")
        print(f"Style Score: {style_score}")
        print(f"Combined Score: {combined}")
        print(f"Guess: {guess}")
        print(f"Label: {label}")
        print("-" * 50)
