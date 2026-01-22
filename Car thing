from cmu_graphics import *

app.stepsPerSecond=60
app.background = 'deepskyblue'
app.speed=0
app.pointx1=400
app.pointx2=0
#Enviroment moves
Rect(0,300,400,100,fill='gray',border=None,borderWidth=2,opacity=100,rotateAngle=0,dashes=False,align='top-left',visible=True)
lineGroup=Group(
    Line(800,250,-400,250,fill='brown',lineWidth=100,dashes=(25,70),opacity=100,visible=True,arrowStart=False,arrowEnd=False),    
    Line(800,290,-400,290,fill='silver',lineWidth=20,dashes=(15,25),opacity=100,visible=True,arrowStart=False,arrowEnd=False),
    Line(800,345,-400,345,fill='yellow',lineWidth=5,dashes=(18,14),opacity=100,rotateAngle=0,visible=True),
        )
#Train
train=Polygon(360,170,320,170,320,165,200,165,200,80,195,80,195,70,255,70,255,80,250,80,250,110,330,110,327,85,353,85,350,110,360,110,365,120,365,160,fill=rgb(0,0,0))
trainColor=Polygon(320,145,200,145,200,80,195,80,195,70,255,70,255,80,250,80,250,110,320,110,fill=rgb(20,65,140),border=rgb(235,235,235))
window=Polygon(240,80,240,110,210,110,210,80,fill='deepskyblue',border=rgb(235,235,235),borderWidth=2)

cowcatcher=Group(
    Polygon(400,173,365,173,365,145,fill=None,border=rgb(20,65,140)),
    Polygon(392,173,365,173,365,145,fill=None,border=rgb(23,82,150)),
    Polygon(384,173,365,173,365,145,fill=None,border=rgb(23,82,150)),
    Polygon(376,173,365,173,365,145,fill=None,border=rgb(23,82,150)),
    Polygon(368,173,365,173,365,145,fill=None,border=rgb(23,82,150))
    )

frontWheelF=Circle(298,160,19,fill='black',border=rgb(70,70,70),borderWidth=4)
frontWheel=Circle(298,160,15,fill=None,border=rgb(235,235,235),borderWidth=2)
frontWheelSpoke=Star(298,160,15,8,roundness=30,fill=rgb(20,65,140))
frontWheelAttach=Circle(298,152,5,fill=rgb(20,65,140))

middleWheelF=Circle(260,160,19,fill='black',border=rgb(70,70,70),borderWidth=4)
middleWheel=Circle(260,160,15,fill=None,border=rgb(235,235,235),borderWidth=2)
middleWheelSpoke=Star(260,160,15,8,roundness=30,fill=rgb(20,65,140))
middleWheelAttach=Circle(260,152,5,fill=rgb(20,65,140))

rearWheelF=Circle(222,160,19,fill='black',border=rgb(70,70,70),borderWidth=4)
rearWheel=Circle(222,160,15,fill=None,border=rgb(235,235,235),borderWidth=2)
rearWheelSpoke=Star(222,160,15,8,roundness=30,fill=rgb(20,65,140))
rearWheelAttach=Circle(222,152,5,fill=rgb(20,65,140))

tinyWheelF=Circle(340,165,14,fill='black',border=rgb(70,70,70),borderWidth=4)
tinyWheel=Circle(340,165,10,fill=None,border=rgb(235,235,235),borderWidth=2)
tinyWheelSpoke=Star(340,165,10,8,roundness=30,fill=rgb(20,65,140))

FrontWheel=Group(frontWheelF,frontWheelSpoke,frontWheel,frontWheelAttach)
MiddleWheel=Group(middleWheelF,middleWheelSpoke,middleWheel,middleWheelAttach)
RearWheel=Group(rearWheelF,rearWheelSpoke,rearWheel,rearWheelAttach)
TinyWheel=Group(tinyWheelF,tinyWheelSpoke,tinyWheel)

wheelLink=Line(298,152,222,152,fill=rgb(25,70,145),lineWidth=3)

Locomotive=Group(train,trainColor,window,cowcatcher,FrontWheel,MiddleWheel,RearWheel,TinyWheel,wheelLink)

coalCar=Polygon(180,150,180,140,160,140,160,120,180,80,180,70,0,70,0,80,20,120,20,140,0,140,0,150,24,150,24,152,12,152,12,168,52,168,52,152,40,152,40,150,60,150,70,160,110,160,120,150,140,150,140,152,128,152,128,168,168,168,168,152,156,152,156,150,fill=rgb(0,0,0))
coalCarColor=Polygon(180,150,180,140,160,140,160,120,180,80,180,70,0,70,0,80,20,120,20,140,0,140,0,150,fill=rgb(23,82,150),border=rgb(235,235,235))
coalCar1beams=Line(5,110,175,110,lineWidth=80,dashes=(5,28),fill=rgb(235,235,235))
coalCar1beams2=Line(90,70,90,150,lineWidth=170,dashes=(5,70),fill=rgb(235,235,235))
coalCar2beams=Line(5,110,175,110,lineWidth=80,dashes=(5,28),fill=rgb(235,235,235))
coalCar2beams2=Line(90,70,90,150,lineWidth=170,dashes=(5,70),fill=rgb(235,235,235))
coalCar2=Polygon(180,150,180,140,160,140,160,120,180,80,180,70,0,70,0,80,20,120,20,140,0,140,0,150,24,150,24,152,12,152,12,168,52,168,52,152,40,152,40,150,60,150,70,160,110,160,120,150,140,150,140,152,128,152,128,168,168,168,168,152,156,152,156,150,fill=rgb(0,0,0))
coalCar2Color=Polygon(180,150,180,140,160,140,160,120,180,80,180,70,0,70,0,80,20,120,20,140,0,140,0,150,fill=rgb(23,82,150),border=rgb(235,235,235))
Link=Polygon(168,165,179,165,179,168,189,168,189,165,200,165,200,155,189,155,189,152,179,152,179,155,168,155,fill=rgb(0,0,0))
Link2=Polygon(168,165,179,165,179,168,189,168,189,165,200,165,200,155,189,155,189,152,179,152,179,155,168,155,fill=rgb(0,0,0))

cartWheel1F=Circle(166,165,14,fill='black',border=rgb(70,70,70),borderWidth=4)
cartWheel1=Circle(166,165,10,fill=None,border=rgb(235,235,235),borderWidth=2)
cartWheel1Spoke=Star(166,165,10,8,roundness=30,fill=rgb(20,65,140))

cartWheel2F=Circle(130,165,14,fill='black',border=rgb(70,70,70),borderWidth=4)
cartWheel2=Circle(130,165,10,fill=None,border=rgb(235,235,235),borderWidth=2)
cartWheel2Spoke=Star(130,165,10,8,roundness=30,fill=rgb(20,65,140))

cartWheel3F=Circle(50,165,14,fill='black',border=rgb(70,70,70),borderWidth=4)
cartWheel3=Circle(50,165,10,fill=None,border=rgb(235,235,235),borderWidth=2)
cartWheel3Spoke=Star(50,165,10,8,roundness=30,fill=rgb(20,65,140))

cartWheel4F=Circle(14,165,14,fill='black',border=rgb(70,70,70),borderWidth=4)
cartWheel4=Circle(14,165,10,fill=None,border=rgb(235,235,235),borderWidth=2)
cartWheel4Spoke=Star(14,165,10,8,roundness=30,fill=rgb(20,65,140))

CartWheel1=Group(cartWheel1F,cartWheel1Spoke,cartWheel1)
CartWheel2=Group(cartWheel2F,cartWheel2Spoke,cartWheel2)
CartWheel3=Group(cartWheel3F,cartWheel3Spoke,cartWheel3)
CartWheel4=Group(cartWheel4F,cartWheel4Spoke,cartWheel4)

cart2Wheel1F=Circle(166,165,14,fill='black',border=rgb(70,70,70),borderWidth=4)
cart2Wheel1=Circle(166,165,10,fill=None,border=rgb(235,235,235),borderWidth=2)
cart2Wheel1Spoke=Star(166,165,10,8,roundness=30,fill=rgb(20,65,140))

cart2Wheel2F=Circle(130,165,14,fill='black',border=rgb(70,70,70),borderWidth=4)
cart2Wheel2=Circle(130,165,10,fill=None,border=rgb(235,235,235),borderWidth=2)
cart2Wheel2Spoke=Star(130,165,10,8,roundness=30,fill=rgb(20,65,140))

cart2Wheel3F=Circle(50,165,14,fill='black',border=rgb(70,70,70),borderWidth=4)
cart2Wheel3=Circle(50,165,10,fill=None,border=rgb(235,235,235),borderWidth=2)
cart2Wheel3Spoke=Star(50,165,10,8,roundness=30,fill=rgb(20,65,140))

cart2Wheel4F=Circle(14,165,14,fill='black',border=rgb(70,70,70),borderWidth=4)
cart2Wheel4=Circle(14,165,10,fill=None,border=rgb(235,235,235),borderWidth=2)
cart2Wheel4Spoke=Star(14,165,10,8,roundness=30,fill=rgb(20,65,140))

cart2Wheel1=Group(cart2Wheel1F,cart2Wheel1Spoke,cart2Wheel1)
cart2Wheel2=Group(cart2Wheel2F,cart2Wheel2Spoke,cart2Wheel2)
cart2Wheel3=Group(cart2Wheel3F,cart2Wheel3Spoke,cart2Wheel3)
cart2Wheel4=Group(cart2Wheel4F,cart2Wheel4Spoke,cart2Wheel4)

Cart=Group(Link,coalCar,coalCarColor,coalCar1beams,coalCar1beams2,CartWheel1,CartWheel2,CartWheel3,CartWheel4)
Cart2=Group(Link2,coalCar2,coalCar2Color,coalCar2beams,coalCar2beams2,cart2Wheel1,cart2Wheel2,cart2Wheel3,cart2Wheel4)
Cart2.centerX=-90
Train=Group(Locomotive,Cart2,Cart)
Train.Speed=1
#Enviroment
bridge = Line(0,190,400,190,fill='brown',lineWidth=30,dashes=False,opacity=100,visible=True,arrowStart=False,arrowEnd=False)
rail = Line(0,265,400,265,fill=gradient('grey','gray', 'silver', 'lightgrey', 'silver', 'grey', 'grey', 'grey',start='top'),lineWidth=30,dashes=False,opacity=100,visible=True,arrowStart=False,arrowEnd=False)
solidLine = Line(0,355,400,355,fill='yellow',lineWidth=5,dashes=False,opacity=100,visible=True,arrowStart=False,arrowEnd=False)
#Car
Car = Group(
Polygon(50,310,54,305,60,270,110,255,170,230,220,230,260,235,350,250,335,280,340,310,fill='black',border=None,borderWidth=2,opacity=100,rotateAngle=0,dashes=False,visible=True),
Polygon(110,255,170,230,180,230,130,255,fill='deepSkyBlue',border='black',borderWidth=1,opacity=100,rotateAngle=0,dashes=False,visible=True),
Polygon(150,308,180,308,200,232,180,232,130,258,fill='deepskyblue',border='black',borderWidth=2,opacity=100,rotateAngle=0,dashes=False,visible=True),
Polygon(240,308,180,308,200,232,220,232,260,238,fill='deepskyblue',border='black',borderWidth=2,opacity=100,rotateAngle=0,dashes=False,visible=True),
Polygon(50,310,54,305,60,270,110,255,330,255,340,310,fill='Blue',border=None,borderWidth=2,opacity=100,rotateAngle=0,dashes=False,visible=True),
Polygon(150,308,180,308,200,232,180,232,130,258,fill=None,border='black',borderWidth=1,opacity=100,rotateAngle=0,dashes=False,visible=True),
Polygon(240,308,180,308,200,232,220,232,260,238,fill=None,border='black',borderWidth=1,opacity=100,rotateAngle=0,dashes=False,visible=True),
Polygon(60,270,82,265,72,272,60,277,fill='orangeRed',border=None,borderWidth=1,opacity=100,rotateAngle=0,dashes=False,visible=True),
Polygon(345,260,331,260,335,280,fill='orangered',border=None,borderWidth=2,opacity=100,rotateAngle=0,dashes=False,visible=True),
Polygon(331,260,330,255,347,255,345,260,fill='ivory',border=None,borderWidth=2,opacity=100,rotateAngle=0,dashes=False,visible=True),
Arc(290,310,65,80,270,180,fill='dimGray',border=None,borderWidth=5,opacity=100,rotateAngle=0,dashes=False,visible=True),
Arc(110,310,65,80,270,180,fill='dimGray',border=None,borderWidth=5,opacity=100,rotateAngle=0,dashes=False,visible=True),
Arc(290,310,65,80,270,180,fill='black',border=None,borderWidth=5,opacity=30,rotateAngle=0,dashes=False,visible=True),
Arc(110,310,65,80,270,180,fill='black',border=None,borderWidth=5,opacity=30,rotateAngle=0,dashes=False,visible=True),
    )
    
Circle(110,300,12,fill=gradient('red', 'red', 'orange', 'red'),border=None,borderWidth=5,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True)
frontBrakeDarkness = Circle(110,300,12,fill='dimgrey',border=None,borderWidth=5,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True)
Arc(110,300,26,26,220,110,fill='yellow',border=None,borderWidth=2,opacity=100,rotateAngle=0,dashes=False,visible=True)
Arc(110,300,26,26,220,110,fill='black',border=None,borderWidth=2,opacity=30,rotateAngle=0,dashes=False,visible=True),

#rear brakes
Circle(290,300,12,fill=gradient('red', 'red', 'orange', 'red'),border=None,borderWidth=5,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True)
rearBrakeDarkness = Circle(290,300,12,fill='dimgray',border=None,borderWidth=5,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True)
Arc(290,300,26,26,20,120,fill='yellow',border=None,borderWidth=1,opacity=100,rotateAngle=0,dashes=False,visible=True)
Arc(290,300,26,26,20,120,fill='black',border=None,borderWidth=2,opacity=30,rotateAngle=0,dashes=False,visible=True)
Arc(290,300,26,26,230,80,fill='yellow',border=None,borderWidth=2,opacity=100,rotateAngle=0,dashes=False,visible=True)
Arc(290,300,26,26,230,80,fill='black',border=None,borderWidth=2,opacity=30,rotateAngle=0,dashes=False,visible=True)

frontWheel = Group(
Star(110,300,25,7,fill='silver',border='black',borderWidth=1,roundness=20,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True),
Star(110,300,25,7,fill='black',border='black',borderWidth=1,roundness=20,opacity=30,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(110,300,19,fill=None,border='black',borderWidth=5,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(110,300,19,fill=None,border='black',borderWidth=5,opacity=30,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(110,300,20,fill=None,border='silver',borderWidth=5,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(110,300,20,fill=None,border='black',borderWidth=5,opacity=30,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(110,300,25,fill=None,border='Black',borderWidth=5,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(110,300,25,fill=None,border='Black',borderWidth=5,opacity=30,rotateAngle=0,dashes=False,align='center',visible=True),
    )
rearWheel = Group(
Star(290,300,25,7,fill='silver',border='black',borderWidth=1,roundness=20,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True),
Star(290,300,25,7,fill='black',border='black',borderWidth=1,roundness=20,opacity=30,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(290,300,19,fill=None,border='black',borderWidth=5,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(290,300,19,fill=None,border='black',borderWidth=5,opacity=30,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(290,300,20,fill=None,border='silver',borderWidth=5,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(290,300,20,fill=None,border='black',borderWidth=5,opacity=30,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(290,300,25,fill=None,border='Black',borderWidth=5,opacity=100,rotateAngle=0,dashes=False,align='center',visible=True),
Circle(290,300,25,fill=None,border='Black',borderWidth=5,opacity=30,rotateAngle=0,dashes=False,align='center',visible=True),
)
Polygon(60,270,80,265,70,270,60,275,fill='ivory',border=None,borderWidth=1,opacity=100,rotateAngle=0,dashes=False,visible=True)
Polygon(350,250,328,247,330,255,347,255,fill='red',border=None,borderWidth=2,opacity=100,rotateAngle=0,dashes=False,visible=True)

def onStep():
#Train
    Train.Speed=10+app.speed
    wheelLink.x1=frontWheelAttach.centerX
    wheelLink.y1=frontWheelAttach.centerY
    wheelLink.x2=rearWheelAttach.centerX
    wheelLink.y2=rearWheelAttach.centerY
    FrontWheel.rotateAngle+=10
    MiddleWheel.rotateAngle+=10
    RearWheel.rotateAngle+=10
    TinyWheel.rotateAngle+=10
    CartWheel1.rotateAngle+=10
    CartWheel2.rotateAngle+=10
    CartWheel3.rotateAngle+=10
    CartWheel4.rotateAngle+=10
    cart2Wheel1.rotateAngle+=10
    cart2Wheel2.rotateAngle+=10
    cart2Wheel3.rotateAngle+=10
    cart2Wheel4.rotateAngle+=10
    Train.centerX+=Train.Speed
    if (Train.centerX>2000):
        Train.centerX=-10000+randrange(4000)-(app.speed*100)
#Car
    if (frontBrakeDarkness.opacity<100):
        frontBrakeDarkness.opacity+=0.5
        rearBrakeDarkness.opacity=frontBrakeDarkness.opacity
    frontWheel.rotateAngle-=app.speed
    rearWheel.rotateAngle-=app.speed
#enviroment calculation
    lineGroup.centerX+=app.speed
#enviroment move
    #foreward
    if (app.speed>=0):
        app.pointx1+=app.speed
        if (lineGroup.centerX>=600):
            lineGroup.centerX=-200
    #backward
    if (app.speed<=0):
        app.pointx2+=app.speed
        if (lineGroup.centerX<=-200):
            lineGroup.centerX=600
def onKeyHold(keys):
    if ('w' in keys):
        if (app.speed<200):
            app.speed+=0.25
            if (app.speed<0):
                if (frontBrakeDarkness.opacity > 2):
                    frontBrakeDarkness.opacity-=1
                    rearBrakeDarkness.opacity=frontBrakeDarkness.opacity
    if ('s' in keys):
        if (app.speed>-200):
            app.speed-=0.25
            if (app.speed>0):
                if (frontBrakeDarkness.opacity > 2):
                    frontBrakeDarkness.opacity-=1
                    rearBrakeDarkness.opacity=frontBrakeDarkness.opacity
    if ('space' in keys):
        if (app.speed<0):
            app.speed+=0.75
            if (frontBrakeDarkness.opacity > 2):
                frontBrakeDarkness.opacity-=2
                rearBrakeDarkness.opacity=frontBrakeDarkness.opacity
        if (app.speed>0):
            app.speed-=0.75
            if (frontBrakeDarkness.opacity > 2):
                frontBrakeDarkness.opacity-=2
                rearBrakeDarkness.opacity=frontBrakeDarkness.opacity
        if (app.speed==-0.25):
            app.speed=0
        if (app.speed==0.25):
            app.speed=0

cmu_graphics.run()
