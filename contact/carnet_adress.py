import os
import json

# Nom du fichier pour sauvegarder les contacts
FICHIER_CONTACTS = "contacts.json"

def charger_contacts():
    """
    Charge les contacts depuis le fichier JSON
    """
    try:
        if os.path.exists(FICHIER_CONTACTS):
            with open(FICHIER_CONTACTS, 'r', encoding='utf-8') as fichier:
                return json.load(fichier)
        else:
            return {}
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️  Erreur lors du chargement du fichier. Nouveau carnet créé.")
        return {}

def sauvegarder_contacts(contacts):
    """
    Sauvegarde les contacts dans le fichier JSON
    """
    try:
        with open(FICHIER_CONTACTS, 'w', encoding='utf-8') as fichier:
            json.dump(contacts, fichier, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")
        return False

def ajouter_contact(contacts):
    """
    Ajoute un nouveau contact au carnet d'adresses
    """
    print("\n" + "="*50)
    print("         📝 AJOUTER UN CONTACT")
    print("="*50)
    
    nom = input("Nom du contact : ").strip()
    
    if not nom:
        print("❌ Le nom ne peut pas être vide !")
        return contacts
    
    # Vérifier si le contact existe déjà
    if nom.lower() in [n.lower() for n in contacts.keys()]:
        print(f"⚠️  Le contact '{nom}' existe déjà !")
        choix = input("Voulez-vous le modifier ? (o/n) : ").lower()
        if choix not in ['o', 'oui', 'y', 'yes']:
            return contacts
    
    telephone = input("Numéro de téléphone : ").strip()
    
    if not telephone:
        print("❌ Le numéro de téléphone ne peut pas être vide !")
        return contacts
    
    # Validation basique du numéro
    if not any(c.isdigit() for c in telephone):
        print("⚠️  Le numéro semble invalide, mais il sera quand même enregistré.")
    
    # Ajouter des informations supplémentaires (optionnel)
    email = input("Email (optionnel) : ").strip()
    adresse = input("Adresse (optionnel) : ").strip()
    
    # Créer le contact
    contact_info = {
        "telephone": telephone,
        "email": email if email else "",
        "adresse": adresse if adresse else ""
    }
    
    contacts[nom] = contact_info
    
    if sauvegarder_contacts(contacts):
        print(f"✅ Contact '{nom}' ajouté avec succès !")
    else:
        print("❌ Erreur lors de la sauvegarde !")
    
    return contacts

def rechercher_contact(contacts):
    """
    Recherche un contact par nom
    """
    print("\n" + "="*50)
    print("         🔍 RECHERCHER UN CONTACT")
    print("="*50)
    
    if not contacts:
        print("📭 Aucun contact dans le carnet d'adresses.")
        return
    
    nom_recherche = input("Nom à rechercher : ").strip()
    
    if not nom_recherche:
        print("❌ Veuillez saisir un nom à rechercher !")
        return
    
    # Recherche exacte
    contact_trouve = None
    for nom, info in contacts.items():
        if nom.lower() == nom_recherche.lower():
            contact_trouve = (nom, info)
            break
    
    if contact_trouve:
        nom, info = contact_trouve
        print(f"\n✅ Contact trouvé :")
        print("-" * 30)
        print(f"📝 Nom : {nom}")
        print(f"☎️  Téléphone : {info['telephone']}")
        if info.get('email'):
            print(f"📧 Email : {info['email']}")
        if info.get('adresse'):
            print(f"🏠 Adresse : {info['adresse']}")
    else:
        # Recherche partielle
        resultats_partiels = []
        for nom, info in contacts.items():
            if nom_recherche.lower() in nom.lower():
                resultats_partiels.append((nom, info))
        
        if resultats_partiels:
            print(f"\n🔍 Aucun contact exact trouvé, mais voici les résultats similaires :")
            print("-" * 50)
            for nom, info in resultats_partiels:
                print(f"📝 {nom} - ☎️  {info['telephone']}")
        else:
            print(f"❌ Aucun contact trouvé pour '{nom_recherche}'")

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
    print("-" * 60)
    
    # Trier les contacts par ordre alphabétique
    contacts_tries = sorted(contacts.items())
    
    for i, (nom, info) in enumerate(contacts_tries, 1):
        print(f"{i:2d}. 📝 {nom}")
        print(f"     ☎️  {info['telephone']}")
        if info.get('email'):
            print(f"     📧 {info['email']}")
        if info.get('adresse'):
            print(f"     🏠 {info['adresse']}")
        print()

def supprimer_contact(contacts):
    """
    Supprime un contact du carnet d'adresses
    """
    print("\n" + "="*50)
    print("         🗑️  SUPPRIMER UN CONTACT")
    print("="*50)
    
    if not contacts:
        print("📭 Aucun contact à supprimer.")
        return contacts
    
    nom_a_supprimer = input("Nom du contact à supprimer : ").strip()
    
    if not nom_a_supprimer:
        print("❌ Veuillez saisir un nom !")
        return contacts
    
    # Recherche du contact
    contact_a_supprimer = None
    for nom in contacts.keys():
        if nom.lower() == nom_a_supprimer.lower():
            contact_a_supprimer = nom
            break
    
    if contact_a_supprimer:
        print(f"\n📝 Contact à supprimer : {contact_a_supprimer}")
        print(f"☎️  Téléphone : {contacts[contact_a_supprimer]['telephone']}")
        
        confirmation = input("\n⚠️  Êtes-vous sûr de vouloir supprimer ce contact ? (o/n) : ").lower()
        
        if confirmation in ['o', 'oui', 'y', 'yes']:
            del contacts[contact_a_supprimer]
            if sauvegarder_contacts(contacts):
                print(f"✅ Contact '{contact_a_supprimer}' supprimé avec succès !")
            else:
                print("❌ Erreur lors de la sauvegarde !")
        else:
            print("❌ Suppression annulée.")
    else:
        print(f"❌ Aucun contact trouvé pour '{nom_a_supprimer}'")
    
    return contacts

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

def afficher_statistiques(contacts):
    """
    Affiche les statistiques du carnet d'adresses
    """
    print("\n" + "="*50)
    print("           📊 STATISTIQUES")
    print("="*50)
    
    nb_contacts = len(contacts)
    nb_avec_email = 0
    nb_avec_adresse = 0
    
    for contact in contacts.values():
        if contact.get('email'):
            nb_avec_email += 1
        if contact.get('adresse'):
            nb_avec_adresse += 1
    
    print(f"📞 Nombre total de contacts : {nb_contacts}")
    print(f"📧 Contacts avec email : {nb_avec_email}")
    print(f"🏠 Contacts avec adresse : {nb_avec_adresse}")
    
    if nb_contacts > 0:
        completude = ((nb_avec_email + nb_avec_adresse) / (nb_contacts * 2) * 100)
        print(f"📈 Complétude moyenne : {completude:.1f}%")

def main():
    """
    Programme principal
    """
    print("🎉 Bienvenue dans votre carnet d'adresses !")
    
    # Charger les contacts au démarrage
    contacts = charger_contacts()
    
    while True:
        afficher_menu()
        
        try:
            choix = input("Votre choix : ").strip()
            
            if choix == "1":
                contacts = ajouter_contact(contacts)
            elif choix == "2":
                rechercher_contact(contacts)
            elif choix == "3":
                afficher_tous_contacts(contacts)
            elif choix == "4":
                contacts = supprimer_contact(contacts)
            elif choix == "5":
                afficher_statistiques(contacts)
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

# Lancement du programme
if __name__ == "__main__":
    main()