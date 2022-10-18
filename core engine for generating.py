import rhinoscriptsyntax as rs
import ghpythonlib.components as comp
import scriptcontext as sc
import math
max1F = 8
count1F = 0
ssaa = []
XS = []
a = []
b = []
c = []
e = []
h = []
AreaList = []
st1 = []
nd2 = []
rd3 = []
th4 = []
th5 = []
body = []
poly = []
blocks = []
Allstairs = []
finished = []
core = []
Well = []
potentialRoute = []
pointAvaiable = []
pointAvaiableForUp = []
walls = []
transportationList = []
shareSpaces = []
degenerateSpaces = []
cols = []
blockRemain = []

class pPoint():
    def __init__(self,iD,whichside,point3D):
        self.ID = iD
        self.ax = whichside
        self.point = point3D

class block():
    
    def __init__(self,l,w,h,ang0,ang1,ang2,ang3,Tlength1,Tlength2,Tlength3,Tlength4):
        
        self.center = [0,0,0]
        self.layer = 0
        self.ID = 0
        self.formerP = 0
        self.length = l
        self.width = w
        self.height = h
        self.allBody = []
        self.stairs = []
        self.rect = rs.coercecurve(rs.AddRectangle(self.center,self.length,self.width))
        self.end = []
        self.tanangles = []
        self.endPoint = []
        self.connectionMode = []
        self.connectionWhich = []
        edgesof = comp.Explode(self.rect,True)[0]
        verticesof = comp.Explode(self.rect,True)[1]
        mid1 = comp.CurveMiddle(edgesof[1])
        mid2 = comp.CurveMiddle(edgesof[3])
        tentacle0 = comp.Line(mid1,verticesof[1])
        tentacle1 = comp.Line(mid1,verticesof[2])
        tentacle2 = comp.Line(mid2,verticesof[0])
        tentacle3 = comp.Line(mid2,verticesof[3])

        rs.RotateObject(tentacle0,mid1,ang0)
        rs.RotateObject(tentacle1,mid1,-1*ang1)
        rs.RotateObject(tentacle2,mid2,-1*ang2)
        rs.RotateObject(tentacle3,mid2,ang3)

        self.minLength0 = 1 /math.cos(comp.Radians(ang0))
        self.minLength1 = 1 /math.cos(comp.Radians(ang1))
        self.minLength2 = 1 /math.cos(comp.Radians(ang2))
        self.minLength3 = 1 /math.cos(comp.Radians(ang3))
        rs.ScaleObject(tentacle0,mid1,(Tlength1*self.minLength0,Tlength1*self.minLength0,Tlength1*self.minLength0))
        rs.ScaleObject(tentacle1,mid1,(Tlength2*self.minLength1,Tlength2*self.minLength1,Tlength2*self.minLength1))
        rs.ScaleObject(tentacle2,mid2,(Tlength3*self.minLength2,Tlength3*self.minLength2,Tlength3*self.minLength2))
        rs.ScaleObject(tentacle3,mid2,(Tlength4*self.minLength3,Tlength4*self.minLength3,Tlength4*self.minLength3))
        
        endPoint0 = comp.EndPoints(tentacle0)[1]
        endPoint1 = comp.EndPoints(tentacle1)[1]
        endPoint2 = comp.EndPoints(tentacle2)[1]
        endPoint3 = comp.EndPoints(tentacle3)[1]

        self.tanangles.append(tentacle0)
        self.tanangles.append(tentacle1)
        self.tanangles.append(tentacle2)
        self.tanangles.append(tentacle3)
        self.endPoint.append(endPoint0)
        self.endPoint.append(endPoint1)
        self.endPoint.append(endPoint2)
        self.endPoint.append(endPoint3)
        self.rotateAng = 0
    def show(self):
        self.sf = comp.BoundarySurfaces(self.rect)
        self.bre = comp.Extrude(self.sf,rs.VectorCreate((0,0,0),(0,0,-1*self.height)))

for i in range(len(x)):
    p = block(x[i],y[i],z[i],tanangle[i*4+0],tanangle[i*4+1],tanangle[i*4+2],tanangle[i*4+3],tanlength[i*4+0],tanlength[i*4+1],tanlength[i*4+2],tanlength[i*4+3])
    blocks.append(p)

t= 0 
k =0
m = 0
rot = 0
count = 0
angacc = 0

bd = comp.Rectangle(rs.WorldXYPlane(),fieldX,fieldY,0)[0]


for it in range(iter):
    blk = blocks[it]
    relife = True
    
    while relife == True:
   
        blk.ID = count
        """transform to be adjcent"""
        
        if count > 0:
            minHeight = 2
            pavList = []
            minHeightPoints = []
            ddd = 0
            for kk in pointAvaiable:
                if ddd == 0:
                    minHeight = kk.point[2]
                else:
                    if kk.point[2] < minHeight:
                        minHeight = kk.point[2]
                ddd = 1
            for kk in pointAvaiable:
                if  kk.point[2] == minHeight:
                    minHeightPoints.append(kk)
            pptA = minHeightPoints[0]
            blk.formerP = pptA.ax
            list.remove(pointAvaiable,pptA)
            vec = rs.VectorCreate(pptA.point,blk.endPoint[2])
            for l in blk.tanangles:
                rs.MoveObject(l,vec)
            for l in blk.endPoint:
                rs.MoveObject(l,vec)
            rs.MoveObject(blk.rect,vec)
            
        if count == 0:
            vec = rs.VectorCreate([fieldX/2,fieldY/20,0],[0,0,0])
            for l in blk.tanangles:
                rs.MoveObject(l,vec)
            for l in blk.endPoint:
                rs.MoveObject(l,vec)
            rs.MoveObject(blk.rect,vec)
        """transform to be adjcent"""
        
        
        """judge the direction to bend"""
        idd = 0
        axx = 0
    
        if len(pointAvaiable) > 0:
            allObj = []
            allObj.append(blk.rect)
            for l in blk.tanangles:
                allObj.append(l)
            for l in blk.endPoint:
                allObj.append(l)
            idd = pptA.ID
            axx = pptA.ax
            P1 = comp.EndPoints(finished[pptA.ID].tanangles[pptA.ax])[0]
            P2 = comp.EndPoints(finished[pptA.ID].tanangles[pptA.ax])[1]
            P3 = comp.EndPoints(blk.tanangles[2])[0]
            vecT1 =rs.VectorCreate(P2,P1)
            vect2 =rs.VectorCreate(P3,P2)
            angD = comp.Angle(vecT1,vect2,rs.WorldXYPlane())[0]
            angDe = comp.Degrees(angD)
            rs.RotateObjects(allObj,blk.endPoint[2],-1*angDe)
            
        """judge the direction to bend"""
    
        """move to upstairs"""
        listforIter = range(len(finished))
        ZFinal = 0 
        relife = False

        zMax = 0
        
        for i in listforIter:
            life = True
            st = comp.Area(blk.rect)[1][2] - comp.Area(finished[i].rect)[1][2]
            if st<0:
                st = 0
            if st< z[i] and st >= 0 :
                coreFort = comp.Move(core[i],comp.VectorXYZ(0,0,st)[0])[0]
            for tant in finished[i].tanangles:
                if comp.CurveXCurve(tant,blk.rect)[0] != None:
                    life = False
            if(comp.CurveXCurve(blk.rect,coreFort)[0] != None) or life == False:
                if zMax < z[i]-st:
                    zMax = z[i]-st
                
        if zMax != 0:
            ZFinal += zMax
            rs.MoveObject(blk.rect,[0,0,zMax])
            for l in blk.tanangles:
                rs.MoveObject(l,[0,0,zMax])
            for l in blk.endPoint:
                rs.MoveObject(l,[0,0,zMax])
            vsct = comp.VectorXYZ(0,0,-1*zMax/2)[0]
                
                
        """detect whether to rebuild"""
        life2 = True
        for i in listforIter:
            st = comp.Area(blk.rect)[1][2] - comp.Area(finished[i].rect)[1][2]
            if st<0:
                st = 0
            if st< z[i] and st >= 0 :
                coreFort = comp.Move(core[i],comp.VectorXYZ(0,0,st)[0])[0]
            for tant in finished[i].tanangles:
                if comp.CurveXCurve(tant,blk.rect)[0] != None:
                    life2 = False
            if(comp.CurveXCurve(blk.rect,coreFort)[0] != None) or life2 == False:
                relife = True
                break
        OutP = 0
        for i in blk.endPoint:
            if comp.PointInCurve(i,bd)[0] == 0:
                OutP += 1
        if OutP > 2:
            relife = True

        if relife == False and count > 0:
            finished[pptA.ID].connectionWhich.append(count)
            finished[pptA.ID].connectionMode.append(pptA.ax)
        if ZFinal != 0 and relife == False:
            finished[idd].stairs.append(rs.AddLine(comp.EndPoints(blk.tanangles[2])[0],comp.EndPoints(finished[idd].tanangles[axx])[0]))

        if relife == True:
            print(count)
    """move to upstairs"""
    if blk.endPoint[0][2] == 0:
        count1F += 1


    core.append(blk.rect)


    for i in range(4):
        if i != 2:
            live = True
            if len(finished) != 0:
                for nbs in finished:
                    if comp.PointInCurve(blk.endPoint[i],nbs.rect)[0] ==2 and blk.endPoint[i][2] == comp.Area(nbs.rect)[1][2]:
                        live = False
            
            if comp.PointInCurve(blk.endPoint[i],bd)[0] == 2 and comp.CurveClosestPoint(blk.endPoint[i],bd)[2] >5 and live == True:
                pointAvaiable.append(pPoint(count,i,blk.endPoint[i]))
    if count1F >max1F:
        for kkk in pointAvaiable:
            if kkk.point[2] == 0:
                pointAvaiable.remove(kkk)
    """
    for ppp in pointAvaiable:
    """

    count += 1
    finished.append(blk)


"""layer ratio"""
for i in range(5):
    AreaList.append([0,0,0])
for bl in finished:
    
    if comp.Deconstruct(bl.endPoint[0])[2] == 0:
        bl.layer = 1
        AreaList[0][0] += comp.Area(bl.rect)[0]
    if comp.Deconstruct(bl.endPoint[0])[2] == 4:
        bl.layer = 2
        AreaList[1][0] += comp.Area(bl.rect)[0]
    if comp.Deconstruct(bl.endPoint[0])[2] == 8:
        bl.layer = 3
        AreaList[2][0] += comp.Area(bl.rect)[0]
    if comp.Deconstruct(bl.endPoint[0])[2] == 12:
        bl.layer = 4
        AreaList[3][0] += comp.Area(bl.rect)[0]
    if comp.Deconstruct(bl.endPoint[0])[2] == 16:
        bl.layer = 5
        AreaList[4][0] += comp.Area(bl.rect)[0]


"""layer ratio"""



"""detect the routes"""

if ifDetectRoutes == True:
    transportationList.append([0])
    
    for bl in finished:
        if bl.connectionWhich != None and len(bl.connectionWhich) > 0:
            for listn in transportationList:
                if listn != None:
                    if listn[len(listn)-1] == bl.ID:
                        list2 = [i for i in listn]
                        list3 = [i for i in listn]
                        listn.append(bl.connectionWhich[0])
                        if(len(bl.connectionWhich) >=2 ):
                             list2.append(bl.connectionWhich[1])
                             transportationList.append(list2)
                        if(len(bl.connectionWhich) >=3 ):
                             list3.append(bl.connectionWhich[2])
                             transportationList.append(list3)
                             
    for k in transportationList:
        ssaa.append (k)
        print(k)

"""detect the routes"""

"""degenerate"""

"""degenerate"""
if ifTransform == True:
    
    """detect the connection"""
    for bl in finished:
        if 0 == 0:
            IST = False
            TW = 0
            ISZ = False
            ZW = 0
            ISO = False
            OW = 0
            contl = 0
            for numb in bl.connectionMode:
                
                if numb == 3:
                    IST = True
                    TW = contl
                if numb == 0:
                    ISZ = True
                    ZW = contl
                if numb == 1:
                    ISO = True
                    OW = contl
                contl += 1
                ifSameH = False
            pps = comp.Explode(bl.rect,True)[1]
            
            if ISZ == False :
                bl.endPoint[0] = pps[1]
                bl.tanangles[0] = comp.Line(comp.EndPoints(bl.tanangles[0])[0], pps[1])
            if ISO == False :
                bl.endPoint[1] = pps[2]
                bl.tanangles[1] = comp.Line(comp.EndPoints(bl.tanangles[1])[0], pps[2])
            if IST == False :
                bl.endPoint[3] = pps[3]
                bl.tanangles[3] = comp.Line(comp.EndPoints(bl.tanangles[3])[0], pps[3])
               
                
    for bl in finished:
        if 0 == 0:
            IST = False
            TW = 0
            ISZ = False
            ZW = 0
            ISO = False
            OW = 0
            contl = 0
            for numb in bl.connectionMode:
                
                if numb == 3:
                    IST = True
                    TW = contl
                if numb == 0:
                    ISZ = True
                    ZW = contl
                if numb == 1:
                    ISO = True
                    OW = contl
                contl += 1
                ifSameH = False

            if IST == True :
                heightX = comp.Deconstruct(blocks[bl.connectionWhich[TW]].endPoint[0])[2]-comp.Deconstruct(bl.endPoint[0])[2]
                if (heightX ==0):
                    ifSameH = True
                if ifSameH == True :
                    ll1 = comp.Line(bl.endPoint[1],comp.EndPoints(blocks[bl.connectionWhich[TW]].tanangles[2])[0])
                    ll2 = comp.Line(blocks[bl.connectionWhich[TW]].endPoint[0],comp.EndPoints(bl.tanangles[2])[0])
                    Xpoint = comp.CurveXCurve(ll1 , ll2)[0]
                    ll1 = comp.Line(bl.endPoint[1],Xpoint)
                    ll2 = comp.Line(blocks[bl.connectionWhich[TW]].endPoint[0],Xpoint)
                    midp1 = comp.CurveMiddle(ll1)
                    midp2 = comp.CurveMiddle(ll2)
                    li22 = comp.Line(midp1,midp2)
                    midp5 = comp.CurveMiddle(li22)
                    
                    ll3 = comp.Line(bl.endPoint[2],comp.EndPoints(blocks[bl.connectionWhich[TW]].tanangles[2])[0])
                    ll4 = comp.Line(blocks[bl.connectionWhich[TW]].endPoint[3],comp.EndPoints(bl.tanangles[2])[0])
                    Xpoint = comp.CurveXCurve(ll3 , ll4)[0]
                    ll3 = comp.Line(bl.endPoint[2],Xpoint)
                    ll4 = comp.Line(blocks[bl.connectionWhich[TW]].endPoint[3],Xpoint)
                    midp3 = comp.CurveMiddle(ll3)
                    midp4 = comp.CurveMiddle(ll4)
                    poly1 = comp.PolyLine([bl.endPoint[1],midp1,midp2,blocks[bl.connectionWhich[TW]].endPoint[0]],False)
                    poly2 = comp.PolyLine([bl.endPoint[2],midp3,midp4,blocks[bl.connectionWhich[TW]].endPoint[3]],False)
                    polyall = comp.PolyLine([bl.endPoint[1],midp1,midp2,blocks[bl.connectionWhich[TW]].endPoint[0],blocks[bl.connectionWhich[TW]].endPoint[2]],True)
                    area1 = comp.Area(polyall)[0]
                    AreaList[bl.layer - 1][1] += area1
                    shareSpaces.append(polyall)
                    
                    polyall = comp.PolyLine([blocks[bl.connectionWhich[TW]].endPoint[3],blocks[bl.connectionWhich[TW]].endPoint[2],bl.endPoint[2],midp3,midp4],True)
                    area2 = comp.Area(polyall)[0]
                    AreaList[bl.layer - 1][2] += area2
                    shareSpaces.append(polyall)
                   
                    walls.append(poly2)
                    walls.append(poly1)
                   
                if ifSameH == False:
                    col1 = comp.Line(bl.endPoint[3],blocks[bl.connectionWhich[TW]].endPoint[2])
                    cols.append(col1)
                    length1 =comp.Distance(bl.endPoint[2],bl.endPoint[3])
                    length2 =comp.Distance(blocks[bl.connectionWhich[TW]].endPoint[2],blocks[bl.connectionWhich[TW]].endPoint[3])
                    hig1 = length1 * heightX/(length1 + length2)
                    vec = comp.VectorXYZ(0,0,hig1)[0]
                    s1 = comp.Line(bl.endPoint[2],comp.Move(bl.endPoint[3],vec)[0])
                    s2 = comp.Line(comp.Move(bl.endPoint[3],vec)[0],blocks[bl.connectionWhich[TW]].endPoint[3])
                    
                    Allstairs.append(s1)
                    Allstairs.append(s2)
                    
            ifSameH = False
                   
            if ISO == True :
                heightX = comp.Deconstruct(blocks[bl.connectionWhich[OW]].endPoint[0])[2]- comp.Deconstruct(bl.endPoint[0])[2]
                if (heightX ==0):
                    ifSameH = True
                if ifSameH == True:
                    pt1 = comp.EndPoints(blocks[bl.connectionWhich[OW]].tanangles[0])[0]
                    pt2 = comp.EndPoints(bl.tanangles[0])[0]
                    crv1 = comp.Line(pt1,pt2)
                    ed1 = comp.Line(blocks[bl.connectionWhich[OW]].endPoint[2],blocks[bl.connectionWhich[OW]].endPoint[0])
                    ed2 = comp.Line(bl.endPoint[1],bl.endPoint[0])

                    x1 = comp.LineXLine(crv1,ed2)[2]
                    x2 = comp.LineXLine(crv1,ed1)[2]
                    are = comp.PolyLine([x1,x2,bl.endPoint[1]],True)
                    shareSpaces.append(are)
                if ifSameH == False:
                    s0 = comp.Line(bl.endPoint[1],blocks[bl.connectionWhich[OW]].endPoint[3])
                    Allstairs.append(s0)
                    
                    
            ifSameH = False
            
            if  ISZ == True :
                heightX = comp.Deconstruct(blocks[bl.connectionWhich[ZW]].endPoint[0])[2]- comp.Deconstruct(bl.endPoint[0])[2]
                if (heightX ==0):
                    ifSameH = True
                if ifSameH == True:
                 
                    ll1 = comp.Line(bl.endPoint[2],comp.EndPoints(blocks[bl.connectionWhich[ZW]].tanangles[2])[0])
                    ll2 = comp.Line(blocks[bl.connectionWhich[ZW]].endPoint[0],comp.EndPoints(bl.tanangles[0])[0])
                    Xpoint = comp.CurveXCurve(ll1 , ll2)[0]
                    ll1 = comp.Line(bl.endPoint[2],Xpoint)
                    ll2 = comp.Line(blocks[bl.connectionWhich[ZW]].endPoint[0],Xpoint)
                    midp1 = comp.CurveMiddle(ll1)
                    midp2 = comp.CurveMiddle(ll2)
                    lll = comp.Line(midp1,midp2)
                    midp5 = comp.CurveMiddle(lll)
                    
                    ll3 = comp.Line(bl.endPoint[1],comp.EndPoints(blocks[bl.connectionWhich[ZW]].tanangles[2])[0])
                    ll4 = comp.Line(blocks[bl.connectionWhich[ZW]].endPoint[3],comp.EndPoints(bl.tanangles[1])[0])
                    Xpoint = comp.CurveXCurve(ll3 , ll4)[0]
                    ll3 = comp.Line(bl.endPoint[1],Xpoint)
                    ll4 = comp.Line(blocks[bl.connectionWhich[ZW]].endPoint[3],Xpoint)
                    midp3 = comp.CurveMiddle(ll3)
                    midp4 = comp.CurveMiddle(ll4)
                    poly1 = comp.PolyLine([bl.endPoint[2],midp1,midp2,blocks[bl.connectionWhich[ZW]].endPoint[0]],False)
                    poly2 = comp.PolyLine([bl.endPoint[1],midp3,midp4,blocks[bl.connectionWhich[ZW]].endPoint[3]],False)
                    polyall = comp.PolyLine([bl.endPoint[2],midp1,midp2,blocks[bl.connectionWhich[ZW]].endPoint[0],bl.endPoint[0]],True)
                    shareSpaces.append(polyall)
                    area1 = comp.Area(polyall)[0]
                    AreaList[bl.layer - 1][1] += area1
                    polyall = comp.PolyLine([blocks[bl.connectionWhich[ZW]].endPoint[3],midp4,midp3,bl.endPoint[1],bl.endPoint[0]],True)
                    area2 = comp.Area(polyall)[0]
                    AreaList[bl.layer - 1][2] += area2
                    shareSpaces.append(polyall)
                    
                    walls.append(poly2)
                    walls.append(poly1)
                if ifSameH == False:
                    col1 = comp.Line(bl.endPoint[0],blocks[bl.connectionWhich[ZW]].endPoint[2])
                    cols.append(col1)
                    length1 =comp.Distance(bl.endPoint[0],bl.endPoint[1])
                    length2 =comp.Distance(blocks[bl.connectionWhich[ZW]].endPoint[2],blocks[bl.connectionWhich[ZW]].endPoint[3])
                    hig1 = length1 * heightX/(length1 + length2)
                    vec = comp.VectorXYZ(0,0,hig1)[0]
                    print(hig1)
                    s1 = comp.Line(bl.endPoint[1],comp.Move(bl.endPoint[0],vec)[0])
                    s2 = comp.Line(comp.Move(bl.endPoint[0],vec)[0],blocks[bl.connectionWhich[ZW]].endPoint[3])
                    Allstairs.append(s1)
                    Allstairs.append(s2)
    
    """detect the connection"""

"""addCol"""
if Addcol == True:
    for bl in finished:
        if bl.endPoint[0][2] != 0:
            for poi in bl.endPoint:
                poiLife = True
                for bk in finished:
                    if comp.PointInCurve(poi,bk.rect)[0] == 2:
                        poiLife = False
                        break
                if poiLife == True:
                    xi = comp.Deconstruct(poi)[0]
                    yi = comp.Deconstruct(poi)[1]
                    col = comp.Line(comp.ConstructPoint(xi,yi,0),poi)
                    cols.append(col)
        
"""addCol"""

"""show"""
d = rs.AddRectangle(rs.WorldXYPlane(),fieldX,fieldY)
for bl in finished:
    pppppt = []
    bl.show()
    a.append(bl.rect)
    b.append(bl.sf)
    c.append(bl.bre)
    for l in bl.tanangles:
        h.append(l)
    for l in bl.stairs:
        XS.append(l)
    pppppt.append(bl.endPoint[0])
    pppppt.append(bl.endPoint[1])
    pppppt.append(bl.endPoint[3])
    pppppt.append(bl.endPoint[2])
    poly.append(comp.PolyLine(pppppt,True))
    body.append(comp.Line(comp.EndPoints(bl.tanangles[0])[0],comp.EndPoints(bl.tanangles[2])[0]))
    
"""show"""