package tests;


public class factorial {
	public static void hello(int a, int b) {
		System.out.println(a);
		System.out.println(b);
	}
	
	public static int fact(int n) {
		int fact = 1;
		hello(fact, 2);
		for (int i = 1; i <= n; i++)
			fact *= i;
		return fact;
	}
	
	public static void main(String[] args) {
		final int N = 7;
		System.out.printf("%d!=%d\n", N, fact(N));
		
		return;
	}
}
