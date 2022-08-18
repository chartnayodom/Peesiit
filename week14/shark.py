"""shark"""
def main():
    """main"""
    shark = {"THE SHALLOW ZONE":['BULL SHARK'],\
"THE TWILIGHT ZONE":['GREAT WHITE SHARK', 'CHAIN CATSHARK', 'GUMMY SHARK', 'MAKO SHARK',\
    'BLUE SHARK'],\
"THE MIDNIGHT ZONE":['FRILLED SHARK', 'GOBLIN SHARK', 'SIXGILL SHARK', 'GREENLAND SHARK',\
    'COOKIECUTTER SHARK'],
"THE ABYSSAL ZONE": ['MEGAMOUTH SHARK']}
    gotta = input()
    if gotta in shark["THE SHALLOW ZONE"]:
        print("THE SHALLOW ZONE")
    elif gotta in shark["THE TWILIGHT ZONE"]:
        print("THE TWILIGHT ZONE")
    elif gotta in shark["THE MIDNIGHT ZONE"]:
        print("THE MIDNIGHT ZONE")
    elif gotta in shark["THE ABYSSAL ZONE"]:
        print("THE ABYSSAL ZONE")
    else:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")

main()
