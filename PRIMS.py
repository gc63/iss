class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

class PrimMST:
    def __init__(self, edges, start_node):
        self.graph = {}
        for edge in edges:
            if edge.src not in self.graph:
                self.graph[edge.src] = []
            if edge.dest not in self.graph:
                self.graph[edge.dest] = []
            self.graph[edge.src].append((edge.dest, edge.weight))
            self.graph[edge.dest].append((edge.src, edge.weight))
        self.start_node = start_node

    def heappush(self, pq, item):
        pq.append(item)
        pq.sort(key=lambda x: x[0])

    def heappop(self, pq):
        return pq.pop(0)

    def prim_mst(self):
        visited = set()
        min_cost = 0
        pq = [(0, self.start_node, self.start_node)]

        while pq:
            weight, src, dest = self.heappop(pq)
            if dest not in visited:
                min_cost += weight
                print(f"Edge: src - dest Weight: ",weight)
                visited.add(dest)
                for neighbor, neighbor_weight in self.graph[dest]:
                    if neighbor not in visited:
                        self.heappush(pq, (neighbor_weight, dest, neighbor))

        return min_cost

if __name__ == "__main__":
    num_edges = int(input("Enter the number of edges: "))
    edges = []
    for i in range(num_edges):
        src, dest, weight = input(f"Enter source, destination, and weight of edge i + 1: ").split()
        edges.append(Edge(src, dest, int(weight)))

    start_node = input("Enter the starting node: ")

    prim = PrimMST(edges, start_node)
    print("Minimum Spanning Tree using Prim's algorithm:")
    total_cost = prim.prim_mst()
    print("Total minimum cost:", total_cost)