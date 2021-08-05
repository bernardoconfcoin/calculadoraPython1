"""
Programa:   Calculadora em Python
Autor:      Marcelo Clara
Descrição:  Calculadora com funções básicas utilizando o conteúdo apresentada na segunda aula de Python:
- Variáveis str, int, float
- Recebendo dados através do input()s

- Verificando tipos de variáveis com type()
- Conversão de variaveis str() int() float()
- Exibindo textos na console com o print() e print(f' {}) para exibir conteúdo de variáveis
- Testes de condição lógica com if , else, elif
- Loop utilizando while e for next
- Funções
- Ajuda com dir() e help()
- Obs: no exercício poderiamos também usar a função eval() para a calculadora
- Atenção:  observar a identação nos comandos do tipo shell ( if, while , for next )
            observar o espaçamento de duas linhas entre funcoes.
            Estas são boas práticas de um programador Python, gerando código Pythonico.
            Esta padrão é denominado PEP8.
"""

import os, math
def tela(operacao, resultado, valor, ):
    """
    Monta a tela da calculadora a partir dos parâmetros informados.
    :param operacao:
    :param resultado:
    :param valor:
    :return:
    """
    # Emulate terminal in output console tem que estar habilitado para a tela ser limpa pelo comando abaixo
    # Ative esta opção no PyCharm, em Edit Run Configurations 'calculadora.py', fica na aba Run:
    # da IDE do PyCharm, na lateral direita identificado com um ícone de uma 'ferramenta'.
    os.system('cls' if os.name == 'nt' else 'clear') or None
    # formata linha com o valor
    tamanho_linha = 29 - len(operacao) - 7
    tamanho_valor = len(str(valor))
    espacos_valor = int((tamanho_linha - tamanho_valor))
    display_valor = (' ' * espacos_valor) + str(valor) + '  (' + operacao + ') ' + '='
    # formata linha com o resultado
    if resultado == 0:
        tamanho_linha = 29 - len(operacao) - 8
    else:
        tamanho_linha = 29 - len(operacao) - 7
    tamanho_valor = len(str(resultado))
    espacos_resultado = int((tamanho_linha - tamanho_valor))
    display_resultado = (' ' * espacos_resultado) + str(resultado) + ' Mem. ' + '='
    print('=============================')
    print('=  Calculadora em Python    =')
    print('=============================')
    print(f'={display_resultado}')
    print(f'={display_valor}')
    print('=============================')
    print('=  sqr |   **  |            =')
    print('= --------------------------=')
    print('=   C  |  +/-  |  %   |  /  =')
    print('= --------------------------=')
    print('=   7  |   8   |   9  |  X  =')
    print('= --------------------------=')
    print('=   4  |   5   |   5  |  -  =')
    print('= --------------------------=')
    print('=   1  |   2   |   3  |  +  =')
    print('= --------------------------=')
    print('=        0     |  ,   |  =  =')
    print('=============================')
    print('====  < s > para Sair  ======')
    return
def somar(num1, num2):
    """
    Efetua a operação de cálculo adição
    :param num1:
    :param num2:
    :return:
    """
    resultado = num1 + num2
    return resultado
def diminuir(num1, num2):
    """
    Efetua a operação de cálculo subtração
    :param num1:
    :param num2:
    :return:
    """
    resultado = num1 - num2
    return resultado
def multiplicar(num1, num2):
    """
    Efetua a operação de cálculo multiplicação
    :param num1:
    :param num2:
    :return:
    """
    resultado = num1 * num2
    return resultado
def dividir(num1, num2):
    """
    Efetua a operação de cálculo divisão
    :param num1:
    :param num2:
    :return:
    """
    resultado = num1 / num2
    return resultado
def exponenciar(num1, num2):
    """
    Efetua a operação de cálculo exponenciação
    :param num1:
    :param num2:
    :return:
    """
    resultado = num1 ** num2
    return resultado
def raiz_quadrada(num):
    """
    Efetua a operação de cálculo raiz quadrada
    :param num:
    :return:
    """
    resultado =  math.sqrt(num)
    return resultado
def calcula(resultado, numero, opcao):
    """
    Realiza o cálculo da opção informada para o resultado e número informado
    :param resultado:
    :param numero:
    :param opcao:
    :return:
    """
    if opcao == '+':
        resultado = somar(resultado,numero)
    elif opcao == '-':
        resultado = diminuir(resultado,numero)
    elif opcao == '*':
        resultado = multiplicar(resultado, numero)
    elif opcao == '/':
        if numero != 0:
            resultado = dividir(resultado,numero)
        else:
            resultado = None
    elif opcao == '**':
        resultado = exponenciar(resultado,numero)
    elif opcao == 'sqr':
        resultado = raiz_quadrada(numero)
    return resultado
opcao = 0
operacao = ''
resultado = 0
valor = 0
tela(operacao, resultado, valor)
while opcao != 's' and  opcao != 'S':
    opcao = input()
    if opcao in('+','-','/','*','**', 'sqr'):
        operacao = opcao
        if numero:
            resultado = calcula(resultado, numero, opcao)
            numero = 0
    elif opcao == 'c' or opcao == 'C':
        # Reinicializa todas as variáveis da calculadora
        resultado = 0
        numero = 0
        operacao = ''
    elif opcao == '=':
        opcao = operacao
        resultado = calcula(resultado, numero, opcao)
        numero = 0
    else:
        try:
            numero = float(opcao)
        except:
            numero = None
    tela(operacao, resultado, numero)
