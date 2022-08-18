"""LasStand"""
import json
def main():
    """main"""
    wer = json.loads(input())
    for i in wer:
        #print(i)
        print(i%10)
main()
