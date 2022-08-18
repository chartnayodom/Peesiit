"""Colors"""
def main():
    """main"""
    m_color = ['Red', 'Yellow', 'Blue']
    mix = {"orange": ["Red", "Yellow"], "purple": ["Red", "Blue"], "green": ["Blue", "Yellow"]}
    col1 = input().capitalize()
    col2 = input().capitalize()
    if col1 not in m_color or col2 not in m_color:
        print("Error")
        return
    if col1 in mix["orange"] and col2 in mix["orange"]:
        print("Orange")
    elif col1 in mix["purple"] and col2 in mix["purple"]:
        print("Violet")
    elif col1 in mix["green"] and col2 in mix["green"]:
        print("Green")
    elif col1 == col2:
        print(col1)


main()
