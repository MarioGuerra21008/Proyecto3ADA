# Universidad del Valle de Guatemala
# Análisis y Diseño de Algoritmos - Sección: 20
# Proyecto 3 - Implementación de algoritmo MTF
# Mario Antonio Guerra Morales - Carné: 21008

# Función para calcular el costo de acceso en el algoritmo MTF (Move-to-Front)
def mtf_access_cost(config_list, sequence):
    access_cost = 0  # Inicializar el costo de acceso
    reorganization_cost = 0  # Inicializar el costo de reorganización
    
    # Iterar sobre cada solicitud en la secuencia
    for s in sequence:
        access_cost += 1  # Incrementar el costo de acceso para cada solicitud
        
        # Verificar si el elemento está en la lista de configuración
        if s in config_list:
            # Calcular el costo de reorganización como la distancia del elemento al frente de la lista
            reorganization_cost += config_list.index(s)
            
            # Mover el elemento al frente de la lista
            config_list.remove(s)
            config_list.insert(0, s)
        else:
            # Si el elemento no está en la lista, agregarlo al frente
            config_list.insert(0, s)
        
        # Imprimir la configuración de la lista, la solicitud y los costos
        print("Configuración de la lista:", config_list)
        print("Solicitud:", s)
        print("Costo de acceso:", access_cost)
        print("Costo de reorganización:", reorganization_cost)
    
    # Calcular el costo total sumando el costo de acceso y el costo de reorganización
    total_cost = access_cost + reorganization_cost
    print("Costo total de los accesos:", total_cost)

# Función para calcular el costo de acceso en el algoritmo IMTF (Improved Move-to-Front)
def imtf_access_cost(config_list, sequence):
    access_cost = 0  # Inicializar el costo de acceso
    reorganization_cost = 0  # Inicializar el costo de reorganización
    
    # Iterar sobre cada solicitud en la secuencia
    for i, s in enumerate(sequence):
        if s in sequence[:i]:  # Verificar si el elemento ha sido accedido previamente
            access_cost += 1
            
            # Calcular el costo de reorganización si el elemento se mueve al frente de la lista
            if s != config_list[0]:
                reorganization_cost += s
                config_list.remove(s)
                config_list.insert(0, s)
        else:
            access_cost += 1
            reorganization_cost += s
        
        # Imprimir la configuración de la lista, la solicitud y los costos
        print("Configuración de la lista:", config_list)
        print("Solicitud:", s)
        print("Costo de acceso:", access_cost)
        print("Costo de reorganización:", reorganization_cost)
    
    # Calcular el costo total sumando el costo de acceso y el costo de reorganización
    total_cost = access_cost + reorganization_cost
    return total_cost

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
total_cost_best = imtf_access_cost(config_list, sequence)
print("Costo total de acceso en el mejor caso de MTF:", total_cost_best)

# Peor caso de MTF: secuencia con un solo elemento repetido
config_list = [0, 1, 2, 3, 4]
sequence = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
print("\nPeor caso de MTF:")
total_cost_worst = imtf_access_cost(config_list, sequence)
print("Costo total de acceso en el peor caso de MTF:", total_cost_worst)
