"""Circular II"""
from math import sqrt


def main():
    """Main function"""
    m_x = float(input())
    m_y = float(input())
    m_r = float(input())
    f_x = float(input())
    f_y = float(input())
    f_r = float(input())
    #คำณวนหาระยะห่าง ของสองจุด
    distance = sqrt(((m_x - f_x)**2) + ((m_y - f_y)**2))
    #print(distance)
    if m_r + f_r > distance:
        print("Yes")
    else:
        print("No")
main()

    