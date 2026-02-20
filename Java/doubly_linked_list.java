import java.util.*;

class Node{
	int data;
	Node next;
	Node prev;
	Node(int data, Node next, Node prev){
		this.next=next;
		this.data=data;
		this.prev=prev;
	}
	Node(int data){
		this.data=data;
		this.next=null;
		this.prev=null;
	}
}
public class doubly_linked_list {
	public static void main(String[] args){
		Node head =new Node(2);
		System.out.println(head);
		System.out.println(head.data);
	}
}


