def squre(a,b) : 
	if b == 1 :
		return a;
	return a*squre(a,b-1)

def main() :
	inputs = [int(x) for x in input().split()]
	print(squre(inputs[0],inputs[1]))

if __name__ == "__main__" :
	main()