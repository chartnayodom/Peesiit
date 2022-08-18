"""Lotto"""
def main():
    """Main function"""
    first_reward = input()
    last_2 = input()
    first_3_1 = input()
    first_3_2 = input()
    last_3_1 = input()
    last_3_2 = input()
    lotto = input()
    al_first_1 = ""
    al_first_2 = ""
    if first_reward == "000000":
        al_first_1 = "000001"
        al_first_2 = "999999"
    elif first_reward == "999999":
        al_first_1 = "000000"
        al_first_2 = "999998"
    else:
        al_first_1 = "%06d" %(int(first_reward) + 1)
        al_first_2 = "%06d" %(int(first_reward) - 1)
    reward = 0
    if lotto == first_reward:
        reward += 6000000
    if lotto == al_first_1 or lotto == al_first_2:
        reward += 100000
    if lotto[-2:] == last_2:
        reward += 2000
    if lotto[:3] == first_3_1:
        reward += 4000
    if lotto[:3] == first_3_2:
        reward += 4000
    if lotto[-3:] == last_3_1:
        reward += 4000
    if lotto[-3:] == last_3_2:
        reward += 4000

    print(reward)
main()
