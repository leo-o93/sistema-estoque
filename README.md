Este código implementa uma aplicação de gerenciamento de produtos, permitindo ao usuário adicionar, editar, navegar e buscar produtos armazenados em um arquivo JSON. A aplicação é baseada em um menu interativo por linha de comando.

Classes

ProductNavigator
A classe `ProductNavigator` é responsável por gerenciar os produtos. Ela permite carregar, salvar, exibir e manipular os produtos de um arquivo JSON.


Construtor (`__init__`)

def __init__(self, file_name="products.json"):

- Parâmetros:
  - `file_name` (str): Nome do arquivo JSON onde os produtos serão armazenados. O valor padrão é `"products.json"`.
  
  O construtor inicializa a lista de produtos e o índice do produto atual e carrega os produtos a partir de um arquivo JSON.


Métodos

`load_products`

def load_products(self):

Carrega os produtos a partir do arquivo JSON especificado no construtor. Se o arquivo não for encontrado, cria uma lista vazia de produtos.

`save_products`

def save_products(self):

Salva a lista de produtos no arquivo JSON, utilizando formatação com indentação de 4 espaços.

display_current_product

def display_current_product(self):

Exibe as informações do produto atual, incluindo nome, fornecedor, marca e preço. Se não houver produtos, exibe uma mensagem informando que não há produtos disponíveis.

next_product

def next_product(self):

Exibe o próximo produto na lista. Se o índice atingir o final da lista, ele volta ao primeiro produto, permitindo a navegação cíclica. Chama o método `display_current_product` para exibir o produto.

previous_product

def previous_product(self):

Exibe o produto anterior na lista. Se o índice atingir o começo da lista, ele volta ao último produto, permitindo a navegação cíclica. Chama o método `display_current_product` para exibir o produto.

add_product

def add_product(self):

Permite ao usuário adicionar um novo produto à lista. O nome, fornecedor, marca e preço são solicitados ao usuário e o produto é adicionado à lista de produtos. Após a adição, o arquivo JSON é atualizado.

edit_product

def edit_product(self):

Permite ao usuário editar o produto atual. O usuário pode modificar o nome, fornecedor, marca e preço do produto atual. As alterações são salvas no arquivo JSON.

search_product

def search_product(self):

Permite ao usuário buscar produtos por nome. O usuário insere um termo de busca e a função retorna todos os produtos cujo nome contém o termo pesquisado. Os produtos encontrados são exibidos com nome, marca, fornecedor e preço.



Funções

main

def main():

Função principal que exibe o menu de opções e gerencia a interação do usuário com a aplicação. A função é responsável por capturar as escolhas do usuário e chamar os métodos da classe `ProductNavigator` para executar a ação desejada.

Opções do Menu:
- 1. Exibir produto atual: Exibe as informações do produto atualmente selecionado.
- 2. Próximo produto: Exibe o próximo produto na lista de produtos.
- 3. Produto anterior: Exibe o produto anterior na lista de produtos.
- 4. Adicionar produto: Permite adicionar um novo produto à lista.
- 5. Editar produto: Permite editar o produto atual.
- 6. Buscar produto: Permite buscar produtos pelo nome.
- 7. Sair: Encerra o programa.

Execução

Quando o script é executado, o programa carrega a lista de produtos do arquivo. O usuário é então apresentado a um menu interativo, no qual pode escolher uma das opções listadas. A interação continua até que o usuário escolha a opção de sair (`7`).

Exemplo de Uso

Exibição do produto atual

Menu:
1. Exibir produto atual
2. Próximo produto
3. Produto anterior
4. Adicionar produto
5. Editar produto
6. Buscar produto
7. Sair
Escolha uma opção: 1
Produto atual (1/3):
Nome: Produto A
Fornecedor: Fornecedor A
Marca: Marca A
Preço: R$10.00


Adicionar produto

Digite o nome do produto: Produto B
Digite o fornecedor: Fornecedor B
Digite a marca do produto: Marca B
Digite o preço: R$20.00
Produto 'Produto B' adicionado com sucesso!


Editar produto

Novo nome do produto (ou deixe vazio para manter): Produto C
Nova marca do produto (ou deixe vazio para manter): Marca C
Novo fornecedor (ou deixe vazio para manter): Fornecedor C
Novo preço (ou deixe vazio para manter): 25.00
Produto atualizado com sucesso!


Buscar produto

Digite o nome ou parte do nome do produto: Produto
Produtos encontrados:
Nome: Produto A, Marca: Marca A, Fornecedor: Fornecedor A, Preço: R$10.00
Nome: Produto B, Marca: Marca B, Fornecedor: Fornecedor B, Preço: R$20.00
