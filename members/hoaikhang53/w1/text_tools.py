
def word_count(text: str) -> dict[str, int]:
    """Count how many times each word appears in a text.

    The text is lower-cased and the punctuation characters ``.,!?;:`` are
    treated as word separators.

    Args:
        text: The input text.

    Returns:
        A dict mapping each lower-cased word to its number of occurrences.
    """
    text = text.lower()
    for char in ".,!?;:":
        text = text.replace(char, " ")

    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the ``k`` most frequent words in a text.

    Words are ordered by descending count, with ties broken alphabetically.

    Args:
        text: The input text.
        k: Maximum number of words to return. Values below 0 are treated as 0.

    Returns:
        A list of ``(word, count)`` tuples, at most ``k`` long.
    """
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    return sorted_words[:max(0, k)]

print(top_k("Git is fun. Git is fast!", 2))
