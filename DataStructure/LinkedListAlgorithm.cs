using System;

class Node {
    public int data;
    public Node next;

    public Node(int d) {
        data = d;
        next = null;
    }
}

class LinkedList {
    private Node head;

    // Construtor
    public LinkedList() {
        head = null;
    }

    // Inserção no início da lista (O(1))
    public void Insert(int newData) {
        Node newNode = new Node(newData);
        newNode.next = head;
        head = newNode;
    }

    // Busca (O(n))
    public bool Search(int key) {
        Node current = head;
        while (current != null) {
            if (current.data == key)
                return true;
            current = current.next;
        }
        return false;
    }

    // Exclusão (O(n))
    public void Delete(int key) {
        Node temp = head;
        Node prev = null;

        if (temp != null && temp.data == key) {
            head = temp.next;
            return;
        }

        while (temp != null && temp.data != key) {
            prev = temp;
            temp = temp.next;
        }

        if (temp == null) return;

        prev.next = temp.next;
    }

    // Atualização (O(n))
    public void Update(int oldData, int newData) {
        Node current = head;
        while (current != null) {
            if (current.data == oldData) {
                current.data = newData;
                return;
            }
            current = current.next;
        }
    }

    // Exibição da lista
    public void Display() {
        Node current = head;
        while (current != null) {
            Console.Write(current.data + " ");
            current = current.next;
        }
        Console.WriteLine();
    }
}

class Program {
    static void Main(string[] args) {
        LinkedList list = new LinkedList();

        // Inserção (O(1))
        list.Insert(10);
        list.Insert(20);
        list.Insert(30);

        Console.WriteLine("Lista atual:");
        list.Display();

        // Busca (O(n))
        Console.WriteLine("Busca por 20: " + list.Search(20));

        // Exclusão (O(n))
        list.Delete(20);
        Console.WriteLine("Lista após excluir 20:");
        list.Display();

        // Atualização (O(n))
        list.Update(10, 15);
        Console.WriteLine("Lista após atualizar 10 para 15:");
        list.Display();
    }
}


// Inserção: A inserção é feita no início da lista, então é uma operação de tempo constante, O(1).
// Busca: Para procurar um elemento, a lista é percorrida sequencialmente, o que resulta em uma complexidade de tempo linear, O(n).
// Exclusão: Similar à busca, a lista é percorrida para encontrar o elemento a ser excluído, então a exclusão também é uma operação de tempo linear, O(n).
// Atualização: Para atualizar um valor, a lista é percorrida até encontrar o elemento desejado, então a operação é linear, O(n).