def convert_temperature(dst, val, src='C'):
    if src == dst:
        return val
    if src != 'C' and dst != 'C':
        auxiliary_value = convert_temperature('C', val, src)
        return convert_temperature(dst, auxiliary_value, 'C')

    if dst == 'C':
        match src:
            case 'F':
                return (val - 32) * 5/9
            case 'K':
                return val - 273
    elif src == 'C':
        match dst:
            case 'F':
                return (val * 9/5) + 32
            case 'K':
                return val + 273
    else:
        raise ValueError("Błąd" + src)


print(convert_temperature('F',30,'K'))

