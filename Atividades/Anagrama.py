array = ["IMJ0O51", "RHD6B03", "SNE8B12", "HTM1C21", "OHE2T42", "JED8N46", "OTA9H48", "KCC3V06", "BRW5B37"] 


def countingSort(array, indice_str):
    size = len(array)
    output = [0] * size
    count = [0] * 91

    # Calculate count of elements
    for i in range(0, size):
        index = ord(array[i][indice_str])  
        count[index] += 1

    # Calculate cumulative count
    for i in range(1, 91):
        count[i] += count[i - 1]

    # the elements in sorted order
    i = size - 1
    while i >= 0:
        index = ord(array[i][indice_str])  
        output[count[index] - 1] = array[i]
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
    
    return array

def radixSort(array):
    indice_str = 6
    while indice_str >= 0:
        countingSort(array, indice_str)
        indice_str -= 1

    return array


print (radixSort(array))