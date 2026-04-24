# -*- coding: utf-8 -*-
# Parte B — Colas
from collections import deque
import heapq

# TODO 3: Simulación de turnos con cola (FIFO)
def simulacion_turnos(clientes):
    print(f"Iniciando simulación con: {clientes}")
    # Convertimos la lista en una cola (deque)
    cola = deque(clientes)
    
    while cola:
        # Desencolamos al primero que llegó (izquierda)
        cliente_actual = cola.popleft()
        print(f"Atendiendo a: {cliente_actual}")
        print(f"Quedan en espera: {list(cola)}")

# TODO 4: Cola de prioridad de tareas con heapq
def cola_priority(tareas):
    # tareas: lista de tuplas (prioridad, tarea)
    # Creamos una lista vacía que funcionará como nuestro "heap"
    heap = []
    
    # Encolar todas las tareas respetando su prioridad
    for item in tareas:
        heapq.heappush(heap, item)
        print(f"Agregada: {item[1]} con prioridad {item[0]}")

    print("\n--- Atendiendo por orden de prioridad ---")
    
    while heap:
        # Extraemos el que tenga el número de prioridad más BAJO (el más importante)
        prioridad, descripcion = heapq.heappop(heap)
        print(f"Ejecutando: '{descripcion}' (Prioridad: {prioridad})")

if __name__ == "__main__":
    print("== Colas ==")
    print("Simulación de turnos:")
    simulacion_turnos(["Cliente1", "Cliente2", "Cliente3"])

    print("\nCola de prioridad:")
    # Nota: El número menor es la prioridad más ALTA (1 es más urgente que 3)
    cola_priority([(2,"tarea media"), (1,"tarea alta"), (3,"tarea baja")])