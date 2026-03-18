def analyze_text(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))

    return {
        "words": word_count,
        "characters": char_count,
        "characters_without_spaces": char_count_no_spaces
    }