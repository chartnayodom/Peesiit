"""Inverter"""
def main():
    """Inverter"""
    text = [i for i in input()]
    for i in range(len(text)):
        if text[i] == "0":
            text[i] = "1"
        elif text[i] == "1":
            text[i] = "0"
    if text.count("1") == 0:
        print()
    else:
        print(*text[text.index("1"):], sep="")
main()