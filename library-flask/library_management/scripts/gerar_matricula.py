import random

def gerar_matricula(ano,nivel):
    parte_fixa = str(ano)
    nivel_str = str(nivel).zfill(2)#formado com 2 digitos
    parte_aleatoria = str(random.randint(1,100)).zfill(3)
    matricula = parte_fixa + nivel_str + parte_aleatoria
    return matricula


'''matriculas_geradas = []
for _ in range(10):
    ano = random.choice([2022,2023,2024])
    nivel = random.randint(1,3)
    matricula = gerar_matricula(ano,nivel)
    matriculas_geradas.append(matricula)
matricula = gerar_matricula(2022,1)


print("Matrículas geradas:")
for matricula in matriculas_geradas:
    print(matricula)'''