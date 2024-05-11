# Universidad del Valle de Guatemala
# Análisis y Diseño de Algoritmos - Sección: 20
# Proyecto 3 - Implementación de algoritmo MTF
# Mario Antonio Guerra Morales - Carné: 21008

def mtf_access_cost(config_list, sequence):
    access_cost = 0
    reorganization_cost = 0
    
    for s in sequence:
        access_cost += 1  # Incrementar el costo de acceso para cada solicitud
        
        if s in config_list:
            # Calcular el costo de reorganización como la distancia del elemento al frente de la lista
            reorganization_cost += config_list.index(s)
            
            # Mover el elemento al frente de la lista
            config_list.remove(s)
            config_list.insert(0, s)
        else:
            # Si el elemento no está en la lista, simplemente agregarlo al frente
            config_list.insert(0, s)
        
        print("Configuración de la lista:", config_list)
        print("Solicitud:", s)
        print("Costo de acceso:", access_cost)
        print("Costo de reorganización:", reorganization_cost)
    
    total_cost = access_cost + reorganization_cost
    print("Costo total de los accesos:", total_cost)

def imtf_access_cost(config_list, sequence):
    access_cost = 0
    for i, s in enumerate(sequence):
        if s in sequence[:i]:
            access_cost += 1
            config_list.remove(s)
            config_list.insert(0, s)
        else:
            access_cost += 1
        print("Configuración de la lista:", config_list)
        print("Solicitud:", s)
        print("Costo de acceso:", access_cost)
    return access_cost

# Prueba de la primera secuencia de solicitudes
print("Primera secuencia de solicitudes!!!")
config_list = [0, 1, 2, 3, 4]
sequence = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
mtf_access_cost(config_list, sequence)
print("\n\n")

# Prueba de la segunda secuencia de solicitudes
print("Segunda secuencia de solicitudes!!!")
config_list = [0, 1, 2, 3, 4]
sequence = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
mtf_access_cost(config_list, sequence)
print("\n\n")

# Prueba de la tercera secuencia de solicitudes
print("Tercera secuencia de solicitudes!!!")
config_list = [0, 1, 2, 3, 4]
sequence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mtf_access_cost(config_list, sequence)
print("\n\n")

# Prueba de la cuarta secuencia de solicitudes
print("Cuarta secuencia de solicitudes!!!")
config_list = [0, 1, 2, 3, 4]
sequence = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
mtf_access_cost(config_list, sequence)
print("\n\n")

# Prueba de la quinta secuencia de solicitudes
print("Quinta secuencia de solicitudes!!!")
config_list = [0, 1, 2, 3, 4]
sequence = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
mtf_access_cost(config_list, sequence)
print("\n\n")

# Prueba de la sexta secuencia de solicitudes

# Mejor caso de MTF:
config_list = [0, 1, 2, 3, 4]
sequence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print("Mejor caso de MTF:")
total_cost_best = imtf_access_cost(config_list.copy(), sequence)
print("Costo total de acceso en el mejor caso de MTF:", total_cost_best)

# Peor caso de MTF: secuencia con un solo elemento repetido
config_list = [0, 1, 2, 3, 4]
sequence = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
print("\nPeor caso de MTF:")
total_cost_worst = imtf_access_cost(config_list.copy(), sequence)
print("Costo total de acceso en el peor caso de MTF:", total_cost_worst)