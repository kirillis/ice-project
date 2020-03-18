from xl_reader import starter

path = 'C:\\Users\\bushanka\\Desktop\\test.xlsx'
answer_path = 'C:\\Users\\bushanka\\Desktop\\answ.odt'
size_2 = 'A1:AD10'
size_1 = 'D4:J12'
size_3 = 'A1:M10'
print(starter(path, size_2, 200000, answer_path))
