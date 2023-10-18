chaine = "Ceci est un texte qui est un faux-texte"

dico = {'texte': '1',
 'lorem': '2',
 'qui': '3',
 'donc': '4',
 'est': '5',
 'que': '6',
 'pour': '7',
 'ceci': '8',
 'faux-texte': '9',
 'dans': '10',
 'plus': '11',
 'avec': '12'}

def decoupage(str):
    return str.split(' ')
    
def reconstitution(liste):
    sep = " "
    return sep.join(liste)

def compression(liste, dictionnaire):
    result = []
    for i in liste:
        if (i in dictionnaire):
            result.append(dictionnaire.get(i))
        else:
            result.append(i)
            
    return result

def decompression(liste, dictionnaire):
    dictionnaire = inverserDictionnaire(dictionnaire)
    result = []
    for i in liste:
        if (i in dictionnaire):
            result.append(dictionnaire.get(i))
        else:
            result.append(i)
            
    return result

def inverserDictionnaire(dictionnaire):
    inverse_dict = dict((v, k) for k, v in dictionnaire.items())
    return inverse_dict

print(decompression(compression(decoupage(chaine), dico), dico))