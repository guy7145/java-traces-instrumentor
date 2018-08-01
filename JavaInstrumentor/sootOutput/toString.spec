type tests.sll$SLL {
	next:tests.sll$SLL
	data:int
}
toString(mut $r1:java.lang.StringBuilder, mut $r2:java.lang.StringBuilder, mut $r3:java.lang.String, mut $i0:int, mut r0:tests.sll$SLL) -> ($r3:java.lang.String) {
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
	example {
		[$r1 == null && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == null && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == null && $i0 == 0 && r0 == null]
		-> [$r1 == new java.lang.StringBuilder && $r2 == virtualinvoke $r1.<java.lang.StringBuilder: java.lang.StringBuilder append(int)>($i0) && $r3 == virtualinvoke $r2.<java.lang.StringBuilder: java.lang.String toString()>() && $i0 == 0 && r0 == null]
	}
}