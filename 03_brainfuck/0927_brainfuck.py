#import doctest
#from tkinter import N

tape_length = 200




def input_spc():
    lst_ptr = ""
    lst_str = input()
    for i in lst_str:
        if i != ' ':
            lst_ptr+=i

    global length
    length = lst_ptr
    return lst_ptr


def process(lst_ptr, start_num , end_point):
    lst_mmr = [0 for _ in range(tape_length)]
    pivot = 0
    """
    >>> process("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.")
    'A'
    >>> process("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.")
    'HI'
    >>> process("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++++++++++++++.------------.<<+++++++++++++++.>.+++.------.--------.>+.")
    'Hello, world!'
    """
    #print("process", start_num, end_point)

    rev_point = 0
    i = 0
    str_print = ""
    while True:
        #print(str_print)
        if i>= length:
            break
        #print(i, lst_mmr)
        if lst_ptr[i] == '+':
            #print(lst)
            lst_mmr[pivot] += 1
        if lst_ptr[i] == '-':
            lst_mmr[pivot] -= 1
        if lst_ptr[i] =='>':
            pivot +=1
        if lst_ptr[i] =='<':
            pivot -=1
        if lst_ptr[i] == '.':
            str_print += chr(lst_mmr[pivot])
            #print(str_print)
        if lst_ptr[i] == '[':
            rev_point = i
        if lst_ptr[i] == ']':
            if lst_mmr[pivot] == 0:
                pass
            else:
                i = rev_point
        i+=1
    return str_print

#lst_ptr = input_spc()
lst_ptr = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++++++++++++++.------------.<<+++++++++++++++.>.+++.------.--------.>+."
#lst_ptr = "++++++++++[>]"
length = len(lst_ptr)
print(process(lst_ptr, 0, length))
