from hw3 import *

'''

<Example 1>

num_v = 4
num_e = 4

in_a = [ 0, 1, 2, 0 ]
in_b = [ 1, 2, 0, 3 ]

Answer :
0 1 2
3

<Example 2>

num_v = 10
num_e = 15

in_a = [0, 0, 0, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9]
in_b = [1, 2, 3, 4, 5, 6, 2, 4, 7, 9, 3, 5, 6, 5, 8]

3 2 3 4     [0, 1], [0, 2], [0, 3]
1 5         [1, 4]
2 6 7       [2, 5], [2, 6]
2 3 5       [3, 2], [3, 4]
1 8         [4, 7]
1 10        [5, 9]
2 4 6       [6, 3], [6, 5]
1 7         [7, 6]
1 6         [8, 5]
1 9         [9, 8]

Answer :
0
1
2 3 4 6 7
5 8 9

'''

if __name__=="__main__":
    print("Type your <Input>")
    num_line = input().split()
    num_v = int(num_line[0])
    num_e = int(num_line[1])

    adj_list = [ [] for _ in range(num_v) ]
    adj_mat = [ [ 0 for _ in range(num_v) ] for _ in range(num_v) ]
    in_a = []
    in_b = []

    for i in range(num_e) :
        edge_line = input().split()
        in_a.append(int(edge_line[0]))
        in_b.append(int(edge_line[1]))

    for (x, y) in zip(in_a, in_b):
        adj_list[x].append(y)
        adj_mat[x][y] = 1

    out = []
    print("Type your <Output>")
    for i in range(num_v) :
        out.append(int(input()))

    ''' Test for adjacency list '''
    ans1 = [ 0 for _ in range(num_v) ]
    scc1 = find_scc_with_adj_list(adj_list, num_v, num_e, ans1)
    for i in range(num_v) :
        if (ans1[i] != out[i]) :
            print("Fail!")
            break
    # print("answer list :", ans1)
    # for scc_id in range(scc1):
    #    for node_id in range(num_v):
    #        if ans1[node_id] == scc_id:
    #                print(node_id, end=" ")
    #    print("")

    ''' Test for adjacency matrix '''
    ans2 = [ 0 for _ in range(num_v) ]
    scc2 = find_scc_with_adj_mat(adj_mat, num_v, num_e, ans2)
    for i in range(num_v) :
        if (ans2[i] != out[i]) :
            print("Fail!")
            break
    # print("answer list :", ans2)
    # for scc_id in range(scc2):
    #    for node_id in range(num_v):
    #        if ans2[node_id] == scc_id:
    #            print(node_id, end=" ")
    #    print("")
