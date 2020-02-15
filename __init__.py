#My Packages
try:
    from mypackages.mypackages import even
except:
    pass
try:
    from mypackages.mypackages import sort
except:
    pass
try:
    from mypackages.mypackages import sort_by_length
except:
    pass
try:
    from mypackages.mypackages import minimum
except:
    pass
try:
    from mypackages.mypackages import maximum
except:
    pass

#Fractions
try:
    from mypackages.frac import frac
except:
    pass
try:
    from mypackages.frac import addFrac
except:
    pass
try:
    from mypackages.frac import subFrac
except:
    pass
try:
    from mypackages.frac import multFrac
except:
    pass
try:
    from mypackages.frac import divFrac
except:
    pass
try:
    from mypackages.frac import powerFrac
except:
    pass

functions = ['even', 'sort', 'sort_by_length', 'minimum', 'maximum', 'frac', 'addFrac', 'subFrac', 'multFrac', 'divFrac', 'powerFrac']
exp = ["'even' bepaalt of een getal even is of niet.", "'sort' sorteert een lijst numerisch of alfabetisch.", "'sort_by_length' sorteert een lijst op basis van lengte.", "'minimum' geeft de kleinste waarde in een lijst.", "'maximum' geeft de grootste waarde in een lijst.", "'frac' verandert een getal in een breuk."]
def info(*keyword):
    if keyword == ():
        print()
        print('='*34 + ' Functions ' + '='*35)
        for function in functions:
            print(function)
        print('='*80)
    else:
        keyword = str(keyword)
        keyword = keyword[2:len(keyword)-3]
        for i in range (0, len(functions)):
            if keyword == functions[i]:
                print('='*80)
                print()
                print(exp[i])
                print()
                print('='*80)
                break
        else:
            print("'" + str(keyword) + "' is geen bestaande functie.")
