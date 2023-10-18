def decoupage(str):
    return str.split(' ')
    
def reconstitution(liste):
    sep = " "
    return sep.join(liste)
    
    
chaine = "Bonjour, je m'apelle oscar"

print(decoupage(chaine))

print(reconstitution(decoupage(chaine)))