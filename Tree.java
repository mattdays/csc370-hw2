
import java.util.Random;
import java.util.Arrays;

enum NODE_TYPE {OPERATION, OPERAND, VARIABLE}
// enum OPERATIONS {ADD, SUB, MUL, DIV}

public class Tree {
    NODE_TYPE nodeType;
    String operation;
    int constant;
    String variable;
    Tree leftChild;
    Tree rightChild;

    public Tree(int value) {
        this.nodeType = NODE_TYPE.OPERAND;
        this.constant = value;
        this.variable = null;
        this.leftChild = null;
        this.rightChild = null;
    }

    public Tree(String var) {
        this.nodeType = NODE_TYPE.VARIABLE;
        this.constant = 0;
        this.variable = var;
        this.leftChild = null;
        this.rightChild = null;
    }

    public Tree(String strVal, Tree leftChild, Tree rightChild) {
        //Error handling, not sure if we actually need this
        if (strVal.equals("x")) {
            this.nodeType = NODE_TYPE.VARIABLE;
            this.variable = strVal;
        }
        else {
            this.nodeType = NODE_TYPE.OPERATION;
            this.operation = strVal;
        }
        // this.nodeType = strVal.equals("x") ? (this.nodeType = NODE_TYPE.VARIABLE) : (this.nodeType = NODE_TYPE.OPERATION, this.operation = strVal);
        this.constant = 0;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }

    // private boolean isNum(String strNum) {
    //     return strNum.matches("-?\\d+(\\.\\d+)?");
    // }

    public NODE_TYPE getType() {
        return this.nodeType;
    }

    // public int getValue() {
    //     return this.value;
    // }

    public Tree getLeftTree() {
        return this.leftChild;
    }

    public Tree getRightTree() {
        return this.rightChild;
    }

    // private void setOperation(OPERATIONS op) {
    //     switch (op) {
    //         case ADD:
    //             this.operation = "+";
    //         case SUB:
    //             this.operation = "-";
    //         case MUL:
    //             this.operation = "*";
    //         case DIV:
    //             this.operation = "/";
    //         default:
    //             //
    //     }
    // }

    public void setType(NODE_TYPE type) {
        this.nodeType = type;

        // switch (type) {
        //     case OPERATION:
        //         this.operation = "TEST";
        //     case OPERAND:
        //         this.constant = 
                
        // }
    }

    // public void setValue(String newValue) {
    //     this.value = newValue;
    // }

    public void setLeftTree(Tree newLeft) {
        this.leftChild = newLeft;
    }

    public void setRightTree(Tree newRight) {
        this.rightChild = newRight;
    }

    public static void main(String[] args) {
        TreeMaker tester = new TreeMaker();
        Tree test = tester.partialGrow(2);
        tester.dfsPrint(test);
    }
}

class TreeMaker {

    private static String[] OPERATIONS = { "+", "-", "*", "/" };
    private static int MAX_NUMBER = 100;
    private static Random rand = new Random();

    Tree partialGrow(int depth) {
        if (depth == 0 && !rand.nextBoolean()) {
            return new Tree(rand.nextInt(MAX_NUMBER) + 1);
        }
        else if (depth == 0 && !rand.nextBoolean()) {
            return new Tree("x");
        }
        else {
            String op = OPERATIONS[rand.nextInt(OPERATIONS.length)];
            return new Tree(op, partialGrow(depth - 1), partialGrow(depth - 1));
        }


        // if (depth > 0 && rand.nextBoolean()) {
        //     String op = OPERATIONS[rand.nextInt(OPERATIONS.length)];
        //     return new Tree(op, partialGrow(depth - 1), partialGrow(depth - 1));
        // }

        // else {
        //     return new Tree(rand.nextInt(MAX_NUMBER) + 1);
        // }
    }

    Tree fullGrow(int depth) {
        if (depth == 0 && rand.nextBoolean()) {
            return new Tree(rand.nextInt(MAX_NUMBER) + 1);
        }
        else if (depth == 0 && !rand.nextBoolean()) {
            return new Tree("x");
        }
        else {
            String op = OPERATIONS[rand.nextInt(OPERATIONS.length)];
            return new Tree(op, fullGrow(depth - 1), fullGrow(depth - 1));
        }



        // if (depth > 0) {
        //     String op = OPERATIONS[rand.nextInt(OPERATIONS.length)];
        //     return new Tree(op, fullGrow(depth - 1), fullGrow(depth - 1));
        // }

        // else {
        //     return new Tree(rand.nextInt(MAX_NUMBER) + 1);
        // }
    }

    public void dfsPrint(Tree subject) {
        // Tree current = subject;
        if (subject == null) {
            return;
        }
        else {
            dfsPrint(subject.leftChild);
            switch(subject.nodeType) {
                case OPERAND:
                    System.out.println(subject.constant);
                    break;
                case OPERATION:
                    System.out.println(subject.operation);
                    break;
                case VARIABLE:
                    System.out.println("variable");
                    break;
                default:
                    System.out.println(subject.nodeType + "");
                    break;
            }
            dfsPrint(subject.rightChild);
        }
    }
}