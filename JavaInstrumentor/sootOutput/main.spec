type tests.oop$A {
	a:int
}
type tests.oop$B {
	b:int
}
type tests.oop$C {
	c:int
}
type tests.oop$A$InnerA {
	inner_stat:int
	inner_a:int
}
main(mut $r13:tests.oop$B, mut r5:tests.oop$C, mut $r14:tests.oop$C, mut $r6:java.lang.Class, mut $r7:java.io.PrintStream, mut $r8:java.lang.String, mut $r9:tests.oop$A, mut $i0:int, mut $i1:int, mut r5.c:int, mut $i2:int, mut $i3:int, mut $i4:int, mut $r13.b:int, mut $i5:int, mut $i6:int, mut $r9.a:int, mut $r11:java.io.PrintStream, mut $r12:java.io.PrintStream, mut r0:java.lang.String[], mut $r10:tests.oop$A$InnerA) -> () {
	example {
		[$r13 == null && r5 == null && $r14 == null && $r6 == null && $r7 == null && $r8 == null && $r9 == null && $i0 == 0 && $i1 == 0 && r5.c == 0 && $i2 == 0 && $i3 == 0 && $i4 == 0 && $r13.b == 0 && $i5 == 0 && $i6 == 0 && $r9.a == 0 && $r11 == null && $r12 == null && r0 == [Ljava.lang.String;@33909752 && $r10 == null]
		-> [$r7 == java.lang.System.out]
		-> [$r6 == class "Ltests/oop$A;"]
		-> [$r8 == virtualinvoke $r6.<java.lang.Class: java.lang.String getName()>()]
		-> [$r9 == new tests.oop$A]
		-> [$r10 == new tests.oop$A$InnerA]
		-> [$r11 == java.lang.System.out]
		-> [$i0 == 1]
		-> [$r12 == java.lang.System.out]
		-> [$i1 == 10]
		-> [$r13 == new tests.oop$B]
		-> [$r14 == new tests.oop$C]
		-> [r5 == staticinvoke <tests.oop$C: tests.oop$C cmake()>()]
		-> [$r9.a == 4]
		-> [$i3 == 4]
		-> [$i2 == 3]
		-> [$i4 == 12]
		-> [$r13.b == 12]
		-> [$i5 == 4]
		-> [$i6 == 3]
		-> [r5.c == 3]
	}
}