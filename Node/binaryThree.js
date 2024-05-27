// Trade-offs entre BFS (Breadth-First Search) e DFS (Depth-First Search)
// Memória:

// BFS pode usar muita memória se o grafo tiver muitos níveis, pois armazena todos os nós de um nível na fila.
// DFS usa menos memória, pois armazena apenas o caminho atual (exceto se for implementado de forma recursiva em um grafo profundo, o que pode causar um estouro de pilha).
// Caminho mais curto:

// BFS garante encontrar o caminho mais curto em grafos não ponderados.
// DFS não garante o caminho mais curto e pode explorar caminhos mais longos antes de encontrar o destino.
// Completo vs. Incompleto:

// BFS é completo em grafos finitos, sempre encontra uma solução se houver uma.
// DFS pode não ser completo se houver caminhos infinitos ou ciclos sem tratamento adequado.
// Exemplos práticos
// BFS: Imagine que você está procurando a saída de um labirinto e deseja encontrar o caminho mais curto. BFS é ideal para isso, pois explora todas as opções possíveis a cada passo, garantindo o menor caminho.
// DFS: Imagine que você está resolvendo um quebra-cabeça de Sudoku. DFS é útil porque permite explorar todas as combinações possíveis até encontrar a solução.

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
            root.left = this.deleteRecursive(root.left, value);
        else if(value > root.value)
            root.right = this.deleteRecursive(root.right, value);
        else{
            if(root.left === null)
                return root.right;
            else if(root.right === null)
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

    // BFS (Breadth-First Search): Percorre os nós nível por nível.
    // Breadth-First Search (BFS)
    bfs() {
        if (this.root === null) return [];
    
        let queue = [this.root];
        let result = [];
    
        while (queue.length > 0) {
            let node = queue.shift();
            result.push(node.value);
    
            if (node.left !== null) {
                queue.push(node.left);
            }
            if (node.right !== null) {
                queue.push(node.right);
            }
        }
    
        return result;
    }

    // DFS Preorder: Visita o nó atual antes de seus filhos.
    // Depth-First Pre Order (DFS)
    dfsPreOrder(node, result = []) {
        if (node !== null) {
            result.push(node.value);
            this.dfsPreOrder(node.left, result);
            this.dfsPreOrder(node.right, result);
        }
        return result;
    }

    // DFS Inorder: Visita o nó esquerdo, depois o próprio nó, e então o nó direito.
    // Depth-First Search Inorder (DFS)
    dfsInOrder(node, result = []) {
        if (node !== null) {
            this.dfsInOrder(node.left, result);
            result.push(node.value);
            this.dfsInOrder(node.right, result);
        }
        return result;
    }

    // DFS Postorder: Visita os filhos esquerdos e direitos antes de visitar o próprio nó.
    // Depth-First Search Postorder (DFS)
    dfsPostOrder(node, result = []) {
        if (node !== null) {
            this.dfsPostOrder(node.left, result);
            this.dfsPostOrder(node.right, result);
            result.push(node.value);
        }
        return result;
    }
}

const binaryThree = new BinaryThree();
binaryThree.insert(10);
binaryThree.insert(9);
binaryThree.insert(14);
binaryThree.insert(7);
binaryThree.insert(8);
binaryThree.insert(12);
binaryThree.insert(15);
binaryThree.insert(4);
binaryThree.insert(3);
binaryThree.insert(13);

// var nodeExist = binaryThree.nodeExist(binaryThree.root, 4);
// console.log("Node with value {4} exist: " + nodeExist);

// console.log(binaryThree.bfs());

// console.log(binaryThree.dfsPreOrder(binaryThree.root));

// const valueToDelete = 10;
// binaryThree.deleteRecursive(binaryThree.root, valueToDelete);

console.log(`DFS Pre Order ${binaryThree.dfsPreOrder(binaryThree.root)}`);
console.log(`DFS In Order ${binaryThree.dfsInOrder(binaryThree.root)}`);
console.log(`DFS Post Order ${binaryThree.dfsPostOrder(binaryThree.root)}`);