lista_catalogo = []


for i in range (3):
    print(f'\nLivro {i+1}')

    livro = {}

    livro['titulo'] = input('Informe o nome do livro: ')
    livro['autor'] = input('Informe o autor do livro: ')
    livro['ano'] = int(input('Informe o ano de publicação: '))
    livro['genero'] = input('Informe o gênero do livro: ')
    livro['paginas'] = int(input('Informe o número de páginas: '))

    lista_catalogo.append(livro)

# print(lista_catalogo)
for elemento in lista_catalogo: # 3 vezes por ter 3 elementos na lista
    # print(elemento) 
    if elemento['ano'] >= 2020:
        print(f'Nome: {elemento['título']}')
        print(f'Ano: {elemento ['ano']}')

              