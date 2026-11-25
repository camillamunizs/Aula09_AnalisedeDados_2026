def soma (x,y):
    resultado = x + y
    #print(resultado)
    return resultado #retorna o resultado para quem chamou
# NONE = vazio 


# num1 = 5
# num2 = 9
# soma(num1, num2)

for i in range(3):
    num1 = float(input('Informe um número: '))
    num2= float(input('Informe um número: '))
    resultado = soma(num1, num2) # chamada da função
    print(resultado)
