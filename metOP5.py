e = 0.0001
x1 = 1.25
deltaX = 0.01
x3 = 0
xMin = 0
fl = 0

while 1:
    if fl == 0:
        x2 = x1 + deltaX
        f1 = 1/7 * x1**7 - x1**3 + 0.5 * x1**2 - x1
        f2 = 1/7 * x2**7 - x2**3 + 0.5 * x2**2 - x2
        if f1 > f2:
            x3 = x1 + 2 * deltaX 
        else:    
            x3 = x1 - deltaX
        f3 = 1/7 * x3**7 - x3**3 + 0.5 * x3**2 - x3
    
    minF = min(f1, f2, f3)
    if minF == f1:
        xMin = x1
    elif minF == f2:
        xMin = x2
    elif minF == f3:
        xMin = x3
    if ((x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3) == 0:
        x1 = xMin
        fl = 0
    else:
        lineX = 0.5 * ((x2**2 - x3**2) * f1 + (x3**2 - x1**2) * f2 + (x1**2 - x2**2) * f3) / ((x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3)
        lineF = 1/7 * lineX**7 - lineX**3 + 0.5 * lineX**2 - lineX
        if (abs((minF - lineF) / lineF) < e):
            check1 = True
        else:
            check1 = False
        if(abs((xMin - lineX) / lineX) < e):
            check2 = True
        else:
            check2 = False
        if check1 == True and check2 == True:
            print(lineX)
            break
        elif (check1 == False or check2 == False) and x1 <= lineX and lineX <= x3:
            if (x1 <= lineX and lineX <= x2):
                x1 = x1
                x2 = x2 = min(xMin, lineX)
                x3 = x2
            else:
                x1 = x2 
                x2 = min(xMin, lineX)
                x3 = x3
            fl = 1
        else:
            x1 = lineX
            fl = 0