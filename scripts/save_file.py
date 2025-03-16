def save_to_ouput_file(number, factors, time):
    text = f'Prime factors of number {number} are \n{','.join(map(str,factors))} \n' + \
            'It took {time} seconds to find those.'

    try:
        with open(f'Factors_{number}.txt', 'w', newline='') as file:
            file.write(text)
    except Exception as e:
        print(f'Error: {e}')