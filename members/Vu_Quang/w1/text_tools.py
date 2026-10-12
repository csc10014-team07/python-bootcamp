import string
from collections import Counter
def word_count(text: str) -> dict[str, int]:
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    return dict(Counter(words))
def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:k]
van_ban = "Git is fun. Git is fast!"
top_2_tu = top_k(van_ban, 2)
print(f"Văn bản gốc: \"{van_ban}\"")
print("Top 2 từ xuất hiện nhiều nhất:", top_2_tu)