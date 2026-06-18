# AI-Powered Candidate Discovery System

## Overview
This project ranks candidates based on their suitability for a Senior AI Engineer role using candidate profiles, skills, experience, and behavioral signals.

## Dataset(dataset provided by challenge)
- 100,000 candidate profiles
- Skills
- Experience
- Redrob behavioral signals

## Scoring Criteria
- Skills Match (40%)
- Experience Match (20%)
- Profile Completeness (10%)
- GitHub Activity (10%)
- Recruiter Response Rate (10%)
- Location Bonus (10%)


## Repository Structure

- main.py
- scoring.py
- candidate_parser.py
- check.py
- top100_candidates_v2.csv

## Output

The system processes 100,000 candidate profiles and generates the top 100 ranked candidates saved in top100_candidates_v2.csv for a Senior AI Engineer role.

## Output
Top 100 ranked candidates saved in top100_candidates_v2.csv

## Run

pip install pandas numpy tqdm

python main.py
