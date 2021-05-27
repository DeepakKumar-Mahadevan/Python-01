MyRow = ['Name','Gender','Age']

# for items in MyRow:
#     print(items)
#
# for pos in range(len(MyRow)): #range function starts with default 0 to given number -1
#     print(MyRow[pos])

MyTable = [ \
    ['Maaaaaaan','M',65], \
    ['Rbbba','F',59], \
    ['Sccca','M',34], \
    ['Vddddddi','F',32], \
    ['Aeeen','M',6], \
    ['Sfffffa','F',2], \
    ['Mgggggn','M',3], \
    ['Phhha','F',29], \
    ['Diiiik','M',32], \
    ]

Names = []
GenderGroups = set()
CumlativeAge = 0

for row_num in range(len(MyTable)):
    for col_num in range(len(MyTable[row_num])):
        # print(MyTable[row_num][col_num])
        if col_num == 0:
            Names.append(MyTable[row_num][col_num])
        elif col_num == 1:
            GenderGroups.add(MyTable[row_num][col_num])
        else:
            CumlativeAge = (CumlativeAge + MyTable[row_num][col_num])

print("Number of People : ", len(MyTable))
print("List of Names : ", Names)
print("Unique Gender Groups: ", GenderGroups)
print("Average Age : ", round((CumlativeAge/len(MyTable)),2))