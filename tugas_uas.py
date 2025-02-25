from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # Menyimpan hubungan antar kategori pengeluaran
        self.costs = {}   # Menyimpan biaya untuk setiap kategori pengeluaran

    # Menambahkan edge (sisi) ke dalam graf dan biaya untuk kategori
    def add_edge(self, u, v, cost_u, cost_v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
        
        # Menyimpan biaya untuk kategori pengeluaran
        self.costs[u] = cost_u
        self.costs[v] = cost_v

    # Algoritma BFS untuk menelusuri graf dan menampilkan biaya pengeluaran
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        total_cost = 0  # Menyimpan total biaya pengeluaran
        print(f"Mulai penelusuran pengeluaran dari: {start}")
        
        while queue:
            node = queue.popleft()
            print(f"Menelusuri kategori pengeluaran: {node}, Biaya: Rp{self.costs[node]}")
            total_cost += self.costs[node]  # Menambahkan biaya kategori ke total biaya
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # Menampilkan total biaya pengeluaran
        print(f"\nTotal pengeluaran keluarga: Rp{total_cost}")

# Membuat objek graf dan menambahkan kategori pengeluaran
graph = Graph()

# Menambahkan kategori pengeluaran, hubungan antar kategori, dan biaya
graph.add_edge("Makanan", "Transportasi", 100000, 50000)
graph.add_edge("Makanan", "Kesehatan", 100000, 70000)
graph.add_edge("Transportasi", "Hiburan", 50000, 30000)
graph.add_edge("Kesehatan", "Hiburan", 70000, 30000)

# Menjalankan BFS untuk menelusuri graf dari kategori 'Makanan'
graph.bfs("Makanan")