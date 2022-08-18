"""Grade III"""
def main():
    """Main Function"""
    subject = int(input())
    sum_grade = 0
    #avg_grade = 0
    for _ in range(subject):
        score = float(input())
        if score >= 95 and score <= 100:
            sum_grade += 4
        elif score >= 90 and score < 95:
            sum_grade += 3.5
        elif score >= 85 and score < 90:
            sum_grade += 3
        elif score >= 80 and score < 85:
            sum_grade += 2.5
        elif score >= 75 and score < 80:
            sum_grade += 2
        elif score >= 70 and score < 75:
            sum_grade += 1.5
        elif score >= 65 and score < 70:
            sum_grade += 1
        elif score >= 60 and score < 65:
            sum_grade += 0.5
        elif score < 60 and score >= 0:
            sum_grade += 0
    ans = ((sum_grade / subject) * 100) // 1
    print("%.2f" %(ans / 100))
main()

