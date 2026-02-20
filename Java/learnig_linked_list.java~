class Node {
	int data;   
    	Node next;
	
	Node(int data1, Node next1){
		data = data1;
		next= next1;
	}
	
	Node (int data1){
		data = data1;
		next= null;
	}

}
class Solution {
	public Node insertAtHead(Node head, int newData){
		Node newNode = new Node(newData, head);
		return newNode;
	
	}
	public Node deleteFromLast(Node head){
		if(head != null || head.next != null){
			return null;
		}
		Node curr = head;
		while(curr.next.next != null){
			curr= curr.next;
		}
		curr.next= null;
		return head;
	}
	public void printList(Node head){
		Node temp=head;
		while(temp != null){
			System.out.println(temp.data + " ");
			temp=temp.next;
		}
		System.out.println();
	}
}
	
public class learnig_linked_list{
	public static void main(String[] args){
		Solution sol = new Solution();
		Node head = new Node(2);
		head.next = new	Node(3);
		head.next.next= new Node(4);
		/*
		System.out.println("Original data :");
		sol.printList(head);

		head = sol.insertAtHead(head, 1);

		System.out.println("After insert at head :");
		sol.printList(head);
		*/
		head=sol.deleteFromLast(head);
		sol.printList(head);
		
	}
}
