import datetime
import ändra_terminalsaker as tfärg
import os

from läs_loggar import läs_senase_timmens_loggar
from viktiga_konstanter import PATH

def logga_input_från_användare(data):

    tid = datetime.datetime.now()
    tid_sträng = tid.strftime('%Y-%m-%d-%H-%M')
    print(tid_sträng)
    filnamn = f"{tid_sträng}.txt"

    if os.path.exists(f"{PATH}{filnamn}"):
        pass
    else:
        with open(f"{PATH}{filnamn}", "w", encoding="utf-8") as f:
            pass

    with open(f"{PATH}{filnamn}", "a", encoding="utf-8") as f:
        f.write(f"{tfärg.röd_färg(tid)} | {data}\n")


def kör_program():
    while True:
        print("1. Skriv ut något!")
        print("2. Ändra färg i terminalen!")
        print("3. Reset!")
        print("4. Skriv ut logg")
        print("5. Avsluta")
        val = input("Gör ett val: ")
        logga_input_från_användare(val)

        if val == "1":
            print(input("Skriv något"))

        elif val == "2":
            färg = input("Ange färg röd,grön,gul eller blå:")

            if tfärg.ansätt_färg_i_terminalen(färg):
                nu = str(datetime.datetime.now())
                orange_nu = tfärg.orange_färg(nu)

                print(f"Färg ansatt i terminalen! Ändring skedde {orange_nu}")
                
                tfärg.ansätt_färg_i_terminalen(färg)
            else:
                print("Gick inte att ändra färg!")

        elif val == "3":
            tfärg.reset_terminal()

        elif val == "4":
            läs_senase_timmens_loggar()

        elif val == "5":
            break

        else:
            val = tfärg.röd_färg(val)
            print(f"Ogiltligt val {val}! Försök igen")

if __name__ == "__main__":
    print(f"program.py har {__name__=}")
    # print(tfärg.__name__)
    kör_program()
    tfärg.reset_terminal()
