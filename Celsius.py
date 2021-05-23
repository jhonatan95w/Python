# 6) A conversão de graus Fahrenheit para Celsius é obtida pela fórmula C=5/9(F-32).
#    Escreva um programa que calcule e apresente uma tabela de graus Celsius em função 
#    de grau Fahrenheit que vairem de 50 a 150, de 1 em 1.


for F in range (50,151,1):
    celsius=5/9*(F-32)
    print("Graus Celsius:  ""%.2f" %celsius)