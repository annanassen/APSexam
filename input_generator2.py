import random
import string

#Denne input generator skulle meget gerne generere et stort input hvor alle bliver inficerede.

N = 10**5

def generate_strings(count, length):
    results = set() # sørger for at det er unikt
    letters = string.ascii_letters  # Indeholder a-z og A-Z
    
    while len(results) < count:
        # Genererer en tilfældig streng af den valgte længde
        new_str = ''.join(random.choices(letters, k=length))
        results.add(new_str)
        
    return list(results)


people = generate_strings(N, 10)
random.shuffle(people) #blander alle navnene og dette bliver vores infektionskæde
infection_chain = people 

patient0 = infection_chain[0]

infection_day = {} #holder styr på infectiontimes
infection_day[patient0] = 0 



edges = [] 

for i in range(N - 1):
    person1 = infection_chain[i]
    person2 = infection_chain[i+1]

    #Her sikrer vi at de mødes på en dag hvor person1 kan smitte person2
    day = random.randint(
        infection_day[person1] + 1,
        infection_day[person1] + 4
    )
    
    infection_day[person2] = day
    edges.append((person1, person2, day))


#bygger grafen
graph = {}

for person in infection_chain:
    graph[person] = []

for a,b,d in edges:
    graph[a].append((b,d))
    graph[b].append((a,d))

print(patient0, infection_day[patient0] + 2)
print(N)

for person in infection_chain:
    line = [person]

    count = 0
    for neighbor,day in graph[person]:
        if count == 3:
            break

        line.append(neighbor)
        line.append(str(day))
        count += 1
        

    print(*line)