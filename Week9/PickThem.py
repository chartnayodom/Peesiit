"""PickTHem"""
import json
def main():
    """main"""
    # das = input()
    sad = json.loads(input())
    das = []
    for i in sad:
        if i % 2 == 0:
            das.append(i)

    if len(das) == 0:
        print("Nope")
    else:
        for i in das:
            print(i)

main()
