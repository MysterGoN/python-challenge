# Start page: http://www.pythonchallenge.com/pc/return/bull.html

def sequence(max_lvl: int, number: int = 1, lvl: int = 0) -> int:
    """

    example: 
        [1, 11, 21, 1211, 111221, ...

    """
    if lvl == max_lvl:
        return number
    
    prev = ''
    count = 0
    res = ''
    for digit in str(number):
        if prev != '' and prev != digit:
            res += f'{count}{prev}'
            count = 0
        count += 1
        prev = digit

    res += f'{count}{prev}'
    number = int(res)

    return sequence(max_lvl, number, lvl+1)


print(len(str(sequence(30))))
