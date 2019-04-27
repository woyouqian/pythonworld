from os import path


# 对文档进行操作！
def open_file():
    file_path = path.abspath('xls_rd.py').strip('xls_rd.py')
    file_name = "recoder.txt"
    file = file_path+file_name
    file_obj = open(file, 'a')
    return file_obj

def write_file(file, info='\n'):
    file.write('\n')
    file.write(info)

def close_file(file):
    file.close()


if __name__ == "__main__":
    txt_file = open_file()
    write_file(txt_file, info="hello Python world!")
    close_file(txt_file)

