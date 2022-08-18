"""[Midterm] SecondConverter"""
def main():
    """Main Function"""
    k_s = int(input())
    sec = int(input())
    mins = int(input())
    hour = int(input())
    p_s = k_s % sec
    p_m = (k_s // sec) % mins
    p_h = ((k_s // sec) // mins) % hour
    print("%d:%d:%d" %(p_h, p_m, p_s))
main()
