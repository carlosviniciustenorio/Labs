class Node{
    constructor(value){
        this.left = null;
        this.right = null;
        this.value = value;
    }
}

class BinaryThree
{
    constructor()
    {
        this.root = null;
    }

    insert(value){
        this.root = this.insertRecursive(this.root, value);
    }

    // Time complexity - Average: O(log n) / Worst: O(n)
    insertRecursive(root, value){
        if(root === null)
            return new Node(value);

        if(value < root.value)
            root.left = this.insertRecursive(root.left, value);
        else if(value > root.value)
            root.right = this.insertRecursive(root.right, value);

        return root;
    }

    minValue(node)
    {
        const minv = node.value;
        while(node.left != null){
            minv = node.left.value;
            node = node.left;
        }

        return minv;
    }

    deleteRecursive(root, value)
    {   
        if(root === null)
            return;

        if(value < root.value)
            this.deleteRecursive(root.left, value);
        else if(value > root.value)
            this.deleteRecursive(root.right, value);
        else{
            if(root.left == null)
                return root.right;
            else if(root.right == null)
                return root.left;

            root.value = this.minValue(root.right);
            root.right = this.deleteRecursive(root.right, root.value);
        }
        return root;
    }

    nodeExist(root, value)
    {
        if(root === null)
            return false;

        if(value < root.value)
            return this.nodeExist(root.left, value);
        else if(value > root.value)
            return this.nodeExist(root.right, value);

        return true;
    }
}

const binaryThree = new BinaryThree();
binaryThree.insert(10);
binaryThree.insert(5);
binaryThree.insert(4);
binaryThree.insert(6);
binaryThree.insert(14);
binaryThree.insert(12);
binaryThree.insert(15);
binaryThree.insert(13);
binaryThree.insert(9);
binaryThree.insert(8);

var nodeExist = binaryThree.nodeExist(binaryThree.root, 4);
console.log("Node with value {4} exist: " + nodeExist);

binaryThree.deleteRecursive(binaryThree.root, 4);

var nodeExist = binaryThree.nodeExist(binaryThree.root, 4);
console.log("Node with value {4} exist: " + nodeExist);