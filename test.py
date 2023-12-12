from sys import maxsize
from itertools import permutations
v=4

def tspb(graph,s):
    vertex =[]

    for i in range(v):
        if i != s:
            vertex.append(i)

        main_path = maxsize
        next_permutation = permutations(vertex)
        for i in next_permutation:
            
            current_pathweight =0
            k=s

            for j in i:
                current_pathweight += graph[k][j]
                k=j
            current_pathweight += graph[k][s]

            main_path = min(main_path,current_pathweight)
    
    return main_path


if __name__ == "__main__":
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
    [15, 35, 0, 30], [20, 25, 30, 0]]
    s=0
    print(tspb(graph,s))
