largest_number=[6,7,90,78,50,12,4]
max=largest_number[0] 
for number in largest_number:
    if number >max :
        max=number
print(max)
matrix=[
    [1,2,3],
    [4,5,6],
    [5,7,9]
]
for column in matrix :
    for item in column:
        print(item)