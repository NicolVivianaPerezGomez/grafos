class Graph:
    def __init__(self):
        self.graph = {}

    # Crear (Agregar nodo y arista) NODO: CIUDAD ARISTA: CONEXION
    def add_edge(self, ciudad, connections):
        if ciudad not in self.graph:
            self.graph[ciudad] = []  # Agregar ciudad si no existe
        self.graph[ciudad].append(connections)  # Agregar conexión a la ciudad

        # Asegurarse de que la ciudad conectada también esté en el grafo
        if connections not in self.graph:
            self.graph[connections] = []  # Agregar ciudad conectada si no existe

    # Leer (Mostrar las conexiones de un nodo osea ciudad)
    def get_connections(self, ciudad):
        return self.graph.get(ciudad, [])

    # Actualizar (Agregar un vecino adicional a un nodo)
    def update_edge(self, ciudad, connections, new_connections):
        if ciudad in self.graph and connections in self.graph[ciudad]:
            self.graph[ciudad].remove(connections)  # Eliminar la conexión antigua
            self.graph[ciudad].append(new_connections)  # Agregar la nueva conexión

            # Asegurarse de que la nueva conexión también esté en el grafo
            if new_connections not in self.graph:
                self.graph[new_connections] = []  # Agregar si no existe

    # Eliminar (Eliminar un nodo(ciudad) y sus conexiones)
    def delete_node(self, ciudad):
        if ciudad in self.graph:
            del self.graph[ciudad]  # Eliminar una ciudad del grafo
        for connections in self.graph.values():
            if ciudad in connections:
                connections.remove(ciudad)  # Eliminar una ciudad de las conexiones

    # Mostrar el grafo completo
    def display_graph(self):
        for ciudad, connections in self.graph.items():
            print(f"{ciudad}: {connections}")

# Uso
colombia = Graph()

# AGREGAR CONEXIONES:

# Manizales(0) CONEXIONES
colombia.add_edge('Manizales', 'Pereira')
colombia.add_edge('Manizales', 'Armenia')
colombia.add_edge('Manizales', 'Chinchiná')
colombia.add_edge('Manizales', 'Villamaría')
colombia.add_edge('Manizales', 'Palestina')
colombia.add_edge('Manizales', 'Neira')
colombia.add_edge('Manizales', 'La Virginia')
colombia.add_edge('Manizales', 'Dosquebradas')
colombia.add_edge('Manizales', 'Santa Rosa de Cabal')
colombia.add_edge('Manizales', 'Cartago')

#Pereira(1) CONEXIONES
colombia.add_edge('Pereira', 'Manizales')
colombia.add_edge('Pereira', 'Dosquebradas')
colombia.add_edge('Pereira', 'Cartago')
colombia.add_edge('Pereira', 'Ciscasia')
colombia.add_edge('Pereira', 'La Virginia')

#Armenia(2)
colombia.add_edge('Armenia', 'Manizales')
colombia.add_edge('Armenia', 'Pereira')
colombia.add_edge('Armenia','Santa Rosa de Cabal')
colombia.add_edge('Armenia','Cartago')
colombia.add_edge('Armenia','Calarcá')
colombia.add_edge('Armenia','La Tebaida')
colombia.add_edge('Armenia','Montenegro')
colombia.add_edge('Armenia','Ciscasia')
colombia.add_edge('Armenia','Dosquebradas')

#Chinchina(3)
colombia.add_edge('Chinchina','Manizales')

#Villamaría(4)
colombia.add_edge('Villamaria','Manizales')

#Palestina(5)
colombia.add_edge('Palestina','Manizales')

#Neira(6)
colombia.add_edge('Neira','Manizales')

#La Virginia(7)
colombia.add_edge('La Virginia','Cartago')
colombia.add_edge('La Virginia','Pereira')

#Dosquebradas(8)
colombia.add_edge('Dosquebradas','Manizales')
colombia.add_edge('Dosquebradas','Pereira')
colombia.add_edge('Dosquebradas','Cartago')
colombia.add_edge('Dosquebradas','Armenia')

#SantaRosadeCabal(9)
colombia.add_edge('Santa Rosa de cabal','Manizales')
colombia.add_edge('Santa Rosa de cabal','Pereira')
colombia.add_edge('Santa Rosa de cabal','Armenia')

#Cartago(10)
colombia.add_edge('Cartago','La Virginia')
colombia.add_edge('Cartago','Manizales')
colombia.add_edge('Cartago','Pereira')
colombia.add_edge('Cartago','Dosquebradas')
colombia.add_edge('Cartago','Armenia')

#Calarcá(11)
colombia.add_edge('Calarcá','Armenia')

#Ciscasia(12)
colombia.add_edge('Ciscasia','Armenia')

#La Tebaida(13)
colombia.add_edge('La Tebaida','Armenia')

#Montenegro(14)
colombia.add_edge('Montenegro','Armenia')

# MOSTRAR CONEXIONES
print("\n================CONEXIONES DE MANIZALES:================","\n",colombia.get_connections("Manizales"))

#ACTUALIZAR CONEXION
print("\n================DESPUÉS DE ACTUALIZAR UNA CONEXION:================",colombia.update_edge("Manizales","Pereira","Calarcá"))
colombia.display_graph()

#ELIMIAR UNA CIUDAD
print("\n================DESPUÉS DE ELIMINAR UNA CIUDAD PALESTINA:==========")
colombia.delete_node("Palestina")
colombia.display_graph()

# MOSTRAR EL GRAFO
print("\n=================GRAFO COMPLETO========================:")
colombia.display_graph()