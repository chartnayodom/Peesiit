"""RuleofThree"""
def main():
    """Main Function"""
    unit = int(input())
    best = float("-inf")
    best_net = float("-inf")
    best_size_per_price = float("-inf")
    for _ in range(unit):
        price = float(input())
        net = float(input())
        net_price = net / price
        #print(net_price)
        if net_price > best_size_per_price:
            best = price
            best_net = net
            best_size_per_price = net_price
        elif net_price == best_size_per_price and price < best:
            best = price
            best_net = net
            best_size_per_price = net_price
    print("%.02f %.02f" %(best, best_net))
main()
