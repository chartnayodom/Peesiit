"""ball"""

def main():
    """main"""
    height = int(input())
    loop = 0
    height2 = float(height)
    while True:
        if height2 < 0.01:
            break
        else:
            height2 = height2*(3/5)
            # print(height2)
            loop += 1
    print(loop-1)
main()