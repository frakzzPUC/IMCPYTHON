from sys import exit
from string import ascii_letters

def calcular():
    while True:
        print('-' * 20)
        print('CALCULADORA DE IMC')
        print('-' * 20)
        ### Inicio Calculo IMC
        ###
        print('Menu:')
        print('1 - Usar calculadora de IMC')
        print('2 - Sair')
        opcao = int(input('Digite a opção:'))
        listaopcao = [1, 2]
        while opcao not in listaopcao:
            opcao = int(input('Você digitou uma opção não existente, digite novamente:'))
            print(f'Você escolheu a opção {opcao}')
        if opcao == 1:
            valido = ascii_letters + ' áéíóú'
            while True:
                nome = (input('Digite seu nome para Identificação:\n'))
                if all(c in valido for c in nome):
                    break
                else:
                    print('Por favor digite um nome válido. (somente letras e espaços)')
            QueroCalcularIMC = True
            while QueroCalcularIMC:
                tenhoimc = False
                while not tenhoimc:
                    Tenhoaltura = True
                    while Tenhoaltura:
                        try:
                            altura = input('Informe a sua altura em metros :\n').upper()

                            altura = float(altura)

                            if altura <= 0:
                                print('Somente números positivos podem ser digitados\n')

                            elif altura > 2.60:
                                print('Coloque uma altura compativel')

                            else:
                                Tenhoaltura = False

                        except ValueError:
                            print("Somente números podem ser digitados!\n")
                    ### Sistema While, jeito que o maligno ensino###

                    digitoudireito = False
                    while not digitoudireito:
                        try:
                            peso = input('Informe o seu peso em kg:\n').upper()

                            peso = float(peso)

                            if peso <= 0:
                                print('Somente Números positivos podem ser digitados\n')

                            elif peso > 350:
                                print('Coloque um peso compativel')

                            else:
                                digitoudireito = True

                        except ValueError:
                            print('Somente Números podem ser digitados')

                        else:
                            tenhoimc = True

                QueroCalcularIMC = False

                total = peso / (altura ** 2)
                print('Olá {}, seu IMC é igual a: {:.2f}.'.format(nome, total))
                if total < 17:
                    print('Você esta muito abaixo do peso')
                elif total <= 18.49:
                    print('Você esta abaixo do peso')
                elif total <= 24.99:
                    print('Você esta com o peso normal')
                elif total <= 29.99:
                    print('Você esta acima do peso')
                elif total <= 34.99:
                    print('Você esta com obesidade de grau I')
                elif total <= 39.99:
                    print('Você esta com obesidade grau II (severa)')
                elif total > 40:
                    print('Você esta com obesidade grau III (morbida)')

            caloria = str(input('QUER CALCULAR QUANTAS CALORIAS INGERIR? [S] pra SIM e [N] para NÃO\n')).strip().upper()[0]

            while caloria not in 'SsNn':
                caloria = str(input('DADOS INCORRETOS, DIGITE NOVAMENTE:\n')).upper()[0]
                print('Você escolheu a opção:{}'.format(caloria))

            if caloria == 'S':
                print('Você escolheu a opção SIM, continue...\n')

                sexo = str(input('digite o seu sexo [M PARA MASCULINO/F PARA FEMININO] :')).strip().upper()[0]
                while sexo not in 'MmFf':
                    sexo = str(input('dados incorretos! digite seu sexo novamente :'))
                print('Sexo', sexo, 'registrado com sucesso!!!')

                QueroCalcularcalorias = True
                while QueroCalcularcalorias:
                    tenhocalorias = False
                    while not tenhocalorias:
                        Tenhoidade = True
                        while Tenhoidade:
                            try:
                                idade = input('Informe sua idade:\n').upper()

                                idade = int(idade)

                                if idade <= 0:
                                    print('Somente números positivos podem ser digitados\n')

                                elif idade > 100:
                                    print('Coloque uma idade compativel')

                                else:
                                    Tenhoidade = False

                            except ValueError:
                                print("Somente números podem ser digitados!\n")

                            else:
                                tenhocalorias = True
                    QueroCalcularcalorias = False
            else:
                print('Muito Obrigado {} por usar nosso programa!'.format(nome))
                calcular()
            if sexo == 'M':
                alturacm = altura * 100
                tax_metM = 66.5 + (5 * alturacm) + (13.8 * peso) - (6.8 * idade)
                print('Sua taxa metabólica basal é de: {:.2f} calorias.'.format(tax_metM))
                cafemanha = float(input('Digite as CALORIAS ingeridas no café da manhã:\n'))

                almoço = float(input('Digite as CALORIAS ingeridas no almoço:\n'))

                cafetarde = float(input('Digite as CALORIAS ingeridas no café da tarde:\n'))

                jantar = float(input('Digite as CALORIAS ingeridas no jantar:\n'))

                total_calorias_usuario = cafemanha + almoço + cafetarde + jantar

                if total_calorias_usuario > tax_metM:
                    print('Olha {},você ingere mais calorias que o necessário e está fazendo um SUPERÁVIT CALÓRICO para ganhar massa muscular!\n'.format(nome))

                elif total_calorias_usuario < tax_metM:
                    print('Olha {}, você ingere menos calorias que o necessário e está fazendo um DÉFICT CALÓRICO para perder peso!\n'.format(nome))

            elif sexo == 'F':
                alturacm = altura * 100
                tax_metF = 655.1 + (1.8 * alturacm) + (9.5 * peso) - (4.7 * idade)
                print('Sua taxa metabólica basal é de: {:.2f} calorias'.format(tax_metF))
                cafemanha = float(input('Digite as CALORIAS ingeridas no café da manhã:\n'))

                almoço = float(input('Digite as CALORIAS ingeridas no almoço:\n'))

                cafetarde = float(input('Digite as CALORIAS ingeridas no café da tarde:\n'))

                jantar = float(input('Digite as CALORIAS ingeridas no jantar:\n'))

                total_calorias_usuario = cafemanha + almoço + cafetarde + jantar
                if total_calorias_usuario > tax_metF:
                    print('{},você ingere mais calorias que o necessário e está fazendo um SUPERÁVIT CALÓRICO para ganhar massa muscular!\n'.format(nome))

                elif total_calorias_usuario < tax_metF:
                    print('{}, você ingere menos calorias que o necessário e está fazendo um DÉFICT CALÓRICO para perder peso!\n'.format(nome))

            dicas = str(input(
                'PARA RECEBER DICAS DE ALIMENTOS PARA GANHAR MASSA OU PERDER PESO DIGITE S, CASO NÃO QUEIRA, CLIQUE EM QUALQUER BOTAO:\n')).strip().upper()[
                0]
            if dicas == 'S':
                print("-------------Dicas:-------------\n")
                print('AQUI ESTÃO OS 5 MELHORES ALIMENTOS PARA GANHAR MASSA MUSCULAR: OVOS, FRANGO, CARNE VERMELHA, QUEIJOS!\n')
                print(
                    'E ESSES OS MELHORES PARA PERDER PESO:PERA(por ser rica em água e fibras causando a saciedade duranteo dia), CANELA(pois estimula a queima de gordura), BERINJELA, AVEIA e MELANCIA\n')
                print('----------------------------------\n')
                print('OBRIGADO POR USAR NOSSO APLICATIVO\n')
                print('-----------------------------------\n')
            else:
                print('Muito Obrigado {} por usar nosso programa!'.format(nome))
                calcular()
        else:
            calcular()
calcular()