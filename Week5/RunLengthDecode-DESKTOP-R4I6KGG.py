"""RunLengthdecode"""
def main():
    """Main Function"""
    cypher = input()
    time = ''
    enc = ''
    for i in range(0, len(cypher)):
        if cypher[i].isnumeric():

            time += cypher[i]
        elif cypher[i].isalpha():
            enc += cypher[i] * int(time)
            time = ''
        #print("%s" %(cypher[i+1]) * (int(cypher[i])), end="")
    print(enc)
main()
