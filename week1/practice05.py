def mul(n,m) :
    
    if m == 1:
        return n

    if int(m%2) == 0 :
        return mul(2*n,m//2)
    else :
        return n + mul(2*n,m//2)

def main():
    inputs = [int(x) for x in input().split()]
    print(mul(inputs[0],inputs[1]))

if __name__ == "__main__" :
	main()