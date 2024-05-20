from kanren import run, var, fact, Relation, conde, lall


# Definir las relaciones
padres = Relation()

# Agregar hechos a la relación 'padres'
fact(padres, 'christian', 'pedro', 'veronica')
fact(padres, 'amilkar', 'pedro', 'veronica')
fact(padres, 'paola', 'pedro', 'veronica')
fact(padres, 'pedro', 'alberto', 'marta')
fact(padres, 'veronica', 'pablo', 'aida')
fact(padres, 'juan', 'alberto', 'marta')
fact(padres, 'lucia', 'pablo', 'aida')
fact(padres, 'enoc', 'eddy', 'lucia')
fact(padres, 'wilfredo', 'juan', 'silvia')

# Definir las reglas
def padre(P, H):
    M = var()
    return padres(H, P, M)

def madre(M, H):
    P = var()
    return padres(H, P, M)

def hermanos(H, E):
    P, M = var(), var()
    return lall(padres(H, P, M), padres(E, P, M))

def abuelopaterno(A, N):
    H = var()
    return lall(padre(A, H), padre(H, N))

def abuelomaterno(A, N):
    H = var()
    return lall(padre(A, H), madre(H, N))

def abuelapaterno(A, N):
    H = var()
    return lall(madre(A, H), padre(H, N))

def abuelamaterno(A, N):
    H = var()
    return lall(madre(A, H), madre(H, N))

def abuelos(N, AP, AM, AAP, AAM):
    return conde(
        (abuelopaterno(AP, N),),
        (abuelomaterno(AM, N),),
        (abuelapaterno(AAP, N),),
        (abuelamaterno(AAM, N),)
    )

def primospaternos(H, P):
    PA, X = var(), var()
    return lall(padre(PA, H), hermanos(X, PA), padre(X, P))

# Variables para consulta
N, AP, AM, AAP, AAM = var(), var(), var(), var(), var()
H, P = var(), var()

# Ejemplos de consultas
abuelos_result = run(0, (AP, AM, AAP, AAM), abuelos('christian', AP, AM, AAP, AAM))
primospaternos_result = run(0, P, primospaternos('christian', P))

print("Abuelos de Christian:", abuelos_result)
print("Primos paternos de Christian:", primospaternos_result)
