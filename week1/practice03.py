def mul(a,b) :
	if b == 0 :
		return 0
	return a+mul(a,b-1)

def main() :
	inputs = [int(x) for x in input().split()]
	print(mul(inputs[0],inputs[1]))

if __name__ == "__main__" :
	main()