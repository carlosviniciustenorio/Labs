using System;

class Node {
    public int data;
    public Node left, right;

    public Node(int value) {
        data = value;
        left = right = null;
    }
}

class BinarySearchTree {
    private Node root;

    // Construtor
    public BinarySearchTree() {
        root = null;
    }

    // Inserção (O(logn) no caso médio, mas O(n) no pior caso)
    public void Insert(int key) {
        root = InsertRec(root, key);
    }

    private Node InsertRec(Node root, int key) {
        if (root == null) {
            root = new Node(key);
            return root;
        }

        if (key < root.data)
            root.left = InsertRec(root.left, key);
        else if (key > root.data)
            root.right = InsertRec(root.right, key);

        return root;
    }

    // Busca (O(logn) no caso médio, mas O(n) no pior caso)
    public bool Search(int key) {
        return SearchRec(root, key);
    }

    private bool SearchRec(Node root, int key) {
        if (root == null)
            return false;

        if (root.data == key)
            return true;

        if (key < root.data)
            return SearchRec(root.left, key);
        else
            return SearchRec(root.right, key);
    }

    // Exclusão (O(logn) no caso médio, mas O(n) no pior caso)
    public void Delete(int key) {
        root = DeleteRec(root, key);
    }

    private Node DeleteRec(Node root, int key) {
        if (root == null)
            return root;

        if (key < root.data)
            root.left = DeleteRec(root.left, key);
        else if (key > root.data)
            root.right = DeleteRec(root.right, key);
        else {
            // Nó com um ou sem filho
            if (root.left == null)
                return root.right;
            else if (root.right == null)
                return root.left;

            // Nó com dois filhos: Encontra o sucessor do nó
            root.data = MinValue(root.right);

            // Exclui o sucessor
            root.right = DeleteRec(root.right, root.data);
        }

        return root;
    }

    private int MinValue(Node node) {
        int minv = node.data;
        while (node.left != null) {
            minv = node.left.data;
            node = node.left;
        }
        return minv;
    }
}

class Program {
    static void Main(string[] args) {
        BinarySearchTree tree = new BinarySearchTree();

        // Inserção (O(logn) no caso médio, mas O(n) no pior caso)
        tree.Insert(50);
        tree.Insert(30);
        tree.Insert(20);
        tree.Insert(40);
        tree.Insert(70);
        tree.Insert(60);
        tree.Insert(80);

        // Busca (O(logn) no caso médio, mas O(n) no pior caso)
        Console.WriteLine("Busca por 20: " + tree.Search(20));
        Console.WriteLine("Busca por 90: " + tree.Search(90));

        // Exclusão (O(logn) no caso médio, mas O(n) no pior caso)
        tree.Delete(20);
        Console.WriteLine("Busca por 20 após exclusão: " + tree.Search(20));
    }
}

Nesta implementação:

// Inserção: A inserção em uma árvore de busca binária é O(logn) no caso médio, mas pode ser O(n) no pior caso quando a árvore se torna desbalanceada.
// Busca: Assim como a inserção, a busca é O(logn) no caso médio e O(n) no pior caso.
// Exclusão: A exclusão é semelhante à inserção e à busca em termos de complexidade de tempo.
// Esta implementação é uma versão básica e não aborda otimizações avançadas para manter a árvore balanceada em todos os momentos.