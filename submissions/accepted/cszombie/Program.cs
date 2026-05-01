// See https://aka.ms/new-console-template for more information

using System.Dynamic;

String firstLine = Console.ReadLine();

String[] line = firstLine.Split(" ");
String patient0 = line[0];
int dayOfSymptoms = Int32.Parse(line[1]);
int infectionPeriod = 4;

int N = Int32.Parse(Console.ReadLine());

Dictionary<String, List<(String, int)>> graph = new Dictionary<string, List<(String, int)>>();

for (int i = 0; i < N; i++)
{
    String[] personLine = Console.ReadLine().Split(" ");
    String person = personLine[0];

    if (!graph.ContainsKey(person))
    {
        graph.Add(person, new List<(string, int)>());
    }

    for (int j = 1; j < personLine.Length; j += 2)
    {
        String otherPerson = personLine[j];
        int interactionDay = Int32.Parse(personLine[j+1]);

        graph[person].Add((otherPerson,interactionDay));
    }
}
SortedSet<String> infected = new SortedSet<string>();
Dictionary<String, int> infectionDay = new Dictionary<string, int>();
Queue<String> q = new Queue<string>();

infected.Add(patient0);
infectionDay[patient0] = dayOfSymptoms - 2;

q.Enqueue(patient0);

while(q.Count > 0)
{
    String curPerson = q.Dequeue();

   foreach((string, int) tuple in graph[curPerson])
    {
        string neighbor = tuple.Item1;
        int day = tuple.Item2;

        if (infected.Contains(neighbor)){
            continue;
        }
        if (day > infectionDay[curPerson] && day <= (infectionDay[curPerson] + infectionPeriod)){
                    infected.Add(neighbor);
                    infectionDay[neighbor] = day;
                    q.Enqueue(neighbor);
                }
    }    
}

foreach (string zombie in infected)
{
    Console.WriteLine(zombie);
}





