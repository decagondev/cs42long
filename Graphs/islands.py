"""
Write a function that takes a 2D binary array and returns the number of 1 islands. 
An island consists of 1s that are connected to the north, south, east or west. 
For example:

each 1 island == Node / Vertex
each direction of N, S, E, W == Edge / Connection
"""
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]



def island_counter(islands):
    # some visited list / dict / matrix.
    visited = []
    # create our visited graph.
    for i in range(len(islands)):
        visited.append([False] * len(islands[0]))

    # set a counter to zero
    counter = 0
    # traverse the islands
    for col in len(islands[0]):
        for row in len(islands):
            # if we have not visited this island yet
            if not visited[row][col]:
                # if it is a 1 (when we hit an actual island)
                if islands[row][col] == 1:
                    # do a traversal and mark each of its neighbors as visited
                    visited = dft(row, col, islands, visited)
                    # increment a counter
                    counter += 1
                # otherwise just mark the element as visited
                else:
                    visited[row][col] = True
    
    # return the counter to the caller
    return counter

island_counter(islands) # returns 4