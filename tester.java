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
    public static void main(String[] args) throws ParseException, IOException{
        
        BufferedReader dataset = new BufferedReader(new FileReader("dataset1.csv"));
        String line =  null;
        HashMap<String,String> map = new HashMap<String, String>();

        while((line = dataset.readLine()) != null) {
            String str[] = line.split(",");
            map.put(str[0],str[1]);
        }
        for (String name:map.keySet()) {
            System.out.println(name + " " + map.get(name));
        }
    }
}