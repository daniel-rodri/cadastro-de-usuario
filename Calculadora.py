class Calculadora:
    def adicionar( a, b):
        return a + b

    def subtrair( a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        if b == 0:
            return "Erro: Divisão por zero não é permitida"
        return a / b
    
c = Calculadora(10,5)


print(c.adicionar)
print(c.subtrair)
print(c.multiplicar)
print(c.dividir)
