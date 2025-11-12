def q_exemplo():
    n = int(input(""))
    for i in range(0, n+1) :
        if i>1 and i % 2 == 0:
            print(i)

def q1():
    nums = []
    for i in range(3):
        nums.append(int(input('')))
    nums.sort()
    for n in nums:
        print(n)
    pass
    

def q2():
    dias = int(input(''))
    km = int(input(''))

    diaria = 90
    franquia_por_dia = 100
    taxa_km_extra = 12

    custo_base = dias * diaria
    franquia = dias * franquia_por_dia
    km_extra = max(0, km - franquia)
    custo_extra = km_extra * taxa_km_extra
    total = custo_base + custo_extra

    print(f"{total:.2f}")
    pass

def q3():
    n = int(input(''))
    for i in range(1, n+1):
        print(' '.join(str(k) for k in range(1, i+1)) + ' ')
    pass

def q4():
    total = 0.0
    quantidade = 0
    while True:
        line = input('')
        if line == "":
            continue
        nota = float(line)
        if nota == -1.0:
            break
        total += nota
        quantidade += 1
        pass

    if quantidade == 0:
        print("0.00")
    else:
        media = total / quantidade
        print(f"{media:.2f}")
    pass

def q5():
    nome = input('')
    preposicoes = {'da', 'de', 'do', 'e'}
    partes = []
    for palavra in nome.split():
        if palavra.lower() in preposicoes:
            partes.append(palavra.lower())
        else:
            if palavra == "":
                partes.append(palavra)
            else:
                partes.append(palavra[0].upper() + palavra[1:].lower())
    print(' '.join(partes))
    pass


def q6():
    pass

def q7():
    pass

def main():
    q_exemplo()()

if __name__ == "__main__":
    main()