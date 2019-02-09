// Class Declaration
import java.util.Random;
import java.util.Arrays;


public class gpTree {
    // Instance Variables
    int maxDepth;
    String[] operations = {"+","-","*","/"};

    private class Node {
        
        // Start stepping through the array from the beginning
        String value;
        Node leftChild;
        Node rightChild;
        Node parent;

        public Node(String value) {
            this.value = value;
            this.leftChild = Null;
            this.rightChild = Null;
            this.parent = Null;
        }
    }

    // Constructor Declaration of Class
    public gpTree(int maxDepth) 
    { 
        this.maxDepth = maxDepth;
        
        Random rand = new Random();
        int randNum = rand.nextInt(this.operations.length);

        Node root = new Node(Integer.toString(randNum));

        int howBig = rand.nextInt(1);

        if (howBig == 0) {
            this.partialGrow();
        }
        else {
            this.fullGrow();
        }

    }

    private String chooseNext() {
        Random rand3 = new Random();
        int next = rand3.nextInt(1);

        if (next == 0) {
            int whichOp = rand.nextInt(this.operations.length);
            return this.operations[whichOp];
        }
        else {
            int terminalNum = rand3.nextInt();
            return Integer.toString(terminalNum);
        }
    }

    public Node partialGrow(int depth) {
       if (depth == this.maxDepth) {
           Random rand2 = new Random();
           int leaf = rand2.nextInt();
           Node terminating0 = new Node(Integer.toString(leaf));
           return terminating0;
       }

       else {
            Random rand3 = new Random();
            int next = rand3.nextInt(1);

            if (next == 0) {
                int whichOp = rand.nextInt(this.operations.length);
                return Node(this.operations[whichOp]);
            }
            else {
                int terminalNum = rand3.nextInt();
                return Node(Integer.toString(terminalNum));
            }
        //    String newVal = this.chooseNext();
        //    int newInt = Integer.parseInt(newVal);
        //    if (int newInt = Integer.parseInt(newVal)) {
        //        Node terminating1 = new Node()
        //    }
       }

    }

    public void fullGrow(int depth) {
       
    }

    public static void main(String[] args) {
        Dog tuffy = new Dog("tuffy", "papillon", 5, "white");
        System.out.println(tuffy.toString());
    }
}