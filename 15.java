import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Stack;

public class task_1 {
    public static void main(String[] args) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader("input.txt"))) {
            int n = Integer.parseInt(reader.readLine());
            int[] cost = new int[n];
            int i = 0;
            Stack<Integer> stack = new Stack<>();
            for (String el : reader.readLine().split(" ")) {
                cost[i++] = Integer.parseInt(el);
            }
            stack.push(0);

            for(i = 1; i < n; ++i){
                while (!stack.isEmpty() && cost[stack.peek()] > cost[i]){
                    cost[stack.peek()] = i;
                    stack.pop();
                }
                stack.push(i);
            }

            while (!stack.isEmpty()){
                cost[stack.pop()] = -1;
            }
            StringBuilder res = new StringBuilder();
            for (int el : cost){
                res.append(el).append(" ");
            }
            try (FileWriter writer = new FileWriter("output.txt")) {
                writer.write(res.toString().trim());
                writer.flush();
            }
        }


    }
}
