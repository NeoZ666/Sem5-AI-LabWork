from collections import deque

def BiDirectionalSearch(graph,start,target):
    startExplored = {start}
    targetExplored = {target}

    startQue = deque([start])
    targetQue = deque([target])

    while startQue and targetQue:

        nodeFromStart = startQue.popleft()
        for neighb in graph[nodeFromStart]:
            if neighb not in startExplored:
                startQue.append(neighb)
                startExplored.add(neighb)

                if neighb in targetExplored:
                    return f"Path Found! {targetExplored} and {startExplored}"

        nodeFromTarget = targetQue.popleft()
        for neighb in graph[nodeFromTarget]:
            if neighb not in targetExplored:
                targetQue.append(neighb)
                targetExplored.add(neighb)

                if neighb in startExplored:
                    return f"Path Found! {targetExplored} and {startExplored}"

    return "Path not found!"

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
result = BiDirectionalSearch(graph, start_node, target_node)
print(result)
