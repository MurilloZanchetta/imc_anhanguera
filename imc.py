class Imc:
    
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso
        self.calculo()
        
    def calculo(self):
        self.imc = self.peso / (self.altura ** 2)
        
    def mostrar_imc(self) -> float:
        
        if self.imc < 18.5:
            return f'Você está abaixo do peso. Seu imc é:  {self.imc:.2f}'
        elif self.imc >= 18.6 and self.imc <= 24.9:
            return f'Peso ideal, Parabéns! Seu imc é:  {self.imc:.2f}'
        elif self.imc >= 25 and self.imc <= 29.9:
            return f'Levemente acima do peso. Seu imc é:  {self.imc:.2f}'
        elif self.imc >= 30 and self.imc <= 34.9:
            return f'Obesidade grau I. Seu imc é:  {self.imc:.2f}'
        elif self.imc >= 35 and self.imc <= 39.9:
            return f'Obesidade grau II (severa). Seu imc é:  {self.imc:.2f}'
        elif self.imc >= 40:
            return f'Obesidade grau III (mórbita). Seu imc é:  {self.imc:.2f}'

            
            
altura = float(input('Digite a sua altura em (mts): '))
peso = float(input('Digite a seu peso em (kg): '))


calculo = Imc(altura, peso)

resultado = calculo.mostrar_imc()

print(resultado)