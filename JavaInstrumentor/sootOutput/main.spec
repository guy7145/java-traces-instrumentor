type tests.sll$SLL {
	next:tests.sll$SLL
	data:int
}
main(mut i0:int, mut r0:java.lang.String[], mut r1:tests.sll$SLL) -> () {
	example {
		[i0 == 0 && r0 == [Ljava.lang.String;@33909752 && r1 == null]
		-> [i0 == 1 && r0 == [Ljava.lang.String;@33909752 && r1 == null]
		-> [i0 == 1 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 2 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 2 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 3 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 3 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 4 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 4 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 5 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 5 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 6 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 6 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 7 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 7 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 8 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 8 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 9 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 9 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
		-> [i0 == 10 && r0 == [Ljava.lang.String;@33909752 && r1 == staticinvoke <tests.sll: tests.sll$SLL generateListWithLengthN(int)>(i0)]
	}
}