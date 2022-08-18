"""RunLengthdecode"""
def main():
    """Main Function"""
    cypher = input()
    for i in range(0, len(cypher), 2):
        print("%s" %(cypher[i+1]) * (int(cypher[i])), end="")

main()
