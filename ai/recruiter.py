def generate_feedback(
        candidate,
        matched_skills,
        missing_skills,
        score
):

    feedback = {}


    # Strengths

    feedback["strengths"] = matched_skills


    # Weakness

    feedback["weakness"] = missing_skills


    # Decision

    if score >= 85:

        decision = "Highly Recommended"

    elif score >= 70:

        decision = "Recommended"

    else:

        decision = "Needs Improvement"


    feedback["decision"] = decision


    feedback["message"] = (

        f"Candidate scored {score}% "
        "based on AI resume analysis."
    )


    return feedback



def generate_questions(
        skills
):

    questions = []


    for skill in skills:


        if skill.lower()=="python":

            questions.extend([

                "Explain Python decorators.",

                "Difference between list and tuple?"

            ])


        elif skill.lower()=="machine learning":

            questions.extend([

                "Explain bias and variance.",

                "How does Random Forest work?"

            ])


        elif skill.lower()=="nlp":

            questions.extend([

                "Explain TF-IDF.",

                "Explain Transformer architecture."

            ])


        else:

            questions.append(

                f"Explain your experience with {skill}"

            )


    return questions