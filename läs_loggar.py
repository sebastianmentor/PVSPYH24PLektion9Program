import os
import datetime
from viktiga_konstanter import PATH


def läs_senase_timmens_loggar():
    now = datetime.datetime.now()
    
    en_timme_tillbaka = now - datetime.timedelta(hours=1)

    lista_med_filnamn = []
    
    for _ in range(61):
        filnamn = en_timme_tillbaka.strftime('%Y-%m-%d-%H-%M') + '.txt'
        lista_med_filnamn.append(filnamn)

        en_timme_tillbaka += datetime.timedelta(minutes=1)

    for filnamn in lista_med_filnamn:
        fil = f"{PATH}{filnamn}"
        if os.path.exists(fil):
            with open(fil, 'r', encoding='utf-8') as f:
                for logg in f:
                    print(logg.strip())


if __name__ == "__main__":
    läs_senase_timmens_loggar()