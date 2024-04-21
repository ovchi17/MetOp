e = 0.0005
alpha = 0.05

X = 0
Y = 0
Z = 0
while True:
    functionResult = X**2 + Y**2 + Z**2 + 12 * X * Y + 2 * Z
    pX = 2 * X + 12 * Y
    pY = 2 * Y + 12 * X
    pZ = 2 * Z + 2
    XOne = X - alpha * pX
    YOne = Y - alpha * pY
    ZOne = Z - alpha * pZ
    newFunctionResult = XOne**2 + YOne**2 + ZOne**2 + 12 * XOne * YOne + 2 * ZOne
    if abs(newFunctionResult - functionResult) <= e:
        print(XOne, YOne, ZOne)
        print(newFunctionResult)
        break
    else:
        X = XOne
        Y = YOne
        Z = ZOne