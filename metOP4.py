from sympy import symbols, diff

a = 1
b = 1.5
e = 0.05
counter = 1

x = symbols('x')
skelet = 1/7 * x**7 - x**3 + 0.5 * x**2 - x
fun1 = diff(skelet, x)
fun2 = diff(fun1, x)
el = (a + b) / 2
while True:
    print("ШАГ №" + str(counter))
    print(fun1.subs(x, el))
    print(fun2.subs(x, el))
    if abs(fun1.subs(x, el)) > e:
        el = el - fun1.subs(x, el) / fun2.subs(x, el)
        counter += 1
    else:
        break
    print(el)
print(el)
print(1/7 * el**7 - el**3 + 0.5 * el**2 - el)
print(counter)
