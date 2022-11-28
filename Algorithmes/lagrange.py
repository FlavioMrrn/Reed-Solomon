def lagrange(points):
    resultats = ""
        

def evaluationPolynome(polynome, x):
    resultat = 0
    for idx, v in enumerate(polynome):
        resultat += v * pow(x,idx)
    return resultat


def main():
    print(evaluationPolynome([1,2,3], 4))

if __name__ == "__main__":
    main()
