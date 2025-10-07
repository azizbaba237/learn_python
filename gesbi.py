"""GESTION DE BIBLIOTHEQUE

Returns:
    Gestion: gerer une bibliotheque : afficher tous les livres, ajouter un livre, emprunter un livre, retourner un livre
"""
import json 
import os 

BIBLIOTHEQUE = "bibliotheque.json"

class Livre: 
    def __init__(self, titre: str, auteur: str, nombre_pages: int, année_publication: int, disponible: bool = True):
        self.titre = titre
        self.auteur = auteur
        self.nombre_pages = nombre_pages
        self.année_publication = année_publication
        self.disponible = disponible 
        
    def to_dict(self):
        """Convertir l'objet Livre en dictionnaire pour JSON"""
        return {
            'auteur': self.auteur,
            'nombre_pages': self.nombre_pages,
            'année_publication': self.année_publication,
            'disponible': self.disponible
        }
        
    def __str__(self):
        # Gestion de la disponibilité du livre 
        statut = "disponible" if self.disponible else "emprunté"
        return f"\n Titre : {self.titre} \n Auteur : {self.auteur} \n Nombre de pages : {self.nombre_pages} \n Année de publication : {self.année_publication} \n Statut : {statut}"

# Class Bibliotheque
class Bibliotheque:
    def __init__(self):
        # Initialiser la liste des livres
        self.LISTE_LIVRES = []
        self.charger_livres()
        
    # Charger tous les livres depuis le fichier JSON 
    def charger_livres(self):
        """Charger les livres depuis le fichier JSON"""
        try:
            if os.path.exists(BIBLIOTHEQUE):
                with open(BIBLIOTHEQUE, 'r', encoding='utf-8') as fichier:
                    data = json.load(fichier)
                    for titre, infos in data.items():
                        livre = Livre(
                            titre, 
                            infos['auteur'],
                            int(infos['nombre_pages']),
                            int(infos['année_publication']),
                            infos.get('disponible', True)
                        )
                        self.LISTE_LIVRES.append(livre)
                print(f"✅ {len(self.LISTE_LIVRES)} livre(s) chargé(s) depuis {BIBLIOTHEQUE}")
            else:
                print("ℹ️  Aucun fichier trouvé. Nouvelle bibliothèque créée.")
                
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"❌ Erreur de chargement : {e}")
        
    def sauvegarder_livres(self):
        """Sauvegarder tous les livres dans le fichier JSON"""
        try:
            data = {}
            for livre in self.LISTE_LIVRES:
                data[livre.titre] = livre.to_dict()
            
            with open(BIBLIOTHEQUE, 'w', encoding='utf-8') as fichier:
                json.dump(data, fichier, indent=4, ensure_ascii=False)
            print(f"✅ {len(self.LISTE_LIVRES)} livre(s) sauvegardé(s) dans {BIBLIOTHEQUE}")
            return True
            
        except Exception as e:
            print(f"❌ Erreur de sauvegarde : {e}")
            return False
        
    # Ajouter un livre 
    def ajouter_livre(self, livre: Livre):
        """Ajouter livre
        Args:
            livre (Livre): Ajouter les livres dans la bibliotheque
        """
        self.LISTE_LIVRES.append(livre)
        self.sauvegarder_livres()
        print(f"Le livre '{livre.titre}' de {livre.auteur} a été ajouté avec succès.")
        
    def ajouter_livre_interactif(self):
        """Permet d'ajouter un livre de maniere interactive"""
        while True:
            try:
                # Récupérer les informations du livre 
                titre = input("Entrez le titre du livre (ou 'q' pour quitter) : ").strip()
                if titre.lower() == 'q':
                    break
                
                # Si l'utilisateur n'entre pas de titre
                if not titre:
                    print("Il faut absolument un titre.")
                    continue
                
                auteur = input("Entrez le nom de l'auteur : ").strip()
                if not auteur:
                    print("Il faut le nom de l'auteur.")
                    continue
                
                nombre_pages = input("Entrez le nombre de pages : ").strip()
                if not nombre_pages.isdigit():
                    print("Le nombre de pages doit être un nombre entier.")
                    continue 
            
                annee_publication = input("Entrez l'année de publication : ").strip()
                if not annee_publication.isdigit():
                    print("L'année de publication doit être un nombre entier.")
                    continue 
                
                # Créer une instance de livre et l'ajouter à la bibliothèque
                livre = Livre(titre, auteur, int(nombre_pages), int(annee_publication))
                self.ajouter_livre(livre)
                
                continuer = input("Voulez-vous ajouter un livre (o/n) ? ").strip().lower()
                if continuer != 'o':
                    break
                
            except Exception as e:
                print(f"ERREUR : {e}")
    
    # Afficher tous les livres
    def afficher_livre(self):
        """Pour afficher tous les livres"""
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
    def chercher_livre(self, titre: str):
        """Chercher un livre par son titre"""
        count = 0
        livre_trouver = None
        
        # Trouver si le livre existe
        for livre in self.LISTE_LIVRES:
            if titre.lower() in livre.titre.lower():
                count += 1
                livre_trouver = livre 
        
        # Si le livre a été trouvé
        if livre_trouver:
            print("\n" + "=" * 40) 
            print(f"Le livre '{livre_trouver.titre}' a été trouvé : {livre_trouver}")
            print(f"\nNombre d'exemplaires trouvés : {count}")
            return livre_trouver
            
        # Si le livre n'existe pas 
        print(f"Le livre '{titre}' n'existe pas.")
        return None
        
    # Emprunter un livre 
    def emprunter_livre(self, titre: str):
        """Emprunter un livre"""
        # Chercher le livre
        livre = self.chercher_livre(titre)
        
        # Si le livre est trouvé et disponible
        if livre:
            if livre.disponible:
                livre.disponible = False
                self.sauvegarder_livres()
                print(f"✅ Le livre '{livre.titre}' a été emprunté avec succès.")
            # Si le livre n'est pas disponible 
            else:
                print(f"❌ Le livre '{livre.titre}' n'est pas disponible.")
        # Si le livre n'existe pas 
        else:
            print("❌ Le livre n'existe pas.")
            
    # Retourner un livre 
    def retourner_livre(self, titre: str):
        """Retourner un livre emprunté"""
        # Chercher le livre
        livre = self.chercher_livre(titre)

        # Si le livre est trouvé
        if livre:
            if not livre.disponible:
                livre.disponible = True
                self.sauvegarder_livres()
                print(f"✅ Le livre '{livre.titre}' a été retourné avec succès.")
            # Si le livre n'était pas prêté
            else:
                print(f"⚠️  Le livre '{livre.titre}' n'était pas emprunté.")
        # Si le livre n'existe pas
        else:
            print("❌ Le livre n'existe pas.")
    
    # Afficher le nombre de livres dans la bibliothèque 
    def __str__(self):
        return f"La Bibliothèque a {len(self.LISTE_LIVRES)} livre(s)."
    

# Main 
if __name__ == "__main__":
    
    # Créer une instance de la bibliothèque 
    ma_bibliotheque = Bibliotheque()
    
    # Ajouter quelques livres par défaut (seulement si la bibliothèque est vide)
    if len(ma_bibliotheque.LISTE_LIVRES) == 0:
        ma_bibliotheque.ajouter_livre(Livre("1984", "George Orwell", 250, 1949, True))
        ma_bibliotheque.ajouter_livre(Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96, 1943, False))
    
    # Menu interactif
    while True:
        print("\n=== MENU BIBLIOTHÈQUE ===")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Chercher un livre")
        print("4. Emprunter un livre")
        print("5. Retourner un livre")
        print("0. Quitter")
        
        choix = input("\nChoisissez une option : ").strip()
        
        if choix == '1':
            ma_bibliotheque.ajouter_livre_interactif()
        elif choix == '2':
            ma_bibliotheque.afficher_livre()
        elif choix == '3':
            nom_livre = input("Entrez le nom du livre que vous cherchez : ").strip()
            ma_bibliotheque.chercher_livre(nom_livre)
        elif choix == '4':
            nom_livre = input("Entrez le nom du livre que vous voulez emprunter : ").strip()
            ma_bibliotheque.emprunter_livre(nom_livre)
        elif choix == '5':
            nom_livre = input("Entrez le nom du livre que vous voulez remettre : ").strip()
            ma_bibliotheque.retourner_livre(nom_livre)
        elif choix == '0':
            print("Vous avez quitté le programme.")
            break 
        else:
            print("ERREUR : option invalide.")