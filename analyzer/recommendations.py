def generate_recommendations(complexity, patterns, entropy):
    recommendations = []

    if not complexity["length"]:
        recommendations.append("Increase password length to at least 12 characters.")

    if not complexity["uppercase"]:
        recommendations.append("Include uppercase letters.")

    if not complexity["lowercase"]:
        recommendations.append("Include lowercase letters.")

    if not complexity["digits"]:
        recommendations.append("Include numeric digits.")

    if not complexity["special"]:
        recommendations.append("Include special characters.")

    if entropy < 60:
        recommendations.append("Increase password randomness to improve entropy.")

    if patterns:
        recommendations.append("Avoid dictionary words, repeated characters, and keyboard sequences.")

    return recommendations