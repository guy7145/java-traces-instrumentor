package tests;


public class factorial {
	
	public static int fact(int n) {
		int fact = 1;
		for (int i = 1; i <= n; i++)
			fact *= i;
		return fact;
	}
	
	public static void main(String[] args) {
		Object j = new Object();
		System.out.println(j.toString());
		final int N = 7;
		for (int i = 0; i < N; i++) System.out.printf("%d!=%d\n", i, fact(i));
	}
}
