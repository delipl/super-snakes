#!/usr/bin/python
import glob
import sys
# Podaj rozszerzenie bez kropki i w tych plikach zostanie usunięta linijka z dupą 
def main():
    if len(sys.argv) != 2:
        print("Podaj rozszerzenie")
        return -1;
    print ('Usuwam linijkę z dupa')
    nameOne = str(sys.argv[1])
    mylist = [f for f in glob.glob('**/*.' + nameOne,recursive=True)]
    k = 0
    for fileName in mylist:
        print ('Przeszukuje ', fileName, '...')
        file = open(fileName, "r")
        Lines = file.readlines() 
        file.close()
        i = 0
        delLineIndex = []
        for line in Lines:
            temp = line.lower()
            if temp.find("dupa") >  1:
                print("Usuwam linijkę: " , i)
                k += 1
                delLineIndex += [i]
            i = i + 1
        j = 0
        for x in delLineIndex:
            del Lines[x-j]
            j = j+ 1
        file = open(fileName, "w")
        file.writelines(Lines) 
        file.close() 
    print("Usunięto:",k,"dup.")

if __name__ == '__main__':
    main()
