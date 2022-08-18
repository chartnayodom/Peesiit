"""Docstring"""

def main():
    """main"""
    num = str(input())
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for idk in range(len(num)):
        sum1 += int(num[idk])
    #print(sum1)
    sum2 = (int(num)%1000)*10
    #print(sum2)
    sum3 = sum1+sum2
    #print(sum3)
    if sum3 >= 10000:
        print("%04d" %(sum3-10000))
    elif sum3 < 1000:
        print("%04d" %(sum3+1000))
    else:
        print("%04d" %(sum3))

main()
