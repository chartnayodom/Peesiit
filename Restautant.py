"""Restaurant"""
def main():
    """Main function"""
    sam = float(input())
    pro = float(input())
    dis = float(input())
    rec = float(input())
    sum_rec = sam + rec
    #print(sum_rec)
    if sum_rec >= pro:
        sum_rec -= sum_rec*(dis/100)
    if sam >= pro:
        sam -= sam*(dis/100)
    #print(sum_rec)
    if sum_rec > sam:
        print("No %.03f" %(sum_rec - sam))
    elif sum_rec < sam:
        print("Yes %.03f" %(sam - sum_rec))
    else:
        print("Yes")
main()
