"""Vote"""
def main():
    """Main Function"""
    total = float(input())
    high = float(input())
    score_left = total - high
    if score_left <= high:
        low = 0
    else:
        low = score_left - high
    #คะแนนศุงสุดห่างจากต่ำสุดเกิน2
    if high - low > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
