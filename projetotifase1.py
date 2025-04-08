data = input(f'Qual é a data de hoje? ')
vsust = 0
vnsust = 0
litros = int(input(f'\nQuantos litros de aguá você consumiu hoje?(Aprox em L.) '))
energia= float(input(f'Quantos kWh de energia elétrica você consumiu hoje? '))
residuos = float(input(f'Quantos kg de resíduos não reciclados você gerou hoje? '))
reciclados = int(input(f'Qual a porcentagem de resíduos reciclados no total(em %)? '))
transporte1 = int(input(f'Qual meio de transporte você usou hoje?\n 1.Transporte público(onibus,metro,trem)\n 2.Bicicleta\n 3.Caminhada\n 4.Carro(combústiveis fósseis)\n 5.Carro elétrico\n 6.Carona compartilhada:  '))
transporte2 = int(input(f'Você usou outro meio?Se não, aperte 7!\n 1.Transporte público(onibus,metro,trem)\n 2.Bicicleta\n 3.Caminhada\n 4.Carro(combústiveis fósseis)\n 5.Carro elétrico\n 6.Carona compartilhada:  '))

if transporte2 == 7:
    transporte3=7
else:
    transporte3=int(input(f'Você usou outro meio?Se não, aperte 7!\n 1.Transporte público(onibus,metro,trem)\n 2.Bicicleta\n 3.Caminhada\n 4.Carro(combústiveis fósseis)\n 5.Carro elétrico\n 6.Carona compartilhada:  '))
                                                  
if litros <150:
    print(f'\nConsumo de água: Sustentabilidade alta')
    vsust += 1
elif litros >200:
    print(f'\nConsumo de água: Sustentabilidade baixa')
    vnsust += 1
else:
    print(f'\nConsumo de água: Sustentabilidade média')

if energia < 5:
    print(f'Consumo de energia: Sustentabilidade alta')
    vsust += 1
elif energia >10:
    print(f'Consumo de energia: Sustentabilidade baixa')
    vnsust +=1 
else:
    print(f'Consumo de energia: Sustentabilidade média')

if reciclados >50:
    print(f'Geração de resíduos não recicláveis: Sustentabilidade alta')
    vsust += 1
elif reciclados < 20:
    print(f'Geração de resíduos não recicláveis: Sustentabilidade baixa')
    vnsust += 1
else:
    print(f'Geração de resíduos não reciclaveis: Sustentabilidade moderada')

vtransporte=0
vntransporte=0
if (transporte1== 1 or transporte1== 2 or transporte1==3 or transporte1==5):
    vsust+=1
    vtransporte+=1
elif (transporte1==4 or transporte1==6):
    vnsust+=1
    vntransporte+=1
if (transporte2==1 or transporte2==2 or transporte2==3 or transporte2==5):
    vsust+=1
    vtransporte+=1
elif (transporte2==4 or transporte2==6):
    vnsust+=1
    vntransporte+=1
if (transporte3==1 or transporte3==2 or transporte3==3 or transporte3==5):
    vsust+=1
    vtransporte+=1
elif (transporte3==4 or transporte3==6):
    vnsust+=1
    vntransporte+=1

if vtransporte > vntransporte:
    print(f'Transporte: Sustentabilidade alta')
elif vtransporte < vntransporte:
    print(f'Transporte: Sustentabilidade baixa')
else:
    print(f'Sustentabilidade moderada')

if vsust > vnsust:
    print(f'\nSua sustentabilidade é boa! Pontos sustentáveis: {vsust} e Pontos não sustentáveis: {vnsust}')
elif vsust < vnsust:
    print(f'\nSua sustentabilidade tem que melhorar! Pontos sustentáveis: {vsust} e Pontos não sustentáveis: {vnsust}') 
elif vsust == vnsust:
    print(f'\nA sua sustentabilidade é mediana!  Pontos sustentáveis: {vsust} e Pontos não sustentáveis: {vnsust}')

    


