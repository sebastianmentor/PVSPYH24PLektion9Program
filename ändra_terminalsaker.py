import termcolor

RÖD = "\033[31m" #för röd text
GRÖN = "\033[32m" #för grön text
GUL = "\033[33m" #för gul text
BLÅ = "\033[34m" #för blå text
RESET = "\033[0m" #för att återställa standardfärgen


def röd_färg(text):
    return termcolor.colored(text,'red')

def blå_färg(text):
    return termcolor.colored(text,'blue')

def gul_färg(text):
    return termcolor.colored(text,'yellow')

def grön_färg(text):
    return termcolor.colored(text,'green')

def orange_färg(text):
    return "\033[38;5;214m" + text + RESET

def ansätt_färg_i_terminalen(färg):
    if färg == "röd":
        print(RÖD, end='',sep='')

    elif färg == "grön":
        print(GRÖN, end='',sep='')

    elif färg == "gul":
        print(GUL, end='',sep='')

    elif färg == "blå":
        print(BLÅ, end='',sep='')

    else:
        return False
    
    return True

def reset_terminal():
    print(RESET, end='',sep='')


print(f"ändra_terminalsaker har {__name__=}")
if __name__ == "__main__":
    print(röd_färg("röd färg"))
    print(blå_färg("blå färg"))

    while True:
        v = input("Skriv något elle q för att avsluta!")
        if v in ['röd', 'grön', 'gul', 'blå']:
            ansätt_färg_i_terminalen(v)
        elif v == 'q':
            break

        print(v)

    reset_terminal()