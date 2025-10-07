"""GESTION DE BIBLIOTHEQUE

    Returns:
        Gestion: gerer une bibliotheque : afficher tous les livres, ajouter un livre, empruter un livre, retourner un livre
"""
class Livre : 
    def __init__(self, titre: str, auteur: str, nombre_pages: int, année_publication : int, disponible: bool = True):
        self.titre = titre
        self.auteur = auteur
        self.nombre_pages = nombre_pages
        self.année_publication = année_publication
        self.disponible = disponible 
        
    def __str__(self) :
        # Gestion de la disponibilité du livre 
        statut = "disponible." if self.disponible else "emprunté."
        return f"\n Titre : {self.titre} \n Auteur : {self.auteur} \n Nombre de pages : {self.nombre_pages} \n Année de publication : {self.année_publication} \n Statut : {statut}"

# Class Bibliotheque
class Bibliotheque :
    def __init__(self) :
        # Initialiser la liste des livres
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
            try :
                # Récuprer les informations du livre 
                titre = input("Etrez le titre du livre ou ( q pour quitter ) : ").strip()
                if titre =='q':
                    break
                
                # Si l'utilisateur n'entre pas de titre
                if not titre :
                    print("Il faut abbsolument un titre.")
                    continue
                
                auteur = input("Entrez le nom de l'auteur : ").strip()
                if not auteur :
                    print("Il faut le nom de l'auteur. ")
                    continue
                
                nombre_pages = input("Entrez le nombre de pages : ").strip()
                if not  nombre_pages.isdigit() :
                    print("Le nombre de pages doit etre un nombre entier.")
                    continue 
            
                annee_publication = input("Entrez l'année de publication : ").strip()
                if not annee_publication.isdigit() :
                    print("L'année de publication doit etre un nombre entier.")
                    continue 
                
                # Créer une instance de livre et l'jouter a la bibliotheque
                livre = Livre(titre, auteur, int(nombre_pages), int(annee_publication))
                self.ajouter_livre(livre)
                
                continuer = input("Voulez-vous ajouter un livre o/n ? ").strip()
                if continuer != 'o':
                    break
                
            except Exception as e : 
                print(f"ERREUR : {e}")
    
    # Afficher tous les livres
    def afficher_livre(self):
        """ Pour afficher tous les livres """
        if not self.LISTE_LIVRES:
            print("La liste des livres est vide.")
            return
        
        print("\n" + "=" * 40)
        print(f"  LISTE DES LIVRES ({len(self.LISTE_LIVRES)} livre(s))")
        print("=" * 40)
        for i, livre in enumerate(self.LISTE_LIVRES, 1):
            print(f"{i}. {livre}")
        print("=" * 40 + "\n")
                

    # Chercher un livre 
    def chercher_livre(self, titre: str) :
        # chercher un livre par son titre 
        count = 0
        livre_trouver = None
        
        # Trouver si le livre existe
        for livre in self.LISTE_LIVRES :
            if titre.lower() in livre.titre.lower() :
                count += 1
                livre_trouver = livre 
        
        # si le livre a ete trouver 
        if livre_trouver :
            print("\n" + "=" * 40) 
            print(f"Le livre {livre_trouver.titre} a ete trouver : \n {livre_trouver}.")
            print(f"\n Nombre d'exemplaire trouver : {count}")
            return livre_trouver
            
        # si le livre n'existe pas 
        print(f"le livre {titre} n'existe pas.")
        return None
        
        
    # Emprunter un livre 
    def emprunter_livre(self, titre: str ) :
        # chercher le livre
        livre = self.chercher_livre(titre)
        
        # Si le livre est trouver et disponible
        if livre :
            if livre.disponible :
                livre.disponible = False
                print(f"Le livre {livre.titre} a ete emprunter avec succes. ")
            
            # si le livre n'est pas disponible 
            else :
                print(f"Le livre {livre.titre} n'est pas disponible")
        
        # Si le livre n'existe pas 
        else :
            print(f"Le livre n'existe pas.")
            
    # Rerourner un livre 
    def retourner_livre(self, titre: str) :
        # Chercher le livre
        livre = self.chercher_livre(titre)

        # Si le livre est trouver
        if livre:
            if not livre.disponible :
                livre.disponible = True
                print(f"Le livre {livre.titre} est ete retourner avec succes.")
            
            # Si le livre n'etait pas preter
            else :
                print(f"Le livre {livre.titre} n'etais pas preter.")
            
        # Si le livre n'existe pas
        else :
            print(f"Le livre {livre.titre} n'existe pas." )
    
    # Afficher le nombre de livre dans la bibliotheque 
    def __str__(self):
        return f"La Bibliotheque a : {len(self.LISTE_LIVRES)} livres."
    

# Main 
if __name__=="__main__":
    
    # Créer une instance de la bibliotheque 
    ma_bibliotheque = Bibliotheque()
    
    # Ajouter quelques livres par défaut
    ma_bibliotheque.ajouter_livre(Livre("1984", "George Orwell", 250, 1994, "disponible" ))
    ma_bibliotheque.ajouter_livre(Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 500, 1880,  "emprunter"))
    
    
# Menu interactif
    while True:
        print("\n=== MENU BIBLIOTHÈQUE ===")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Chercher un livre")
        print("4. Emprunter un livre")
        print("5. Retourner un livre")
        print("0. Quitter")
        
        choix = input("\nChoisissez une option: ").strip()
        
        if choix == '1':
            ma_bibliotheque.ajouter_livre_interactif()
        elif choix == '2' :
            ma_bibliotheque.afficher_livre()
        elif choix == '3' :
            nom_livre = input("Entrez le nom du livre que vous cherchez : ").strip()
            ma_bibliotheque.chercher_livre(nom_livre)
        elif choix == '4' :
            nom_livre = input("Entrez le nom du livre que vous voulez emprunter :").strip()
            ma_bibliotheque.emprunter_livre(nom_livre)
        elif choix == '5' :
            nom_livre = input("Entrez le nom du livre que vous voulez remttre : ").strip()
            ma_bibliotheque.retourner_livre(nom_livre)
        elif choix == '0' :
            print("Vous avez quitter le programme.")
            break 
        else :
            print("ERREUR : option invalide.")