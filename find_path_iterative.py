import numpy as np
from queue import Queue


def find_path_iterative(matrix, start, end):
    stack = [start]
    path = []
    visited = set()

    while stack:
        current_position = stack.pop()
        x, y = current_position

        if current_position == end:
            path.append(current_position)
            break

        if current_position not in visited and 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 1:
            visited.add(current_position)
            path.append(current_position)
     
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            np.random.shuffle(directions)
            
            for direction in directions:
                new_position = (x + direction[0], y + direction[1])
                stack.append(new_position)

    return path if path else None



def cost_function(path):
    return len(path)



def shortest_path(n, mat, start, end):
    shortest_path = None
    shortest_length = float('inf')

    for _ in range(n): 
        path = find_path_iterative(mat, start, end)

        if path:
            length = cost_function(path)
            
            if length < shortest_length:
                shortest_path = path
                shortest_length = length
    return shortest_path



def find_path2(mat, start, end):
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]  
    
    visited = np.zeros_like(mat, dtype=bool)
    visited[start] = True
    
    queue = Queue()
    queue.put((start, []))
    
    
    while not queue.empty():
        (node, path) = queue.get()
        
        for dx, dy in directions:
            next_node = (node[0]+dx, node[1]+dy)
            
            if (next_node == end):
                print(next_node)
                return path + [next_node]
            if (next_node[0] >= 0 and next_node[1] >= 0 and 
                next_node[0] < len(mat) and next_node[1] < len(mat[0]) and 
                mat[next_node[0]][next_node[1]] == 1 and not visited[next_node]):
                visited[next_node] = True
                queue.put((next_node, path + [next_node]))