from models.banque import Banque


class Menu:
    """ Gère l'interface utilisateur """

    def __init__(self):
        self.banque = Banque("Banque Nationale")

    def afficher_menu(self):
        """ Affiche le menu principal """
        print("\\n" + "="*50)
        print("   GESTION DE COMPTE BANCAIRE")
        print("="*50)
        print(" 1. 📋 Afficher tous les comptes")
        print(" 2. ➕ Ouvrir un compte")
        print(" 3. 💰 Faire un dépôt")
        print(" 4. 💸 Faire un retrait")
        print(" 5. ℹ️  Voir les informations d'un compte")
        print(" 6. 📜 Voir l'historique des transactions")
        print(" 7. 📊 Afficher statistiques de la banque")
        print(" 8. 🔄 Faire un transfert")
        print(" 9. 🆔 Modifier un compte")
        print(" 10 ❌ Supprimer un compte")
        print(" 0. 🚪 Quitter le programme")
        print("="*50)

    def ouvrir_compte_interactif(self):
        """ Interface pour ouvrir un compte """
        print("\\n--- OUVERTURE DE COMPTE ---")
        numero_compte = input("Numéro de compte : ").strip()
        titulaire = input("Nom du titulaire : ").strip()

        try:
            solde = float(input("Solde initial : ").strip())
            succes, message = self.banque.ouvrir_compte(titulaire, numero_compte, solde)

            if succes:
                print(f"✔ {message}")
            else:
                print(f"❌ {message}")
        except ValueError:
            print("❌ Solde invalide")


    def modifier_compte_interactif(self):
        """ Modifier les comptes dans le fichier """
        print("\\n--- MODIFIER UN COMPTE ---")

        # Recuperation des donnees utilisateurs
        numero_compte = input("Le numero du compte que vous souaitez modifier :").strip()
        nouveau_titulaire = input("Le nouveau nom du titulaire : ").strip()

        try:
            succes, message = self.banque.modifier_compte(numero_compte, nouveau_titulaire)
            if succes:
                print(f" ✔ {message}")
            else :
                print(f" ❌ {message} ")
        except Exception as e:
            print(f" ❌ Erreur de modification : {e}")


    def supprimer_compte_interactif(self):
        """ Supprimer un compte du fichier """
        print("\\n--- SUPPRIMER COMPTE ---")

        # Recuperation du compte supprimer
        numero_compte = input("Le numero du compte que vous souhaitez supprimer : ").strip()

        # Si l'utilisateur n'entre rien
        if not numero_compte:
            print("Le numero est obligatoire")
            return

        # Chercher compte
        compte = self.banque.chercher_compte(numero_compte)

        # si le compte n'existe pas
        if not compte:
            print(f"Le compte No {numero_compte} n'existe pas.")
            return

        # Afficher les informations du compte a supprimer
        compte.get_infos()

        # Demander confirmation avant de supprimer
        confirmation = input("Voulez vous vraiment suppriler ce compte o/n ").strip().lower()
        if confirmation not in ['oui', 'o', 'y', 'yes']:
            print(f"Suppression du compte No {numero_compte} annulée.")
            return

        try :
            succes, message = self.banque.supprimer_compte(numero_compte)
            if succes:
                print(f" ✔ {message}")
            else:
                print(f" ❌ {message} ")
        except Exception as e:
            print(f" ❌ Erreur de suppression : {e}")


    def depot_interactif(self):
        """ Interface pour faire un dépôt """
        print("\\n--- DÉPÔT ---")

        numero_compte = input("Numéro de compte : ").strip()

        try:
            montant = float(input("Montant à déposer : ").strip())
            succes, message = self.banque.effectuer_depot(numero_compte, montant)

            if succes:
                print(f"✔ {message}")
            else:
                print(f"❌ {message}")
        except ValueError:
            print("❌ Montant invalide")

    def retrait_interactif(self):
        """ Interface pour faire un retrait """
        print("\\n--- RETRAIT ---")

        numero_compte = input("Numéro de compte : ").strip()

        try:
            montant = float(input("Montant à retirer : ").strip())
            succes, message = self.banque.effectuer_retrait(numero_compte, montant)

            if succes:
                print(f"✔ {message}")
            else:
                print(f"❌ {message}")
        except ValueError:
            print("❌ Montant invalide")

    def transfert_interactif(self):
        """ Interface pour faire un transfert """
        print("\\n--- TRANSFERT ---")

        numero_source = input("Compte source : ").strip()
        numero_dest = input("Compte destinataire : ").strip()

        try:
            montant = float(input("Montant à transférer : ").strip())
            succes, message = self.banque.transferer(numero_source, numero_dest, montant)

            if succes:
                print(f"✔ {message}")
            else:
                print(f"❌ {message}")
        except ValueError:
            print("❌ Montant invalide")

    def executer(self):
        """ Boucle principale du programme """
        print(f"\\n{'='*50}")

        print(f"Bienvenue à la {self.banque.nom_banque}")
        print('='*50)

        while True:
            self.afficher_menu()
            choix = input("\\nVotre choix : ").strip()

            if choix == '1':
                self.banque.lister_comptes()

            elif choix == '2':
                self.ouvrir_compte_interactif()

            elif choix == '3':
                self.depot_interactif()

            elif choix == '4':
                self.retrait_interactif()

            elif choix == '5':
                numero = input("Numéro de compte : ").strip()
                compte = self.banque.chercher_compte(numero)
                if compte:
                    compte.get_infos()
                else:
                    print(f"❌ Compte {numero} introuvable")

            elif choix == '6':
                numero = input("Numéro de compte : ").strip()
                self.banque.afficher_historique(numero)

            elif choix == '7':
                self.banque.obtenir_statistiques()

            elif choix == '8':
                self.transfert_interactif()

            elif choix == '9':
                self.modifier_compte_interactif()

            elif choix == '10':
                self.supprimer_compte_interactif()

            elif choix == '0':
                print("\\n👋 Au revoir !")
                break
            else:
                print("❌ Choix invalide")