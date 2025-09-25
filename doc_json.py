import json 

chemin = r"C:\Users\user\Desktop\doc\doc.json"
# with open(chemin, "r") as f :
    
#     # Pour lire sans oublier le r
#     liste = json.load(f)
#     print(liste)
    
    # Pour ecrire : sans oublier le w 
    #json.dump(list(range(10)), f, indent=4)
    
# ----------------- Pour modifier les desonnes -----------------------
# On affiche d'abord le fichier existant
with open(chemin, "r") as f :
   
    donnees = json.load(f)
    print(donnees)
    
    # On ajoute ce que l'on souhaite 
    donnees.append("Banane")
    
# On ecrit en suite dans le fichier en question 
with open(chemin, "w") as f :
    json.dump(donnees, f)