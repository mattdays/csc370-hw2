
import java.util.Random;
import java.util.Arrays;

public class Tree {
    String value;
    int leafNum = -1;
    Tree leftChild;
    Tree rightChild;

    public Tree(String value) {
        if (this.isNum(value)) {
            this.leafNum = Integer.parseInt(value);
        }
        this.value = value;
        this.leftChild = null;
        this.rightChild = null;
    }

    public Tree(int value, Tree leftChild, Tree rightChild) {
        this.value = value;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }

    private boolean isNum(String strNum) {
        return strNum.matches("-?\\d+(\\.\\d+)?");
    }

    public String getValue() {
        return this.value;
    }

    public Tree getLeftTree() {
        return this.leftChild;
    }

    public Tree getRightTree() {
        return this.rightChild;
    }

    public void setValue(String newValue) {
        this.value = newValue;
    }

    public void setLeftTree(Tree newLeft) {
        this.leftChild = newLeft;
    }

    public void setRightTree(Tree newRight) {
        this.rightChild = newRight;
    }

    public static void main(String[] args) {
        System.out.println("Compiles");
    }
}

class TreeMaker {

    private static String[] OPERATIONS = { "+", "-", "*", "/" };
    private static int MAX_NUMBER = 100;
    private static Random rand = new Random();

    Tree partialGrow(int depth) {
        
        if (depth == 1 && rand.nextBoolean()) {
            String op = OPERATIONS[rand.nextInt(OPERATIONS.length)];
            return new Tree(op, partialGrow(depth - 1), partialGrow(depth - 1));
        }

        else {
            return new Tree(rand.nextInt(MAX_NUMBER) + 1);
        }
    }

    Tree fullGrow(int depth) {
        if (depth == 1) {
            String op = OPERATIONS[rand.nextInt(OPERATIONS.length)];
            return new Tree(op, fullGrow(depth - 1), fullGrow(depth - 1));
        }

        else {
            return new Tree(rand.nextInt(MAX_NUMBER) + 1);
        }
    }
}