def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}

    for word in text.lower().split():
        word = word.strip(".,!?;:")
        if word:
            counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

print(word_count("Git is fun. Git is fast!"))
print(top_k("Git is fun. Git is fast!", 2))