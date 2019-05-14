def precedence(current_op,op_from_ops):
	if op_from_ops == "(":
		return False
	if (current_op == "*" or current_op == "/") and (op_from_ops=="+" or op_from_ops=="-"):
		return False

	return True

def operation(operator,second_num,first_num):
	if operator == "+":
		return second_num+first_num
	elif operator == "-":
		return first_num-second_num

	elif operator=="*":
		return first_num*second_num
	elif operator == "/":
		return first_num // second_num

def basicCalculator3(string):
	num,i = 0,0
	nums,ops = [],[]
	while i < len(string):
		if string[i].isdigit():
			num = int(string[i])
			while i<len(string)-1 and string[i+1].isdigit():
				num = num*10+int(string[i+1])
				i +=1

			nums.append(num)

		elif string[i] in "+-*/":
			if len(ops)>0:
				if precedence(string[i],ops[-1]):
					nums.append(operation(ops.pop(),nums.pop(),nums.pop()))
			ops.append(string[i])
			num = 0

		elif string[i] == "(":
			ops.append(string[i])

		elif string[i] == ")":
			while ops[-1] != "(":
				nums.append(operation(ops.pop(),nums.pop(),nums.pop()))
			ops.pop()

		i +=1

	while len(ops)>0:
		nums.append(operation(ops.pop(),nums.pop(),nums.pop()))

	return nums.pop()


print(basicCalculator3("((  13 /(  (   6+ 19  )/ 14  )  ) +( (   17 * (   ((   (  ( (   ( 18+19  )   +  (5  +   7   ) )*(  17+ (   14   /16 ) )) +7)  / ( ( (   (   14  +  14   )+  ( 7 /  10   ))  * 15  )  /(  (   (  20   +  4)  *13   ) + 1   ))   )*   ( 10+   15 )  )- ( (  (((   (   4  +   17  )   +   (4   * 6) )   +   (   12   +   15   )  )   +   5)+  (  ((( 14  +   19  ) +( 10 +  1  )) -(  ( 11   +17)+ ( 10  +   1)   )   ) +(( (  13  +   20  ) - (18 +17  )   )-  ( (   7  /15  )  -  (  7   - 19   ))   ) ))   -  (  (   17   +  (   ( ( 15 + 2 )  * (  2   -  6 )   )  + (   (  6   +  14   ) + ( 19   * 2  )   ))   )/ (   (  (  ( 18   -3   )+(  6 *13   ) )   +15 )+((   (  17 -19)   +  ( 2  +10)  )+(  ( 8 +18 )  +  (9+  8)   ) ) ))  ) )  )   -( (( (( 14 /   5 )+ ( (   (  ( 13  + 11  ) - ( 3* 20 )   )   -  (   (  15 *  10)  +  (14+ 19  )   ) )-(   ((   8   +  20  )   -  (   5*16   ) )   *(  ( 13 - 1)   /  (   8/ 6) ) ) ) ) +  8) +  5   )  / ( (  (   (( (   ( 18  + 17   )+(  4 + 8 ))  +(   ( 19  *16 )  + (11   *   14  )   )  )   +   (( (   6   + 19  )  *  (7- 17  ) ) +  ( (  12+ 16)   *  (15+ 7  )) )   )* ((   (   (  3 +13)  +   ( 19   +19  )  )   -   (  (4*   7  )  +  11) ) * 18) )   - ((   14  +20 )   *   ((   (   (   12   *   8   )   * (   7   + 12 ) )  /   13 ) * (   (   (  3   -  6  )  +(8/   10   )  )  +(  2+ (15 -   20  )   )  )  )  )) +((   (  (   1*   ( ( 12  -  1   )  +( 7*18  ) )  )*  6   )   + (  (   ((4+   20 ) -   2 )   *(   (   8  -  13  )   *(14 -19 )))*  (  (( 19  +   1   )   +  ( 4  -  13 )   )+  (  (  19  +  4)  *(  19  +   19 )   ) )  )   ) + (  (   (  7 +  (  9   +  (14 +   4)) )  - 9)   *  ((   5  /  (   (  19  +3   )  + (  9   *   15 ) )   ) + ( (( 20   +   12  )+ (17 +   12 ) )  *(  (17  +6   ) +   16 ))))) )  ) ))"))
