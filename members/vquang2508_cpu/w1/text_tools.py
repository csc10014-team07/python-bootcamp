"""Text processing tools for counting words and extracting top frequencies."""

import string
from collections import Counter


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word in the given text, ignoring punctuation and case.

    Args:
        text: Input string to analyze.

    Returns:
        A dictionary mapping each lowercase word to its occurrence count.
    """
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    return dict(Counter(words))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k most frequent words, ordered by frequency desc and word asc.

    Args:
        text: Input text string.
        k: Maximum number of word-frequency pairs to return.

    Returns:
        A list of tuples (word, count) for the top k words.
    """
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:k]


if __name__ == "__main__":
    van_ban = "Git is fun. Git is fast!"
    top_2_tu = top_k(van_ban, 2)
    print(f'Văn bản gốc: "{van_ban}"')
    print("Top 2 từ xuất hiện nhiều nhất:", top_2_tu)
