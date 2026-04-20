from collections import deque


pationt0 , infectedAt =  input().split()
n = int(input())
infectionPeriod = 2

G = {}


for _ in range(n):
    line = input().split()
    node1 = line[0]
    if not G.get(node1):
             G[node1] = list()
    for interation in range(1,len(line), 2):
        node2 = line[interation]
        if not G.get(node2):
             G[node2] = list()
        time = int(line[interation+1])
        G[node1].append((node2, time))
        G[node2].append((node1, time))


infected = set()
infectionTime = {}


infected.add(pationt0)
infectionTime[pationt0] = int(infectedAt) 

q = deque()
q.append(pationt0)

while q:
      node = q.popleft()

      for neighbor, interactionTime in G[node]:
      
            if (neighbor in infected):
                  continue
            if infectionTime[node] <= interactionTime and infectionTime[node] > interactionTime - infectionPeriod:
                infected.add(neighbor)
                infectionTime[neighbor] = interactionTime
                q.append(neighbor)

for no in sorted(infected):
      print(no)
      
