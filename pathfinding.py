#   PROGRAM 3
#   Authors: Matthew Brown and Andrew Harkins
#   Class: CS 330 - 01
#   Date: March 31st, 2023
#==============================================
#   Astar Class File

import numpy
import math

showAstarIterations = False

UNDEFINED = 0
UNVISITED = 1
OPEN      = 2
CLOSED    = 3

class Astar:
    def __init__(self) -> None:
        pass

# Astar.find.lowest(graph, open.nodes) 
    def find_lowest(graph, open_nodes):
        """
        lowest.total   <- min(graph$nodes[open.nodes, TOTAL])                    # Determine lowest total cost of all open nodes
        result.indexes <- which(graph$nodes[open.nodes, TOTAL] == lowest.total)  # Find indexes of all open nodes with lowest total cost
        result         <- open.nodes[min(result.indexes)]                        # Find node number of lowest total cost open node with lowest index
        return(result)
        """
        total_costs = [graph["nodes"][node]["TOTAL"] for node in open_nodes]
        lowest_total = min(total_costs)  # Determine lowest total cost of all open nodes
        result_indexes = [i for i, cost in enumerate(total_costs) if cost == lowest_total]  # Find indexes of all open nodes with lowest total cost
        result = min([open_nodes[i] for i in result_indexes])  # Find node number of lowest total cost open node with lowest index
        return result

# Astar.heuristic(graph, node.1, node.2)
    def heuristic(graph, node1, node2):
        """
        distance <- sqrt((graph$nodes[node.2, LOC.X] - graph$nodes[node.1, LOC.X])^2 +
                   (graph$nodes[node.2, LOC.Z] - graph$nodes[node.1, LOC.Z])^2)
        return(distance)
        """
        distance = math.sqrt((graph["nodes"][node2]["LOC.X"] - graph["nodes"][node1]["LOC.X"])**2 +
                         (graph["nodes"][node2]["LOC.Z"] - graph["nodes"][node1]["LOC.Z"])**2)
        return distance

# Astar.get.connections(graph, current.node)
    def get_connections(graph, current_node):
        """
        result <- which(graph$connections[, FROM.NODE] == current.node)
        return(result)
        """
        result = [i for i, x in enumerate(graph["connections"][:, 0]) if x == current_node]
        return result

    def num_width(num, width, fill):
        return str(num).rjust(width, str(fill))   
    
# Astar.show.iteration.status(graph, iteration, current=NULL)
    def show_iteration_status(graph, iteration, current):
        """
        fill.symbols <- c(".", "O", "X")
        fill.display <- rep("?", graph$n)
        fill.display[1:graph$n] <- fill.symbols[graph$nodes[1:graph$n, STATUS]]
        if (!is.null(current)) { fill.display[current] <- "C" }

        write.text(trace.file, paste(
            "    ",   num.width(iteration, 2, 0),
            "     ",  num.width(length(which(graph$node[, STATUS] == UNVISITED)), 2, 0),
            "     ",  num.width(length(which(graph$node[, STATUS] == OPEN)),      2, 0),
            "     ",  num.width(length(which(graph$node[, STATUS] == CLOSED)),    2, 0), 
            "     ",  paste(fill.display, collapse=""), sep=""))
        """
        fill_symbols = [".", "O", "X"]
        fill_display = ["?" for i in range(graph["n"])]
        for i in range(graph["n"]):
            fill_display[i] = fill_symbols[graph["nodes"][i]["STATUS"]]
        if current is not None:
            fill_display[current] = "C"
        
        trace_file = open("trace.txt", "a")
        trace_file.write("    " + Astar.num_width(iteration, 2, 0) + 
                        "     " + Astar.num_width(len([node for node in graph["nodes"] if node["STATUS"] == UNVISITED]), 2, 0) + 
                        "     " + Astar.num_width(len([node for node in graph["nodes"] if node["STATUS"] == OPEN]), 2, 0) + 
                        "     " + Astar.num_width(len([node for node in graph["nodes"] if node["STATUS"] == CLOSED]), 2, 0) + 
                        "     " + "".join(fill_display) + "\n")
        trace_file.close()

         

# Astar.find.path(graph, first, last)
    def find_path(graph, first, last):
        """
        if (showAstarIterations == TRUE) {
            write.text(trace.file, paste("\n", "A* from ", first, " to ", last, sep=""))
            write.text(trace.file, paste("  itera  unvis   open  closed"))
        }
        """ 
        if showAstarIterations:
            trace_file = open("trace.txt", "a")
            trace_file.write("\nA* from " + str(first) + " to " + str(last) + "\n")
            trace_file.write("  itera  unvis   open  closed\n")
            trace_file.close()      