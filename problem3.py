students = [
    ["Ben", [6, 10, 0, 0, 0, 0, 100, 0, 0]], 
    ["Jim", [99, 99, 99, 99, 99, 99, 99, 99, 99, 99]]
]


def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = max(arr[high][1])     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if max(arr[j][1]) >= pivot:
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
  
# Function to do Quick sort
  
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
  
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

quickSort(students, 0, len(students) - 1)
print(students)