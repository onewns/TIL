# leetcode 819
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

    # my style 36ms 14.2MB
    paragraph = re.sub('[^a-z]', ' ', paragraph.lower())
    words = list(paragraph.split())
    counter = Counter(words).most_common()
    for word, cnt in counter:
        if word not in banned:
            return word

    # use list comprehension, Counter Object 36ms 14.1MB
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    counts = Counter(words)
    return counts.most_common(1)[0][0]