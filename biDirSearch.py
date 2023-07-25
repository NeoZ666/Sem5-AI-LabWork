from collections import deque

def bidirectionalSearch(graph, start, target):
    # Create two sets to keep track of the nodes explored from the start and target nodes.
    startExplored = {start}
    targetExplored = {target}

    # Create two queues to keep track of the nodes to be explored from the start and target nodes.
    startQueue = deque([start])
    targetQueue = deque([target])

    while startQueue and targetQueue:
        # Perform one step of BFS from the start node.
        nodeFromStart = startQueue.popleft()
        for neighbor in graph[nodeFromStart]:
            if neighbor not in startExplored:
                startExplored.add(neighbor)
                startQueue.append(neighbor)

                # Check if this node is also explored from the target node.
                if neighbor in targetExplored:
                    return "Path found!"

        # Perform one step of BFS from the target node.
        nodeFromTarget = targetQueue.popleft()
        for neighbor in graph[nodeFromTarget]:
            if neighbor not in targetExplored:
                targetExplored.add(neighbor)
                targetQueue.append(neighbor)

                # Check if this node is also explored from the start node.
                if neighbor in startExplored:
                    return "Path found!"

    return "Path not found!"

# Create the adjacency list representation of the graph
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2, 7],
    5: [2, 8],
    6: [3, 9],
    7: [4, 10],
    8: [5],
    9: [6],
    10: [7]
}

start_node = 1
target_node = 10
result = bidirectionalSearch(graph, start_node, target_node)
print(result)
