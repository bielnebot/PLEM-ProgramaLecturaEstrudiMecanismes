import itertools

# enllaç ---> "e"
# pes ------> "p"
# actuador -> "a"
# força ----> "f"


def tuplaToStr(t):
    ll = list(t)
    ll = "".join(ll)
    return ll


# aquesta funció no està feta servir
def clausDicc():
    d = {}
    for llarg in range(1,5):
        ll = list(itertools.combinations('epaf', llarg))
        newLL = [tuplaToStr(x) for x in ll]
        d[llarg] = newLL
    return d   


def rangeNodes(nreSolids):
    # llNumeros = [str(i) for i in range(1,nreSolids+1)]
    llNumeros = [i for i in range(1,nreSolids+1)]
    # strNumeros = "".join(llNumeros)
    ll = list(itertools.combinations(llNumeros, 2))
    newLL = [(int(x[0]),int(x[1])) for x in ll]
    return ll


def diccToStr(diccCaracterEnllaç):
    ll = []
    for clau in diccCaracterEnllaç:
        ll.append(diccCaracterEnllaç[clau])
    return "\n".join(ll)


'''
1 :  ['e', 'p', 'a', 'f']
2 :  ['ep', 'ea', 'ef', 'pa', 'pf', 'af']
3 :  ['epa', 'epf', 'eaf', 'paf']
4 :  ['epaf']
'''
