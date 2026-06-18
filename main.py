from candidate_parser import load_candidates
from scoring import calculate_score
import pandas as pd

print("Loading candidates and calculating scores...")

results = []

for candidate in load_candidates("candidates.jsonl"):

    try:
        score = calculate_score(candidate)

        candidate_id = candidate.get(
            "candidate_id",
            candidate.get("id", "UNKNOWN")
        )

        results.append({
            "candidate_id": candidate_id,
            "score": score
        })

    except Exception as e:
        print(
            f"Error processing candidate: {e}"
        )

print(
    f"\nTotal candidates processed: {len(results)}"
)

df = pd.DataFrame(results)

df = df.sort_values(
    by="score",
    ascending=False
)

top100 = df.head(100).copy()

top100["rank"] = range(
    1,
    len(top100) + 1
)

top100["reasoning"] = (
    "Strong skill match and relevant experience"
)

top100 = top100[
    [
        "rank",
        "candidate_id",
        "score",
        "reasoning"
    ]
]

top100.to_csv(
    "top100_candidates.csv",
    index=False
)

print("\nTop 10 Candidates:")
print(top100.head(10))

print(
    "\nFile saved successfully as "
    "'top100_candidates.csv'"
)