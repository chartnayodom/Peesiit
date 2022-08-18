"""Missing number"""
def main():
    """Main function"""
    m_x = int(input())
    text = []
    while True:
        inp = int(input())
        if inp < 1:
            break
        text.append(inp)
    for i in range(1, m_x):
        if text.count(i) < 1:
            print(i)
        else:
            pass
        
main()
