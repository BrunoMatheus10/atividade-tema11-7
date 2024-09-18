# Recebe o número inteiro do usuário
numero = int(input("Digite um número: "))

# Verifica se o número é primo
if numero <= 1:
    # Se o número for menor ou igual a 1, não é primo
    print(numero," não é um número primo.")
else:
    is_primo = True
    divisor = 2
    while divisor * divisor <= numero and is_primo:
        # Verifica se o número é divisível por algum valor entre 2 e a raiz quadrada do número
        if numero % divisor == 0:
            # Se for divisível, não é primo
            is_primo = False
        divisor += 1
    if is_primo:
        # Se não foi encontrado divisor, o número é primo
        print(numero," é um número primo.")
    else:
        # Caso contrário, não é primo
        print(numero," não é um número primo.")
