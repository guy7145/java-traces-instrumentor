package tests;


public class factorial {
	
	public static int fact(int x) {
		int y = 1;
		while (x >= 1) {
			y = y * x;
			x = x - 1;
		}
		return y;
	}
	
	public static void main(String[] args) {
		final int N = 7;
		for (int i = 0; i < N; i++) System.out.printf("%d! = %d\n", i, fact(i));
	}
}
