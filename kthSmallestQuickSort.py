"""
Given List of N integers
find kth smallest element
Quick sort then find kth smallest
O(nlogn)
Algorithm 2: find the kth smallest element in the list using partition procedure of Quicksort recursively
Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).
Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.
"""
    def quickSort():
        # Use first element as V2 will have median of medians
        # after pick median put elements less than pivot to the left and elements great to righ
        # left and right sides
        # new pivot?
        # recursivly partition left and right sub array of the already split at the end of helper func
    def partitionList(listToPart):
        pass
        # use first element for partition
        # organize elements less than to left and greater than to right 
        #

    # create an N size list with random values
    def randomList(size):
        lst = []
        for i in range(size):
            lst.append(random.randint(i, i+20))

        return lst

    def getElement(kth, arr):
        return arr[kth-1]


if __name__ == "__main__":

    print("Random List Generated")
    arrSize = 5
    randomList = randomList(arrSize)
    print(randomList)

    sorted = quickSort(randomList)
    k = random.randint(0, len(randomList))

    print("Sorted: ", sorted)
    
    print("Searhing random valid value after quickSort")
    print("K value: ", k, " - Element at K: ", getElement(k, sorted))







