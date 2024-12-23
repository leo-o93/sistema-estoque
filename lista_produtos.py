import json

class ProductNavigator:
    def __init__(self, file_name="products.json"):
        self.file_name = file_name
        self.products = []
        self.current_index = 0
        self.load_products()
    
    def load_products(self):
        try:
            with open(self.file_name, "r") as file:
                self.products = json.load(file)
        except FileNotFoundError:
            self.products = []
    
    def save_products(self):
        with open(self.file_name, "w") as file:
            json.dump(self.products, file, indent=4)
    
    def display_current_product(self):
        if not self.products:
            print("Nenhum produto disponível.")
            return
        product = self.products[self.current_index]
        print(f"\nProduto atual ({self.current_index + 1}/{len(self.products)}):")
        print(f"Nome: {product['nome']}")
        print(f"Fornecedor: {product['fornecedor']}")
        print(f"Marca: {product['marca']}")
        print(f"Preço: R${product['preco']:.2f}")
        
    
    def next_product(self):
        if not self.products:
            print("Nenhum produto disponível.")
            return
        self.current_index = (self.current_index + 1) % len(self.products)
        self.display_current_product()
    
    def previous_product(self):
        if not self.products:
            print("Nenhum produto disponível.")
            return
        self.current_index = (self.current_index - 1) % len(self.products)
        self.display_current_product()
    
    def add_product(self):
        nome = input("Digite o nome do produto: ")
        fornecedor = input("Digite o fornecedor: ")
        marca = input("Digite a marca do produto: ")
        preco = float(input("Digite o preço: R$"))
        self.products.append({"nome": nome, "marca": marca, "fornecedor": fornecedor, "preco": preco})
        self.save_products()
        print(f"Produto '{nome}' adicionado com sucesso!")
    
    def edit_product(self):
        if not self.products:
            print("Nenhum produto disponível para editar.")
            return
        self.display_current_product()
        choice = input("Deseja editar este produto? (s/n): ").lower()
        if choice == 's':
            nome = input("Novo nome do produto (ou deixe vazio para manter): ")
            marca = input("Nova marca do produto (ou deixe vazio para manter): ")
            fornecedor = input("Novo fornecedor (ou deixe vazio para manter): ")
            preco_input = input("Novo preço (ou deixe vazio para manter): ")
            
            product = self.products[self.current_index]
            if nome:
                product['nome'] = nome
            if marca:
                product['marca'] = marca   
            if fornecedor:
                product['fornecedor'] = fornecedor
            if preco_input:
                product['preco'] = float(preco_input)
            
            self.save_products()
            print("Produto atualizado com sucesso!")
    
    def search_product(self):
        if not self.products:
            print("Nenhum produto disponível.")
            return
        term = input("Digite o nome ou parte do nome do produto: ").lower()
        matches = [p for p in self.products if term in p['nome'].lower()]
        if matches:
            print("\nProdutos encontrados:")
            for product in matches:
                print(f"Nome: {product['nome']}, Marca: {product['marca']}, Fornecedor: {product['fornecedor']}, Preço: R${product['preco']:.2f}")
        else:
            print("Nenhum produto encontrado.")

# Menu principal
def main():
    navigator = ProductNavigator()
    
    while True:
        print("\nMenu:")
        print("1. Exibir produto atual")
        print("2. Próximo produto")
        print("3. Produto anterior")
        print("4. Adicionar produto")
        print("5. Editar produto")
        print("6. Buscar produto")
        print("7. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            navigator.display_current_product()
        elif choice == "2":
            navigator.next_product()
        elif choice == "3":
            navigator.previous_product()
        elif choice == "4":
            navigator.add_product()
        elif choice == "5":
            navigator.edit_product()
        elif choice == "6":
            navigator.search_product()
        elif choice == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
