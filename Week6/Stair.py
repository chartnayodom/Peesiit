"""Stair"""
# def main():
#     """Main finction"""
#     uphigh = int(input())
#     stair = int(input())
#     step = 0
#     stack = 0
#     for _ in range(stair):
#         stp = int(input())
#         if step == "NO":
#             break
#         if stp == uphigh:
#             step += 1
#         elif stp > uphigh:
#             step = "NO"
#         elif stp < uphigh:
#             stack += stp
#             if stack == uphigh:
#                 step += 1
#                 stack = 0
#             elif stack + stp > uphigh:
#                 step += 1
#                 stack = step
#     print(step)
def main():
    """niam"""
    camu = 0
    step = 0
    reach = int(input())
    staircase = int(input())
    is_unreachable = False
    for _ in range(staircase):
        each_case = int(input())
        if camu+each_case > reach:
            if each_case > reach:
                is_unreachable = True
                break
            else:
                step += 1
                camu = each_case
        else:
            camu += each_case
    else:
        if camu <= reach:
            step += 1
    if is_unreachable:
        print("NO")
    else:
        print(step)

main()
