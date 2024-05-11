// using System;

// class Node {
//     public int data;
//     public Node left, right;
//     public int height;

//     public Node(int value) {
//         data = value;
//         left = right = null;
//         height = 1;
//     }
// }

// class AVLTree {
//     private Node root;

//     // Construtor
//     public AVLTree() {
//         root = null;
//     }

//     // Retorna a altura de um nó
//     private int Height(Node node) {
//         if (node == null)
//             return 0;
//         return node.height;
//     }

//     // Calcula o fator de equilíbrio de um nó
//     private int BalanceFactor(Node node) {
//         if (node == null)
//             return 0;
//         return Height(node.left) - Height(node.right);
//     }

//     // Rotação à direita
//     private Node RightRotate(Node y) {
//         Node x = y.left;
//         Node T2 = x.right;

//         // Realiza a rotação
//         x.right = y;
//         y.left = T2;

//         // Atualiza alturas
//         y.height = Math.Max(Height(y.left), Height(y.right)) + 1;
//         x.height = Math.Max(Height(x.left), Height(x.right)) + 1;

//         // Retorna a nova raiz
//         return x;
//     }

//     // Rotação à esquerda
//     private Node LeftRotate(Node x) {
//         Node y = x.right;
//         Node T2 = y.left;

//         // Realiza a rotação
//         y.left = x;
//         x.right = T2;

//         // Atualiza alturas
//         x.height = Math.Max(Height(x.left), Height(x.right)) + 1;
//         y.height = Math.Max(Height(y.left), Height(y.right)) + 1;

//         // Retorna a nova raiz
//         return y;
//     }

//     // Inserção
//     public void Insert(int key) {
//         root = InsertRec(root, key);
//     }

//     private Node InsertRec(Node node, int key) {
//         if (node == null)
//             return new Node(key);

//         if (key < node.data)
//             node.left = InsertRec(node.left, key);
//         else if (key > node.data)
//             node.right = InsertRec(node.right, key);
//         else
//             return node; // Não permitimos duplicatas

//         // Atualiza a altura do nó atual
//         node.height = 1 + Math.Max(Height(node.left), Height(node.right));

//         // Verifica o fator de equilíbrio
//         int balance = BalanceFactor(node);

//         // Se o nó se torna desequilibrado, existem 4 casos de rotação possíveis
//         // Caso esquerdo-esquerdo
//         if (balance > 1 && key < node.left.data)
//             return RightRotate(node);

//         // Caso direito-direito
//         if (balance < -1 && key > node.right.data)
//             return LeftRotate(node);

//         // Caso esquerdo-direito
//         if (balance > 1 && key > node.left.data) {
//             node.left = LeftRotate(node.left);
//             return RightRotate(node);
//         }

//         // Caso direito-esquerdo
//         if (balance < -1 && key < node.right.data) {
//             node.right = RightRotate(node.right);
//             return LeftRotate(node);
//         }

//         return node;
//     }

//     // Busca
//     public bool Search(int key) {
//         return SearchRec(root, key);
//     }

//     private bool SearchRec(Node node, int key) {
//         if (node == null)
//             return false;

//         if (key == node.data)
//             return true;

//         if (key < node.data)
//             return SearchRec(node.left, key);
//         else
//             return SearchRec(node.right, key);
//     }

//     // Exclusão
//     public void Delete(int key) {
//         root = DeleteRec(root, key);
//     }

//     private Node DeleteRec(Node root, int key) {
//         // Implemente a exclusão de um nó em uma árvore AVL
//         // Lembre-se de manter a propriedade de AVL após a exclusão
//         return root;
//     }

//     // Função de utilidade para exibir a árvore
//     private void InOrderTraversal(Node node) {
//         if (node != null) {
//             InOrderTraversal(node.left);
//             Console.Write(node.data + " ");
//             InOrderTraversal(node.right);
//         }
//     }

//     // Exibe a árvore em ordem
//     public void Display() {
//         InOrderTraversal(root);
//         Console.WriteLine();
//     }
// }

// class Program {
//     static void Main(string[] args) {
//         AVLTree tree = new AVLTree();

//         // Inserção
//         tree.Insert(10);
//         tree.Insert(20);
//         tree.Insert(30);
//         tree.Insert(40);
//         tree.Insert(50);
//         tree.Insert(25);

//         // Busca
//         Console.WriteLine("Busca por 30: " + tree.Search(30));
//         Console.WriteLine("Busca por 35: " + tree.Search(35));

//         // Exibição da árvore em ordem
//         Console.WriteLine("Árvore em ordem:");
//         tree.Display();
//     }
// }


// // A inserção é feita mantendo a propriedade de AVL, garantindo que a árvore permaneça balanceada.
// // A busca em uma árvore AVL é similar à busca em uma árvore de busca binária normal, portanto, sua complexidade é O(logn).
// // A exclusão em uma árvore AVL é mais complexa e não foi implementada aqui. Implementar a exclusão em uma árvore AVL requer mais cuidado para garantir que a árvore permaneça balanceada após a exclusão de um nó.