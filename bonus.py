from typing import List

def Cal_length(arr: List) -> List[int]: #count the length
    length = []
    for item in arr:
        if isinstance(item, str):
            length.append(len(item)) #calculate the length and add to the array of list
        elif isinstance(item, int):
            length.append(len(str(item))) #transfer to str, then same with aboving
        else:
            raise ValueError("Wrong type! Input array should be strings or integers")
    return length


input1 = ["abcd", "appletree", "orange"]
input2 = [1224, 45, 9000]

output1 = Cal_length(input1)
output2 = Cal_length(input2)

print("Input:", input1)
print("Output:", output1)

print("\nInput:", input2)
print("Output:", output2)
