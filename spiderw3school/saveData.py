from os import path
from time import asctime


def createFile(i=None):
    if i is None:
        file_name = "w3shoolPython.doc"
    else:
        file_name = "w3shoolPython" + str(i) + ".doc"
    file_path = path.dirname(__file__)
    # print(file_path)
    file = file_path + '/' + file_name

    data_doc = open(file, 'w')
    data_doc.write(asctime()+'\n')
    data_doc.close()
    return file


def saveData(file, strings):
    if strings:
        with open(file, 'a') as f:
            f.write('\n')
            f.write(strings)
            f.write('\n\n')


def copyData(file1, file2):
    "copy file2 data message then paste to file1."
    with open(file2, 'r') as f2:
        text = f2.read()
    if text:
        with open(file1, 'a') as f1:
            f1.write(text)


if __name__ == "__main__":
    file = createFile()
    print(file)
    strings = "hello python world! i'm comming on the way."
    saveData(file, strings)

