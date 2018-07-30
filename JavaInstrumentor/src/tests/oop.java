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
		a1.a = 4;
		b.b = a1.a * c1.c;
		c2.c--;
	}
}
