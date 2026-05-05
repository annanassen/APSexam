
import random
import string


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




patient0 = random.choice(people)
infectionTime = random.randint(0,14)

print(patient0, infectionTime)

print(N)

for person in people:
    toPrint = [person]

    # later in the procces we can make interactions more random 
    for _ in range(3): # interactions

        toPrint.append(random.choice(people))
        toPrint.append(str(random.randint(0,14)))
    print(*toPrint)