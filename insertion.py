


def string_to_int_array(string):
    num_array = []
    curr_num  = ""
    for char in array_string:

        if char.isdigit():
            curr_num += char
        elif char.isspace() and curr_num : 
            num_array.append(int(curr_num))
            curr_num = ""

    if curr_num:
        num_array.append(int(curr_num))
    
    return num_array


array_string =  input("Enter numerical array with each number followed by a space ex:( 1 2 3 4 ): ")


num_array =  string_to_int_array(array_string)
count  = 0

print("number array unsorted: ")
for x in num_array:
    print(x)

for x in num_array:

    if x == num_array[0] & count == 0:
        count+=1
        continue

    check = count-1
    while check >= 0:
        if x < num_array[check]:
            temp = num_array[check]
            num_array[check] = x
            num_array[check + 1] = temp
        check -= 1
    count +=1

print("number array sorted: ")
for x in num_array:
    print(x)