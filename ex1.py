def task(array):
    if not array:
        return('Empty string. Please, enter the string')
    index = array.find('0')
    if index == -1:
        return('There is no "0" in the string')
    else:
        return(index)

print(task("111111111110000000000000000"))