"""
Convert csv file to arff file.
"""
import pandas as pd
import sys
import os


def print_help():
    """
    Print the help message.
    """
    print("""
Usage
======
    python pandas_to_arff.py input-file output-file
    """)


def main(argv):
    """
    The main entrance of the program.

    Parameters
    ----------
    argv: list of str
        The program arguments. The length of argv must be 3.
        The first is the programme, the second and the third arguments are
        input file path and output path respectively.

    Returns
    -------
    None
    """
    if len(argv) != 3:
        print_help()
        return
    input_file = argv[1]
    input_filename = os.path.basename(input_file)
    output_file = argv[2]
    output_filename = os.path.basename(output_file)
    if str(input_filename.split('.')[1]) != 'csv' or str(output_filename.split('.')[1]) != 'arff':
        raise NameError('The extension name of file is wrong!')

    input_csv_file = pd.read_csv(input_file)
    with open(output_file, 'w+') as f:
        relation_name = str(input_filename.split('.')[0])
        f.write('@relation ' + '\'' + relation_name + '\'\n')

        for column in input_csv_file.columns:
            type_name = str(input_csv_file[column].dtype)
            if type_name == 'int64':
                unique_value_list = pd.unique(input_csv_file[column]).tolist()
                if len(unique_value_list) == 2 and unique_value_list[0] == 0 and unique_value_list[1] == 1:
                    f.write('@attribute ' + '\'' + column + '\' ' + '{\'0\', \'1\'}\n')
                else:
                    f.write('@attribute ' + '\'' + column + '\' ' + 'real\n')
            elif type_name == 'float64':
                f.write('@attribute ' + '\'' + column + '\' ' + 'real\n')
            elif type_name == 'object':
                unique_value_list = pd.unique(input_csv_file[column]).tolist()
                str_list = '{' + ','.join(['\'' + i + '\'' for i in unique_value_list]) + '}'
                f.write('@attribute ' + '\'' + column + '\' ' + str_list + '\n')
            else:
                raise ValueError(f'Unknown data type: {type_name} at column {column}')

        f.write('@data\n')
        for index, row in input_csv_file.iterrows():
            row = row.tolist()
            row = list(map(str, row))
            f.write(','.join(row) + '\n')


if __name__ == '__main__':
    try:
        main(sys.argv)
    except ValueError as e:
        print(e)
    except NameError as e:
        print(e)
