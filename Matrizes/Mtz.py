def dia_maior_descanso(horario_descanso):
    soma_dias = [sum(dia) for dia in zip(*horario_descanso)]
    return soma_dias.index(max(soma_dias))

def dia_menor_descanso(horario_descanso):
    soma_dias = [sum(dia) for dia in zip(*horario_descanso)]
    return soma_dias.index(min(soma_dias))

def semana_maior_descanso(horario_descanso):
    return horario_descanso.index(max(horario_descanso, key=sum)) + 1

def semana_menor_descanso(horario_descanso):
    return horario_descanso.index(min(horario_descanso, key=sum)) + 1

def menor_tempo_descanso(horario_descanso):
    return min(min(semana) for semana in horario_descanso)

def maior_tempo_descanso(horario_descanso):
    return max(max(semana) for semana in horario_descanso)

def dias_com_menor_descanso(horario_descanso, menor_tempo):
    return sum(1 for dia in zip(*horario_descanso) if menor_tempo in dia)

def dias_com_maior_descanso(horario_descanso, maior_tempo):
    return sum(1 for dia in zip(*horario_descanso) if maior_tempo in dia)

def percentagem_por_semana(horario_descanso):
    total_por_mes = sum(sum(semana) for semana in horario_descanso)
    return [(sum(semana) / total_por_mes) * 100 for semana in horario_descanso]

horario_descanso = [
    [8, 6, 7, 8, 6],
    [5, 5, 6, 7, 8],
    [6, 7, 8, 6, 5],
    [7, 5, 9, 7, 4]
]

dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex"]

print("1. O dia da semana com maior horário de descanso é:", dias_semana[dia_maior_descanso(horario_descanso)])
print("2. O dia da semana com menor horário de descanso é:", dias_semana[dia_menor_descanso(horario_descanso)])
print("3. A semana com maior horário de descanso é a semana:", semana_maior_descanso(horario_descanso))
print("4. A semana com menor horário de descanso é a semana:", semana_menor_descanso(horario_descanso))
print("5. O menor tempo de descanso é:", menor_tempo_descanso(horario_descanso))
print("6. O maior tempo de descanso é:", maior_tempo_descanso(horario_descanso))
print("7. Quantidade de dias da semana com o menor tempo de descanso:", dias_com_menor_descanso(horario_descanso, menor_tempo_descanso(horario_descanso)))
print("8. Quantidade de dias da semana com o maior tempo de descanso:", dias_com_maior_descanso(horario_descanso, maior_tempo_descanso(horario_descanso)))
print("9. Percentagem por semana em relação ao total por mês:", percentagem_por_semana(horario_descanso))
