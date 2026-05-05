pationt0, infectedAt = input().split()
n = int(input())
infectionPeriod = 2

G = {}
infectionTime = {}

infectionTime[pationt0] = int(infectedAt)

def dfs(current):
    for neighbor, interactionTime in G[current]:
        if neighbor not in infectionTime:
            min = infectionTime[current] +1
            max = infectionTime[current] +3

            if min <= interactionTime <= max:
                infectionTime[neighbor] = interactionTime
                dfs(neighbor)

for _ in range(n):
    line = input().split()
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

print(infectionTime)