from xl_reader import starter

path = 'C:\\Users\\bushanka\\Desktop\\test.xlsx'
size = 'A1:C3'
answer, matrix = starter(path, size, 10500)
print(answer[:, :, -1])
