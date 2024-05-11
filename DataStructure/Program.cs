using System.Linq;

class Node
{
    public int Data;
    public Node Left, Right;    
    
    public Node(int value) => (Data, Left, Right) = (value, null,null);
}        

class BinaryTree
{
    public Node Root;
    
    public BinaryTree() => Root = null;

    public Node Insert(List<int> value)
    {
        foreach (var item in value)
        {
            Root = InsertRec(Root, item);
        }
        return Root; 
    } 
    
    public Node InsertRec(Node root, int value)
    {
        if(root == null)
        {
            root = new Node(value);
            return root;
        }
        
        if(value < root.Data)
            root.Left = InsertRec(root.Left, value);
        else if(value > root.Data)
            root.Right = InsertRec(root.Right,value);

        return root;
    }

    public string Read()
    {
        List<int> result = new();
        ReadInrOrderTransversal(Root, result);
        return string.Join(", ", result);
    }

    public void ReadInrOrderTransversal(Node root, List<int> result)
    {
        if(root != null)
        {
            ReadInrOrderTransversal(root.Left, result);
            result.Add(root.Data);
            ReadInrOrderTransversal(root.Right, result);
        }
    }

    
}

class Program 
{
    static void Main(String[] args) {
        BinaryTree binaryTree = new();
        var response = binaryTree.Insert(new List<int>(){5,3,6,2,4,7,1,10});
        Console.WriteLine("Inorder traversal: " + binaryTree.Read());
    }
}
