
import java.util.Scanner;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.Deque;
import java.util.ArrayDeque;

public class Main {

    static class Edge{
        String node;
        int day;

        Edge(String node, int day){
            this.node = node;
            this.day = day;
        }

        String getNode(){
            return this.node;
        }

        int getDay(){
            return this.day;
        }

    }
    public static void main (String[] args) {

        Scanner scanner = new Scanner(System.in);

        String patient0 = scanner.next();
        int ShowsSymptomsAt = scanner.nextInt();
        int size = scanner.nextInt();

        int infectionTime = 4;

        scanner.nextLine();

        HashMap<String, List<Edge>> hm = new HashMap<>();

        for (int i = 0; i < size; i++) {
            String input = scanner.nextLine().trim();
            String[] line = input.split("\\s+");

            String node1 = line[0];

            if (!hm.containsKey(node1)){
                hm.put(node1, new ArrayList<>());
            }

            if (line.length == 1){
                continue;
            }

            for (int j = 1; j + 1 < line.length; j = j + 2){
                String node2 = line[j];
                int day = Integer.parseInt(line[j+1]);
                Edge edge1 = new Edge(node2, day);
                Edge edge2 = new Edge(node1, day);

                if(!hm.containsKey(node2)){
                    hm.put(node2, new ArrayList<>());
                }

                hm.get(node1).add(edge1);
                hm.get(node2).add(edge2);
            }
            
        }
        Set<String> infected = new HashSet<>();
        HashMap<String, Integer> infectedDay = new HashMap<>();

        infected.add(patient0);
        infectedDay.put(patient0, ShowsSymptomsAt - 2);

        Deque<String> dq = new ArrayDeque<String>();

        dq.addLast(patient0);

        while(!dq.isEmpty()){
            String node = dq.pollFirst();

            if (!hm.containsKey(node)){
                continue;
            }

            for (Edge edge : hm.get(node)){
                String neighbor = edge.getNode();
                int day = edge.getDay();

                if (infected.contains(neighbor)){
                    continue;
                }
                if (day > infectedDay.get(node) && day <= (infectedDay.get(node) + infectionTime)){
                    infected.add(neighbor);
                    infectedDay.put(neighbor, day);
                    dq.addLast(neighbor);
                }

            }

        }
        List<String> result = new ArrayList<>(infected);
        Collections.sort(result);

        for( String person : result){
                System.out.println(person);
            }
    }
}