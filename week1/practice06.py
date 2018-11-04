def quick_sort(list):
    
    if len(list) == 0:
        return []

    pivot = list[0]
    
    left  = [x for x in list[1:] if x <= pivot]
    right = [x for x in list[1:] if x > pivot]
	
    return quick_sort(left) + [pivot] + quick_sort(right)

def main() :
	inputs = [int(x) for x in input().split()]
	print(*quick_sort(inputs))
	
if __name__ == "__main__":
	main()