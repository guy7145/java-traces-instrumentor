package tests;

public class oop {
	public static class A {
		public static class InnerA {
			static int inner_stat = 0;
			int inner_a;
			public InnerA() {
				this.inner_a = 10;
				inner_stat++;
			}
		}
		int a;
		public A() {
			a = 1;
		}
	}
	
	public static class B {
		int b;
		public B() {
			b = 2;
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
		A.InnerA inner = new A.InnerA();
		System.out.println(A.InnerA.inner_stat);
		System.out.println(inner.inner_a);
		B b = new B();
		C c1 = new C();
		C c2 = C.cmake();

		a1.a = 4;
		b.b = a1.a * c1.c;
		c2.c--;
	}
}
