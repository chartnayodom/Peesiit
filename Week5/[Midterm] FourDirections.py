"""[Midterm] FourDirections"""
def left():
    """LEFT"""
    print("""  *
 *
*****
 *
  *""", end="")
def right():
    """RIGHT"""
    print("""  *
   *
*****
   *
  *""", end="")
def upp():
    """UP"""
    print("""  *
 ***
* * *
  *
  *""", end="")
def down():
    """DOWN"""
    print("""""")

def main():
    """Main function"""
    cmd = input()
    for work in range(len(cmd)):
        if cmd[work] == "L":
            left()
        elif cmd[work] == "R":
            right()
        elif cmd[work] == "U":
            upp()
        elif cmd[work] == "D":
            down()

main()