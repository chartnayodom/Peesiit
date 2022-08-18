"""ValidVar"""
def restrict(vari):
    """Restrict condition"""
    import string
    punc = string.punctuation.replace("_", "")+string.whitespace
    num_first_letter = vari[0].isnumeric()
    ban_word = " if else elif while for True False continue break return is in and or from as "
    ban_word += " pass not def None "
    for pun in punc:
        if pun in vari:
            return False
    if num_first_letter:
        return False
    if " %s " % vari in ban_word:
        return False
    if len(vari) == 0:
        return False
    return True

def main():
    """Main Function"""
    h_many = int(input())
    for _ in range(h_many):
        if restrict(input().strip()):
            print("Valid")
        else:
            print("Invalid")
main()
