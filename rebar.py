n = int(input())
L = []
for i in range(n):
    m = int(input())
    L.append(m)

length = len(L)

all_possible_pairs = []

if length >= 6:
    count1 = 0
    count = 0
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                for o in range(k+1, length):
                    for p in range(o+1, length):
                        for q in range(p+1, length):
                            total = L[i] + L[j] + L[k] + L[o] + L[p] + L[q]
                            count1 += 1
                            if total <= 12000:
                                each_pair = str(L[i]) + " + " + str(L[j]) + " + " + str(L[k]) + " + " + str(L[o]) + " + " + str(L[p]) + " + " + str(L[q]) +" = "+ str(total)
                                all_possible_pairs.append((total, each_pair))
                                count += 1
    print(count1)
    print(count)
    
    
if length >= 5:
    count1 = 0
    count = 0
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                for o in range(k+1, length):
                    for p in range(o+1, length):
                        total = L[i] + L[j] + L[k] + L[o] + L[p]
                        count1 += 1
                        if total <= 12000:
                            each_pair = str(L[i]) + " + " + str(L[j]) + " + " + str(L[k]) + " + " + str(L[o]) + " + " + str(L[p]) +" = "+ str(total)
                            all_possible_pairs.append((total, each_pair))
                            count += 1
    print(count1)
    print(count)


if length >= 4:
    count1 = 0
    count = 0
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                for o in range(k+1, length):
                    total = L[i] + L[j] + L[k] + L[o]
                    count1 += 1
                    if total <= 12000:
                        each_pair = str(L[i]) + " + " + str(L[j]) + " + " + str(L[k]) + " + " + str(L[o])+" = "+ str(total)
                        all_possible_pairs.append((total, each_pair))
                        count += 1
    print(count1)
    print(count)


if length >= 3:
    count1 = 0
    count = 0
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                total = L[i] + L[j] + L[k]
                count1 += 1
                if total <= 12000:
                    each_pair = str(L[i]) + " + " + str(L[j]) + " + " + str(L[k]) +" = "+ str(total)
                    all_possible_pairs.append((total, each_pair))
                    count += 1
    print(count1)
    print(count)
    
if length >= 2:
    count1 = 0
    count = 0
    for i in range(length):
        for j in range(i, length):
            total = L[i] + L[j]
            count1 += 1
            if total <= 12000:
                each_pair = str(L[i]) + " + " + str(L[j]) +" = "+ str(total)
                all_possible_pairs.append((total, each_pair))
                count += 1
    print(count1)
    print(count)

     
if length == 1:
    print(L[0])
    
    
    
all_possible_pairs.sort(reverse = True)
expressions = []
for i, j in all_possible_pairs:
    expressions.append(j)

numbers = L

remaining_numbers = numbers[:]
valid_expressions = []          
count = 1

for expression in expressions:
    
    number_part = expression.split("=")[0]  
  
    number_strings = number_part.strip().split("+")

    required_numbers = []
    for item in number_strings:
        required_numbers.append(int(item.strip()))
    
    temp_list = remaining_numbers[:]  
    all_found = True                  
    
    for value in required_numbers:
        if value in temp_list:
            temp_list.remove(value)  
        else:
            all_found = False       
            break
    
    if all_found:
        new_expression = str(count) +") "+ expression 
        count += 1
        valid_expressions.append(new_expression) 
        remaining_numbers = temp_list         

print("Highly Efficient Combination of Rebars for Cutting to Minimize Waste As Far As Possible")
for exp in valid_expressions:
    print(exp)

print("Remaining Bars :")
print(remaining_numbers)
