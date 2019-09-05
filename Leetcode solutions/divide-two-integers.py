def divideTwoIntegers(dividend,divisor):
	sign = 1
	if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
		sign = -1
	ans = 0
	dividend,divisor = abs(dividend),abs(divisor)
	while dividend>=divisor:
		tmp,d = 1,divisor
		while dividend>=d:
			d = d<<1
			tmp = tmp<<1
		d = d>>1
		tmp = tmp>>1
		dividend -= d
		ans += tmp

	if sign == -1:
		ans = -ans
	return max(-2**31,min(ans,2**31-1))


print(divideTwoIntegers(10,-3))