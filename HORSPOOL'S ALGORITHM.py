def horspool(text, pattern):
    shift = [len(pattern)] * 125
    n = len(text)
    m = len(pattern)

    for j in range(m - 1):
        shift[ord(pattern[j])] = m - 1 - j

    i = m - 1
    flag = False
    while i < n:
        k = 0
        while k <= m - 1 and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            print("The position at which the pattern is found is", i - m + 2)
            flag = True
            break
        else:
            i += shift[ord(text[i])]
    if not flag:
        print("Pattern is not found in the given text")

if __name__ == "__main__":
    text = "BESS_KNEW_ABOUT_BAOBABS"
    pattern = "BAOBAB"
    horspool(text, pattern)
