import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class task_1 {
    public static void main(String[] args) throws IOException {
        try(BufferedReader reader = new BufferedReader(new FileReader("input.txt"))){
            String line;
            int[] data = new int['z'+1];
            int max_count = 0;
            StringBuilder sb = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                char[] chars = line.toCharArray();
                for (char symb : chars) {
                    if (symb != ' ') {
                        data[symb] = data[symb] + 1;
                        if (data[symb] > max_count){
                            max_count = data[symb];
                        }
                    }
                }
            }
            for (int i = 0; i < max_count; i++) {
                for (int cnt_symb : data) {
                    if (cnt_symb != 0) {
                        if (cnt_symb > max_count - i - 1) {
                            sb.append('#');
                        } else {
                            sb.append(' ');
                        }
                    }
                }
                sb.append('\n');
            }

            for (int i = 0; i < data.length; ++i) {
                if (data[i] != 0){
                    sb.append((char)i);
                }
            }

            try (FileWriter writer = new FileWriter("output.txt")) {
                writer.write(sb.toString());
                writer.flush();
            }

        }
    }
}