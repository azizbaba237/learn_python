"""
Analyse de texte 📝 : Demande à l'utilisateur de saisir une phrase.

Compter le nombre de mots.

Compter le nombre de voyelles.

Inverser la phrase et l'afficher.

Compétences travaillées : méthodes de chaînes de caractères (.split(), .lower()), boucles, et conditions.
"""
def analyser_texte():
    """
    Programme d'analyse de texte qui :
    - Compte le nombre de mots
    - Compte le nombre de voyelles
    - Inverse la phrase
    """
    
    print("=" * 50)
    print("       📝 ANALYSEUR DE TEXTE 📝")
    print("=" * 50)
    print()
    
    # Demander à l'utilisateur de saisir une phrase
    phrase = input("Veuillez saisir une phrase à analyser : ")
    print()
    
    # Vérifier que l'utilisateur a bien saisi quelque chose
    if not phrase.strip():
        print("❌ Erreur : Vous devez saisir au moins un caractère !")
        return
    
    print("🔍 RÉSULTATS DE L'ANALYSE :")
    print("-" * 30)
    
    # 1. Compter le nombre de mots
    nombre_mots = len(phrase.split())
    print(f"📊 Nombre de mots : {nombre_mots}")
    
    # 2. Compter le nombre de voyelles
    voyelles = "aeiouAEIOUàáâäèéêëìíîïòóôöùúûüÀÁÂÄÈÉÊËÌÍÎÏÒÓÔÖÙÚÛÜ"
    nombre_voyelles = sum(1 for caractere in phrase if caractere in voyelles)
    print(f"🔤 Nombre de voyelles : {nombre_voyelles}")
    
    # 3. Inverser la phrase
    phrase_inversee = phrase[::-1]
    print(f"🔄 Phrase inversée : '{phrase_inversee}'")
    
    print()
    print("✅ Analyse terminée !")
    
    # Proposer de refaire une analyse
    print()
    refaire = input("Voulez-vous analyser une autre phrase ? (o/n) : ").lower()
    if refaire in ['o', 'oui', 'y', 'yes']:
        print()
        analyser_texte()

def afficher_statistiques_detaillees(phrase):
    """
    Fonction bonus pour des statistiques plus détaillées
    """
    print("\n📈 STATISTIQUES DÉTAILLÉES :")
    print("-" * 35)
    
    # Caractères
    nb_caracteres = len(phrase)
    nb_caracteres_sans_espaces = len(phrase.replace(" ", ""))
    
    # Consonnes
    voyelles = "aeiouAEIOUàáâäèéêëìíîïòóôöùúûüÀÁÂÄÈÉÊËÌÍÎÏÒÓÔÖÙÚÛÜ"
    nb_consonnes = sum(1 for c in phrase if c.isalpha() and c not in voyelles)
    
    # Espaces et ponctuation
    nb_espaces = phrase.count(" ")
    nb_ponctuation = sum(1 for c in phrase if not c.isalnum() and not c.isspace())
    
    print(f"📏 Nombre total de caractères : {nb_caracteres}")
    print(f"📝 Caractères sans espaces : {nb_caracteres_sans_espaces}")
    print(f"🎵 Nombre de consonnes : {nb_consonnes}")
    print(f"⬜ Nombre d'espaces : {nb_espaces}")
    print(f"❗ Signes de ponctuation : {nb_ponctuation}")

def version_complete():
    """
    Version complète avec statistiques détaillées
    """
    
    print("=" * 60)
    print("       📝 ANALYSEUR DE TEXTE COMPLET 📝")
    print("=" * 60)
    print()
    
    phrase = input("Veuillez saisir une phrase à analyser : ")
    print()
    
    if not phrase.strip():
        print("❌ Erreur : Vous devez saisir au moins un caractère !")
        return
    
    # Analyses de base
    print("🔍 ANALYSES DE BASE :")
    print("-" * 25)
    
    nombre_mots = len(phrase.split())
    voyelles = "aeiouAEIOUàáâäèéêëìíîïòóôöùúûüÀÁÂÄÈÉÊËÌÍÎÏÒÓÔÖÙÚÛÜ"
    nombre_voyelles = sum(1 for caractere in phrase if caractere in voyelles)
    phrase_inversee = phrase[::-1]
    
    print(f"📊 Nombre de mots : {nombre_mots}")
    print(f"🔤 Nombre de voyelles : {nombre_voyelles}")
    print(f"🔄 Phrase inversée : '{phrase_inversee}'")
    
    # Statistiques détaillées
    afficher_statistiques_detaillees(phrase)
    
    print()
    print("✅ Analyse complète terminée !")

# Programme principal
if __name__ == "__main__":
    print("Choisissez le mode d'analyse :")
    print("1 - Analyse simple (requis)")
    print("2 - Analyse complète (avec statistiques détaillées)")
    
    choix = input("\nVotre choix (1 ou 2) : ")
    print()
    
    if choix == "1":
        analyser_texte()
    elif choix == "2":
        version_complete()
    else:
        print("❌ Choix non valide. Lancement de l'analyse simple...")
        print()
        analyser_texte()