"""Music Lover"""
def main():
    """main"""
    music = {}
    pick = int(input())
    for _ in range(pick):
        answ = input()
        band = answ[:answ.index("-")]
        song = answ[answ.index("-") + 1:]
        # print(band, song)
        if band in music:
            music[band].append(song)
        else:
            music[band] = []
            music[band].append(song)

    for i in music:
        pleng = list(music[i])
        print(i)
        for j in pleng:
            print(j)
main()
