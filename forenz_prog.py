__author__ = 'Jan'

dnk = open("dnk.txt", "r").read()

print "Lastnosti osumljene osebe glede na DNK so:"

#Barva las

if dnk.find ("CCAGCAATCGC") !=-1:
    barva_las = "crna"
    print "Crna barva las"
elif dnk.find ("GCCAGTGCCG") !=-1:
    barva_las = "rjava"
    print "Rjava barva las"
elif dnk.find ("TTAGCTATCGC") !=-1:
    barva_las = "oranzna"
    print "Oranzna barva las"

#Oblika obraza

if dnk.find ("GCCACG") !=-1:
    oblika_obraza = "kvadraten"
    print "Kvadraten obraz"
elif dnk.find ("ACCACAA") !=-1:
    oblika_obraza = "okrogel"
    print "Okrogel obraz"
elif dnk.find ("AGGCCTCA") !=-1:
    oblika_obraza = "ovalen"
    print "Ovalen obraz"

#Barva oci

if dnk.find ("TTGTGGTGGC") !=-1:
    barva_oci = "modra"
    print "Modre oci"
elif dnk.find ("GGGAGGTGGC") !=-1:
    barva_oci = "zelena"
    print "Zelene oci"
elif dnk.find ("AAGTAGTGAC") !=-1:
    barva_oci = "rjava"
    print "Rjave oci"

#Spol

if dnk.find ("TGCAGGAACTTC") !=-1:
    spol = "moski"
    print "Moski spol"
elif dnk.find ("TGAAGGACCTTC") !=-1:
    spol = "zenski"
    print "Zenski spol"

#Rasa

if dnk.find ("AAAACCTCA") !=-1:
    rasa = "belec"
    print "Belec"
elif dnk.find ("CGACTACAG") !=-1:
    rasa = "crnc"
    print "Crnc"
elif dnk.find ("CGCGGGCCG") !=-1:
    rasa = "azijec"
    print "Azijec"

#Baza osumljencev:

if spol == "moski" and rasa == "belec" and barva_las == "oranzna" and barva_oci == "rjava" and oblika_obraza == "okrogla":
    print "Sladoled je pojedel --> ZIGA <--"

elif spol == "moski" and rasa == "belec" and barva_las == "crna" and barva_oci == "modra" and oblika_obraza == "ovalna":
    print "Sladoled je pojedel --> MATEJ <--"

elif spol == "moski" and rasa == "belec" and barva_las == "rjava" and barva_oci == "zelena" and oblika_obraza == "kvadraten":
    print "Sladoled je pojedel --> MIHA <--"
