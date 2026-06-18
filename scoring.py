def calculate_score(candidate):

    score = 0

    try:
        skills = [
            s["name"].lower()
            for s in candidate.get("skills", [])
        ]
    except:
        skills = []

    required_skills =[ "python", "nlp", "llm", "fine-tuning llms", "rag", "retrieval", "ranking", "embeddings", "transformers", "lora", "hugging face", "vector databases", "machine learning", "deep learning", "speech recognition", "image classification" ]

    matched = 0

    for skill in required_skills:
        if skill in skills:
            matched += 1

    # Skills Score (40 Marks)
    score += (matched / len(required_skills)) * 40

    # Experience Score (20 Marks)
    exp = candidate.get("profile", {}).get(
        "years_of_experience", 0
    )

    if 5 <= exp <= 9:
        score += 20
    elif exp > 9:
        score += 15
    elif exp >= 3:
        score += 10

    signals = candidate.get(
        "redrob_signals", {}
    )

    # Profile Completeness (10 Marks)
    completeness = min(
        signals.get(
            "profile_completeness_score", 0
        ),
        100
    )

    score += (completeness / 100) * 10

    # GitHub Activity (10 Marks)
    github = min(
        signals.get(
            "github_activity_score", 0
        ),
        10
    )

    score += github

    # Recruiter Response Rate (10 Marks)
    recruiter = min(
        signals.get(
            "recruiter_response_rate", 0
        ),
        10
    )

    score += recruiter

    # Location Bonus (10 Marks)
    location = candidate.get(
        "profile", {}
    ).get(
        "country", ""
    )

    if str(location).lower() == "india":
        score += 10

    return round(min(score, 100), 2)