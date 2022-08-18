"""[Midterm] Turnstile"""
def main():
    """Main function"""
    status = 0
    pa_s = 0
    while True:
        state = input()
        if state == 'P':
            #DO something
            if status == 0:
                continue
            else:
                pa_s += 1
                status = 0
        elif state == 'C':
            if status == 0:
                status += 1
            else:
                continue
        elif state == 'END':
            break
    print(pa_s)
main()
