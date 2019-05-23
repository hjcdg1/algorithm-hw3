from itertools import product

# Initialization of the variables used as visit flag
def init_DFS_visited(num_v) :
    global visited      # flag indicating if each vertex is visted
    visited = [False for i in range(num_v)]

# Initialization of the variables related to time
def init_DFS_time(num_v) :
    global time         # elapsed time
    global time_d       # discover time of each vertex
    global time_f       # finish time of each vertex
    time = 0
    time_d = [0 for i in range(num_v)]
    time_f = [0 for i in range(num_v)]

# Increase (elapsed) time by 1
def increase_time() :
    global time
    time = time + 1

# Transpose graph represented by adjacency matrix
def transpose_matrix(adj_matrix, num_v, num_e) :
    new_adj_matrix = [[0]*num_v for i in range(num_v)]
    for (i, j) in product(range(num_v), range(num_v)) :
        new_adj_matrix[i][j] = adj_matrix[j][i]
    return new_adj_matrix

# Transpose graph represented by adjacency list
def transpose_list(adj_list, num_v, num_e) :
    new_adj_list = [[] for i in range(num_v)]
    for i in range(num_v) :
        for j in adj_list[i] :
            new_adj_list[j].append(i)
        new_adj_list[j].sort()
    return new_adj_list

# Depth-First Search of G represented by adjacency matrix
def DFS_matrix(adj_matrix, num_v, num_e, ans, is_sorted = False) :
    # print("=========================================================")
    init_DFS_visited(num_v)
    if not is_sorted :
        init_DFS_time(num_v)
        V = range(num_v)
    else :
        V = list(range(num_v))
        V.sort(key = lambda v : time_f[v], reverse = True)
    SCC_id = '0'
    for v in V :
        if not visited[v] :
            DFS_matrix_helper(adj_matrix, num_v, num_e, v, ans, SCC_id)
            SCC_id = str(int(SCC_id) + 1)
    # print("=========================================================")
    return

# Depth-First Search helper function for G represented by adjacency matrix
def DFS_matrix_helper(adj_matrix, num_v, num_e, v, ans, SCC_id) :
    increase_time()
    time_d[v] = time
    visited[v] = True
    # print("방문 노드:", v, "그룹 : ", SCC_id)
    ans[v] = SCC_id
    for neighbor, is_neighbor in enumerate(adj_matrix[v]) :
        if (is_neighbor == 1 and not visited[neighbor]) :
            DFS_matrix_helper(adj_matrix, num_v, num_e, neighbor, ans, SCC_id)
    increase_time()
    time_f[v] = time

# Depth-First Search of G represented by adjacency matrix
def DFS_list(adj_list, num_v, num_e, ans, is_sorted = False) :
    # print("=========================================================")
    init_DFS_visited(num_v)
    if not is_sorted :
        init_DFS_time(num_v)
        V = range(num_v)
    else :
        V = list(range(num_v))
        V.sort(key = lambda v : time_f[v], reverse = True)
    SCC_id = '0'
    for v in V :
        if not visited[v] :
            DFS_list_helper(adj_list, num_v, num_e, v, ans, SCC_id)
            SCC_id = str(int(SCC_id) + 1)
    # print("=========================================================")
    return

# Depth-First Search helper function for G represented by adjacency list
def DFS_list_helper(adj_list, num_v, num_e, v, ans, SCC_id) :
    increase_time()
    time_d[v] = time
    visited[v] = True
    # print("방문 노드 :", v, "그룹 : ", SCC_id)
    ans[v] = SCC_id
    for neighbor in adj_list[v] :
        if not visited[neighbor] :
            DFS_list_helper(adj_list, num_v, num_e, neighbor, ans, SCC_id)
    increase_time()
    time_f[v] = time

# Get strongly connected components of G represented by adjacency matrix
def find_scc_with_adj_mat(adj_matrix, num_v, num_e, ans) :
    DFS_matrix(adj_matrix, num_v, num_e, ans)  # Run DFS on G to compute finish time for each vertex
    adj_matrix_t = transpose_matrix(adj_matrix, num_v, num_e)  # Compute transpose of G
    DFS_matrix(adj_matrix_t, num_v, num_e, ans, is_sorted = True)  # Run DFS on G_t to get answer on SCC

    SCC_ids = list()
    for SCC_id in ans :
        if not (SCC_id in SCC_ids) :
            SCC_ids.append(SCC_id)
    table = dict()
    k = 0
    for SCC_id in SCC_ids :
        table[SCC_id] = k
        k = k + 1
    for v in range(num_v) :
        ans[v] = table[ans[v]]

    return len(SCC_ids)

# Get strongly connected components of G represented by adjacency list
def find_scc_with_adj_list(adj_list, num_v, num_e, ans) :
    DFS_list(adj_list, num_v, num_e, ans)  # Run DFS on G to compute finish time for each vertex
    adj_list_t = transpose_list(adj_list, num_v, num_e)  # Compute transpose of G
    DFS_list(adj_list_t, num_v, num_e, ans, is_sorted = True)  # Run DFS on G_t to get answer on SCC

    SCC_ids = list()
    for SCC_id in ans :
        if not (SCC_id in SCC_ids) :
            SCC_ids.append(SCC_id)
    table = dict()
    k = 0
    for SCC_id in SCC_ids :
        table[SCC_id] = k
        k = k + 1
    for v in range(num_v) :
        ans[v] = table[ans[v]]

    return len(SCC_ids)
