"""FOR!F_Ball""" #ยังไม่เสร็จ
def main():
    """main"""
    g_1 = 1
    g_2 = 0
    g_3 = 0
    cmd = input()
    for i in range(len(cmd)):
        # print(cmd[i])
        if cmd[i] == 'A' and g_1 == 1:
            g_1 = 0
            g_2 = 1
        elif cmd[i] == 'A' and g_2 == 1:
            g_2 = 0
            g_1 = 1
        elif cmd[i] == 'B' and g_2 == 1:
            g_2 = 0
            g_3 = 1
        elif cmd[i] == 'B' and g_3 == 1:
            g_3 = 0
            g_2 = 1
        elif cmd[i] == 'C' and g_1 == 1:
            g_1 = 0
            g_3 = 1
        elif cmd[i] == 'C' and g_3 == 1:
            g_3 = 0
            g_1 = 1
    if g_1 == 1:
        print("1")
    if g_2 == 1:
        print("2")
    if g_3 == 1:
        print("3")

main()
        