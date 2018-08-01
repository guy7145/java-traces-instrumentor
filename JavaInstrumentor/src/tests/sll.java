package tests;

public class sll {
	static class SLL{
		SLL next;
		int data;
		
		public SLL() {
			this.next = null;
		}
		
		@Override
		public String toString() {
			return "sll" + data;
		}
	}
	
	public static SLL generateListWithLengthN(int length) {
		SLL base = new SLL();
		
		SLL head = base;
		for(int i = 0 ; i < length; i++) {
			head.next = new SLL();
			head = head.next;
		}
		
		return base;
	}
	
	public static void fill(SLL list) {
		for (int i = 0; list.next != null; list = list.next, i++) {
			list.data = i;
		}
	}
	
	public static void printSLL(SLL list) {
		while (list.next != null) {
			System.out.print(" --> " + list.data);
			list = list.next;
		}
		System.out.println();
	}

	public static void main(String[] args) {
		for(int i = 1; i < 10; i++) {
			SLL list = generateListWithLengthN(i); 
			fill(list);
			printSLL(list);
		}
	}
}
