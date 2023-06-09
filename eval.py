import math
import numpy


class constants:
    const_dict = {
        'PI': 3.141592653589793,          # PI
        'E': 2.718281828459045,           # Euler's number
        'PLANCK': 6.62607015*(10**-34),   # Planck constant
        'Ke': 8.9875517923*(10**9),       # Coulomb constant
        'Me': 9.1093837015*(10**-31),     # Electron mass
        'Mp': 1.67262192369*(10**-27),    # Proton mass
        'Mn': 1.67492749804*(10**-27),    # Neutron mass
        'Mu': 1.883531627*(10**-28),      # Muon mass
        'A0': 5.291772086*(10**-11),      # Bohr radius
        'UN': 5.0507837461*(10**-27),     # Nuclear magneton
        'Ub': 9.2740100783*(10**-24),     # Bohr magneton
        'FSC': 7.2973525693*(10**-3),     # Fine-Structure Constant
        'Re': 2.8179403262*(10**-15),     # Classical electron radius
        'CW': 2.42631023867*(10**-12),    # Compton Wavelength
        'yp': 267522209.9,                # Gyromagnetic ratio
        'PCW': 1.321409845*(10**-15),     # Proton Compton Wavelength
        'NCW': 1.319590895*(10**-15),     # Neutron Compton Wavelength
        'G': 6.67430*(10**-11),           # Newtonian constant of gravitation
        'R': 10973731.57,                 # Rydberg constant
        'u': 1.66053906660*(10**-27),     # Atomic mass constant
        'Up': 1.410606662 * (10**-26),    # Proton magnetic moment
        'Ue': -9.2847647043*(10**-24),    # Electron magnetic moment
        'Un': -9.6623641*(10**-27),       # Neutron magnetic  moment
        'Uu': -4.49044786*(10**-26),      # Muon magnetic moment
        'F': 96485.3399,                  # Faraday constant
        'Na': 6.02214179*(10**23),        # Avogadro constant
        'k': 1.3806504*(10**-23),         # Boltzman constant
        'Vm': 0.022413996,                # Molar volume of ideal gas
        'MGC': 8.314472,                  # Molar gas constant
        'C1': 3.74177118*(10**-16),       # First  radiation constant
        'C2': 0.0143887752,               # Second radiation constant
        'S': 5.6704*(10**-8),             # Stefan-Boltzmann constant
        'E0': 8.854187817*(10**-12),      # Electric constant
        'U0': 1.256637061*(10**-6),       # Magnetic constant
        'F0': 2.067833667*(10**-15),      # Magnetic flux quantum
        'g': 9.80665,                     # Standard acceleration of gravity
        'G0': 7.7480917*(10**-5),         # Conductance quantum
        'Z0': 376.7303135,                # Characteristic impedance of vacuum
        't': 273.15,                      # Celsius temperature
        'atm': 101325,                    # Standard atmosphere
        'C': 3*(10**8),                   # Speed of light in vaccum
        'Ec': 1.602176634*(10**-19),      # Charge for Proton and put a negative to be charge of Electorn
    }

    def search(const):
        if const in constants.const_dict.keys():
            return constants.const_dict[const]
        else:
            return numpy.nan


def str_formater(eval_str):
    while True:
        eval_str = eval_str.lower()

        if 'ans' in eval_str:
            eval_str = eval_str.replace('ans', str(constants.ans))
            continue

        if '√(' in eval_str:
            eval_str = eval_str.replace('√(', 'math.sqrt(')
            continue

        if '×' in eval_str:
            eval_str = eval_str.replace('×', '*')
            continue

        if '÷' in eval_str:
            eval_str = eval_str.replace('÷', '/')
            continue

        if '^' in eval_str:
            eval_str = eval_str.replace('^', '**')
            continue

        while '|' in eval_str:
            eval_str = eval_str.replace('|', 'abs(', 1)
            eval_str = eval_str.replace('|', ')', 1)

        if 'log' in eval_str and eval_str[eval_str.find('log')-1] != '.':
            eval_str = eval_str.replace('log(', 'math.log(10, ')
            continue

        if 'e' in eval_str and eval_str[eval_str.find('e')-1] != '.':
            eval_str = eval_str.replace('e', 'math.e')
            continue

        if 'ln' in eval_str:
            eval_str = eval_str.replace('ln(', 'math.log(math.e, ')
            continue

        if 'sin' in eval_str and eval_str[eval_str.find('sin')-1] != 'a' and eval_str[eval_str.find('sin')-1] != '.' and eval_str[eval_str.find('sin')+3] != 'h':
            print('sin')
            eval_str = eval_str.replace('sin', 'math.sin')
            continue

        if 'cos' in eval_str and eval_str[eval_str.find('cos')-1] != 'a' and eval_str[eval_str.find('cos')-1] != '.' and eval_str[eval_str.find('cos')+3] != 'h':
            print('cos')
            eval_str = eval_str.replace('cos', 'math.cos')
            continue

        if 'tan' in eval_str and eval_str[eval_str.find('tan')-1] != 'a' and eval_str[eval_str.find('tan')-1] != '.' and eval_str[eval_str.find('tan')+3] != 'h':
            print('tan')
            eval_str = eval_str.replace('tan', 'math.tan')
            continue

        if 'asin' in eval_str and eval_str[eval_str.find('asin')+4] != 'h' and eval_str[eval_str.find('asin')-1] != '.':
            print('asin')
            eval_str = eval_str.replace('asin', 'math.asin')
            continue

        if 'acos' in eval_str and eval_str[eval_str.find('acos')+4] != 'h' and eval_str[eval_str.find('acos')-1] != '.':
            print('acos')
            eval_str = eval_str.replace('acos', 'math.acos')
            continue

        if 'atan' in eval_str and eval_str[eval_str.find('atan')+4] != 'h' and eval_str[eval_str.find('atan')-1] != '.':
            print('atan')
            eval_str = eval_str.replace('atan', 'math.atan')
            continue

        if 'sinh' in eval_str and eval_str[eval_str.find('sinh')-1] != 'a' and eval_str[eval_str.find('sinh')-1] != '.':
            print('sinh')
            eval_str = eval_str.replace('sinh', 'math.sinh')
            continue

        if 'cosh' in eval_str and eval_str[eval_str.find('cosh')-1] != 'a' and eval_str[eval_str.find('cosh')-1] != '.':
            print('cosh')
            eval_str = eval_str.replace('cosh', 'math.cosh')
            continue

        if 'tanh' in eval_str and eval_str[eval_str.find('tanh')-1] != 'a' and eval_str[eval_str.find('tanh')-1] != '.':
            print('tanh')
            eval_str = eval_str.replace('tanh', 'math.tanh')
            continue

        if 'asinh' in eval_str and eval_str[eval_str.find('asinh')-1] != '.':
            print('asinh')
            eval_str = eval_str.replace('asinh', 'math.asinh')
            continue

        if 'acosh' in eval_str and eval_str[eval_str.find('acosh')-1] != '.':
            print('acosh')
            eval_str = eval_str.replace('acosh', 'math.acosh')
            continue

        if 'atanh' in eval_str and eval_str[eval_str.find('atanh')-1] != '.':
            print('atanh')
            eval_str = eval_str.replace('atanh', 'math.atanh')
            continue

        if 'factorial(' in eval_str and eval_str[eval_str.find('factorial')-1] != '.':
            eval_str = eval_str.replace('factorial(', 'math.factorial(')
            continue

        if '!' in eval_str:
            index = eval_str.find('!')
            while eval_str[index] not in ['+', '-', '*', '/'] and index != 0:
                index -= 1

            if index == 0:
                eval_str = str(math.factorial(int(eval_str[0:eval_str.find('!')]))) + eval_str[eval_str.find('!')+1:]
                continue
            else:
                eval_str = eval_str[:index+1] + str(math.factorial(int(eval_str[index+1:eval_str.find('!')]))) + eval_str[eval_str.find('!')+1:]
                continue

        if 'π' in eval_str:
            eval_str = eval_str.replace('π', 'math.pi')
            continue
        break
    return eval_str


def runner(input_str):
    return eval(str_formater(input_str))


if __name__ == "__main__":
    print('π = ', runner('π'))
    print(runner('4!+4-8*9.3'))
