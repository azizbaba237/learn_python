"""
    Gesbi
"""
class Livre : 
    def __init__(self, titre: str, auteur: str, disponible: bool = True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible 
        
    def __str__(self):
        statut = "disponible." if self.disponible else "emprunté."
        return f"Titre : {self.titre}, Auteur: {self.auteur}, Statut: {statut}"

class Bibliotheque :
    def __init__(self) :
        self.LISTE_LIVRES = []
        
    # Ajouter un livre 
    def ajouter_livre(self, livre: Livre) :
        """ajouter livre 

        Args:
            livre (Livre): Ajouter les livres dans la bibliotheque
        """
        self.LISTE_LIVRES.append(livre)
        print(f"Le livre {livre.titre} de {livre.auteur} a été ajouté avec succès.")
        
    def ajouter_livre_interactif(self) :
        # Permet d'ajouter un livre de maniere interactive    
        while True :
            titre = input("Etrez le titre du livre ou ( q pour quitter ) : ").strip()
            if titre =='q':
                break
            
            if not titre :
                print("Il faut abbsolument un titre.")
                continue
            
            auteur = input("Entrez le nom de l'auteur : ").strip()
            if not auteur :
                print("Il faut le nom de l'auteur. ")
                continue
                
            livre = Livre(titre, auteur)
            self.ajouter_livre(livre)
            
            continuer = input("Voulez-vous ajouter un livre o/n ? ").strip()
            if continuer != 'o':
                break
    def afficher_livre(self) :
        """ Pour afficher tous les livres """
        if not self.LISTE_LIVRES :
            print("La liste des livres est vide.")
            return 
            
        for i, livres in enumerate(self.LISTE_LIVRES, 1 ):
            print("\n=== LISTE DES LIVRES ===")
            print(f"{i}. {livres}")
            
    # Chercher un livre 
    def chercher_livre(self, titre: str) : 
        for livre in self.LISTE_LIVRES :
            if titre in self.LISTE_LIVRES:
                return livre
            return None
        
    # Emprunter un livre 
    def emprunter_livre(self, titre: str ) :
        livre = self.chercher_livrez(titre)
        if livre :
            if livre.disponible :
                livre.disponible = False
                print(f"Le livre {livre.titre} a ete emprunter avec succes. ")
            else :
                print(f"Le livre {livre.titre} n'est pas disponible")
        else :
            print(f"Le livre n'existe pas.")
            
    # Rerourner un livre 
    def retourner_livre(self, titre: str) :
        livre = self.chercher_livre(titre)
        if livre:
            if livre.disponible :
                livre.disponible = True
                print(f"Le livre {livre.titre} est ete retourner avec succes.")
            else :
                print(f"Le livre {livre.titre} n'etais pas preter.")
                
        else :
            print(f"Le livre {livre.titre} n'existe pas." )
    
    def __str__(self):
        return f"La Bibliotheque a : {len(self.LISTE_LIVRES())} livres."
    

# Main 
if __name__=="__main__":
    ma_bibliotheque = Bibliotheque()
     # Ajouter quelques livres par défaut
    ma_bibliotheque.ajouter_livre(Livre("1984", "George Orwell", "disponible" ))
    ma_bibliotheque.ajouter_livre(Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "emprunter"))
    
    
# Menu interactif
    while True:
        print("\n=== MENU BIBLIOTHÈQUE ===")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Emprunter un livre")
        print("4. Retourner un livre")
        print("5. Quitter")
        
        choix = input("\nChoisissez une option: ").strip()
        
        if choix == '1':
            ma_bibliotheque.ajouter_livre_interactif()
        elif choix == '2' :
            ma_bibliotheque.afficher_livre()
        elif choix == '3' :
            nom_livre = input("Entrez le nom du livre que vous cherchez : ").strip()
            ma_bibliotheque.chercher_livre(nom_livre)
        elif choix == '4' :
            nom_livre = input("Entrez le nom du livre que vous voulez remttre : ")
            ma_bibliotheque.retourner_livre(nom_livre)
        elif choix == '5' :
            print("Vous avez quitter le programme.")
            break 
        else :
            print("ERREUR : option invalide.")