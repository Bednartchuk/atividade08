class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        desconto_valor = self.preco * (percentual / 100)
        preco_com_desconto = self.preco - desconto_valor
        return preco_com_desconto

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor
    
    def desconto(self, percentual):
        desconto_geral = super().desconto(percentual)
        desconto_adicional = desconto_geral * 0.10
        preco_com_desconto = desconto_geral - desconto_adicional
        return preco_com_desconto

class Jogo(Produto):
    def __init__(self, nome, preco, plataforma):
        super().__init__(nome, preco)
        self.plataforma = plataforma

livro = Livro("Aventuras Incríveis", 50.0, "João Autor")
jogo = Jogo("Fantasy Quest", 60.0, "PC")

preco_livro_com_desconto = livro.desconto(15)
preco_jogo_com_desconto = jogo.desconto(20)

print(f"Preço do livro com desconto: R${preco_livro_com_desconto:.2f}")
print(f"Preço do jogo com desconto: R${preco_jogo_com_desconto:.2f}")
