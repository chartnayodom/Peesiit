"""Hamming"""
def main():
    """psit"""
    text1 = input()
    text2 = input()
    total = 0
    for i in range(len(text1)):
        if text1[i] == text2[i]:
            pass
        else:
            total += 1
    print(total)
main()
