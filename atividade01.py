contatos = []

for i in range (3):
    print(f'\nCliente {i+1}')

    contato = {}

    contato['nome'] = input('Informe o nome completo: ')
    contato['telefone'] = int(input('Informe o telefone: '))
    contato['email'] = input('Informe o e-mail: ')


    contatos.append(contato)


for elemento in contatos:
    print(f'\nNome: {elemento['nome']}')
    print(f'Telefone: {elemento['telefone']}')
    print(f'E-mail: {elemento['email']}')

   





