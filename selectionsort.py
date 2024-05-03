def selection_sort(arr):
    steps = []
    steps.append(arr.copy())  # Initial state of the array
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())  # Record each step of sorting
    return steps

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    arr = []
    print("Enter the elements:")
    for _ in range(n):
        element = int(input())
        arr.append(element)
    
    sorted_steps = selection_sort(arr)
    
    print("\nSteps of Selection Sort:")
    for i, step in enumerate(sorted_steps):
        print(f"Step {i+1}: {step}")
