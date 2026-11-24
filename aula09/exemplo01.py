produto1 = {}  # Dicionário vazio 
# Utiliza para registrar informações de pessoas, produtos,etc

produto = {
    'nome': 'Notebook',
    'preco': 3500.80,
    'marca': 'Lenovo'
}

# print(type(produto)) = mostra o tipo de objeto
print(produto) # todas as chaves e valores 
print(produto['nome'])  # printa apenas uma chave 'NOME'
print(produto['preco']) 

# Alterando o valor 
produto['marca'] = "Positivo"   
print(produto['marca']) 

# Adicionando Chaves
produto['tela'] = '18"'   
print(produto)

# Deletando uma chave
del (produto['marca']) 
print(produto)

print(produto.keys()) # mostra as chaves
print(produto.values()) # mostra os valores
print(produto.items()) # separa cada item com chave e valor