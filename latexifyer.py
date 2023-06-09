import matplotlib.pyplot as plt
import sympy


def into_latex(lat_str):
    def mul():
        return "\\times "

    def pow(base='□', pow='□'):
        return "replaceable_base^{replaceable_pow}".replace("replaceable_base", base).replace("replaceable_pow", pow)

    def sqrt(base='□'):
        return "\\sqrt{replaceable_sqrt}".replace("replaceable_sqrt", base)

    def root(base='□', root='□'):
        return "\\sqrt[replaceable_root]{replaceable_base}".replace("replaceable_root", root).replace("replaceable_base", base)

    def intigration(func='□'):
        return "\\int replaceable_func".replace("replaceable_func", func)

    def numerical_intigration(s='□', e='□', func='□'):
        return "\\int_replaceable_s^replaceable_e replaceable_func".replace("replaceable_s", s).replace("replaceable_e", e).replace("replaceable_func", func)

    def sum(s='□', e='□', func='□'):
        return "\\sum_replaceable_s^replaceable_e replaceable_func".replace("replaceable_s", s).replace("replaceable_e", e).replace("replaceable_func", func)

    def POS(s='□', e='□', func='□'):
        return "\\prod_replaceable_s^replaceable_e replaceable_func".replace("replaceable_s", s).replace("replaceable_e", e).replace("replaceable_func", func)

    def o_intigration(s='□', e='', func='□'):
        return "\\oint_replaceable_s^replaceable_e replaceable_func".replace("replaceable_s", s).replace("replaceable_e", e).replace("replaceable_func", func)

    def fraction(n='□', d='□'):
        return "\\frac{replaceable_n}{replaceable_d}".replace("replaceable_n", n).replace("replaceable_d", d)

    while True:
        if '*' in lat_str:
            lat_str = lat_str.replace('*', mul())
            continue

        if 'pow' in lat_str and lat_str.find('pow') == 0 or lat_str[lat_str.find('pow')-1] in ['*', '×', '÷', '+', '-']\
                or lat_str[lat_str.find('pow')-7:lat_str.find('pow')] == mul():
            lat_str = lat_str.replace('pow', pow(), 1)
            continue

        if 'sqrt' in lat_str and lat_str.find('sqrt') == 0 or lat_str[lat_str.find('sqrt')-1] in ['*', '×', '÷', '+', '-']\
                or lat_str[lat_str.find('sqrt')-7:lat_str.find('sqrt')] == mul():
            lat_str = lat_str.replace('sqrt', sqrt(), 1)
            continue

        if 'root' in lat_str and lat_str.find('root') == 0 or lat_str[lat_str.find('root')-1] in ['*', '×', '÷', '+', '-']\
                or lat_str[lat_str.find('root')-7:lat_str.find('root')] == mul():
            lat_str = lat_str.replace('root', root(), 1)
            continue

        if 'numerical_intigration' in lat_str and lat_str.find('numerical_intigration') == 0\
            or lat_str[lat_str.find('numerical_intigration')-1] in ['*', '×', '÷', '+', '-']\
                or lat_str[lat_str.find('numerical_intigration')-7:lat_str.find('numerical_intigration')] == mul():
            lat_str = lat_str.replace('numerical_intigration', numerical_intigration(), 1)
            continue

        if 'o_intigration' in lat_str and lat_str.find('o_intigration') == 0 or lat_str[lat_str.find('o_intigration')-1] in ['*', '×', '÷', '+', '-']\
                or lat_str[lat_str.find('o_intigration')-7:lat_str.find('o_intigration')] == mul():
            lat_str = lat_str.replace('o_intigration', o_intigration(), 1)
            continue

        if 'intigration' in lat_str and lat_str[lat_str.find('intigration')-1] != '_'\
            and lat_str.find('intigration') == 0 or lat_str[lat_str.find('intigration')-1] in ['*', '×', '÷', '+', '-']\
                or lat_str[lat_str.find('intigration')-7:lat_str.find('intigration')] == mul():
            print(lat_str[lat_str.find('intigration')-1])
            lat_str = lat_str.replace('intigration', intigration(), 1)
            continue

        if 'sum' in lat_str and lat_str.find('sum') == 0 or lat_str[lat_str.find('sum')-1] in ['*', '×', '÷', '+', '-']\
                or lat_str[lat_str.find('sum')-7:lat_str.find('sum')] == mul():
            lat_str = lat_str.replace('sum', sum(), 1)
            continue

        if 'pos' in lat_str and lat_str.find('pos') == 0 or lat_str[lat_str.find('pos')-1] in ['*', '×', '÷', '+', '-']\
                or lat_str[lat_str.find('pos')-7:lat_str.find('pos')] == mul():
            lat_str = lat_str.replace('pos', POS(), 1)
            continue

        if 'fraction' in lat_str and lat_str.find('fraction') == 0 or lat_str[lat_str.find('fraction')-1] in ['*', '×', '÷', '+', '-']\
                or lat_str[lat_str.find('fraction')-7:lat_str.find('fraction')] == mul():
            lat_str = lat_str.replace('fraction', fraction(), 1)
            continue
        break
    return lat_str


if __name__ == "__main__":
    ax = plt.axes([0.1, 0.1, 1, 1])  # left,bottom,width,height
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    print(into_latex("pow+intigration-fraction*numerical_intigration"))
    plt.text(0, 0, '$%s$' % into_latex("pow+intigration-fraction*numerical_intigration"), size=30, color='black')
    plt.show()
