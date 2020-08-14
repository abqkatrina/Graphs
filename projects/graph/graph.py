"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # vertices have connections
        self.vertices[vertex_id]= set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # edges connect two vertices which must already have been added
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            return('Vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # return the vertices added by the id given
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue and add the first vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # keep track of which vertices have been visited so as not to revisit them
        visited = set()
        # while there is something in the queue...
        while q.size() > 0:
            # the current vertex is the one taken from the queue
            v = q.dequeue()
            # if it's not already visited, mark it visited, else ignore
            if v not in visited:
                visited.add(v)
                print(v)
                # repeat the process with the next vertex connected to the current vertex
                # by putting in the queue to be set as the current vertex
                for n in self.get_neighbors(v):
                    q.enqueue(n)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack to call from, starting with the first vertex
        s = Stack()
        s.push(starting_vertex)
        # keep track of visited vertices
        visited = set()
        while s.size() > 0:
            # current vertex is off the stack
            v = s.pop()
            # if it's not already visited, mark visited and move next vertex onto stack
            if v not in visited:
                visited.add(v)
                print(v)
                for n in self.get_neighbors(v):
                    s.push(n)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # base progress on list of visited vertices, keeping track by adding the current vertex
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        # for each vertex --starting from start -- if it hasn't been visited, repeat process
        for n in self.get_neighbors(starting_vertex):
            if n not in visited:
                self.dft_recursive(n, visited)
            

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # for a search, we need to return a specific path
        path = []
        path.append(starting_vertex)
        # the queue keeps the path as an item
        q = Queue()
        q.enqueue(path)
        # keep track of visited vertices
        visited = set()

        while q.size() > 0 :
            cur_path = q.dequeue()
            cur_node = cur_path[-1]
            # the last vertex in the queue's current path is the current node
            # if that node is the destination, program is done, return path
            if cur_node == destination_vertex:
                return cur_path
            # if node is not destination, and it hasn't already been visited
            if cur_node not in visited:
                # mark the node visited and copy a path for each neighboring vertex
                visited.add(cur_node)
                for n in self.get_neighbors(cur_node):
                    path_copy = cur_path[:]
                    # add the neighbor to their copy of the path
                    path_copy.append(n)
                    # add that path to the queue and repeat process with this path as current
                    q.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # keep track of visited vertices
        visited = set()
        # make a stack of items starting with the first vertex
        s = Stack()
        s.push([starting_vertex])
        # while there's something in the stack, choose the latest too be the path
        while s.size() > 0:
            path = s.pop()
            # make the current vertex the last in the current path
            v = path[-1]
            if v not in visited:
                # if the current vertext is the destinations, we're done; return path
                if v == destination_vertex:
                    return path
                # mark current vertex visited
                visited.add(v)
                # make a path for each neighboring vertex and add them to it
                for n in self.get_neighbors(v):
                    copy = list(path)
                    copy.append(n)
                    # add that path to the stack and start again
                    s.push(copy)
        

    def dfs_recursive(self, starting_vertex, destination_vertex, path = None, visited = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order. This should be done using recursion.
        """
        # basing progress on visited vertices
        if visited is None:
            visited = set()
        # need to return a specific path, starting with the origin
        if path is None:
            path = []
        path.append(starting_vertex)
        # work from the current vertex which is the origin and mark it visited
        cur = starting_vertex
        visited.add(cur)
        # if we are at the destination, we're done; return path
        if cur == destination_vertex:
            return path
        # else: make a copy of path for neighbors of current vertex
        for n in self.get_neighbors(cur):
            copy = path.copy()
            # if the neighbor hasn't been visited, make a new path and run again
            if n not in visited:
                new_path = self.dfs_recursive(n, destination_vertex, copy, visited)
                if new_path:
                    return new_path
        return None




if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
