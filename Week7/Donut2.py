"""[Midterm] Donut"""
#---ไว้สำหรับการคิด--
#เราก็เขียนลูปค่อยๆคิดคำณวน
#โดย
def main():
    """Main Function"""
    price = int(input())
    free_con = int(input())
    free_donut = int(input())
    require = int(input())
    total = 0
    get = 0
    use_pro = require//(free_con + free_donut) #จำนวนโปนที่เข้า
    set_pro = require%(free_con + free_donut) #เศษจากโปรโมชั่น
    if set_pro >= free_con: #ถ้าเศษมันมากกว่า หรือเท่ากับfree_con
        set_pro = free_con + free_donut
        all_price = free_con * price
    else:
        all_price = price * set_pro
    total = use_pro * free_con * price + all_price
    get = use_pro * (free_con + free_donut) + set_pro
    print(total, get)
main()
