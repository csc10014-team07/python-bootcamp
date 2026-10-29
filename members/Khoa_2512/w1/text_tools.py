"""Count word frequencies and find the most common words."""


def word_count(text: str) -> dict[str, int]:
    """Count the occurrences of each word in the text.

    Punctuation is removed and all words are converted to lowercase.

    Args:
        text: The input text to analyze.

    Returns:
        A dictionary mapping each word to its frequency.
    """
    temp = (
        text.replace(",", "")
        .replace("!", "")
        .replace(".", "")
        .replace("?", "")
        .replace(";", "")
        .replace(":", "")
        .lower()
        .split()
    )
    thisdict: dict[str, int] = {}

    for x in temp:
        count = 0
        for y in temp:
            if x == y:
                count += 1
        thisdict.update({x: count})

    return thisdict


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words, sorted by frequency and alphabetically.

    Args:
        text: The input text to analyze.
        k: The maximum number of words to return.

    Returns:
        A list of (word, frequency) tuples, ordered by descending frequency
        and then alphabetically.
    """
    my_dict = word_count(text)
    mylist = list(my_dict.items())
    mylist.sort(key=lambda x: (-x[1], x[0]))
    return mylist[:k]


print(top_k("Git is fun. Git is fast!", 2))
