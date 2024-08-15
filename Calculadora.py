class Calculadora:
    def adicionar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero não é permitida"
        return a / b
    
    def restoDaDivisao(self, a, b):
        return a % b

c = Calculadora()

print("adicionar: ", c.adicionar(10,5))
print("subtrair: ", c.subtrair(10,5))
print("multiplicar: ", c.multiplicar(10,5))
print("dividir: ", c.dividir(10,5))
print("restoDaDivisao: ", c.restoDaDivisao(10,5))