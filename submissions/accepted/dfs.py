import sys

pationt0, infectedAt = sys.stdin.readline().split()
n = int(sys.stdin.readline())
infectionPeriod = 2

G = {}
infectionTime = {}
infected = set()
infected.add(pationt0)
infectionTime[pationt0] = int(infectedAt) -2

def dfs(current):
    global G, infected 
  
    for neighbor, interactionTime in G[current]:
        
        if neighbor not in infectionTime:
            min = infectionTime[current] +1
            max = infectionTime[current] +4

            if min <= interactionTime <= max:
               
                infected.add(neighbor)
                infectionTime[neighbor] = interactionTime
                dfs(neighbor)

for _ in range(n):
    line = sys.stdin.readline().split()
    node1 = line[0]

    if node1 not in G:
        G[node1] = []

    for i in range(1, len(line), 2):
        node2 = line[i]
        time = int(line[i+1])

        if node2 not in G:
            G[node2] = []

        G[node1].append((node2, time))
        G[node2].append((node1, time))

dfs(pationt0)

for no in sorted(infected):
      print(no)