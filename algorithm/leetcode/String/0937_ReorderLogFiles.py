# leetcode 937
def reorderLogFiles(self, logs: List[str]) -> List[str]:

    # use lambda 32ms , 14.2MB
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
    return letters + digits