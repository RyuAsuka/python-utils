import os
import time


def mkSubFile(lines, head, srcName, sub):
    '''
    Generate the sub file of the main file
    :param lines: The content to write in
    :param head: An optional parameter, the file's first line. You can omit it.
    :param srcName: The main file name
    :param sub: The number of generated sub file
    :return: Sub + 1
    '''
    [des_filename, extname] = os.path.splitext(srcName)
    filename = des_filename + '_' + str(sub) + extname
    print('make file: %s' % filename)
    fout = open(filename, 'w')
    try:
        # fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()


def splitByLineCount(filename, count):
    '''
    Split a file by line count
    :param filename: The file name to split
    :param count: The number of lines to split
    :return: None
    '''
    fin = open(filename, 'r')
    try:
        head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == count:
                sub = mkSubFile(buf, head, filename, sub)
                buf = []
        if len(buf) != 0:
            sub = mkSubFile(buf, head, filename, sub)
    finally:
        fin.close()


# You can modify the MAIN part for you own
if __name__ == '__main__':
    begin = time.time()
    main_file_name = 'YOUR FILE NAME'
    line_number = 2 # The number of lines
    splitByLineCount(main_file_name, line_number)
    end = time.time()
    print('Time elapsed: %.2f s' % (end - begin))
