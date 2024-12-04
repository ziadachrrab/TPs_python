# ex1

l= [1,2,3,4]
def somme_liste(l):
    s=0
    for i in l:
        s+=i
    print(s)    

somme_liste(l)
# --------------------------------------------------------------------------
# ex2

tpl = (1,15,2,4,16)
def max_tpl(var):
    return max(var)

print(max_tpl(tpl))
# --------------------------------------------------------------------------
# ex3

ensemble1 = {1,5,4,5,6,8,7,99,15}
ensemble2 = {2,5,4,7,8,9,1,3,6,4,7,8,9,8,99}
def intersection_ensemble(en1, en2):
    return en1& en2
result = intersection_ensemble(ensemble1, ensemble2)
print(result)
# --------------------------------------------------------------------------
# ex4

words = ["ziad", "ali", "ayman", "ziad", "kali"]
def compte_occurences(list):
    occurrences = {}
    for mot in list:
        if mot in occurrences:
            occurrences[mot] += 1
        else :
            occurrences[mot] = 1
    return occurrences

result = compte_occurences(words)
print(result)
# --------------------------------------------------------------------------
# ex5

def factorielle(nbr):
    if nbr == 0 or nbr == 1:
        return 1
    else:
        return nbr * factorielle(nbr - 1)
    
print(factorielle(9))
# --------------------------------------------------------------------------
# ex6

carre = lambda x:x ** 2
print(carre(6))
# --------------------------------------------------------------------------
# ex7

def salutation(nom, message="Bonjour"):
    print(f"{message}, {nom}")

salutation("Ziad")
# --------------------------------------------------------------------------
# ex8

def somme_varargs(*args):
    return sum(args)

print(somme_varargs(1,2,5,8))
# --------------------------------------------------------------------------
# ex9
def analyse_texte(text):
    mots = text.split()
    nbr_mots = len(mots)
    nbr_carac = len(text)
    return {
        "Nombre mots: ": nbr_mots,
        "Nombre caractes: ": nbr_carac
    }

text = "The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets."
result = analyse_texte(text)
print(result)
# --------------------------------------------------------------------------
# ex10

def fusionner_dicts(dict1, dict2):
    fusion = dict1.copy()
    for key, value in dict2.items():
        if key in fusion:
            fusion[key] += value
        else:
            fusion[key] = value
    return fusion

dict1 = {'a':1, 'b':5, 'c':95, 'd':6 }
dict2 = {'c':5, 'e':5, 'f':45, 'g':64 }
result  = fusionner_dicts(dict1, dict2)
print(result)