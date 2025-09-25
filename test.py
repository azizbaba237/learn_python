chemin = r"C:\Users\user\Desktop\doc\doc.txt"
with open(chemin, "r") as f :
    # Pour lire le fichier 
    contenu = f.read()
    print(contenu)
    
    # Pour ecrire dans le fichier :
        # - " w " ecris mais efface tout
        # - " a " ajoute a ce q ui existe deja
    # \n pour les retours a la ligne
    #f.write("\n Baba")
    
