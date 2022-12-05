def lagrange(p):
    somme = [0]
    for i in range(len(p)) :
        produit = [1]
        for j in range(len(p)) :
            if i!= j :
                produit = multiplication(produit, [1/(p[i][0] - p[j][0]), -(p[j][0]/(p[i][0] - p[j][0]))])
        produit = multiplication(produit, [p[i][1]])
        somme = addition(somme, produit)
    return reversed(somme)

def addition(a,b):
    m = max(len(a),len(b))
    s0 = [0 for k in range(m)]
    for k in range(m):
        if (k<len(a)):
            s0[k] += a[k]
        if (k<len(b)):
            s0[k] += b[k]
    return remove_zeros(s0)


def remove_zeros(p):
     m = len(p)
     n = 1
     while n<=m and p[-n] == 0:
        n += 1
     return p[:m-n+1]

def multiplication(a,b): 
    prod = [0]*(len(a) + len(b) -1)
    for k in range(len(a)):
       for l in range(len(b)):
            prod[k+l] +=  a[k]*b[l] 
    return prod
            
def evaluationPolynome(polynome, x):
    resultat = 0
    for idx, v in enumerate(polynome):
        resultat += v * pow(x,idx)
    return resultat

def pol_string(p):
    s = ''
    for l,k in enumerate(p):
        if k != 0:
            if k < 0:
               s += ' '  
            elif l > 0 and k > 0:
               s += ' + '              
            if l == 0: s += str(k)
            else:
               if k != 1 : s+= str(k)+'*'
               if l == 1: s += 'x '
               if l >1: s += 'x^' + str(l)
    return s

def main():
    p = [62,34,13]
    points = [
        [29, evaluationPolynome(p, 29)],
        [42, evaluationPolynome(p, 42)],
        [71, evaluationPolynome(p, 71)]
    ]
    print(pol_string(lagrange(points)))

if __name__ == "__main__":
    main()
