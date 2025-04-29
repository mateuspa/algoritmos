## Função que percorre array e retorna items divididos por 2, adicionando os resultados em uma nova array

import array

def halve_prices(cart):
        for price in cart:
            print(f"New Price {price/2}")
            cart_halves.append (price/2)
    
## array original
cart_list = [5, 20, 8, 19]

## cria array para armazenar valores divididos por 2
cart_halves = []

halve_prices (cart_list)

## exibe array com os resultados
print (f"{cart_halves}")