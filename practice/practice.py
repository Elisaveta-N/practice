# https://github.com/Elisaveta-N/test.git
# Task 1.1
from ast import Lambda
import math 


def func1(x, z, y):
    n = len(x)
    sum = 0
    y = [0] + y
    z = [0] + z
    x = [0] + x
    for i in range(1, n+1):
        a = 47*z[i]
        b = 4 * math.pow(y[n + 1 - math.ceil(i/2)], 2)
        c = math.pow(x[n + 1 - math.ceil(i/2)], 3) / 48
        sum += pow(a - b - c, 2)
    print(sum)

func1([-0.56, -0.55, -0.01, 0.43, 0.76, -0.94],
[0.08, -0.23, -0.26, 0.49, 0.97, 0.19],
[0.66, -0.63, -0.19, 0.27, -0.7, -0.66])

# Task 2.1
def func1960(x, f, m, l):
    if x[2] == 1960:
        return f
    if x[2] == 2003:
        return m
    return l

def func1988(x, f, m, l):
    if x[3] == 1988:
        return f
    if x[3] == 1977:
        return m
    return l

def func1969(x, f, l):
    if x[0] == 1969:
        return f
    return l

def func2(x):
    if x[1] == 2014:
        return func1960(x, func1988(x, 0, 1, 2), func1969(x, 3, 4), 5)
    if x[1] == 2007:
        return 6
    return func1960(x, func1960(x, 7, func1988(8, 9, 10), 11))

print(func2([1969, 2007, 1960, 1988]))

# Task 3.1
def func3(x):
    i = int(x)
    c1 = 0b1111111 & i
    c2 = 0b1111111111 & (i>>7)
    c3 = 0b11 & (i>>17)
    c4 = 0b111111111 & i>>27
    return str(c1), str(c2), str(c3), str(c4)

print(func3('51593330143'))

# Task 4.1
import re


def func4(str):
    pat1 = r'q\(\w+\)'
    res1 = re.findall(pat1, str)
    i = 0
    for val in res1:
        res1[i] = val[2:-1]
        i+=1
    pat2 = r'\|.\w+;'
    res2 = re.findall(pat2, str)
    i = 0
    for val in res2:
        res2[i] = val[1:-1]
        if res2[i][0] == ' ':
            res2[i] = res2[i][1:]
        i+=1
    res = {}
    for i in range(0, len(res1)):
        res[res1[i]] = res2[i]   
    print(res)
    
func4('<block> {let q(arlaso) <|-8318; } {let q(xeon) <|-5427;} { letq(ondi_649) <| 327; } \
{ let q(cere) <| 6908;}</block>')


# Task 4.2
def func5(str):
    pat1 = r'loc \w+ ?<'
    res1 = re.findall(pat1, str)
    i = 0
    for val in res1:
        res1[i] = val[4:-1]
        if res1[i][-1] == ' ':
            res1[i] = res1[i][:-1]
        i+=1

    pat2 = r'\| \w+ ?<'
    res2 = re.findall(pat2, str)
    i = 0
    for val in res2:
        res2[i] = val[2:-1]
        if res2[i][-1] == ' ':
            res2[i] = res2[i][:-1]
        i+=1

    res = list(zip(res1, res2))
    print(res)

func5('<data> loc sore <| quon_555</data>,<data> loc erinla <| aenenge \
</data>, <data> loc enonve<| lemaa </data>,<data> loc vema_813 <| \
angeor </data>,')

# Task 5.1
class MealyError(Exception):
    pass

class StateMachine:
    def __init__(self):
        self.state = 'A'

    def spin(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'E'
            return 3
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 6
        raise MealyError('spin')

    def punch(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'E':
            self.state = 'A'
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 9 
        raise MealyError('punch')

    def stand(self):
        if self.state == 'B':
            self.state = 'G'
            return 2 
        if self.state == 'E':
            self.state = 'G'
            return 8

def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None

def test():
    o = main()
    assert o.spin() == 0
    assert o.punch() == 1
    assert o.spin() == 4
    assert o.spin() == 5
    assert o.punch() == 7
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.spin() == 6
    assert o.punch() == 9

    o = main()
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.stand() == 8

    o = main()
    assert o.spin() == 0
    assert o.stand() == 2

    raises(lambda: o.spin, MealyError)
    raises(lambda: o.stand, MealyError)
    raises(lambda: o.punch, MealyError)

test()