class Node:
    def __init__(self, node_num, x, z):
        self.node_num = node_num
        self.status = 1  # unvisited = 1, open = 2, closed = 3
        self.cost_so_far = float('inf')
        self.estimated_heuristic = None
        self.estimated_total = None
        self.previous_node = None
        self.x = x
        self.z = z
        self.connections = []

class Connection:
    def __init__(self, conn_num, from_node, to_node, cost):
        self.conn_num = conn_num
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

class Graph:
    def __init__(self):
        self.nodes = []
        self.connections = []

    def add_node(self, node_num, x, z):
        node = Node(node_num, x, z)
        self.nodes.append(node)

    def add_connection(self, conn_num, from_node_num, to_node_num, cost):
        from_node = self.nodes[from_node_num]
        to_node = self.nodes[to_node_num]
        connection = Connection(conn_num, from_node, to_node, cost)
        from_node.connections.append(connection)
        to_node.connections.append(connection)
        self.connections.append(connection)

