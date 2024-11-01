with open ('text.txt', 'r', encoding='utf-8') as infile, open('output.txt', 'w', encoding='utf-8') as outfile:#открытие файлов
    data=infile.readlines()#перекидывание файла 
    i=0#инициализация индекса
    for str in data:#цикл для перебора 
        if len(data[i])>5:#условие чтобы исключить подходящие 
            outfile.write(data[i])#переписывание подходящих в новый файл
        i+=1#увеличение индекса 