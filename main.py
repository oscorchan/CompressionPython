chaine = "Ceci est un texte qui est un faux-texte"
texte2 = "Bonjour, je m'apelle oscar et j'aime beaucoup les chips. Les ananas sont délicieux. I ls cat"
texte3 = "je ne veux remplacer que les mots de plus de 3 caractères qui apparaissent au moins 2 fois"

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

def creerDictionnaireBasique(liste):
    n = 0
    dictionnaire = {}
    for i in liste:
        if i not in dictionnaire:
            dictionnaire[i] = n
            n += 1
        
    return dictionnaire

def creerDictionnaireAvance(liste):
    n = 0
    dictionnaire = {}
    for i in liste:
        strN = str(n)
        if i not in dictionnaire and len(i) > len(strN):
            dictionnaire[i] = n
            n = n+1
            
    return dictionnaire
    
def creerDictionnaireSuperAvance(liste):
    n = 0
    dictionnaire = {}
    for i in liste:
        cnt = liste.count(i)
        if i not in dictionnaire and cnt > 1 and len(i) > 3:
            dictionnaire[i] = n
            n = n+1
    
    return dictionnaire

liste = decoupage(texte3)

dicoSimple = creerDictionnaireBasique(liste)
dicoAvance = creerDictionnaireAvance(liste)
dicoSuperAvance = creerDictionnaireSuperAvance(liste)

print(dicoSuperAvance)