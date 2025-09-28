def analyser_text ():
    """
    - Compter le nombre de mot dans la phrase 
    - Compter le nombre de voyelle
    - inverser la phrase 
    """
    # Récuperer la phrase de l'utilisateur 
    phrase = input("Entrez votre phrase : ")
    
    # Verification: si l'utilisateur n'entre rien 
    if not phrase.strip() :
        print("Erreur : veuillez entrer quelque chose s'il vous plait : ")
        return 
    
    # Compter le nombre de mot dans la phrase 
    nombre_de_mot = len(phrase.split())
    print(f"Le nombre de mot dans votre phrase est : {nombre_de_mot}")
    
    # Compter nombre de voyelle dans la phrase 
    voyelle = "aeiouAEIOUàáâäèéêëìíîïòóôöùúûüÀÁÂÄÈÉÊËÌÍÎÏÒÓÔÖÙÚÛÜ"
    nombre_de_voyelle = sum(1 for caractere in phrase if caractere in voyelle)
    print(f"Le nombre de voyelle dans votre phrase est de {nombre_de_voyelle}")
    
    # Inverser la phrase 
    phrase_inversee = phrase[::-1]
    print(f"Votre phrase inversée est : {phrase_inversee}")
    
    print("Fin de l'analyse.")
    
    print('=' * 50)
    
    refaire = input("Voulez vous refaire une autre analyse o/n ? ")
    if refaire in ['o', 'YES', 'yes', 'y', 'oui', 'OUI'] :
        print()
        analyser_text()
        print("Fin de l'analyse. ") 
        

# Main 
if __name__ == "__main__":
    analyser_text()