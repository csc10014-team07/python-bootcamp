PUNCTUATION = ".,!?;:"

def word_count(text: str) -> dict[str, int]:
    cleaned = text.lower()
    for ch in PUNCTUATION:
        cleaned = cleaned.replace(ch, "")

    counts = {}
    for word in cleaned.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    # sort by count (descending), then alphabetically (ascending)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:k]

print(top_k("Git is fun. Git is fast!", 2))