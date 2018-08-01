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
cmake(mut $r1:tests.oop$C, mut $r1.c:int) -> ($r1:tests.oop$C) {
	example {
		[$r1 == null && $r1.c == 0]
		-> [$r1 == new tests.oop$C]
		-> [$r1.c == 4]
	}
}