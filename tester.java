import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.text.ParseException;
import java.io.IOException;

public class tester {
    private HashMap<String, String> map = new HashMap<>();

    public static void fitness(float ourValue) {
        // int sum_sq = 0;
        // double mse;

        // for (i = 0; i < h; ++i) {
        // for (j = 0; j < w; ++j) {
        // int p1 = image1[i][j];
        // int p2 = image2[i][j];
        // int err = p2 - p1;
        // sum_sq += (err * err);
        // }
        // }
        // mse = (double) sum_sq / (h * w);
        // for (String name : this.map.keySet()) {
        //     System.out.println(name + " " + this.map.get(name));
        // }
        System.out.println(this.map[0]);
    }

    private void parseCSV(String fileName) throws ParseException, IOException {
        try {
            BufferedReader dataset = new BufferedReader(new FileReader(fileName));
            String line = null;
            // HashMap<String, String> map = new HashMap<String, String>();

            while ((line = dataset.readLine()) != null) {
                String str[] = line.split(",");
                this.map.put(str[0], str[1]);
            }
            // for (String name : map.keySet()) {
            // System.out.println(name + " " + this.map.get(name));
            // }
            dataset.close();
        } catch (FileNotFoundException exception) {
            System.out.println("File not found");
        }

    }

    public static void main(String[] args) {
        // Tester test = new Tester.
    }
}