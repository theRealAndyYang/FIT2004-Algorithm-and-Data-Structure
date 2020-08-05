
import sys
import queue
import heapq

class Vertex:
    """
    this is the class for vertex which containing an ID and an array of tuple representing
    the edges
    """

    def __init__(self, vertex):
        """
        this is the initialisation of the vertex, it constructs the ID of the vertex and an 
        array of tuples containing (target, weight)
        @param vertex: an integer
        @return none
        @time-complexity: O(1)
        @space-complexity: O(e) where e is the number of edges
        """
        self.vertex_id = vertex
        self.adjacent = []
    
    def add_adjacent(self, target, weight = 0):
        """
        this method adds a neighbour(edge) to the vertex
        @param target: the target vertex
        @param weight: the weight of the edge
        @return none
        @time-complexity: O(1)
        @space-complexity: O(1)
        """
        self.adjacent.append((target, weight))

    def get_vertex(self):
        return self.vertex_id

    def get_adjacent(self):
        return self.adjacent

    def get_weight(self, target):
        for v in self.adjacent:
            if target == v[0]:
                return v[1]

class Graph:
    """
    this is the class for graph, which represented in adjacency list
    """

    def __init__(self, gfile):
        """
        this is the initialisation of the graph, it constructs an adjacency list
        @param gfile: a txt file containing a graph
        @return none
        @time-complexity: O(v^2) where v is the number of vertices in the graph
        @space-complexity: O(v+e) where v is the number of vertices and e is number of edges
        """
        file = open(gfile, "r")
        graph_info = file.read().splitlines()
        file.close()
        self.vertex_num = int(graph_info.pop(0))
        self.graph = []
        for v in range(self.vertex_num):
            self.add_vertex(v)
        for e in graph_info:
            self.add_edge(e)

    def add_vertex(self, new_vertex):
        """
        this method adds a vertex into the graph
        @param new_vertex: a new vertex
        @return none
        @time-complexity: O(1)
        @space-complexity: O(1)
        """
        vertex = Vertex(new_vertex)
        self.graph.append(vertex)
    
    def add_edge(self, new_edge):
        """
        this method adds an edge into the graph
        @param new_edge: a new edge as a list containing [start, end, weight]
        @return none
        @time-complexity: O(v) where v is the number of vertices in the graph
        @space-complexity: O(1)
        """
        new_edge = new_edge.split(" ")
        start = int(new_edge[0])
        end = int(new_edge[1])
        weight = int(new_edge[2])
        for v in self.graph:
            if v.vertex_id == start:
                v.add_adjacent(end, weight)
        # reverse
        for v in self.graph:
            if v.vertex_id == end:
                v.add_adjacent(start, weight)

    def shallowest_spanning_tree(self):
        SST = []
        for v in range(self.vertex_num):
            result = self.shallow_spanning_tree(v)
            if result[1] <= 1:
                return result
            SST.append(result)
        SST.sort(key = lambda x:x[1]) # O(NlogN)
        return SST[0]

    def shallow_spanning_tree(self, root):
        dist = [-1] * self.vertex_num
        pred = [None] * self.vertex_num
        q = queue.Queue(maxsize = self.vertex_num)
        q.put(root)
        dist[root] = 0
        while not q.empty():
            u = q.get()
            u = self.graph[u].get_vertex()
            adjacent = self.graph[u].get_adjacent()
            for v in adjacent:
                if dist[v[0]] == -1:
                    dist[v[0]] = dist[u] + 1
                    pred[v[0]] = u
                    q.put(v[0])
        return (root, max(dist))

    def shortest_errand(self, home, destination, ice_locs, ice_cream_locs):
        path = []
        path.append(home)
        total = 0
        ice_loc = 0
        ice_cream_loc = 0
        #while got_ice == False:
        temp = []
        to_ice = self.djikstra(home)
        for dest in ice_locs:
            for v in range(len(to_ice)):
                if dest == v:
                    temp.append((v, to_ice[v][0]))
        temp.sort(key = lambda x:x[1])
        local_min = temp[0]
        ice_loc = local_min[0]
        pre_vertex = ice_loc
        restore_walk = []
        while pre_vertex != home:
            restore_walk.append(pre_vertex)
            pre_vertex = to_ice[1][pre_vertex]
        for w in restore_walk:
            path.append(w)
        total += local_min[1]
        #while got_icecream == False:
        temp = []
        to_icecream = self.djikstra(ice_loc)
        for dest in ice_cream_locs:
            for v in range(len(to_icecream)):
                if dest == v:
                    temp.append((v, to_icecream[v][0]))
        temp.sort(key = lambda x:x[1])
        local_min = temp[0]
        ice_cream_loc = local_min[0]
        pre_vertex = ice_cream_loc
        restore_walk = []
        while pre_vertex != ice_cream_loc:
            restore_walk.append(pre_vertex)
            pre_vertex = to_icecream[1][pre_vertex]
        for w in restore_walk:
            path.append(w)
        total += local_min[1]
        #while got_dest == False:
        temp = []
        to_dest = self.djikstra(ice_cream_loc)
        for v in range(len(to_dest)):
            if dest == destination:
                temp.append((v, to_dest[v][0]))
        temp.sort(key = lambda x:x[1])
        local_min = temp[0]
        pre_vertex = destination
        restore_walk = []
        while pre_vertex != destination:
            restore_walk.append(pre_vertex)
            pre_vertex = to_dest[1][pre_vertex]
        for w in restore_walk:
            path.append(w)
        total += local_min[1]
        return (total, path)

    def shortest_path(self, start):
        """
        this method returns the shortest distance to all the vertex and the predecessor of a vertex using Djikstra's Algorithm
        @param start: the start vertex of the graph
        @return (distance to each vertex of the graph from start, predecessor of each vertex)
        @time-complexity: O(ElogV) where v is the number of vertex and e is the number of edge
        @space-complexity: O(v) where v is the number of vertices
        """
        dist = [sys.maxsize] * self.vertex_num
        dist[start] = 0
        pred = [None] * self.vertex_num
        q = []
        for v in range(self.vertex_num):
            heapq.heappush(q, (v, dist[v]))
        while not len(q) == 0:
            u = heapq.heappop(q)
            u = self.graph[u[0]].get_vertex()
            adjacent = self.graph[u].get_adjacent()
            for v in adjacent:
                if dist[u] + v[1] < dist[v[0]]:
                    dist[v[0]] = dist[u] + v[1]
                    for i in range(len(q)):
                        if q[i][0] == v[0]:
                            q[i] = (v[0], dist[u] + v[1])
                            break
                    pred[v[0]] = u
        # filter from dist
        return (dist, pred)