
def custom_write(file_name: str, strings:list):
    string_positions = {}
    line_number = 1
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        line_byte = file.tell()
        file.write(f'{string}\n')
        string_positions[(line_number, line_byte)]= string
        line_number += 1
    file.close()
    return string_positions

if __name__=='__main__':
    info = [

        'Text for tell.','\n'

        'Используйте кодировку utf-8.','\n'

        'Because there are 2 languages!','\n'

        'Спасибо!''\n'

    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
