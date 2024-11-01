name = "Vincent"
teacher1 = "Mr. Gallo"
teacher2 = "Mr. Cusimano"
teacher3 = 'Mr. Bisogno'

sub1 = "Computer Science"
sub2 = "Chemistry"
sub3 = "Functions"

print(f"""+{'-'*60}+
| {'1'} | {sub1:>30} | {teacher1:>21} {'|':>1}
| {'2'} | {sub2:>30} | {teacher2:>21} {'|':>1}
| {'3'} | {sub3:>30} | {teacher3:>21} {'|':>1}
+{'-'*60}+""")