"""Run Length Encoding"""
def main():
    """Main Function"""
    txt = input()
    stack = ""
    ans = ""
    for i in range(len(txt)):
        if len(stack) == 0:
            stack += txt[i]
        elif txt[i] == stack[0]:
            stack += txt[i]
        elif txt[i] != stack[0]:
            ans += str(len(stack))
            ans += stack[0]
            stack = txt[i]
    ans += str(len(stack))
    ans += stack[0]
    print(ans)
main()
