package tests;

public class oop {
	public static class A {
		int a;
		public A() {
			a = 1;
		}
	}
	
	public static class B extends A {
		int b;
		public B() {
			b = 2;
			a++;
		}
	}
	
	public static class C {
		int c;
		public C() {
			super();
			c = 3;
		}
		
		public static C cmake() {
			C c = new C();
			c.c = 4;
			Object o = new Object();
			System.out.println(c.c);
			return c;
		}
	}
	
	
	public static void main(String[] args) {
		System.out.println(A.class.getName());
		A a1 = new A();
		B b = new B();
		C c1 = new C();
		C c2 = C.cmake();
		A a2 = new A();
		
		System.out.println(a1.a);
		System.out.println(b.b);
		System.out.println(b.a);
		System.out.println(c1.c);
		System.out.println(c2.c);
		System.out.println(a1.a + b.a + b.b + c1.c);
	}
}
