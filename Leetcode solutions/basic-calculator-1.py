def basicCalulator1(string):
	res,num,sign,stack = 0,0,1,[]
	for i in range(len(string)):
		if string[i] == "(":
			stack.append(res)
			stack.append(sign)
			res,sign = 0,1

		elif string[i].isdigit():
			num = num*10+int(string[i])

		elif string[i] == ")":
			res += sign*num
			res *= stack.pop()
			res += stack.pop()
			num = 0

		elif string[i] in "+-":
			res += sign*num
			num = 0
			if string[i] == "-":
				sign = -1
			else:
				sign = 1

	return res+(sign*num)



string = "(1+(4+5+2)-3)+(6+8)"
print(basicCalulator1(string))