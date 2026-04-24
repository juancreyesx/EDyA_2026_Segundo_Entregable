# -*- coding: utf-8 -*-
# Parte C — Listas Enlazadas Simples

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # TODO 5: Insertar al final
    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    # TODO 6: Mostrar lista
    def mostrar_lista(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")

if __name__ == "__main__":
    print("== Listas Enlazadas ==")
    mi_lista = ListaEnlazada()
    mi_lista.insertar_final("Buga")
    mi_lista.insertar_final("Cali")
    mi_lista.insertar_final("Jamundí")
    mi_lista.mostrar_lista()