package tests;


public class factorial {
	public static void main(String[] args) {
		int fact = 1;
		final int N = 6;
		for (int i = 1; i <= N; i++)
			fact *= i;
		System.out.printf("%d!=%d\n", N, fact);
		
		return;
	}
}
