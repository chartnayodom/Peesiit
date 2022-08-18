""""Milk"""


def main():
    """main func"""
    price_a = float(input())
    fah_b = int(input())
    get_b_c = int(input())
    bottle_d = int(input())
    get_d_e = int(input())
    money_f = float(input())
    get_bottle = int(money_f / price_a)
    bottle = get_bottle
    fah = get_bottle
    total = get_bottle
    while get_bottle > 0:
        sekfah = 0
        sekbot = 0
        bottle = get_bottle + sekbot
        fah = get_bottle + sekfah
        get_bottle = 0
        
        
        count = fah // fah_b
        sekfah = fah % fah_b
        get_bottle += count * get_b_c
        total += get_bottle

        count_b = bottle // bottle_d
        sekbot = bottle % bottle_d
        get_bottle += count_b * get_d_e
        total += get_bottle
         
        print(total)
main()