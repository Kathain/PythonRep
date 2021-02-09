# менеджеры контекста - служат для того что бы критические функции срабатывали при ошиьках

with open('test.txt', 'wt', encoding='utf-8') as inFile:
    num = int(input())
    line = str('1 / ' + str(num) + ' = ' + str(1 / num))
    print(line)
    inFile.write(line)  # это записывает нащ результат в файл
