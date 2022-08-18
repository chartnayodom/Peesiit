"""FOR!F-Ball"""
def main():
    """main function"""
    glass1 = 1
    glass2 = 0
    glass3 = 0
    move = input()
    for i in range(len(move)):
        if move[i] == 'A' and glass1 == 1:
            glass = 0
            
main()
