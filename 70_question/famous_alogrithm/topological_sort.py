from collections import defaultdict
from collections import deque


class Graph:


    def __init__(self, vertices, dependencies):
        self.graph = defaultdict(list)
        self.vertices = vertices

        # Add edge to graph
        for u, v in dependencies:
            self.graph[u].append(v)



    def topological_sort_util(self, v, visited, stack, cyclic_stack):
        """
        Return True if the graph is cyclic. Otherwise, returns False if graph is not cyclic.
        Depth First Search (DFS) recursively to determine the topological order.
        A valid topological order is stored in the stack.

        DAG (Directed Acylic Graph) has a topological order.
        A cyclic graph does not have topological order.
        """
        # Mark the current node as visited
        visited[v] = True

        # Mark current in this path/cycle to determine if graph is cyclic.
        cyclic_stack.appendleft(v)

        # Recursive for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.topological_sort_util(neighbour, visited, stack, cyclic_stack):
                    return True
            elif neighbour in cyclic_stack:
                print("{} -> {} is causing a cyclic graph {}.".format(v, neighbour, cyclic_stack))
                return True

        # Push current vertex to stack which stores the result
        stack.appendleft(v)

        # Remove current vertex in this path
        cyclic_stack.popleft()

        # No cyclic till here
        return False

    def topological_sort(self, dependencies):
        """
        Main function to retrieve topological sorted order.

        Returns a valid topological sorted order of vertices if graph
        is a DAG (Directed Acyclic Graph).

        Otherwise, returns an empty list for cyclic graph.
        """
        print("Performing topologicalSort({}))".format(dependencies))
        stack = deque()
        cyclic_stack = deque()
        visited = defaultdict(lambda: False)
        # Call the recursive helper function to store toplogical sort starting
        # from all vertices one by one
        for i in self.vertices:
            if not visited[i]:
                cyclic = self.topological_sort_util(i, visited, stack, cyclic_stack)
                if cyclic:
                    print("topologicalSort({})=[] is cyclic".format(dependencies))
                    return []

        stack = list(stack)
        # Print contents of the stack
        print("topologicalSort({})= {}".format(dependencies, stack))
        print()
        return stack

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and adds to recursion stack
        visited[v] = True
        recStack[v] = True

        #print("visiting v = ", v, recStack)

        # Recur for all neighbours
        # if any neighbour is visited and in recStack then graph is cyclic
        for neighbour in self.graph[v]:
            #print("visiting neighbour n = ", neighbour)
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False

        #print("reset v's stack", v, recStack)
        return False


    def is_cyclic(self):

        visited = defaultdict(lambda: False)
        stack = defaultdict(lambda: False)
        for i in self.vertices:
            if not visited[i]:
                if self.isCyclicUtil(i, visited, stack):
                    return True
        return False



def topologicalSort(jobs, dependencies):
    g = Graph(jobs, dependencies)

    #print(g.is_cyclic())

    return g.topological_sort(dependencies)




if __name__ == "__main__":
    jobs2 = [1, 2, 3, 4, 5, 6, 7, 8]
    deps2 = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [6, 7], [1, 2], [7, 6]]
    jobs, dependencies = [1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]


    topologicalSort(jobs, dependencies)
    topologicalSort(jobs2, deps2)
