def file_read(fname):
    from itertools import islice
    with open(fname, "w") as myfile:
        myfile.write("Bài tập Python\n")
        myfile.write("Bài tập Java")
    txt = open(fname)
    print(txt.read())

file_read('D:/a.txt')