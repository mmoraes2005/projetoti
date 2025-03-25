data = input(f'\nQual é a data de hoje? ')
vsust = 0
vnsust = 0
litros = int(input(f'\nQuantos litros de aguá você consumiu hoje?(Aprox em L.) '))
energia= float(input(f'\nQuantos kWh de energia elétrica você consumiu hoje? '))
residuos = float(input(f'\nQuantos kg de resíduos não reciclados você gerou hoje? '))
reciclados = int(input(f'\nQual a porcentagem de resíduos reciclados no total(em %)? '))
meio = int(input(f'\nQual meio de transporte você usou hoje?\n 1.Transporte público(onibus,metro,trem)\n 2.Bicicleta\n 3.Caminhada\n 4.Carro(combústiveis fósseis)\n 5.Carro elétrico\n 6.Carona compartilhada:  '))

                                                  
if litros <150:
    print(f'Consumo de água: Sustentabilidade alta')
    vsust += 1
elif litros >200:
    print(f'Consumo de água: Sustentabilidade baixa')
    vnsust += 1
else:
    print(f'Consumo de água: Sustentabilidade média')

if energia < 5:
    print(f'Consumo de energia: Sustentabilidade alta')
    vsust += 1
elif energia >10:
    print(f'Consumo de energia: Sustentabilidade baixa')
    vnsust +=1 
else:
    print(f'Consumo de energia: Sustentabilidade média')

if residuos >50:
    print(f'Geração de resíduos não recicláveis: Sustentabilidade alta')
    vsust += 1
elif residuos < 20:
    print(f'Geração de resíduos não recicláveis: Sustentabilidade baixa')
    vnsust += 1
else:
    print(f'Geração de resíduos não reciclaveis:Sustentabilidade moderada')

if meio == 1 or 2 or 3:
    print(f'Meio de transporte: Sustentabilidade alta')
    vsust += 1 
elif meio == 4 or 6:
    print(f'Meio de transporte: Sustentabilidade baixa')
    vnsust += 1
elif meio == 5:
    print(f'Meio de transporte: Sustentabilidade média')



if vsust > vnsust:
    print(f'Sua sustentabilidade é boa! Pontos sustentáveis: {vsust} e Pontos não sustentáveis: {vnsust}')
elif vsust < vnsust:
    print(f'Sua sustentabilidade tem que melhorar! Pontos sustentáveis: {vsust} e Pontos não sustentáveis: {vnsust}') 
elif vsust == vnsust:
    print(f'A sua sustentabilidade é mediana!  Pontos sustentáveis: {vsust} e Pontos não sustentáveis: {vnsust}')
print(data)
    


