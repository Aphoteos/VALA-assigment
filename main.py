from scripts import prima_factor_ui, prime_factor
import sys

def main():
    if len(sys.argv) == 2:
        number = sys.argv[1]
        prime_factor.command_line_prime_factors(number)
    elif len(sys.argv) == 1:
        prima_factor_ui.main()
    else:
        print('Give only one argument if you want to run this on commandline. ' + \
              'If you want UI, run without any arguments')

if __name__ == '__main__':
    main()