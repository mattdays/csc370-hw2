import java.util.Arrays;
import java.util.Stack;
import java.util.Random;
// import Tree.java;
// import tester.java;

public class gp {
    // private int count = 0;
    private static Random rand = new Random();

    public static Tree[] crossover(NODE_TYPE type, Tree parent1, Tree parent2) {
        Tree sub1 = selectSubtree(type, parent1);
        Tree sub2 = selectSubtree(type, parent2);

        Tree temp = new Tree();
        temp.constant = sub1.constant;
        temp.operation = sub1.operation;
        temp.variable = sub1.variable;
        temp.leftChild = sub1.leftChild;
        temp.rightChild = sub1.rightChild;

        sub1.constant = sub2.constant;
        sub1.operation = sub2.operation;
        sub1.variable = sub2.variable;
        sub1.leftChild = sub2.leftChild;
        sub1.rightChild = sub2.rightChild;

        sub2.constant = temp.constant;
        sub2.operation = temp.operation;
        sub2.variable = temp.variable;
        sub2.leftChild = temp.leftChild;
        sub2.rightChild = temp.rightChild;

        Tree[] results = {parent1, parent2};
        return results;

    }

    public static Tree mutation(NODE_TYPE type, Tree parent1) {
        Tree sub1 = selectSubtree(type, parent1);
        Tree sub2 = selectSubtree(type, parent1);

        Tree temp = new Tree();
        temp.constant = sub1.constant;
        temp.operation = sub1.operation;
        temp.variable = sub1.variable;
        // temp.leftChild = sub1.leftChild;
        // temp.rightChild = sub1.rightChild;

        sub1.constant = sub2.constant;
        sub1.operation = sub2.operation;
        sub1.variable = sub2.variable;
        // sub1.leftChild = sub2.leftChild;
        // sub1.rightChild = sub2.rightChild;

        sub2.constant = temp.constant;
        sub2.operation = temp.operation;
        sub2.variable = temp.variable;
        // sub2.leftChild = temp.leftChild;
        // sub2.rightChild = temp.rightChild;

        // Tree[] results = {parent1, parent2};
        return parent1;

    }

    // private Tree combine (Tree parent) {

    // }

    private static Tree selectSubtree(NODE_TYPE type, Tree root) {
        int count = countNodes(type, root, 0);
        // System.out.println("Count Nodes: " + this.count);
        if (count == 0) {
            return null;
        } else {
            int randomInt = 1 + rand.nextInt(count);
            // System.out.println("RANDNUM: " + randomInt);
            return pickNode(type, root, randomInt);
        }
    }

    private static Boolean isNodeType(NODE_TYPE type, Tree current) {
        if (current == null) {
            return false;
        } else if (current.nodeType.equals(type)) {
            return true;
        } else {
            return false;
        }
    }

    private static int countNodes(NODE_TYPE type, Tree root, int count) {
        Stack<Tree> s = new Stack<>();
        s.push(root);
        int c = count;
        while (!s.isEmpty()) {
            Tree v = s.pop();
            c++;
            if (v.leftChild != null) {
                s.push(v.leftChild);
                s.push(v.rightChild);
            }
        }

        // if (root == null) {
        //     return;
        // }
        // countNodes(type, root.leftChild, this.count);
        // if (isNodeType(type, root)) {
        //     this.count++;
        // }
        // countNodes(type, root.rightChild, this.count);
        return c;
    }

    private static Tree pickNode(NODE_TYPE type, Tree root, int randNum) {
        Stack<Tree> s = new Stack<>();
        Tree left = null;
        Tree right = null;


        s.push(root);
        int count = 0;
        if (isNodeType(type, root)) {
            count++;
            if (count == randNum) {
                return root;
            }
        }
        Tree temp = null;
        // Boolean isLeft = false;
        while (!s.isEmpty()) {
            if (s.size() > 1) {
                right = s.pop();
                if (isNodeType(type, right)) {
                    if (count == randNum) {
                        // if (count % 2 == 0 && s.size() >= 2) {
                        //     temp = s.pop();
                        // }
                        temp = right;
                        break;
                    }
                    count++;
                }
                left = s.pop();
                if (isNodeType(type, left)) {
                    if (count == randNum) {
                        // if (count % 2 == 1 && s.size() >= 2) {
                        //     temp = s.pop();
                        // }
                        temp = left;
                        break;
                    }
                    count++;
                }
                if (left != null) {
                    s.push(left);
                    s.push(right);                
                }
            }
            else{
                Tree v = s.pop();
                if (v.leftChild != null) {
                    s.push(v.leftChild);
                    s.push(v.rightChild);                
                }
            }
        }
        return temp;
    }

    public static void main(String[] args) {
        TreeMaker tester = new TreeMaker();
        Tree testTree = tester.fullGrow(2);
        tester.dfsPrint(testTree);
        System.out.println("-----------------------------------------------------------");
        // Tree testTree2 = tester.fullGrow(2);
        // tester.dfsPrint(testTree2);

        NODE_TYPE op = NODE_TYPE.OPERATION;

        // Tree[] result = gp.crossover(op, testTree, testTree2);
        // System.out.println("-----------------------------------------------------------");

        // tester.dfsPrint(result[0]);
        // System.out.println("-----------------------------------------------------------");
        // tester.dfsPrint(result[1]);


        // NODE_TYPE op = NODE_TYPE.OPERATION;
        // Tree sub = new gp().selectSubtree(op, testTree);

        // // System.out.println("_______________________________________________________");
        // tester.dfsPrint(sub);
        // System.out.println("" + sub.constant);

        Tree testTree3 = gp.mutation(op, testTree);
        tester.dfsPrint(testTree3);
    }
}