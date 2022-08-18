"""Nearer"""
def main():
    """Main Function"""
    alice = int(input())
    bob = int(input())
    iceman = int(input())
    if abs(iceman - alice) < abs(iceman - bob):
        print("Alice %d" %abs(iceman-alice))
    elif abs(iceman - alice) > abs(iceman - bob):
        print("Bob %d" %abs(iceman-bob))
    elif abs(iceman - alice) == abs(iceman - bob):
        print("Sundaes %d" %abs(iceman-bob))
main()
