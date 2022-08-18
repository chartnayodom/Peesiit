"""WeightStation"""
def main():
    """Main Function"""
    avge = float(input())
    mes_1 = float(input())
    mes_2 = float(input())
    mes_3 = float(input())
    total = avge * 4
    if total > 15000 :
        print("Overweight")
        return
    if abs(mes_1 - avge) > avge/2: 
        print("Unbalance")
        return
    if abs(mes_2 - avge) > avge/2 :
        print("Unbalance")
        return
    if abs(mes_3 - avge) > avge/2:
        print("Unbalance")
        return
    print("Pass %.2f" %(total - (mes_1 + mes_2 + mes_3)))
main()
