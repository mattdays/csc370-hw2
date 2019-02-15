
import java.util.Random;
import java.util.Stack;
import java.util.Arrays;

enum NODE_TYPE {
    OPERATION, OPERAND, VARIABLE
}

public class Tree {
    NODE_TYPE nodeType;
    String operation;
    float constant;
    String variable;
    Tree leftChild;
    Tree rightChild;

    public Tree(int value) {
        this.nodeType = NODE_TYPE.OPERAND;
        this.operation = null;
        this.constant = (float) value;
        this.variable = null;
        this.leftChild = null;
        this.rightChild = null;
    }

    public Tree(String var) {
        this.nodeType = NODE_TYPE.VARIABLE;
        this.operation = null;
        this.constant = (float) 0;
        this.variable = var;
        this.leftChild = null;
        this.rightChild = null;
    }

    public Tree(String strVal, Tree leftChild, Tree rightChild) {
        // Error handling, not sure if we actually need this
        if (strVal.equals("x")) {
            this.nodeType = NODE_TYPE.VARIABLE;
            this.variable = strVal;
        } else {
            this.nodeType = NODE_TYPE.OPERATION;
            this.operation = strVal;
        }
        this.constant = (float) 0;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }

    public NODE_TYPE getType() {
        return this.nodeType;
    }

    public Tree getLeftTree() {
        return this.leftChild;
    }

    public Tree getRightTree() {
        return this.rightChild;
    }

    public void setType(NODE_TYPE type) {
        this.nodeType = type;
    }

    public void setLeftTree(Tree newLeft) {
        this.leftChild = newLeft;
    }

    public void setRightTree(Tree newRight) {
        this.rightChild = newRight;
    }

    public static void main(String[] args) {
        TreeMaker tester = new TreeMaker();
        Tree test = tester.fullGrow(2);
        tester.dfsPrint(test);

        float output = tester.evaluate(test, (float) 2);
        System.out.println("Answer:" + Float.toString(output));
    }
}

class TreeMaker {

    private static String[] OPERATIONS = { "+", "-", "*", "/" };
    private static int MAX_NUMBER = 100;
    private static Random rand = new Random();

    Tree partialGrow(int depth) {
        if (depth > 0 && rand.nextBoolean()) {
            String op = OPERATIONS[rand.nextInt(OPERATIONS.length)];
            return new Tree(op, partialGrow(depth - 1), partialGrow(depth - 1));
        } else {
            if (rand.nextBoolean()) {
                return new Tree(rand.nextInt(MAX_NUMBER) + 1);
            } else {
                return new Tree("x");
            }
        }
    }

    Tree fullGrow(int depth) {
        if (depth > 0) {
            String op = OPERATIONS[rand.nextInt(OPERATIONS.length)];
            return new Tree(op, fullGrow(depth - 1), fullGrow(depth - 1));
        } else {
            if (rand.nextBoolean()) {
                return new Tree(rand.nextInt(MAX_NUMBER) + 1);
            } else {
                return new Tree("x");
            }
        }
    }

    public void dfsPrint(Tree subject) {
        if (subject == null) {
            return;
        } else {
            dfsPrint(subject.leftChild);
            switch (subject.nodeType) {
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

    public float evaluate(Tree root, float num) {
        float result, operand1, operand2;

        if (root == null)
            result = 0;
        else {
            NODE_TYPE temp = root.nodeType;
            if (temp == NODE_TYPE.OPERATION) {
                operand1 = evaluate(root.leftChild, num);
                operand2 = evaluate(root.rightChild, num);
                result = compute(root.operation, operand1, operand2);
            } else if (temp == NODE_TYPE.VARIABLE) {
                result = num;
            } else
                result = root.constant;
        }

        return result;
    }

    private static float compute(String operator, float operand1, float operand2) {
        float result = 0;
        if (operator.equals("+")) {
            result = operand1 + operand2;
        } else if (operator.equals("-")) {
            result = operand1 - operand2;
        } else if (operator.equals("*")) {
            result = operand1 * operand2;
        } else {
            result = (operand2 == 0) ? (result = (float) 0) : (result = operand1 / operand2);
        }
        return result;
    }
}