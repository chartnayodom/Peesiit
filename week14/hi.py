"""Digit v2"""
def main():
    """psit"""
    text = input().split()
    many = 0
    mem = 0
    for i in text:
        if i == "thousand":
            many = 4
            # break
        elif i == "hundred":
            many = 3
            # break
        elif i.count("ty") or i.count("en") or i.count("lve"):
            many = 2
            # break
        if many >= mem:
            mem = many
    if mem == 0:
        print(1)
    else:
        print(mem)
main()
