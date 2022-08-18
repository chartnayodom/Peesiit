"""Fever"""
def main():
    """Fever"""
    temp = float(input())
    if 40 <= temp <= 43:
        print("Very High Fever")
    elif 39 <= temp < 40:
        print("High Fever")
    elif 38 <= temp < 39:
        print("Mild Fever")
    elif 36 <= temp < 38:
        print("No Fever")

main()
