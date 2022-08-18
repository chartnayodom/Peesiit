"""Kuga"""
def main():
    """ชีวะจักรโบราณ"""
    num = int(input())
    sum = 0
    for i in range(10):
        if i <= num:
            sum = i
    print(sum)
    while sum < num:
        #หาตัวคูณมากที่สุดที่คูณกันได้ <= num
        for i in range(1,10):
            if sum * i <= num:
                o_num = i
            
        sum1 = sum * o_num
        #หาตัวบวกมากที่สุดที่บวกกันได้ <= num
        for j in range(1,10):
            if sum + j <= num:
                p_num = j
        sum2 = sum + p_num
        if sum1 <= num:
            print("* " ,sum1)
            sum = sum1
            continue
        else:
            print("+ " ,sum2)
            sum = sum2
            continue

main()
