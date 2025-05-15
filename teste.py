import mysql.connector
import sys

# Cifra de César sem uso de ord(), chr(), isalpha() ou isupper()
SHIFT_KEY = 4  # deslocamento para cifrar/decifrar
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"

# Funções de criptografia e descriptografia

def encrypt(text: str, shift: int = SHIFT_KEY) -> str:
    result = []
    for char in text:
        if char in UPPER:
            idx = UPPER.find(char)
            new_idx = (idx + shift) % 26
            result.append(UPPER[new_idx])
        elif char in LOWER:
            idx = LOWER.find(char)
            new_idx = (idx + shift) % 26
            result.append(LOWER[new_idx])
        else:
            result.append(char)
    return ''.join(result)


def decrypt(text: str, shift: int = SHIFT_KEY) -> str:
    # Basta inverter o sinal do deslocamento
    return encrypt(text, -shift)


def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="MuriloMoraes",
        password="Buck2005#",
        database="bd_projetoti"
    )


def classify_water(litros: int) -> str:
    if litros < 150:
        return "Alta Sustentabilidade"
    elif litros <= 200:
        return "Moderada Sustentabilidade"
    else:
        return "Baixa Sustentabilidade"


def classify_energy(energia: float) -> str:
    if energia < 5:
        return "Alta Sustentabilidade"
    elif energia <= 10:
        return "Moderada Sustentabilidade"
    else:
        return "Baixa Sustentabilidade"


def classify_waste(residuos: float) -> str:
    if residuos < 5:
        return "Alta Sustentabilidade"
    elif residuos <= 10:
        return "Moderada Sustentabilidade"
    else:
        return "Baixa Sustentabilidade"


def classify_recyclables(perc: int) -> str:
    if perc > 50:
        return "Alta Sustentabilidade"
    elif perc >= 20:
        return "Moderada Sustentabilidade"
    else:
        return "Baixa Sustentabilidade"


def classify_transport(opcs: dict) -> str:
    uso_publico = opcs.get('publico')
    bicicleta = opcs.get('bike')
    caminhada = opcs.get('walk')
    carro = opcs.get('carro')
    eletrico = opcs.get('eletrico')
    carona = opcs.get('carona')
    # Alta: apenas opções sustentáveis
    if (uso_publico or bicicleta or caminhada or eletrico) and not (carro or carona):
        return "Alta Sustentabilidade"
    # Moderada: mistura
    if (uso_publico or bicicleta or caminhada or eletrico) and (carro or carona):
        return "Moderada Sustentabilidade"
    # Baixa: só combustíveis fósseis
    if carro or carona:
        return "Baixa Sustentabilidade"
    return "Moderada Sustentabilidade"


def input_transport():
    print("\nResponda com 'S' ou 'N' qual meio de transporte você usou hoje:")
    opcs = {}
    opcs['publico'] = input('1. Transporte público (ônibus, metrô, trem): ').upper() == 'S'
    opcs['bike'] = input('2. Bicicleta: ').upper() == 'S'
    opcs['walk'] = input('3. Caminhada: ').upper() == 'S'
    opcs['carro'] = input('4. Carro (combustíveis fósseis): ').upper() == 'S'
    opcs['eletrico'] = input('5. Carro elétrico: ').upper() == 'S'
    opcs['carona'] = input('6. Carona compartilhada (fósseis): ').upper() == 'S'
    return opcs


def register(cursor):
    data = input("Qual é a data (yyyy-MM-dd): ")
    litros = int(input("Quantos litros de água você consumiu hoje?: "))
    energia = float(input("Quantos kWh de energia elétrica você consumiu hoje?: "))
    residuos = float(input("Quantos kg de resíduos não recicláveis você gerou hoje?: "))
    reciclados = int(input("Qual a porcentagem de resíduos reciclados hoje? (em %): "))
    transport_ops = input_transport()

    # Classificações
    c_agua = classify_water(litros)
    c_energia = classify_energy(energia)
    c_residuos = classify_waste(residuos)
    c_reciclaveis = classify_recyclables(reciclados)
    c_transporte = classify_transport(transport_ops)

    # Criptografar
    enc_agua = encrypt(c_agua)
    enc_energia = encrypt(c_energia)
    enc_residuos = encrypt(c_residuos)
    enc_reciclaveis = encrypt(c_reciclaveis)
    enc_transporte = encrypt(c_transporte)

    sql = ("INSERT INTO sustentabilidade (data, consumo_agua, consumo_energia, geracao_residuos, residuos_reciclaveis, uso_transporte)"
           " VALUES (%s, %s, %s, %s, %s, %s)")
    cursor.execute(sql, (data, enc_agua, enc_energia, enc_residuos, enc_reciclaveis, enc_transporte))
    print("Dados inseridos com sucesso!\n")


def list_records(cursor):
    cursor.execute("SELECT id, data FROM sustentabilidade ORDER BY data;")
    rows = cursor.fetchall()
    for r in rows:
        print(f"ID: {r[0]}, Data: {r[1]}")
    return [r[0] for r in rows]


def update_record(cursor):
    print("\n--- Atualizar Parâmetros ---")
    ids = list_records(cursor)
    rec_id = int(input("Digite o ID do registro que deseja alterar: "))
    if rec_id not in ids:
        print("ID inválido.\n")
        return
    litros = int(input("Quantos litros de água você consumiu hoje?: "))
    energia = float(input("Quantos kWh de energia elétrica você consumiu hoje?: "))
    residuos = float(input("Quantos kg de resíduos não recicláveis você gerou hoje?: "))
    reciclados = int(input("Qual a porcentagem de resíduos reciclados hoje? (em %): "))
    transport_ops = input_transport()

    c_agua = encrypt(classify_water(litros))
    c_energia = encrypt(classify_energy(energia))
    c_residuos = encrypt(classify_waste(residuos))
    c_reciclaveis = encrypt(classify_recyclables(reciclados))
    c_transporte = encrypt(classify_transport(transport_ops))
    sql = ("UPDATE sustentabilidade SET consumo_agua=%s, consumo_energia=%s, geracao_residuos=%s,"
           " residuos_reciclaveis=%s, uso_transporte=%s WHERE id=%s")
    cursor.execute(sql, (c_agua, c_energia, c_residuos, c_reciclaveis, c_transporte, rec_id))
    print("Registro atualizado com sucesso!\n")


def delete_record(cursor):
    print("\n--- Excluir Parâmetros ---")
    ids = list_records(cursor)
    rec_id = int(input("Digite o ID do registro que deseja excluir: "))
    if rec_id not in ids:
        print("ID inválido.\n")
        return
    cursor.execute("DELETE FROM sustentabilidade WHERE id=%s", (rec_id,))
    print("Registro excluído com sucesso!\n")


def classify_all(cursor):
    print("\n--- Classificação Geral ---")
    cursor.execute("SELECT id, data, consumo_agua, consumo_energia, geracao_residuos, residuos_reciclaveis, uso_transporte FROM sustentabilidade ORDER BY data;")
    rows = cursor.fetchall()
    if not rows:
        print("Nenhum registro cadastrado.\n")
        return
    for r in rows:
        print(f"ID {r[0]} - Data: {r[1]}")
        print(f"  Água: {decrypt(r[2])}")
        print(f"  Energia: {decrypt(r[3])}")
        print(f"  Resíduos: {decrypt(r[4])}")
        print(f"  Recicláveis: {decrypt(r[5])}")
        print(f"  Transporte: {decrypt(r[6])}\n")
    mapping = {'Alta Sustentabilidade': 3, 'Moderada Sustentabilidade': 2, 'Baixa Sustentabilidade': 1}
    sums = [0]*5
    for r in rows:
        sums[0] += mapping[decrypt(r[2])]
        sums[1] += mapping[decrypt(r[3])]
        sums[2] += mapping[decrypt(r[4])]
        sums[3] += mapping[decrypt(r[5])]
        sums[4] += mapping[decrypt(r[6])]
    n = len(rows)
    avgs = [s/n for s in sums]
    rev_map = {3: 'Alta Sustentabilidade', 2: 'Moderada Sustentabilidade', 1: 'Baixa Sustentabilidade'}
    print("Média Geral de Sustentabilidade:")
    # Desempacotando médias sem usar enumerate ou indexing
    avg1, avg2, avg3, avg4, avg5 = avgs

    # Função auxiliar para arredondar sem usar round()
    def arredonda(val):
        return int(val + 0.5)

    # Função auxiliar para mapear chave numérica para texto
    def map_key(k):
        if k >= 3:
            return "Alta Sustentabilidade"
        elif k == 2:
            return "Moderada Sustentabilidade"
        else:
            return "Baixa Sustentabilidade"

    # Processando cada parâmetro individualmente e imprimindo com f-string
    k1 = arredonda(avg1)
    print(f" Água: {map_key(k1)}")
    k2 = arredonda(avg2)
    print(f" Energia: {map_key(k2)}")
    k3 = arredonda(avg3)
    print(f" Resíduos: {map_key(k3)}")
    k4 = arredonda(avg4)
    print(f" Recicláveis: {map_key(k4)}")
    k5 = arredonda(avg5)
    print(f" Transporte: {map_key(k5)}")




