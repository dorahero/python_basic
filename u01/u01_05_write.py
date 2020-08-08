path = 'test.txt'
f = open(path, 'w', encoding='utf-8')
f.write('test write file\n')
f.close()

f = open(path, 'a', encoding='utf-8')
f.write('test\n')
f.write('test again\n')
f.close()
