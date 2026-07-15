def skill_match(candidate_skills, job_skills):

    candidate = set(skill.lower() for skill in candidate_skills)

    required = set(skill.lower() for skill in job_skills)

    matched = candidate.intersection(required)

    missing = required.difference(candidate)

    if len(required) == 0:
        percentage = 0
    else:
        percentage = round(
            (len(matched) / len(required)) * 100,
            2
        )

    return {

        "matched": list(matched),

        "missing": list(missing),

        "percentage": percentage

    }
def calculate_score(similarity, skill_percentage):

    score = (
        similarity * 0.6
        +
        skill_percentage * 0.4
    )

    return round(score, 2)