"""
Code principale qui permet de déterminer si un mot est un palindrome 
"""
#### Fonction secondaire
def ispalindrome(p):
    """
    Fonction secondaire
    """
    # votre code ici
    p = p.lower()
    l = str.maketrans('éèàùêôëç','eeaueoec')
    p = p.replace(' ','')
    p = p.translate(l)
    v = ''
    for _, j in enumerate(p):
        if j.isalnum():
            v+=j
    print(v)
    if v != v[::-1]:
        return False
    print(v)
    return True
#### Fonction principale
def main():
    """
    Fonction principale
    """
    # vos appels à la fonction secondaire ici
    print('voiture', ispalindrome('voiture'))
    print('anticonstitutionnellement', ispalindrome('anticonstitutionnellement'))
    print('sos', ispalindrome('sos'))
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
