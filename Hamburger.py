"""Hamburger"""
def main():
    """Main Function"""
    top_bun = int(input())
    bottom_bun = int(input())
    print("|" * top_bun, end="")
    print("*" * (2*top_bun), end="")
    print("*" * (2*bottom_bun), end="")
    print("|" * bottom_bun)
main()
