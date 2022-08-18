"""Saitama"""
def high(num1, num2):
    """Find the highest day to reach"""
    if num1 >= num2:
        return num1
    else:
        return num2
def main():
    """Main Function"""
    r_push = int(input())
    r_situp = int(input())
    r_squat = int(input())
    r_run = int(input())
    d_push = int(input())
    d_situp = int(input())
    d_run = int(input())
    d_squat = int(input())

    push_day = r_push // d_push + (r_push % d_push > 0)
    situp_day = r_situp // d_situp + (r_situp % d_situp > 0)
    squat_day = r_squat // d_squat + (r_squat % d_squat > 0)
    run_day = r_run // d_run + (r_run % d_run > 0)
    print(int(high(high(high(push_day, situp_day), squat_day), run_day)))
main()

