import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class knapsack {

    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {


            int capacity = sc.nextInt();
            int objectAmount = sc.nextInt();

            int[] values = new int[objectAmount];
            int[] weights = new int[objectAmount];
            for (int i = 0; i < objectAmount; i++) {
                int value = sc.nextInt();
                int weight = sc.nextInt();
                values[i] = value;
                weights[i] = weight;
            }

            int[][] table = new int[objectAmount+1][capacity+1];
            for (int i = 1; i < objectAmount+1; i++) {
                for (int c = 1; c < capacity+1; c++) {


                    if (weights[i-1] <= c) { // the item fits in the bag

                        int includeItem = values[i-1] + table[i-1][c-weights[i-1]];
                        int excludeItem = table[i-1][c];

                        if (includeItem > excludeItem) {
                            table[i][c] = includeItem;
                        }
                        else {
                            table[i][c] = excludeItem;
                        }

                    }
                    else {
                        table[i][c] = table[i-1][c];
                    }
                }

            }


            ArrayList<Integer> res = new ArrayList<>();
            int i = objectAmount;
            int c = capacity;


            while (i > 0 && c > 0) {
                if (table[i][c] == table[i-1][c]){

                    i-= 1;
                }
                else {
                    res.add(i-1);

                    c -= weights[i-1];
                    i -= 1;
                }
            }


            // output

            // amount of elements in knapsack
            System.out.println(res.size());


            // index of the elements
            for (int k = 0; k < res.size(); k++) {
                System.out.print(res.get(k));

                if (k < res.size() - 1) {
                    System.out.print(" ");
                }
            }
            System.out.println();


    }
    }


}
