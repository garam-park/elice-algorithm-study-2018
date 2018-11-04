def add_from_to(f,t):
    if f >= t :
        return t
    return add_from_to(f,t-1)+t

def main():
	t = int(input())
	print(add_from_to(1,t))
	
if __name__ == "__main__":
	main()