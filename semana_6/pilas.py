# -*- coding: utf-8 -*-
# Parte A — Pilas (LIFO)

# TODO 1: Invertir una cadena usando una pila
def invertir_cadena(texto):
    pila = []
    # Metemos cada letra en la pila
    for caracter in texto:
        pila.append(caracter)
    
    texto_invertido = ""
    # Sacamos de la pila (sale en orden inverso)
    while pila:
        texto_invertido += pila.pop()
    
    return texto_invertido

# TODO 2: Verificación de paréntesis balanceados
def parentesis_balanceados(expresion):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    
    for caracter in expresion:
        if caracter in "( [{":
            pila.append(caracter)
        elif caracter in ") ]}":
            if not pila or pila.pop() != pares[caracter]:
                return False
    return len(pila) == 0

if __name__ == "__main__":
    print("== Pilas ==")
    palabra = "UAO-Cali"
    print(f"Original: {palabra} -> Invertida: {invertir_cadena(palabra)}")
    
    ejemplo = "{[()()]}"
    print(f"¿'{ejemplo}' está balanceado?: {parentesis_balanceados(ejemplo)}")