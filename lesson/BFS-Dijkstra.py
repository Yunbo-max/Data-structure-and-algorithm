from pythonds.graphs import PriorityQueue,Graph, Vertex
from pythonds.basic import Queue


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

def dijkstra(aGragh,start):
    pq=PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v)for v in aGragh])
    while not pq.isEmpty():
        currentVert=pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist=currentVert.getConnections()\
                    +currentVert.getWeight(nextVert)
            if newDist<nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


wordgraph = buildGraph("fourletterwords.txt")

dijkstra(wordgraph, wordgraph.getVertex('FOOL'))

traverse(wordgraph.getVertex('AAHS'))

# traverse(wordgraph.getVertex('COOL'))