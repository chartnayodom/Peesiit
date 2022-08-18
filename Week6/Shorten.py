"""Shorten"""
# def notmain():
#     """Main function"""
#     text = ""
#     stack = 0
#     stack2 = ""
#     while True:
#         inp = int(input())
#         if inp == -1:
#             if len(stack2) > 1 and stack2.find(str(stack)):
#                 text += "-"
#                 text += str(stack)
#                 #text += ", "
#                 #text += str(inp)
#                 # stack = inp
#                 # stack2 = str(inp)
#             else:
#                 pass
#             break
#         else:
#             if stack <= 0:
#                 text += str(inp)
#                 stack = inp
#                 stack2 += str(inp)
#             elif stack > 0:
#                 #print(1, stack)
#                 if inp == stack + 1:
#                     stack2 += str(inp)
#                     stack = inp
#                     #print("pass")
#                 elif inp != stack + 1:
#                     if len(stack2) > 1:
#                         text += "-"
#                         text += str(stack)
#                         text += ", "
#                         text += str(inp)
#                         stack = inp
#                         stack2 = str(inp)
#                     else:
#                         text += ", "
#                         text += str(inp)
#                         stack = inp
#                         stack2 = str(inp)
#     print(text)
def main():
    """notmain"""
    ans = ""
    start_number = None
    prev_number = None
    while True:
        number = int(input())
        if number == -1:
            break

        if start_number == None:
            start_number = number
            prev_number = number
        else:
            if prev_number != number-1:
                if start_number == prev_number:
                    ans += "%d, " % (start_number)
                else:
                    ans += "%d-%d, " % (start_number, prev_number)
                start_number = number
                prev_number = number
            else:
                prev_number = number
    if start_number != None:
        if start_number == prev_number:
            ans += "%d, " % (start_number)
        else:
            ans += "%d-%d, " % (start_number, prev_number)

    print(ans.strip(", "))

main()

