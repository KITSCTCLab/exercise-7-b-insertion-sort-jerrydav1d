from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(size-1):
    min=array[i]
    minpos=i
    for j in range(i,size):
      
      if array[j]<min:
        min=array[j]
        minpos=j
    temp=array[i]
    array[i]=min
    array[minpos]=temp
  return array 
    
    

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
