tab = [] # Déclaration d'une table pour recevoir les notes

note, nbrNote, somNote, moyenne = 0, 0, 0, 0
  
while note >= 0 and note <= 20 and (nbrNote + 1) < 4 :
    try:
        note  = float(input("Saisir la note " +str(int(nbrNote + 1)) + " : "))
    except:
        print('Input invalide, veuillez saisir un nombre compris entre 0 et 20.')
        continue
    if note >= 0 and note <= 20 :
        nbrNote += 1
        somNote += note
        tab.append(note)
        
print("Vous avez saisie : ", nbrNote, " notes")

for j in tab:
    print("%0.2f" % j, end = ' ') # Affichage de chaque valeur du tableau  
    
print()

moyenne = (somNote / nbrNote)

print("La moyenne des notes saisies est : ", "%0.2f" % moyenne)

if moyenne >= 14 :
    print("Cet étudiant est admis !")
else :
    print("Cet étudiant est recalé !")