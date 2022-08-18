"""Milk"""
def main():
    """Main Function"""
    price = int(input())
    pro_ex = int(input()) #โปรฝา
    if pro_ex == 0:
        pro_ex = 1
    ex_get = int(input()) #ได้จากโปร
    money = int(input())
    buy_milk = money // price
    fah = buy_milk
    all_milk = buy_milk
    #แลกฝานมเรื่อยๆ
    while True:
        if fah >= pro_ex:
            pro_get = (fah // pro_ex) * ex_get #ขวดที่ได้
            all_milk += pro_get 
            fah = fah % pro_ex #กลายเป็นเศษฝา
            fah += pro_get
        else:
            break
    print(all_milk)
main()
