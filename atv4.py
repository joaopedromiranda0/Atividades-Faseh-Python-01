#Faça um programa para uma loja virtual calcular a compra dos produtos e mostar ao final o valor total da compra, o valor a vista com desconto de 10%, e o valor com acréscimo de 5% em compra parcelada de 3x e mostre também o valor da parcela. Os produtos são iphone, samsung s24, tablet , ipad e notebook

precosProdutos = {
    "Iphone": 120 , 
    "Samsung S24": 44 ,
    "Tablet": 150 ,
    "iPad": 30 ,
    "Notebook": 400
}

print("Produtos disponíveis:")
for produto, preco in precosProdutos.items():
    print(f"{produto}: R$ {preco:.2f}")

print("\nDigite o nome dos produtos que você deseja comprar, separados por vírgula:")
produtosSelecionados = input().split(",")


produtoSelecionados = [produto.strip() for produto in produtosSelecionados]

valor_total = 0.0
for produto in produtosSelecionados:
    if produto in precosProdutos:
        valor_total += precosProdutos[produto]
    else:
        print(f"Produto '{produto}' não encontrado na lista.")

desconto = valor_total * 0.10
valor_a_vista = valor_total - desconto

acrescimo = valor_total * 0.05
valorParcelado = valor_total + acrescimo
valorParcela = valorParcelado / 3

print(f"\nValor total da compra: R$ {valor_total:.2f}")
print(f"Valor à vista com 10% de desconto: R$ {valor_a_vista:.2f}")
print(f"Valor parcelado em 3x com 5% de acréscimo: R$ {valorParcelado:.2f}")
print(f"Valor de cada parcela: R$ {valorParcela:.2f}")
