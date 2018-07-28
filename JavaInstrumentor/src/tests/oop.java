package tests;

public class oop {
	static class A {
		int a;
		public A() {
			a = 1;
		}
	}
	
	static class B extends A {
		int b;
		public B() {
			super();
			b = 2;
			a++;
		}
	}
	
	static class C {
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
		A a = new A();
		B b = new B();
		C c1 = new C();
		C c2 = C.cmake();
		A ab = new B();
		
		System.out.println(a.a);
		System.out.println(b.b);
		System.out.println(b.a);
		System.out.println(c1.c);
		System.out.println(c2.c);
		System.out.println(a.a + b.a + b.b + c1.c);
		System.out.println(Math.pow(c1.c, c2.c));
		System.out.println(ab instanceof B);
		System.out.println(ab instanceof A);
	}
}
