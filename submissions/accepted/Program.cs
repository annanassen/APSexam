using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string firstLine = Console.ReadLine();

        string[] line = firstLine.Split(" ");
        string patient0 = line[0];
        int dayOfSymptoms = Int32.Parse(line[1]);
        int infectionPeriod = 4;

        int N = Int32.Parse(Console.ReadLine());

        Dictionary<string, List<KeyValuePair<string,int>>> graph = new Dictionary<string, List<KeyValuePair<string,int>>>();

        for (int i = 0; i < N; i++)
        {
            string[] personLine = Console.ReadLine().Split(" ");
            string person = personLine[0];

            if (!graph.ContainsKey(person))
            {
                graph.Add(person, new List<KeyValuePair<string, int>>());;
            }

            for (int j = 1; j + 1 < personLine.Length; j += 2)
            {
                string otherPerson = personLine[j];
                int interactionDay = Int32.Parse(personLine[j+1]);

                if (!graph.ContainsKey(otherPerson))
                {
                    graph.Add(otherPerson, new List<KeyValuePair<string, int>>());
                }

                graph[person].Add(new KeyValuePair<string, int>(otherPerson, interactionDay));
                graph[otherPerson].Add(new KeyValuePair<string, int>(person, interactionDay));
            }
        }
        HashSet<string> infected = new HashSet<string>();
        Dictionary<string, int> infectionDay = new Dictionary<string, int>();
        Queue<string> q = new Queue<string>();

        infected.Add(patient0);
        infectionDay[patient0] = dayOfSymptoms - 2;

        q.Enqueue(patient0);

        while(q.Count > 0)
        {
            string curPerson = q.Dequeue();

            if (!graph.ContainsKey(curPerson))
            {
                continue;
            }

            foreach (KeyValuePair<string, int> tuple in graph[curPerson])
                {
                    string neighbor = tuple.Key;
                    int day = tuple.Value;

                    if (infectionDay.ContainsKey(neighbor))
                    {
                        continue;
                    }

                    if (day > infectionDay[curPerson] && day <= infectionDay[curPerson] + infectionPeriod)
                        {
                            infected.Add(neighbor);
                            infectionDay[neighbor] = day;
                            q.Enqueue(neighbor);
                        }
                }    
        }

        List<string> result = new List<string>(infected);
        result.Sort(StringComparer.Ordinal);
        foreach (string zombie in result)
        {
            Console.WriteLine(zombie);
        }

    }
}

