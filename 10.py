nrgaini = int(input("dati numarul de gaini: "))
nrboabe = int(input("dati numarul de boabe: "))
if (nrboabe % nrgaini == 0):
    print("Fiecare gaina a primit ",nrboabe // nrgaini," boabe, iar curcanul nu a primit.")
elif (nrboabe % nrgaini !=0):
    if ((nrboabe % nrgaini) > (nrboabe // nrgaini)):
        print("Curcanul a primit cu ",nrboabe % nrgaini," boabe mai mult")
    if ((nrboabe % nrgaini) < (nrboabe // nrgaini)):
        print("Fiecare gaina a primit cu ",nrboabe // nrgaini," boabe mai mult")
    else:
        print("Numar egal")