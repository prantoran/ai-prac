#Name: Pinku Deb Nath
#NSU ID: 1310610042
#assignment no: 1

from queue import PriorityQueue
from sys import maxsize
inf = maxsize-1000

parents=[]        #to store the index of the parent of the node in the minimum cost path from source
parentstepcost=[] #to store the path cost from parent of child node, used in the printpath() function
cityindex={}   #dictionary to map city name strings to city node numbers
citynames={}   #dictionary to map city node numbers to city name strings
nodes=1
Graph=[]       #to store the Graph of the citi map

def printpath(p,des):
    pathlist=[]
    cid=des
    while( parents[cid] ):   #source node has parents[source]=0
        pathlist.append((parents[cid],cid))  #adding (parent,child) pair
        cid=parents[cid]
    pathlist=pathlist[::-1]  #reversing the pathlist
    for item in pathlist:
       u,v=map(int,item)
       print(citynames[u]," to ",citynames[v],", ",parentstepcost[v]," km",sep="")
                             #seps defines the char to print in place of ,

def dijkstra(G,src,des):
    dist=[(inf)]*len(G)      #all distances are set max value
    
    Q=PriorityQueue()  
    dist[src]=0          
    Q.put((0,src))           #pushed (cost,source) pair into priority queue

    found = False
    while(Q.empty()==False and found==False):
        curcost,curnode=Q.get()
        if (curnode==des):
            found=True       #check for destination node
        else:
            for childnode,pathcost in G[curnode]:
                if (dist[childnode]>pathcost+curcost): #check to find better path
                    dist[childnode]=pathcost+curcost   #updating path cost
                    Q.put((dist[childnode],childnode))
                    parents[childnode]=curnode
                    parentstepcost[childnode]=pathcost #this will be needed in the printpath() fucntion
    return dist[des]


filename,source,destination=map(str,input().split())

fin= open(filename,"r")

fin.close()

#counting and mapping the cities to unique node numbers

fin= open(filename,"r")
while(1):
    v1,v2,val=map(str,fin.readline().split())
    
    if v1=="END" and v2=="OF" and val=="INPUT":
        break;                         #check for end of file (EOF)
    val=int(val)
    if v1 not in cityindex.keys():
        cityindex[v1]=nodes
        citynames[nodes]=v1
        nodes+=1
    if v2 not in cityindex.keys():
        cityindex[v2]=nodes
        citynames[nodes]=v2
        nodes+=1
        
fin.close()


source=cityindex[source]
destination=cityindex[destination]

#creating the graph

Graph = [ [] for i in range(nodes+1)]  #setting up initial graph using path comprehension

#taking the graph input

fin= open(filename,"r")

while(1):
    v1,v2,val=map(str,fin.readline().split())
    
    if v1=="END" and v2=="OF" and val=="INPUT":
        break;
    val=int(val)
    u=cityindex[v1]
    v=cityindex[v2]
    Graph[u].append((v,val))
    Graph[v].append((u,val))

fin.close()

#setting up the initial parents and parentstepcost lists
parents=[0]*(nodes+2)
parentstepcost=[0]*(nodes+2)

distance=dijkstra(Graph,source,destination)

#inf refers to max int value found by calling sys.maxsize
if distance==inf:
    print("distance: infinity")
    print("route:")
    print("none")
else:
    print("distance:",distance,"km")
    print("route:")
    printpath(parents,destination)


