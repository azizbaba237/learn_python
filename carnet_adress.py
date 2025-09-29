import json
import os 

FICHIERS_CONTACTS = "contacts.json"

def charger_contact() :
    """
        Charger les contacts depuis le fichier json 
    """
    try :
        if os.path.exists(FICHIERS_CONTACTS) :
            with open(FICHIERS_CONTACTS, 'r', encoding='utf-8') as fichier :
                return json.load(fichier)
        else :
            return {}
    
    except (json.JSONDecodeError, FileExistsError):
        print("Erreur de chargement... nouveau carnet d'adresse creer.")
        return {}

def sauvegarder_contact(contacts) :
    """
        Sauvegarder les contact dans le fichier JSON 

    Args:
        contact (int et str): pour enregistrer les donnees des contacts 
    """
    try :
        with open(FICHIERS_CONTACTS, 'w', encoding='utf-8') as fichier :
            json.dump(contacts, fichier, indent=4 , ensure_ascii= False)
            return True 
    
    except Exception as e :
        print(f"Erreur de sauvegarde : {e}")
        return False

def ajouter_contact(contacts):
    """
    Ajoute un nouveau contact au carnet d'adresses
    """
    print("\n" + "="*50)
    print("         📝 AJOUTER UN CONTACT")
    print("="*50)
    
    # Recuperer le nom 
    nom = input("Entrez votre nom : ").strip()
    
    if not nom :
        print("Le nom ne peut pas etre vide.")
        return contacts
    
    # Verifie si le contact existe deja 
    if nom.lower() in [n.lower() for n in contacts.keys()] :
        print(f"Le contact {nom} existe deja.")
        choix = input("Voulez vous le modifier o/n ?")
        if choix not in ['OUI', 'oui', 'o', 'O', 'YES', 'yes', 'y', 'Y']:
            return contacts
    
    # Recuperer me numero 
    telephone = input("Votre numero de telephone :").strip()
    
    if not telephone :
        print("Le numero ne peut pas etre vide.")
        return contacts
    
    if not any(c.isdigit() for c in contacts) :
        print("Le numero n est pas valide mais il sera quand meme enregistrer.")
        
    # Ajouter les infos supplementaire : optionnel 
    email = input("Entrez votre adresse mail ( Optionnel ) : ").strip()
    adresse = input("Entrez votre adresse ( Optionnel ) : ").strip()
    
    # Creation du contact 
    contact_infos = {
        "telephone":telephone,
        "email":email if email else '',
        "adresse":adresse if adresse else ''
    } 
    
    contacts[nom] = contact_infos
    
    if sauvegarder_contact(contacts) :
        print(f"La sauvegarde du contact de M/Mme {nom} a reussie.")
    else :
        print("La sauvagarde a echouée. ")
        
def afficher_tous_contacts(contacts):
    """
    Affiche tous les contacts du carnet d'adresses
    """
    print("\n" + "="*60)
    print("             📞 TOUS LES CONTACTS")
    print("="*60)
    
    if not contacts:
        print("📭 Le carnet d'adresses est vide.")
        return
    
    print(f"📊 Nombre total de contacts : {len(contacts)}")
    for nom, infos in contacts.items():
        print(f"- {nom}")
        print(f"  Téléphone : {infos.get('telephone', 'N/A')}")
        print(f"  Email     : {infos.get('email', 'N/A')}")
        print(f"  Adresse   : {infos.get('adresse', 'N/A')}")
        print("-" * 60)
    
def afficher_menu():
        """
        Affiche le menu principal
        """
        print("\n" + "="*60)
        print("                ☎️  CARNET D'ADRESSES")
        print("="*60)
        print("1. 📝 Ajouter un contact")
        print("2. 🔍 Rechercher un contact")
        print("3. 📞 Afficher tous les contacts")
        print("4. 🗑️  Supprimer un contact")
        print("5. 📊 Statistiques")
        print("0. 🚪 Quitter")
        print("-"*60)

# Main
def main() :
    """
    Programme principal
    """
    print("🎉 Bienvenue dans votre carnet d'adresses !")
    
    # Charger les contacts au démarrage
    contacts = charger_contact()
    
    while True:
        afficher_menu()
        
        try:
            choix = input("Votre choix : ").strip()
            
            if choix == "1":
                ajouter_contact(contacts)
                contacts = charger_contact(contacts)
            # elif choix == "2":
            #     rechercher_contact(contacts)
            elif choix == "3":
                contacts = charger_contact()
                afficher_tous_contacts(contacts)
            # elif choix == "4":
            #     contacts = supprimer_contact(contacts)
            # elif choix == "5":
            #     afficher_statistiques(contacts)
            elif choix == "0":
                print("\n👋 Au revoir ! Vos contacts sont sauvegardés.")
                break
            else:
                print("❌ Choix invalide ! Veuillez sélectionner une option du menu.")
            
            input("\n⏸️  Appuyez sur Entrée pour continuer...")
            
        except KeyboardInterrupt:
            print("\n\n👋 Programme interrompu. Au revoir !")
            break
        except Exception as e:
            print(f"❌ Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__" :
    main()
