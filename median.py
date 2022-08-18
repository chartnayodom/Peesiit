"""Median"""
def main():
    """Main Function"""
    how = int(input())
    number = []
    for _ in range(how):
        number.append(int(input()))
    number.sort()
    #print(number)
    if how % 2 == 1:
        print("%.01f" %(number[how//2]))
    elif how % 2 == 0:
        diff = (number[how//2] - number[how//2-1]) / 2
        #print(diff)
        print("%0.1f" %(number[how//2-1] + diff))
main()
