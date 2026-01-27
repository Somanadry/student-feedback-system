def categorize_issue(text):
    text = text.lower()

    if any(word in text for word in ["water", "leak", "fan", "electric", "repair", "broken"]):
        return "Maintenance"

    if any(word in text for word in ["dirty", "smell", "washroom", "garbage", "clean"]):
        return "Hygiene"

    if any(word in text for word in ["teacher", "exam", "marks", "class", "lecture"]):
        return "Academics"

    if any(word in text for word in ["hostel", "room", "mess", "food"]):
        return "Hostel"

    return "Other"
