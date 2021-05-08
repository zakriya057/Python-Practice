## Iterative BFS
['S', 'C', 'D', 'A', 'F', 'E', 'B', 'G']
## Recursive DFS
from queue import PriorityQueue
graph={
    'S':{'A':3,'C':2,'D':2},
    'A':{},
    'C':{'F':1},
    'D':{'G':8,'B':3},
    'B':{'E':2},
    'F':{'G':4,'E':0},
    'E':{'G':2},
    'G':{}
}
def uniformcost(mygraph,start,end,cost):
    q = PriorityQueue()
    q.put((0,start))
    path=[]
    while q:
        vertex=q.get(0)
        x=vertex[-1][-1]
        if x not in path:
            path.append(x)
        if x == end:
            print("The cost from starting point to the Goal node is :",vertex[0])
            print("And the paths visited are",path)
            w=str(vertex)
            s=''
            for i in path:
                if i in w:
                    s+=i
                    s+='-'
            return s
        g=list(mygraph[x].keys())
        w=list(mygraph[x].values())
        for i in range(len(g)):
              add=list(vertex)
              add.append(g[i])
              f=((vertex[0]+w[i]),add)
              q.put(f)
    return path
        
#print(graph)
print(uniformcost(graph,"S","G",0))