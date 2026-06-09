import math

# Adjacency Matrix

M = math.inf # Representasi "tidak ada jalur"

# Adjacency Matrix untuh graph berarah berbobot
# Node: 1, 2, 3, 4, 5 (index 0 = node 1, dst.)

ad_matrix = [
    # 1    2    3    4    5
    [ M,   1,   3,   M,   M], # dari node 1
    [ M,   M,   1,   M,   5], # dari node 2
    [ 3,   M,   M,   2,   M], # dari node 3
    [ M,   M,   M,   M,   1], # dari node 4
    [ M,   M,   M,   M,   M], # dari node 5
]

# Graph list?

graph_list = {
    1: [(2, 1), (3, 3)],
    2: [(3, 1), (5, 5)],
    3: [(1, 3), (4, 2)],
    4: [(5, 1)],
    5: []
}