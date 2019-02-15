import java.util.Arrays;
import java.util.Stack;
import java.util.Random;
// import Tree.java;
// import tester.java;


public class gp {
    // private TreeMaker tester;
    // private Tree test;
    private int count=0;
    private static Random rand = new Random();
    // public gp() {
        
    // }

    // public void countNodes(Tree r, )

    public Tree selectSubtree (NODE_TYPE type, Tree root) {
        // int count = this.count;
        countNodes(type, root, this.count);
        System.out.println("Count Nodes: "+ this.count);
        // return root;
        if (this.count == 0) {
            // System.out.println("HERE");
            return null;
        }
        else {
            // System.out.println("hi");
            int randomInt =  1 + rand.nextInt(this.count);
            System.out.println("RANDNUM: " + randomInt);
            // this.count = 0;
            return pickNode(type, root, randomInt);
        }
    }

    private Boolean isNodeType (NODE_TYPE type, Tree current) {
        if (current == null) {
            return false;
        }
        else if (current.nodeType.equals(type)){
            return true;
        }
        else {
            return false;
        }
        // NODE_TYPE currentType = current.nodeType;
        // if (currentType.equals(type)) {
        //     return true;
        // }
        // else {
        //     return false;
        // }
    }

    private void countNodes (NODE_TYPE type, Tree root, int count) {
        // int temp = count; 
        if (root == null){
            return;
        }
        countNodes(type, root.leftChild, this.count);
        if (isNodeType(type, root)) {
            this.count ++;
        }
        countNodes(type, root.rightChild, this.count);
        // return;
    }

    private int tally(int count) {
        return count++;
    }

    private Tree pickNode (NODE_TYPE type, Tree root, int randNum) {
        Stack<Tree> s = new Stack<>();
        s.push(root);
        int count = 0;
        if (isNodeType(type, root)){
            count++;
            if (count == randNum) {
                System.out.println("HERE" + randNum);
                // if (randNum == 0){
                //     return root;
                // }                
                return root;            }
        }
        Tree temp = null;
        while (!s.isEmpty()){
            Tree v = s.pop();
            
            // if (isNodeType(type, v)) {
            //     if (count == randNum) {
            //         // if (randNum == 0){
            //         //     return root;
            //         // }                
            //         temp = v;
            //         break;
            //     }
            //     count++;
            // }
            // count++;
            
            if (v.leftChild != null) {
                s.push(v.leftChild);
                if (isNodeType(type, v.leftChild)){
                    
                    if (count == randNum) {
                        if (count % 2 == 0 && s.size() >=2){
                            temp = s.pop();
                        }                
                        temp = s.pop();
                        break;
                    }
                    count++;
                }
                s.push(v.rightChild);
                if (isNodeType(type, v.rightChild)){
                    
                    if (count == randNum) {
                        if (count % 2 == 1 && s.size() >= 2){
                            temp = s.pop();
                        }                    
                        temp = s.pop();
                        break;
                    }
                    count++;
                }
            }
        }
        return temp;
        
        //   // int temp = count; 
        // if (root == null){
        //     return root;
        // }
        // countNodes(type, root.leftChild, this.count);
        // if (isNodeType(type, root)) {
        //     this.count ++;
        // }
        // countNodes(type, root.rightChild, this.count);
        // return;
        // if (root == null) {
        //     // System.out.println("BASE");
        //     return null;
        // }
        // // else {
        //     if (isNodeType(type, root)) {
        //         this.count++;
        //         if (this.count >= randNum) {
        //             System.out.println("ROOT");
        //             return root;
        //         }
        //     }

        //     Tree[] children = new Tree[2];

        //     for (int i =0; i < children.length; i++) {
        //         Tree v = pickNode(type, children[i], randNum, count);

        //         if (v != null) {
        //             System.out.println("V");
        //             return v;
        //         }
        //     }
        //     // Tree v1 = pickNode(type, root.leftChild, randNum, count);
        //     // Tree v2 = pickNode(type, root.rightChild, randNum, count);
            
        //     // if (v1 == null) {
        //     //     if (v2 == null) {
        //     //         System.out.println("DOUBLE IF");
        //     //         return null;
        //     //     }
        //     //     return v2;
        //     // }
        //     // return v1;
        //     // System.out.println("End");
        //     return null;
        }
    // }

    public static void main(String[] args) {
        TreeMaker tester = new TreeMaker();
        Tree testTree = tester.fullGrow(2);

        tester.dfsPrint(testTree);


        NODE_TYPE op = NODE_TYPE.OPERATION;
        Tree sub = new gp().selectSubtree(op, testTree);
        
        System.out.println("_______________________________________________________");
        tester.dfsPrint(sub);
        // System.out.println("" + sub.constant);
    }
}