"""Ascending sort"""
def main():
    """mmain"""
    ask = []
    for _ in range(0, 5):
        ask.append(int(input()))
    ask.sort()
    for i in ask:
        print(i)
main()
