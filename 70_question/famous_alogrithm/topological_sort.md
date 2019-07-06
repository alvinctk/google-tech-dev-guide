A topological sort (or topological ordering) of a directed acyclic graph (DAG) is a linear ordering of its vertices such that very directed edge u -> v from vertex u to vertex v, u comes before v in the ordering. A topological ordering is possible if and only if the graph has no directed cycles, i.e. if the graph is directed acyclic graph (DAG).

Types of edges in DAG:

1. Tree edge (u, v)
- Vertex u has higher order than vertex v.

2. Back edge (u, v)
- Vertex v has higher order than vertex u.

3.Forward edge (u, v)
- Vertex u has higher order than vertex v.

4. Cross edge (u, v)
Vertex u has higher order than vertex v.

Notes:
- [Understanding the Topological sort using Depth-First-Search](https://medium.com/@yasufumy/algorithm-depth-first-search-76928c065692)
- [Detect cycle in a graph](https://www.geeksforgeeks.org/detect-cycle-in-a-graph/)
- [Topological Sorting](https://www.geeksforgeeks.org/topological-sorting/)
- [Topological Sorting using departure time](https://www.techiedelight.com/topological-sorting-dag/)
- [Topological lectures notes from UW](https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect20.pdf)
