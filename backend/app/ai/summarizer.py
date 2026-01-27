def summarize_issue(text):
    words = text.split()
    short = " ".join(words[:20])
    return short + ("..." if len(words) > 20 else "")
