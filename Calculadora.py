numero1=float(input("Digite o primeiro número: "))
numero2=float(input("Digite o segundo número: "))
5

print("1 -somar:")
print("2 -subtrair:")
print("3 -multiplicar:")
print("4 -dividir:")

opcao=int(input("Escolha a operação desejada: "))

if opcao==1:
    resultado=numero1+numero2
    print("O resultado da soma é:", resultado)

elif opcao==2:
    resultado=numero1-numero2
    print("O resultado da subtração é:", resultado)

elif opcao==3:
    resultado=numero1*numero2
    print("O resultado da multiplicação é:", resultado)

elif opcao==4:
    if numero2!=0:
        resultado=numero1/numero2
        print("O resultado da divisão é:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")

else:
    print("Opção inválida. Por favor, escolha uma operação válida.")    

