import sys

patient0 , showedSymptoms =  sys.stdin.readline().split()
showedSymptoms = int(showedSymptoms)
infectedAt = showedSymptoms - 2
infectionPeriod = 4


people = sys.stdin.readline()
people = int(people)

interactions = []

for _ in range(people):
    line = sys.stdin.readline().split()

    node1 = line[0]

    for i in range (1,len(line), 2):
        node2 = line[i]
        day = line[i+1]
        day = int(day)

        interactions.append((node1,node2,day))

infected = [(patient0, infectedAt)]

updated = True

while updated:
    updated = False
    for a,b,t in interactions:
            aInfected = False
            aTime = None

            for name, time in infected:
                if name == a:
                    aInfected = True
                    aTime = time
                
            bInfected = False
            bTime = None

            for name, time in infected:
                if name == b:
                    bInfected = True
                    bTime = time
                       

            if aInfected and not bInfected:
                start = aTime + 1
                end = aTime + 4

                if t >= start and t <= end:
                    infected.append((b,t))
                    updated = True

            if bInfected and not aInfected:
                start = bTime + 1
                end = bTime + 4

                if t >= start and t <= end:
                    infected.append((a,t))
                    updated = True

result = []

for zombie,_ in infected:
    if zombie not in result:
        result.append(zombie)

for zombie in sorted(result):
    print(zombie)


