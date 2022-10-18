"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""


import rhinoscriptsyntax as rs
import ghpythonlib.components as comp
AllList = []
a = []
b= []
po = comp.ConstructPoint(100,200,0)
col = 180/x
print(y)
lth = 0
bbq = 1
for i in range(x):
    tran = comp.VectorXYZ(0,5*i,0)[0]
    """
    tran = comp.Rotate(tran,comp.Radians(col*i),rs.WorldXYPlane())[0]
    """
    ca = comp.Move(po,tran)[0]
    a.append(ca)
    
for p in y:
    for l in range(len(p)-1):
        lst = [p[l],p[l+1]]
        life = True
        for s in AllList:
            if s[0] == lst[0] and s[1] == lst[1]:
                life = False
        if life == True:
            AllList.append(lst)
            li = comp.Line(a[int(p[l])],a[int(p[l+1])])
            midp = comp.CurveMiddle(li)
            midp = comp.Move(midp,comp.VectorXYZ(lth*bbq,0,0)[0])[0]
            b.append(comp.NurbsCurve([a[int(p[l])],midp,a[int(p[l+1])]],2,False)[0])
            lth += 1.5  
            bbq *= -1

for l in AllList:
    print(l)
