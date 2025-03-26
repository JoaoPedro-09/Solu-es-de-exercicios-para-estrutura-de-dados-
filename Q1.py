#Exercício 1:

def inverter_string(s):
    pilha = []
    for char in s:
        pilha.append(char)
    inverso = ""
    while pilha:
        inverso += pilha.pop()
    return inverso

print(inverter_string("Hello")) 


