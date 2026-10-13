import string
def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )
    return sorted_words[:max(0, k)]
print(top_k("Git is fun. Git is fast!", 2))