class Node:
    def __init__(self, node_num, x, z):
        self.node_num = node_num
        self.status = 1  # unvisited = 1, open = 2, closed = 3
        self.cost_so_far = float('inf')
        self.heuristic = None
        self.total = None
        self.previous_node = None
        self.x = x
        self.z = z
        self.connections = []

    def printNode(self):
        print(
        self.node_num,
        self.status,  # unvisited = 1, open = 2, closed = 3
        self.cost_so_far,
        self.heuristic,
        self.total,
        self.previous_node,
        self.x,
        self.z)

class Connection:
    def __init__(self, conn_num, from_node, to_node, cost):
        self.conn_num = conn_num
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

    def printConnection(self):
        print(
        self.conn_num,
        self.from_node,
        self.to_node,
        self.cost)

class Graph:
    def __init__(self):
        self.nodes = []
        self.connections = []

    def buildGraph(self, nodeFile, conFile):
        with open(nodeFile, 'r') as fp:
            for line in fp:
                currentLine = line.strip()
                if not currentLine.startswith('#'):
                    info = line.split(',')
                    self.add_node(info[1], info[7], info[8]) 
                   #print(info[1], info[7], info[8])

        with open(conFile, 'r') as fp:
            for line in fp:
                currentLine = line.strip()
                if not currentLine.startswith('#'):
                    info = line.split(',')
                    self.add_connection(info[1], int(info[2]), int(info[3]), int(info[4])) 
                    #print(info[1], int(info[2]), int(info[3]), int(info[4]))
                    
    def printGraph(self):
        for n in self.nodes:
            n.printNode()
        
        for c in self.connections:
            c.printConnection()

    def add_node(self, node_num, x, z):
        node = Node(node_num, x, z)
        self.nodes.append(node)

    def add_connection(self, conn_num, from_node_num, to_node_num, cost):
        from_node = self.nodes[from_node_num - 1]
        to_node = self.nodes[to_node_num - 1]
        connection = Connection(conn_num, from_node, to_node, cost)
        from_node.connections.append(connection)
        to_node.connections.append(connection)
        self.connections.append(connection)

g = Graph()
g.buildGraph('CS 330, Pathfinding, Graph AB Nodes v3.txt', 'CS 330, Pathfinding, Graph AB Connections v3.txt')
g.printGraph()