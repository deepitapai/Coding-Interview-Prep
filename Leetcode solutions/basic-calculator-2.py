def basicCalculator2(string):
	stack,num,sign = [],0,"+"
	for i in range(len(string)):
		if string[i].isdigit():
			num = num*10+ord(string[i])-ord("0")

		if (not string[i].isdigit() and not string[i].isspace()) or i == len(string)-1:
			if sign == "-":
				stack.append(-num)
			elif sign == "+":
				stack.append(num)
			elif sign == "*":
				stack.append(stack.pop*num)
			else:
				tmp = stack.pop()
				if tmp//num <0 and tmp%num != 0:
					stack.append(tmp//num+1)
				else:
					stack.append(tmp//num)

			num = 0
			sign = string[i]

	return sum(stack)



print(basicCalculator2("3+5/2"))