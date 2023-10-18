chaine = "Ceci est un texte qui est un faux-texte"
texte2 = "Bonjour, je m'apelle oscar et j'aime beaucoup les chips. Les ananas sont délicieux. I ls cat"
texte3 = "je ne veux remplacer que les mots de plus de 3 caractères qui apparaissent au moins 2 fois"
texte4 = "Cette fonction vous permet de voir quels mots apparaissent le plus souvent dans le texte, et s'il est efficace de les remplacer par une référence : par exemple, remplacer le mot 'un' par la référence '254' n'entraîne pas de gain de place, mais au contraire une perte !À partir de vos observations, construisez un dictionnaire plus riche que celui proposé en exemple, tester votre compression / décompression et regardez le gain de place.Il vous est également possible de générer automatiquement un dictionnaire de références à des contraintes de votre choix, par exemple .Il vous faut pour cela une fonction E qui prend en paramètre un dictionnaire de nombre d'apparition des mots, et qui retourne un dictionnaire de référence."

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

def assignation(liste, dictionnaire):
    result = []
    for i in liste:
        if (i in dictionnaire):
            result.append(str(dictionnaire.get(i)))
        else:
            result.append(i)
            
    return result

def assignationInverse(liste, dictionnaire):
    dictionnaire = inverserDictionnaire(dictionnaire)
    result = []
    print(dictionnaire)
    for i in liste:
        print(i)
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
            dictionnaire[i] = strN
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

def compresser(texte):
    liste = decoupage(texte)
    dictionnaire = creerDictionnaireAvance(liste)
    listeCompresse = assignation(liste, dictionnaire)
    texteCompresse = reconstitution(listeCompresse)
    
    return texteCompresse, dictionnaire

def decompresser(texte, dictionnaire):
    print(dictionnaire)
    liste = decoupage(texte)
    listeDecompressee = assignationInverse(liste, dictionnaire)
    texteDecompresse = reconstitution(listeDecompressee)
    
    print(texteDecompresse)
    return texteDecompresse

texteCompresse, dictionnaire = compresser(texte3)

decompresser(texteCompresse, dictionnaire)