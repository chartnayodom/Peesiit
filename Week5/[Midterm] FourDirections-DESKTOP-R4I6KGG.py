"""[Midterm] FourDirections"""
def upp(row):
    """UP"""
    if row == 0 or row == 4 or row == 3:
        print("  *  ", end=" ")
    elif row == 1:
        print(" *** ", end=" ")
    elif row == 2:
        print("* * *", end=" ")
def down(row):
    """DOWN"""
    if row == 0 or row == 4 or row == 1:
        print("  *  ", end=" ")
    elif row == 3:
        print(" *** ", end=" ")
    elif row == 2:
        print("* * *", end=" ")
def left(row):
    """LEFT"""
    if row == 2:
        print("*****", end=" ")
    elif row == 0 or row == 4:
        print("  *  ", end=" ")
    elif row == 1 or row == 3:
        print(" *   ", end=" ")
def right(row):
    """RIGHT"""
    if row == 2:
        print("*****", end=" ")
    elif row == 0 or row == 4:
        print("  *  ", end=" ")
    elif row == 1 or row == 3:
        print("   * ", end=" ")

def main():
    """Main Function"""
    cmd = input().upper()
    for i in range(5):
        for j in range(len(cmd)):
            if cmd[j] == "U":
                upp(i)
            elif cmd[j] == "D":
                down(i)
            elif cmd[j] == "L":
                left(i)
            elif cmd[j] == "R":
                right(i)
        print()
main()
