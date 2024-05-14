// using System.Linq;

// class Node
// {
//     public int Data;
//     public Node Left, Right;    
    
//     public Node(int value) => (Data, Left, Right) = (value, null,null);
// }        

// class BinaryTree
// {
//     public Node Root;
    
//     public BinaryTree() => Root = null;

//     // Average O(m * log n) | Worst O(m * n)
//     public Node Insert(List<int> value)
//     {
//         foreach (var item in value)
//         {
//             Root = InsertRec(Root, item);
//         }
//         return Root; 
//     } 
    
//     // Average O(log n) | Average O(n)
//     public Node InsertRec(Node root, int value)
//     {
//         if(root == null)
//         {
//             root = new Node(value);
//             return root;
//         }
        
//         if(value < root.Data)
//             root.Left = InsertRec(root.Left, value);
//         else if(value > root.Data)
//             root.Right = InsertRec(root.Right,value);

//         return root;
//     }

//     // Average O(n)
//     public string Read()
//     {
//         List<int> result = new();
//         ReadInrOrderTransversal(Root, result);
//         return string.Join(", ", result);
//     }

//     // Average O(log n) | Worst O(n)
//     public void ReadInrOrderTransversal(Node root, List<int> result)
//     {
//         if(root != null)
//         {
//             ReadInrOrderTransversal(root.Left, result);
//             result.Add(root.Data);
//             ReadInrOrderTransversal(root.Right, result);
//         }
//     }

//     // Average O(log n) | Worst O(n)
//     public bool Search(Node root, int value)
//     {
//         if(root is null)
//             return false;

//         if(value < root.Data)
//             return Search(root.Left, value);
//         if(value > root.Data)
//             return Search(root.Right, value);

//         return true;
//     }

//     // Average O(log n) | O(n)
//     public Node Delete(Node root, int value)
//     {
//         if (root == null)
//             return null;

//         if (value < root.Data)
//             root.Left = Delete(root.Left, value);
//         else if (value > root.Data)
//             root.Right = Delete(root.Right, value);
//         else {
//             // Caso 1: nó sem filho ou com apenas um filho
//             if (root.Left == null)
//                 return root.Right;
//             else if (root.Right == null)
//                 return root.Left;
            
//             // Caso 2: nó com dois filhos
//             // Encontrar o sucessor (menor nó na subárvore direita) 
//             root.Data = MinValue(root.Right);

//             // Excluir o sucessor da subárvore direita
//             root.Right = Delete(root.Right, root.Data);
//         }
//         return root;
//     }

// private int MinValue(Node node)
// {
//     int minv = node.Data;
//     while (node.Left != null)
//     {
//         minv = node.Left.Data;
//         node = node.Left;
//     }
//     return minv;
// }

    
// }

// class Program 
// {
//     static void Main(String[] args) {
//         BinaryTree binaryTree = new();
//         var response = binaryTree.Insert(new List<int>(){5,3,6,2,4,7,1,12,10,11,9});
//         Console.WriteLine("Inorder traversal: " + binaryTree.Read());
//         Console.WriteLine($"Elemento existe: {binaryTree.Search(binaryTree.Root, 10)}");
//         Console.WriteLine($"Deletando elemento:");
//         binaryTree.Delete(binaryTree.Root, 10);
//         Console.WriteLine($"Elemento existe: {binaryTree.Search(binaryTree.Root, 10)}");
//     }
// }
