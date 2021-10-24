def int_a_romano(numero:int) -> str:
        lista_simbolos=[["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        romano = ""
        for simbolo, valor in reversed(lista_simbolos):
            if numero // valor:
                count = numero // valor
                romano += (simbolo * count)
                numero = numero % valor
        return romano

print(int_a_romano(499))
print(int_a_romano(875))
print(int_a_romano(32))
print(int_a_romano(124))