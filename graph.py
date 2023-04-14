class Node:
    #constructor
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

    #Function for testing, prints the node
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

    #constructor
    def __init__(self, conn_num : int, from_node : int, to_node : int, cost : int):
        self.conn_num = conn_num
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

    #Function for testing, prints connections
    def printConnection(self):
        print(
        self.conn_num,
        self.from_node,
        self.to_node,
        self.cost)

class Graph:
    #constructor
    def __init__(self):
        self.nodes = [] #list of nodes
        self.connections = [] #list of connections
        self.firstTime = True #used for file Output correction

    #Build the graph from given files
    def buildGraph(self, nodeFile, conFile):
        #open Node File
        with open(nodeFile, 'r') as fp:
            for line in fp:
                currentLine = line.strip()
                if not currentLine.startswith('#'):
                    info = line.split(',')
                    self.add_node(int(info[1]), float(info[7]), float(info[8])) 
                   
        #open Connection File
        with open(conFile, 'r') as fp:
            for line in fp:
                currentLine = line.strip()
                if not currentLine.startswith('#'):
                    info = line.split(',')
                    self.add_connection(int(info[1]), int(info[2]), int(info[3]), int(info[4])) 
                   
    #Function for testing, prints the entire graph Nodes and Connections      
    def printGraph(self):
        for n in self.nodes:
            n.printNode()
        
        for c in self.connections:
            c.printConnection()

    #adds a node
    def add_node(self, node_num, x, z):
        node = Node(node_num, x, z)
        self.nodes.append(node)

    #creates a connection and adds those connections to nodes
    def add_connection(self, conn_num, from_node_num, to_node_num, cost):
        from_node = self.nodes[from_node_num - 1]
        to_node = self.nodes[to_node_num - 1]
        connection = Connection(conn_num, from_node_num, to_node_num, cost)
        from_node.connections.append(connection)
        to_node.connections.append(connection)
        self.connections.append(connection)
