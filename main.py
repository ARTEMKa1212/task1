from scipy.misc import derivative



def function(x):
    return 3 * x ** 4 - x ** 3 + 10 * x ** 2 - 5 * x - 3


def other_function(a, b, eps):
    first = derivative(function, a, n = 2)
    if (function(b) * first > 0):
        answer = b
    else:
        answer = a
    second = derivative(function, answer, n = 1)
    new_answer = answer - function(answer) / second
    while (abs(new_answer - answer) > eps):
        answer = new_answer
        new_answer = answer - function(answer) / second
    return print(new_answer)
other_function(1,2,0.0001)



def function(x):
    return 3 * x ** 4 - x ** 3 + 10 * x ** 2 - 5 * x - 3


def other_function(a, b, eps):
    if (derivative(function, a, n = 2) * (derivative(function, a, n = 1)) > 0):
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    while (abs(ai - bi)) > eps:
        first = ai - function(ai) * (bi - ai) / (function(bi) - function(ai))
        second = bi - function(bi) / derivative(function, bi, n = 1)
        ai = first
        bi = second
    x = (ai + bi) / 2

    return print(x)
other_function(1,2,0.0001)


