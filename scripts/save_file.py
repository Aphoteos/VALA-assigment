def save_to_ouput_file(number, factors, time):
    '''Save result to output file. File name is Factors_<number>'''
    file_path = f'Factors_{number}.txt'
    text = f'Prime factors of number {number} are \n{','.join(map(str,factors))} \n' + \
           f'It took {time} seconds to find those.'

    try:
        with open(file_path, 'w', newline='') as file:
            file.write(text)
    except Exception as e:
        print(f'Error: {e}')

    return file_path