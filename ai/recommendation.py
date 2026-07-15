def recommend(score):

    if score >= 85:
        return "Highly Recommended"

    elif score >= 70:
        return "Recommended"

    elif score >= 50:
        return "Maybe"

    else:
        return "Not Recommended"