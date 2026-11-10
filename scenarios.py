"""
Provenance Guard — Unit 8, Milestone 3

Evaluation scenarios for acceptance criteria.
run_eval.py runs these scenarios three times.
"""

SCENARIOS = [
    # Criterion 1: Human writing false positives
    {
        "name": "human writing false positives",
        "criterion": 1,
        "texts": [
            "During my internship, I worked on a rich text editor using React. I started with basic features and learned how to add more advanced functionality. Some parts were difficult, but I improved my understanding by testing different solutions.",

            "I developed a PDF question answering application using Python and LangChain. The application allows users to upload documents and ask questions. I learned about text chunking, embeddings, and vector databases while building this project.",

            "Last week I was working on my application when I noticed that one feature was not working correctly. I checked the code and tested different possibilities. After some debugging, I found the issue and fixed it.",

            "When I started learning React, I was confused about components and props. I practiced by creating small applications. Over time, I became more comfortable using hooks and managing state.",

            "I enjoy working on software development projects because they help me learn new technologies. Sometimes I face unexpected errors, but solving those problems helps me understand the concepts better.",

            "In one of my assignments, I had to prepare a machine learning dataset before training the model. I checked missing values, selected useful features, and divided the data into training and testing sets.",

            "Yesterday I spent some time reviewing my Python code. I wanted to make sure that the functions were working correctly. I tested different inputs and made small changes where necessary.",

            "During my project, I learned that testing is an important part of software development. Even when an application appears to work, unexpected inputs can reveal problems that need to be fixed.",

            "I recently worked on integrating an API with a frontend application. At first, the response data was not displayed correctly. I checked the request and response format before finding the problem.",

            "Learning new programming concepts takes time and practice. I usually start by understanding the basic idea and then try implementing it in a small project. This approach helps me remember what I learned.",
        ],
    },

    # Criterion 2: AI vs human score separation
    {
        "name": "score separation",
        "criterion": 2,
        "texts": [
            "Artificial intelligence has transformed the landscape of modern technology by enabling automated decision-making, improving operational efficiency, and facilitating data-driven innovation across multiple industries.",

            "Machine learning systems rely on carefully structured training processes, comprehensive feature engineering, and systematic evaluation methodologies to achieve reliable predictive performance.",

            "Yesterday I tried to finish my project but got stuck on an error. I checked a few things and then asked my friend for help. We found a small mistake in the code.",
        ],
    },

    # Criterion 3: All three labels reachable
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "The implementation uses a structured pipeline to process input data, extract relevant features, and generate predictions. Each component is designed to improve consistency, reliability, and overall system performance.",

            "Yesterday I was working on my project and got stuck on an error. I checked my code several times but could not find the problem. After taking a short break, I noticed a small mistake and fixed it.",

            "I started working on the application in the morning. The first test worked, but the second one gave an unexpected result. I changed a few things and ran it again. I still need to check whether the results are correct.",
        ],
    },

    # Criterion 5: Invalid input handling
    {
        "name": "bad input validation",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_empty"},
            {"creator_id": "eval_missing"},
            {"text": None, "creator_id": "eval_null"},
            {"text": 123, "creator_id": "eval_number"},
            {"text": "word " * 3000, "creator_id": "eval_long"},
            {"text": "Valid text", "creator_id": ""},
            {"text": [], "creator_id": "eval_list"},
            {"text": {}, "creator_id": "eval_dict"},
            {"text": False, "creator_id": "eval_boolean"},
            {"text": "Hello", "creator_id": None},
        ],
    },
]


def validate() -> list[str]:
    """
    Validate scenarios before evaluation.
    """
    problems = []

    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} has both texts and bodies"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict"
                    )
            continue

        if not texts:
            problems.append(
                f"scenario {i} has no texts and no bodies"
            )
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i}, text {j} is still a placeholder"
                )

    return problems