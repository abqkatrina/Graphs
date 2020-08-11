from util import Stack, Queue
# graph is the family tree -- make graph class with methods
class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            pass
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            return('Vertex does not exist')

    def get_parents(self, vertex_id):
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_vertex):
    # make tree
    tree = Graph()
    # for every relationship, add a parent and a child with an edge between
    for x in ancestors:
        tree.add_vertex(x[0])
        tree.add_vertex(x[1])
        tree.add_edge(x[1], x[0])
    # make a stack of vertices and add the first vertex
    s = Stack()
    s.push([starting_vertex])
    # make a list of visited vertices
    visited = set()
    # make and object of results to print
    results = []
    # while there is something in the stack
    while s.size() > 0:
        # p is the current relationship -- popped from the stack
        p = s.pop()
        # the last vertex is the last in the relationship p
        last = p[-1]
        # 
        if len(tree.get_parents(last)) == 0:
            results.append(p)
        # mark last vertex as visited and its parents added to their own copy of the stack
        if last not in visited:
            visited.add(last)
            for n in tree.get_parents(last):
                copy = p.copy()
                copy.append(n)
                s.push(copy)
    print(results)
    # when stack is empty, if the results is same as the start, there is no parent
    if results[-1][-1] == starting_vertex:
        return -1
    else:
    # find the longest result -- furthest ancestor
        max_length = max([len(i) for i in results])
        return min([i[-1] for i in results if len(i) == max_length])
