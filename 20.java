import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Stack;

public class task_1 {
    public static void main(String[] args) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader("input.txt"))) {
            int k = Integer.parseInt(reader.readLine());
            int[] data = new int[k];
            int n = 0;
            for (String el : reader.readLine().split(" ")) {
                data[n++] = Integer.parseInt(el);
                int i = n - 1;
                while (i > 0 && data[i] < data[(i - 1) / 2]){
                    int cur = data[i];
                    data[i] = data[(i - 1) / 2];
                    data[(i - 1) / 2] = cur;
                    i = (i - 1) / 2;
                }
            }

            for (int y = 0; y < data.length; y ++) {
                n -= 1;
                int cur  = data[0];
                data[0] = data[n];
                data[n] = cur;
                int i = 0;
                while (2 * i + 1 < n) {
                    int j = 2 * i + 1;
                    if (2 * i + 2 < n && data[2 * i + 2] < data[j])
                        j = 2 * i + 2;
                    if (data[i] <= data[j])
                        break;
                    else {
                        int curr = data[i];
                        data[i] = data[j];
                        data[j] = curr;
                        i = j;
                    }
                }
                System.out.print(data[n] + " ");
            }
        }
    }
}
