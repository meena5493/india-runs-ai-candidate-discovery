from candidate_parser import load_candidates

first_candidate = next(load_candidates("candidates.jsonl"))

print(first_candidate.keys())

print("\nSkills:")
print(first_candidate["skills"][:10])