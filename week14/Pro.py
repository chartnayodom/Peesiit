"""Pro"""
def main():
    """psit"""
    pro_many = int(input())
    pro_left = int(input())
    priceperone = int(input())
    many_come = int(input())
    total = 0
    t_pro = many_come // pro_many
    total += (pro_left * priceperone) * t_pro
    total += (many_come % pro_many) * priceperone
    print(total)
main()
