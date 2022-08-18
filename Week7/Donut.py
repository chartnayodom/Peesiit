"""Donut"""
def main():
    """main Function"""
    price_d = int(input())
    promotion_d = int(input())
    free_d = int(input())
    expected_d = int(input())

    sum_pro_free = promotion_d + free_d #รวมแถมแต่ละรอบ
    amount_pro = expected_d // sum_pro_free #ได้โปรกี่นอบ
    remnant = expected_d % sum_pro_free

    if remnant != 0:
        amount1 = ((amount_pro+1)*promotion_d)*price_d
        amount2 = ((amount_pro*promotion_d)+remnant)*price_d
        if amount1 > amount2:
            if remnant % promotion_d != 0:
                get = ((amount_pro+(remnant//promotion_d))*sum_pro_free)+remnant%promotion_d
                print("%d %d"%(amount2, get))
            elif remnant % promotion_d:
                get = (amount_pro*sum_pro_free)+remnant
                print("%d %d"%(amount2, get))
        elif amount1 <= amount2:
            get = (amount_pro+1)*sum_pro_free
            print("%d %d"%(amount1, get))
    elif remnant == 0:
        get = amount_pro*sum_pro_free
        pay = amount_pro*promotion_d
        print("%d %d"%(pay*price_d, get))
main()
