dictOpr = {
    '+': ' Plus ',
    '-': ' Minus ',
    '*': ' Times ',
    '/': ' Divided By ',
    '**': ' To The Power Of ',
    '=': ' Equals ',
    '!=': ' Does Not Equal ',
    }
dict = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '10': 'Ten',
    }


def expression_out(exp):
    exp = exp.split()
    return (dict.get(exp[0]) + dictOpr.get(exp[1], 'x')
            + dict.get(exp[2]) if dictOpr.get(exp[1], 'x') != 'x'
             else "That's not an operator!")