def merge(arr1: list, arr2: list) -> list:
    i, j, arr = 0, 0, []
    #
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    if i == len(arr1):
        for n in range(j, len(arr2)):
            arr.append(arr2[n])
    else:
        for n in range(i, len(arr1)):
            arr.append(arr1[n])
    return arr
        


def mergeSort(arr: list):
    #Caso base | arr tiene un solo elemento o ninguno por definicion se encuentra ordenado
    if len(arr) <= 1:
        return arr
    #de lo contrario debemos hacer uso de dividir y conquistar
    #partimos el arreglo a la mitad hasta que llegue al caso base
    else:
        mid = len(arr) // 2
        arr1 = mergeSort(arr[:mid])
        arr2 = mergeSort(arr[mid:])
        #llamado al merge para unir el arr1 y arr2 ordenado
        return merge(arr1, arr2)
    
l1 = [9, 8, 7, 6, 5, 4, 10, 9, 10]

print(mergeSort(l1))