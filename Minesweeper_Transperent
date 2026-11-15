from cmu_graphics import *

#Easy Version
grid = Group()
for i in range (0,400,40):
    for j in range(0,400,40):
        grid.add(Rect(i,j,40,40,fill='lime',border='black',borderWidth=1))
        
app.bomb1X = 20+randrange(0,10)*40
app.bomb2X = 20+randrange(0,10)*40
app.bomb3X = 20+randrange(0,10)*40
app.bomb4X = 20+randrange(0,10)*40
app.bomb5X = 20+randrange(0,10)*40
app.bomb6X = 20+randrange(0,10)*40
app.bomb7X = 20+randrange(0,10)*40
app.bomb8X = 20+randrange(0,10)*40
app.bomb9X = 20+randrange(0,10)*40
app.bomb10X = 20+randrange(0,10)*40

app.bomb1Y = 20+randrange(0,10)*40
app.bomb2Y = 20+randrange(0,10)*40
app.bomb3Y = 20+randrange(0,10)*40
app.bomb4Y = 20+randrange(0,10)*40
app.bomb5Y = 20+randrange(0,10)*40
app.bomb6Y = 20+randrange(0,10)*40
app.bomb7Y = 20+randrange(0,10)*40
app.bomb8Y = 20+randrange(0,10)*40
app.bomb9Y = 20+randrange(0,10)*40
app.bomb10Y = 20+randrange(0,10)*40

app.wins=0
app.ran=False

bomb1 = Group(
    Circle(20,20,10),
    Star(20,20,15,5,fill='black'),
    Rect(20,20,39,39,align='center',fill=None)
    )
    
bomb2 = Group(    
    Circle(20,20,10),    
    Star(20,20,15,5,fill='black'),    
    Rect(20,20,39,39,align='center',fill=None)   
    )
    
bomb3 = Group(    
    Circle(20,20,10),    
    Star(20,20,15,5,fill='black'),    
    Rect(20,20,39,39,align='center',fill=None)   
    )
    
bomb4 = Group(    
    Circle(20,20,10),    
    Star(20,20,15,5,fill='black'),    
    Rect(20,20,39,39,align='center',fill=None)   
    )
    
bomb5 = Group(    
    Circle(20,20,10),    
    Star(20,20,15,5,fill='black'),    
    Rect(20,20,39,39,align='center',fill=None)   
    )
    
bomb6 = Group(    
    Circle(20,20,10),    
    Star(20,20,15,5,fill='black'),    
    Rect(20,20,39,39,align='center',fill=None)   
    )
    
bomb7 = Group(    
    Circle(20,20,10),    
    Star(20,20,15,5,fill='black'),    
    Rect(20,20,39,39,align='center',fill=None)   
    )
    
bomb8 = Group(    
    Circle(20,20,10),    
    Star(20,20,15,5,fill='black'),    
    Rect(20,20,39,39,align='center',fill=None)   
    )
    
bomb9 = Group(    
    Circle(20,20,10),    
    Star(20,20,15,5,fill='black'),    
    Rect(20,20,39,39,align='center',fill=None)   
    )
    
bomb10 = Group(    
    Circle(20,20,10),    
    Star(20,20,15,5,fill='black'),    
    Rect(20,20,39,39,align='center',fill=None)   
    )

p00 = Label(0,20,20,size=25,fill='black',border='black',borderWidth=1)
p01 = Label(0,60,20,size=25,fill='black',border='black',borderWidth=1)
p02 = Label(0,100,20,size=25,fill='black',border='black',borderWidth=1)
p03 = Label(0,140,20,size=25,fill='black',border='black',borderWidth=1)
p04 = Label(0,180,20,size=25,fill='black',border='black',borderWidth=1)
p05 = Label(0,220,20,size=25,fill='black',border='black',borderWidth=1)
p06 = Label(0,260,20,size=25,fill='black',border='black',borderWidth=1)
p07 = Label(0,300,20,size=25,fill='black',border='black',borderWidth=1)
p08 = Label(0,340,20,size=25,fill='black',border='black',borderWidth=1)
p09 = Label(0,380,20,size=25,fill='black',border='black',borderWidth=1)

p10 = Label(0,20,60,size=25,fill='black',border='black',borderWidth=1)
p11 = Label(0,60,60,size=25,fill='black',border='black',borderWidth=1)
p12 = Label(0,100,60,size=25,fill='black',border='black',borderWidth=1)
p13 = Label(0,140,60,size=25,fill='black',border='black',borderWidth=1)
p14 = Label(0,180,60,size=25,fill='black',border='black',borderWidth=1)
p15 = Label(0,220,60,size=25,fill='black',border='black',borderWidth=1)
p16 = Label(0,260,60,size=25,fill='black',border='black',borderWidth=1)
p17 = Label(0,300,60,size=25,fill='black',border='black',borderWidth=1)
p18 = Label(0,340,60,size=25,fill='black',border='black',borderWidth=1)
p19 = Label(0,380,60,size=25,fill='black',border='black',borderWidth=1)

p20 = Label(0,20,100,size=25,fill='black',border='black',borderWidth=1)
p21 = Label(0,60,100,size=25,fill='black',border='black',borderWidth=1)
p22 = Label(0,100,100,size=25,fill='black',border='black',borderWidth=1)
p23 = Label(0,140,100,size=25,fill='black',border='black',borderWidth=1)
p24 = Label(0,180,100,size=25,fill='black',border='black',borderWidth=1)
p25 = Label(0,220,100,size=25,fill='black',border='black',borderWidth=1)
p26 = Label(0,260,100,size=25,fill='black',border='black',borderWidth=1)
p27 = Label(0,300,100,size=25,fill='black',border='black',borderWidth=1)
p28 = Label(0,340,100,size=25,fill='black',border='black',borderWidth=1)
p29 = Label(0,380,100,size=25,fill='black',border='black',borderWidth=1)

p30 = Label(0,20,140,size=25,fill='black',border='black',borderWidth=1)
p31 = Label(0,60,140,size=25,fill='black',border='black',borderWidth=1)
p32 = Label(0,100,140,size=25,fill='black',border='black',borderWidth=1)
p33 = Label(0,140,140,size=25,fill='black',border='black',borderWidth=1)
p34 = Label(0,180,140,size=25,fill='black',border='black',borderWidth=1)
p35 = Label(0,220,140,size=25,fill='black',border='black',borderWidth=1)
p36 = Label(0,260,140,size=25,fill='black',border='black',borderWidth=1)
p37 = Label(0,300,140,size=25,fill='black',border='black',borderWidth=1)
p38 = Label(0,340,140,size=25,fill='black',border='black',borderWidth=1)
p39 = Label(0,380,140,size=25,fill='black',border='black',borderWidth=1)

p40 = Label(0,20,180,size=25,fill='black',border='black',borderWidth=1)
p41 = Label(0,60,180,size=25,fill='black',border='black',borderWidth=1)
p42 = Label(0,100,180,size=25,fill='black',border='black',borderWidth=1)
p43 = Label(0,140,180,size=25,fill='black',border='black',borderWidth=1)
p44 = Label(0,180,180,size=25,fill='black',border='black',borderWidth=1)
p45 = Label(0,220,180,size=25,fill='black',border='black',borderWidth=1)
p46 = Label(0,260,180,size=25,fill='black',border='black',borderWidth=1)
p47 = Label(0,300,180,size=25,fill='black',border='black',borderWidth=1)
p48 = Label(0,340,180,size=25,fill='black',border='black',borderWidth=1)
p49 = Label(0,380,180,size=25,fill='black',border='black',borderWidth=1)

p50 = Label(0,20,220,size=25,fill='black',border='black',borderWidth=1)
p51 = Label(0,60,220,size=25,fill='black',border='black',borderWidth=1)
p52 = Label(0,100,220,size=25,fill='black',border='black',borderWidth=1)
p53 = Label(0,140,220,size=25,fill='black',border='black',borderWidth=1)
p54 = Label(0,180,220,size=25,fill='black',border='black',borderWidth=1)
p55 = Label(0,220,220,size=25,fill='black',border='black',borderWidth=1)
p56 = Label(0,260,220,size=25,fill='black',border='black',borderWidth=1)
p57 = Label(0,300,220,size=25,fill='black',border='black',borderWidth=1)
p58 = Label(0,340,220,size=25,fill='black',border='black',borderWidth=1)
p59 = Label(0,380,220,size=25,fill='black',border='black',borderWidth=1)

p60 = Label(0,20,260,size=25,fill='black',border='black',borderWidth=1)
p61 = Label(0,60,260,size=25,fill='black',border='black',borderWidth=1)
p62 = Label(0,100,260,size=25,fill='black',border='black',borderWidth=1)
p63 = Label(0,140,260,size=25,fill='black',border='black',borderWidth=1)
p64 = Label(0,180,260,size=25,fill='black',border='black',borderWidth=1)
p65 = Label(0,220,260,size=25,fill='black',border='black',borderWidth=1)
p66 = Label(0,260,260,size=25,fill='black',border='black',borderWidth=1)
p67 = Label(0,300,260,size=25,fill='black',border='black',borderWidth=1)
p68 = Label(0,340,260,size=25,fill='black',border='black',borderWidth=1)
p69 = Label(0,380,260,size=25,fill='black',border='black',borderWidth=1)

p70 = Label(0,20,300,size=25,fill='black',border='black',borderWidth=1)
p71 = Label(0,60,300,size=25,fill='black',border='black',borderWidth=1)
p72 = Label(0,100,300,size=25,fill='black',border='black',borderWidth=1)
p73 = Label(0,140,300,size=25,fill='black',border='black',borderWidth=1)
p74 = Label(0,180,300,size=25,fill='black',border='black',borderWidth=1)
p75 = Label(0,220,300,size=25,fill='black',border='black',borderWidth=1)
p76 = Label(0,260,300,size=25,fill='black',border='black',borderWidth=1)
p77 = Label(0,300,300,size=25,fill='black',border='black',borderWidth=1)
p78 = Label(0,340,300,size=25,fill='black',border='black',borderWidth=1)
p79 = Label(0,380,300,size=25,fill='black',border='black',borderWidth=1)

p80 = Label(0,20,340,size=25,fill='black',border='black',borderWidth=1)
p81 = Label(0,60,340,size=25,fill='black',border='black',borderWidth=1)
p82 = Label(0,100,340,size=25,fill='black',border='black',borderWidth=1)
p83 = Label(0,140,340,size=25,fill='black',border='black',borderWidth=1)
p84 = Label(0,180,340,size=25,fill='black',border='black',borderWidth=1)
p85 = Label(0,220,340,size=25,fill='black',border='black',borderWidth=1)
p86 = Label(0,260,340,size=25,fill='black',border='black',borderWidth=1)
p87 = Label(0,300,340,size=25,fill='black',border='black',borderWidth=1)
p88 = Label(0,340,340,size=25,fill='black',border='black',borderWidth=1)
p89 = Label(0,380,340,size=25,fill='black',border='black',borderWidth=1)

p90 = Label(0,20,380,size=25,fill='black',border='black',borderWidth=1)
p91 = Label(0,60,380,size=25,fill='black',border='black',borderWidth=1)
p92 = Label(0,100,380,size=25,fill='black',border='black',borderWidth=1)
p93 = Label(0,140,380,size=25,fill='black',border='black',borderWidth=1)
p94 = Label(0,180,380,size=25,fill='black',border='black',borderWidth=1)
p95 = Label(0,220,380,size=25,fill='black',border='black',borderWidth=1)
p96 = Label(0,260,380,size=25,fill='black',border='black',borderWidth=1)
p97 = Label(0,300,380,size=25,fill='black',border='black',borderWidth=1)
p98 = Label(0,340,380,size=25,fill='black',border='black',borderWidth=1)
p99 = Label(0,380,380,size=25,fill='black',border='black',borderWidth=1)

def resetValue():
    for number in numberGroup:
        number.fill='black'
        number.border='black'
    p00.value=0
    p01.value=0
    p02.value=0
    p03.value=0
    p04.value=0
    p05.value=0
    p06.value=0
    p07.value=0
    p08.value=0
    p09.value=0
    
    p10.value=0
    p11.value=0
    p12.value=0
    p13.value=0
    p14.value=0
    p15.value=0
    p16.value=0
    p17.value=0
    p18.value=0
    p19.value=0
    
    p20.value=0
    p21.value=0
    p22.value=0
    p23.value=0
    p24.value=0
    p25.value=0
    p26.value=0
    p27.value=0
    p28.value=0
    p29.value=0
    
    p30.value=0
    p31.value=0
    p32.value=0
    p33.value=0
    p34.value=0
    p35.value=0
    p36.value=0
    p37.value=0
    p38.value=0
    p39.value=0

    p40.value=0
    p41.value=0
    p42.value=0
    p43.value=0
    p44.value=0
    p45.value=0
    p46.value=0
    p47.value=0
    p48.value=0
    p49.value=0
    
    p50.value=0
    p51.value=0
    p52.value=0
    p53.value=0
    p54.value=0
    p55.value=0
    p56.value=0
    p57.value=0
    p58.value=0
    p59.value=0
    
    p60.value=0
    p61.value=0
    p62.value=0
    p63.value=0
    p64.value=0
    p65.value=0
    p66.value=0
    p67.value=0
    p68.value=0
    p69.value=0
    
    p70.value=0
    p71.value=0
    p72.value=0
    p73.value=0
    p74.value=0
    p75.value=0
    p76.value=0
    p77.value=0
    p78.value=0
    p79.value=0
    
    p80.value=0
    p81.value=0
    p82.value=0
    p83.value=0
    p84.value=0
    p85.value=0
    p86.value=0
    p87.value=0
    p88.value=0
    p89.value=0
    
    p90.value=0
    p91.value=0
    p92.value=0
    p93.value=0
    p94.value=0
    p95.value=0
    p96.value=0
    p97.value=0
    p98.value=0
    p99.value=0
    
bombGroup = Group()
bombGroup.add(bomb1)
bombGroup.add(bomb2)
bombGroup.add(bomb3)
bombGroup.add(bomb4)
bombGroup.add(bomb5)
bombGroup.add(bomb6)
bombGroup.add(bomb7)
bombGroup.add(bomb8)
bombGroup.add(bomb9)
bombGroup.add(bomb10)

numberGroup = Group()
numberGroup.add(p00)
numberGroup.add(p01)
numberGroup.add(p02)
numberGroup.add(p03)
numberGroup.add(p04)
numberGroup.add(p05)
numberGroup.add(p06)
numberGroup.add(p07)
numberGroup.add(p08)
numberGroup.add(p09)

numberGroup.add(p10)
numberGroup.add(p11)
numberGroup.add(p12)
numberGroup.add(p13)
numberGroup.add(p14)
numberGroup.add(p15)
numberGroup.add(p16)
numberGroup.add(p17)
numberGroup.add(p18)
numberGroup.add(p19)

numberGroup.add(p20)
numberGroup.add(p21)
numberGroup.add(p22)
numberGroup.add(p23)
numberGroup.add(p24)
numberGroup.add(p25)
numberGroup.add(p26)
numberGroup.add(p27)
numberGroup.add(p28)
numberGroup.add(p29)

numberGroup.add(p30)
numberGroup.add(p31)
numberGroup.add(p32)
numberGroup.add(p33)
numberGroup.add(p34)
numberGroup.add(p35)
numberGroup.add(p36)
numberGroup.add(p37)
numberGroup.add(p38)
numberGroup.add(p39)

numberGroup.add(p40)
numberGroup.add(p41)
numberGroup.add(p42)
numberGroup.add(p43)
numberGroup.add(p44)
numberGroup.add(p45)
numberGroup.add(p46)
numberGroup.add(p47)
numberGroup.add(p48)
numberGroup.add(p49)

numberGroup.add(p50)
numberGroup.add(p51)
numberGroup.add(p52)
numberGroup.add(p53)
numberGroup.add(p54)
numberGroup.add(p55)
numberGroup.add(p56)
numberGroup.add(p57)
numberGroup.add(p58)
numberGroup.add(p59)

numberGroup.add(p60)
numberGroup.add(p61)
numberGroup.add(p62)
numberGroup.add(p63)
numberGroup.add(p64)
numberGroup.add(p65)
numberGroup.add(p66)
numberGroup.add(p67)
numberGroup.add(p68)
numberGroup.add(p69)

numberGroup.add(p70)
numberGroup.add(p71)
numberGroup.add(p72)
numberGroup.add(p73)
numberGroup.add(p74)
numberGroup.add(p75)
numberGroup.add(p76)
numberGroup.add(p77)
numberGroup.add(p78)
numberGroup.add(p79)

numberGroup.add(p80)
numberGroup.add(p81)
numberGroup.add(p82)
numberGroup.add(p83)
numberGroup.add(p84)
numberGroup.add(p85)
numberGroup.add(p86)
numberGroup.add(p87)
numberGroup.add(p88)
numberGroup.add(p89)

numberGroup.add(p90)
numberGroup.add(p91)
numberGroup.add(p92)
numberGroup.add(p93)
numberGroup.add(p94)
numberGroup.add(p95)
numberGroup.add(p96)
numberGroup.add(p97)
numberGroup.add(p98)
numberGroup.add(p99)

Cover = Group()

def start(ran):
    if(ran==False):
        for bomb in bombGroup:
            for number in numberGroup:
                if(((number.centerX >= bomb.centerX-40) and (number.centerX <= bomb.centerX+40)) and ((number.centerY >= bomb.centerY-40) and (number.centerY <= bomb.centerY+40))):
                    number.value+=1
                    
                if((bomb.centerX == number.centerX) and (bomb.centerY == number.centerY)):
                        number.fill=None
                        number.border=None
                
        for number in numberGroup:
            if(number.value==0):
                number.fill=None
                number.border=None

def onStep():
    if(app.ran==False):
        if(bomb1.hitsShape(bomb2)==True):
            app.bomb2X = 20+randrange(0,10)*40
            app.bomb2Y = 20+randrange(0,10)*40
            bomb2.centerX=app.bomb2X
            bomb2.centerY=app.bomb2Y
        if(bomb1.hitsShape(bomb3)==True):
            app.bomb3X = 20+randrange(0,10)*40
            app.bomb3Y = 20+randrange(0,10)*40
            bomb3.centerX=app.bomb3X
            bomb3.centerY=app.bomb3Y
        if(bomb1.hitsShape(bomb4)==True):
            app.bomb4X = 20+randrange(0,10)*40
            app.bomb4Y = 20+randrange(0,10)*40
            bomb4.centerX=app.bomb4X
            bomb4.centerY=app.bomb4Y
        if(bomb1.hitsShape(bomb5)==True):
            app.bomb5X = 20+randrange(0,10)*40
            app.bomb5Y = 20+randrange(0,10)*40
            bomb5.centerX=app.bomb5X
            bomb5.centerY=app.bomb5Y
        if(bomb1.hitsShape(bomb6)==True):
            app.bomb6X = 20+randrange(0,10)*40
            app.bomb6Y = 20+randrange(0,10)*40
            bomb6.centerX=app.bomb6X
            bomb6.centerY=app.bomb6Y
        if(bomb1.hitsShape(bomb7)==True):
            app.bomb7X = 20+randrange(0,10)*40
            app.bomb7Y = 20+randrange(0,10)*40
            bomb7.centerX=app.bomb7X
            bomb7.centerY=app.bomb7Y
        if(bomb1.hitsShape(bomb8)==True):
            app.bomb8X = 20+randrange(0,10)*40
            app.bomb8Y = 20+randrange(0,10)*40
            bomb8.centerX=app.bomb8X
            bomb8.centerY=app.bomb8Y
        if(bomb1.hitsShape(bomb9)==True):
            app.bomb9X = 20+randrange(0,10)*40
            app.bomb9Y = 20+randrange(0,10)*40
            bomb9.centerX=app.bomb9X
            bomb9.centerY=app.bomb9Y
        if(bomb1.hitsShape(bomb10)==True):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
            bomb10.centerX=app.bomb10X
            bomb10.centerY=app.bomb10Y
            
        if(bomb2.hitsShape(bomb1)==True):
            app.bomb2X = 20+randrange(0,10)*40
            app.bomb2Y = 20+randrange(0,10)*40
            bomb2.centerX=app.bomb2X
            bomb2.centerY=app.bomb2Y
        if(bomb2.hitsShape(bomb3)==True):
            app.bomb3X = 20+randrange(0,10)*40
            app.bomb3Y = 20+randrange(0,10)*40
            bomb3.centerX=app.bomb3X
            bomb3.centerY=app.bomb3Y
        if(bomb2.hitsShape(bomb4)==True):
            app.bomb4X = 20+randrange(0,10)*40
            app.bomb4Y = 20+randrange(0,10)*40
            bomb4.centerX=app.bomb4X
            bomb4.centerY=app.bomb4Y
        if(bomb2.hitsShape(bomb5)==True):
            app.bomb5X = 20+randrange(0,10)*40
            app.bomb5Y = 20+randrange(0,10)*40
            bomb5.centerX=app.bomb5X
            bomb5.centerY=app.bomb5Y
        if(bomb2.hitsShape(bomb6)==True):
            app.bomb6X = 20+randrange(0,10)*40
            app.bomb6Y = 20+randrange(0,10)*40
            bomb6.centerX=app.bomb6X
            bomb6.centerY=app.bomb6Y
        if(bomb2.hitsShape(bomb7)==True):
            app.bomb7X = 20+randrange(0,10)*40
            app.bomb7Y = 20+randrange(0,10)*40
            bomb7.centerX=app.bomb7X
            bomb7.centerY=app.bomb7Y
        if(bomb2.hitsShape(bomb8)==True):
            app.bomb8X = 20+randrange(0,10)*40
            app.bomb8Y = 20+randrange(0,10)*40
            bomb8.centerX=app.bomb8X
            bomb8.centerY=app.bomb8Y
        if(bomb2.hitsShape(bomb9)==True):
            app.bomb9X = 20+randrange(0,10)*40
            app.bomb9Y = 20+randrange(0,10)*40
            bomb9.centerX=app.bomb9X
            bomb9.centerY=app.bomb9Y
        if(bomb2.hitsShape(bomb10)==True):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
            bomb10.centerX=app.bomb10X
            bomb10.centerY=app.bomb10Y
            
        if(bomb3.hitsShape(bomb1)==True):
            app.bomb2X = 20+randrange(0,10)*40
            app.bomb2Y = 20+randrange(0,10)*40
            bomb2.centerX=app.bomb2X
            bomb2.centerY=app.bomb2Y
        if(bomb3.hitsShape(bomb2)==True):
            app.bomb3X = 20+randrange(0,10)*40
            app.bomb3Y = 20+randrange(0,10)*40
            bomb3.centerX=app.bomb3X
            bomb3.centerY=app.bomb3Y
        if(bomb3.hitsShape(bomb4)==True):
            app.bomb4X = 20+randrange(0,10)*40
            app.bomb4Y = 20+randrange(0,10)*40
            bomb4.centerX=app.bomb4X
            bomb4.centerY=app.bomb4Y
        if(bomb3.hitsShape(bomb5)==True):
            app.bomb5X = 20+randrange(0,10)*40
            app.bomb5Y = 20+randrange(0,10)*40
            bomb5.centerX=app.bomb5X
            bomb5.centerY=app.bomb5Y
        if(bomb3.hitsShape(bomb6)==True):
            app.bomb6X = 20+randrange(0,10)*40
            app.bomb6Y = 20+randrange(0,10)*40
            bomb6.centerX=app.bomb6X
            bomb6.centerY=app.bomb6Y
        if(bomb3.hitsShape(bomb7)==True):
            app.bomb7X = 20+randrange(0,10)*40
            app.bomb7Y = 20+randrange(0,10)*40
            bomb7.centerX=app.bomb7X
            bomb7.centerY=app.bomb7Y
        if(bomb3.hitsShape(bomb8)==True):
            app.bomb8X = 20+randrange(0,10)*40
            app.bomb8Y = 20+randrange(0,10)*40
            bomb8.centerX=app.bomb8X
            bomb8.centerY=app.bomb8Y
        if(bomb3.hitsShape(bomb9)==True):
            app.bomb9X = 20+randrange(0,10)*40
            app.bomb9Y = 20+randrange(0,10)*40
            bomb9.centerX=app.bomb9X
            bomb9.centerY=app.bomb9Y
        if(bomb3.hitsShape(bomb10)==True):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
            bomb10.centerX=app.bomb10X
            bomb10.centerY=app.bomb10Y 
            
        if(bomb4.hitsShape(bomb1)==True):
            app.bomb2X = 20+randrange(0,10)*40
            app.bomb2Y = 20+randrange(0,10)*40
            bomb2.centerX=app.bomb2X
            bomb2.centerY=app.bomb2Y
        if(bomb4.hitsShape(bomb2)==True):
            app.bomb3X = 20+randrange(0,10)*40
            app.bomb3Y = 20+randrange(0,10)*40
            bomb3.centerX=app.bomb3X
            bomb3.centerY=app.bomb3Y
        if(bomb4.hitsShape(bomb2)==True):
            app.bomb4X = 20+randrange(0,10)*40
            app.bomb4Y = 20+randrange(0,10)*40
            bomb4.centerX=app.bomb4X
            bomb4.centerY=app.bomb4Y
        if(bomb4.hitsShape(bomb5)==True):
            app.bomb5X = 20+randrange(0,10)*40
            app.bomb5Y = 20+randrange(0,10)*40
            bomb5.centerX=app.bomb5X
            bomb5.centerY=app.bomb5Y
        if(bomb4.hitsShape(bomb6)==True):
            app.bomb6X = 20+randrange(0,10)*40
            app.bomb6Y = 20+randrange(0,10)*40
            bomb6.centerX=app.bomb6X
            bomb6.centerY=app.bomb6Y
        if(bomb4.hitsShape(bomb7)==True):
            app.bomb7X = 20+randrange(0,10)*40
            app.bomb7Y = 20+randrange(0,10)*40
            bomb7.centerX=app.bomb7X
            bomb7.centerY=app.bomb7Y
        if(bomb4.hitsShape(bomb8)==True):
            app.bomb8X = 20+randrange(0,10)*40
            app.bomb8Y = 20+randrange(0,10)*40
            bomb8.centerX=app.bomb8X
            bomb8.centerY=app.bomb8Y
        if(bomb4.hitsShape(bomb9)==True):
            app.bomb9X = 20+randrange(0,10)*40
            app.bomb9Y = 20+randrange(0,10)*40
            bomb9.centerX=app.bomb9X
            bomb9.centerY=app.bomb9Y
        if(bomb4.hitsShape(bomb10)==True):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
            bomb10.centerX=app.bomb10X
            bomb10.centerY=app.bomb10Y
            
        if(bomb5.hitsShape(bomb1)==True):
            app.bomb2X = 20+randrange(0,10)*40
            app.bomb2Y = 20+randrange(0,10)*40
            bomb2.centerX=app.bomb2X
            bomb2.centerY=app.bomb2Y
        if(bomb5.hitsShape(bomb2)==True):
            app.bomb3X = 20+randrange(0,10)*40
            app.bomb3Y = 20+randrange(0,10)*40
            bomb3.centerX=app.bomb3X
            bomb3.centerY=app.bomb3Y
        if(bomb5.hitsShape(bomb3)==True):
            app.bomb4X = 20+randrange(0,10)*40
            app.bomb4Y = 20+randrange(0,10)*40
            bomb4.centerX=app.bomb4X
            bomb4.centerY=app.bomb4Y
        if(bomb5.hitsShape(bomb4)==True):
            app.bomb5X = 20+randrange(0,10)*40
            app.bomb5Y = 20+randrange(0,10)*40
            bomb5.centerX=app.bomb5X
            bomb5.centerY=app.bomb5Y
        if(bomb5.hitsShape(bomb6)==True):
            app.bomb6X = 20+randrange(0,10)*40
            app.bomb6Y = 20+randrange(0,10)*40
            bomb6.centerX=app.bomb6X
            bomb6.centerY=app.bomb6Y
        if(bomb5.hitsShape(bomb7)==True):
            app.bomb7X = 20+randrange(0,10)*40
            app.bomb7Y = 20+randrange(0,10)*40
            bomb7.centerX=app.bomb7X
            bomb7.centerY=app.bomb7Y
        if(bomb5.hitsShape(bomb8)==True):
            app.bomb8X = 20+randrange(0,10)*40
            app.bomb8Y = 20+randrange(0,10)*40
            bomb8.centerX=app.bomb8X
            bomb8.centerY=app.bomb8Y
        if(bomb5.hitsShape(bomb9)==True):
            app.bomb9X = 20+randrange(0,10)*40
            app.bomb9Y = 20+randrange(0,10)*40
            bomb9.centerX=app.bomb9X
            bomb9.centerY=app.bomb9Y
        if(bomb5.hitsShape(bomb10)==True):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
            bomb10.centerX=app.bomb10X
            bomb10.centerY=app.bomb10Y 
            
        if(bomb6.hitsShape(bomb1)==True):
            app.bomb2X = 20+randrange(0,10)*40
            app.bomb2Y = 20+randrange(0,10)*40
            bomb2.centerX=app.bomb2X
            bomb2.centerY=app.bomb2Y
        if(bomb6.hitsShape(bomb2)==True):
            app.bomb3X = 20+randrange(0,10)*40
            app.bomb3Y = 20+randrange(0,10)*40
            bomb3.centerX=app.bomb3X
            bomb3.centerY=app.bomb3Y
        if(bomb6.hitsShape(bomb3)==True):
            app.bomb4X = 20+randrange(0,10)*40
            app.bomb4Y = 20+randrange(0,10)*40
            bomb4.centerX=app.bomb4X
            bomb4.centerY=app.bomb4Y
        if(bomb6.hitsShape(bomb4)==True):
            app.bomb5X = 20+randrange(0,10)*40
            app.bomb5Y = 20+randrange(0,10)*40
            bomb5.centerX=app.bomb5X
            bomb5.centerY=app.bomb5Y
        if(bomb6.hitsShape(bomb5)==True):
            app.bomb6X = 20+randrange(0,10)*40
            app.bomb6Y = 20+randrange(0,10)*40
            bomb6.centerX=app.bomb6X
            bomb6.centerY=app.bomb6Y
        if(bomb6.hitsShape(bomb7)==True):
            app.bomb7X = 20+randrange(0,10)*40
            app.bomb7Y = 20+randrange(0,10)*40
            bomb7.centerX=app.bomb7X
            bomb7.centerY=app.bomb7Y
        if(bomb6.hitsShape(bomb8)==True):
            app.bomb8X = 20+randrange(0,10)*40
            app.bomb8Y = 20+randrange(0,10)*40
            bomb8.centerX=app.bomb8X
            bomb8.centerY=app.bomb8Y
        if(bomb6.hitsShape(bomb9)==True):
            app.bomb9X = 20+randrange(0,10)*40
            app.bomb9Y = 20+randrange(0,10)*40
            bomb9.centerX=app.bomb9X
            bomb9.centerY=app.bomb9Y
        if(bomb6.hitsShape(bomb10)==True):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
            bomb10.centerX=app.bomb10X
            bomb10.centerY=app.bomb10Y 
            
        if(bomb7.hitsShape(bomb1)==True):
            app.bomb2X = 20+randrange(0,10)*40
            app.bomb2Y = 20+randrange(0,10)*40
            bomb2.centerX=app.bomb2X
            bomb2.centerY=app.bomb2Y
        if(bomb7.hitsShape(bomb2)==True):
            app.bomb3X = 20+randrange(0,10)*40
            app.bomb3Y = 20+randrange(0,10)*40
            bomb3.centerX=app.bomb3X
            bomb3.centerY=app.bomb3Y
        if(bomb7.hitsShape(bomb3)==True):
            app.bomb4X = 20+randrange(0,10)*40
            app.bomb4Y = 20+randrange(0,10)*40
            bomb4.centerX=app.bomb4X
            bomb4.centerY=app.bomb4Y
        if(bomb7.hitsShape(bomb4)==True):
            app.bomb5X = 20+randrange(0,10)*40
            app.bomb5Y = 20+randrange(0,10)*40
            bomb5.centerX=app.bomb5X
            bomb5.centerY=app.bomb5Y
        if(bomb7.hitsShape(bomb5)==True):
            app.bomb6X = 20+randrange(0,10)*40
            app.bomb6Y = 20+randrange(0,10)*40
            bomb6.centerX=app.bomb6X
            bomb6.centerY=app.bomb6Y
        if(bomb7.hitsShape(bomb6)==True):
            app.bomb7X = 20+randrange(0,10)*40
            app.bomb7Y = 20+randrange(0,10)*40
            bomb7.centerX=app.bomb7X
            bomb7.centerY=app.bomb7Y
        if(bomb7.hitsShape(bomb8)==True):
            app.bomb8X = 20+randrange(0,10)*40
            app.bomb8Y = 20+randrange(0,10)*40
            bomb8.centerX=app.bomb8X
            bomb8.centerY=app.bomb8Y
        if(bomb7.hitsShape(bomb9)==True):
            app.bomb9X = 20+randrange(0,10)*40
            app.bomb9Y = 20+randrange(0,10)*40
            bomb9.centerX=app.bomb9X
            bomb9.centerY=app.bomb9Y
        if(bomb7.hitsShape(bomb10)==True):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
            bomb10.centerX=app.bomb10X
            bomb10.centerY=app.bomb10Y 
            
        if(bomb8.hitsShape(bomb1)==True):
            app.bomb2X = 20+randrange(0,10)*40
            app.bomb2Y = 20+randrange(0,10)*40
            bomb2.centerX=app.bomb2X
            bomb2.centerY=app.bomb2Y
        if(bomb8.hitsShape(bomb2)==True):
            app.bomb3X = 20+randrange(0,10)*40
            app.bomb3Y = 20+randrange(0,10)*40
            bomb3.centerX=app.bomb3X
            bomb3.centerY=app.bomb3Y
        if(bomb8.hitsShape(bomb3)==True):
            app.bomb4X = 20+randrange(0,10)*40
            app.bomb4Y = 20+randrange(0,10)*40
            bomb4.centerX=app.bomb4X
            bomb4.centerY=app.bomb4Y
        if(bomb8.hitsShape(bomb4)==True):
            app.bomb5X = 20+randrange(0,10)*40
            app.bomb5Y = 20+randrange(0,10)*40
            bomb5.centerX=app.bomb5X
            bomb5.centerY=app.bomb5Y
        if(bomb8.hitsShape(bomb5)==True):
            app.bomb6X = 20+randrange(0,10)*40
            app.bomb6Y = 20+randrange(0,10)*40
            bomb6.centerX=app.bomb6X
            bomb6.centerY=app.bomb6Y
        if(bomb8.hitsShape(bomb6)==True):
            app.bomb7X = 20+randrange(0,10)*40
            app.bomb7Y = 20+randrange(0,10)*40
            bomb7.centerX=app.bomb7X
            bomb7.centerY=app.bomb7Y
        if(bomb8.hitsShape(bomb7)==True):
            app.bomb8X = 20+randrange(0,10)*40
            app.bomb8Y = 20+randrange(0,10)*40
            bomb8.centerX=app.bomb8X
            bomb8.centerY=app.bomb8Y
        if(bomb8.hitsShape(bomb9)==True):
            app.bomb9X = 20+randrange(0,10)*40
            app.bomb9Y = 20+randrange(0,10)*40
            bomb9.centerX=app.bomb9X
            bomb9.centerY=app.bomb9Y
        if(bomb8.hitsShape(bomb10)==True):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
            bomb10.centerX=app.bomb10X
            bomb10.centerY=app.bomb10Y 
            
        if(bomb9.hitsShape(bomb1)==True):
            app.bomb2X = 20+randrange(0,10)*40
            app.bomb2Y = 20+randrange(0,10)*40
            bomb2.centerX=app.bomb2X
            bomb2.centerY=app.bomb2Y
        if(bomb9.hitsShape(bomb2)==True):
            app.bomb3X = 20+randrange(0,10)*40
            app.bomb3Y = 20+randrange(0,10)*40
            bomb3.centerX=app.bomb3X
            bomb3.centerY=app.bomb3Y
        if(bomb9.hitsShape(bomb3)==True):
            app.bomb4X = 20+randrange(0,10)*40
            app.bomb4Y = 20+randrange(0,10)*40
            bomb4.centerX=app.bomb4X
            bomb4.centerY=app.bomb4Y
        if(bomb9.hitsShape(bomb4)==True):
            app.bomb5X = 20+randrange(0,10)*40
            app.bomb5Y = 20+randrange(0,10)*40
            bomb5.centerX=app.bomb5X
            bomb5.centerY=app.bomb5Y
        if(bomb9.hitsShape(bomb5)==True):
            app.bomb6X = 20+randrange(0,10)*40
            app.bomb6Y = 20+randrange(0,10)*40
            bomb6.centerX=app.bomb6X
            bomb6.centerY=app.bomb6Y
        if(bomb9.hitsShape(bomb6)==True):
            app.bomb7X = 20+randrange(0,10)*40
            app.bomb7Y = 20+randrange(0,10)*40
            bomb7.centerX=app.bomb7X
            bomb7.centerY=app.bomb7Y
        if(bomb9.hitsShape(bomb7)==True):
            app.bomb8X = 20+randrange(0,10)*40
            app.bomb8Y = 20+randrange(0,10)*40
            bomb8.centerX=app.bomb8X
            bomb8.centerY=app.bomb8Y
        if(bomb9.hitsShape(bomb8)==True):
            app.bomb9X = 20+randrange(0,10)*40
            app.bomb9Y = 20+randrange(0,10)*40
            bomb9.centerX=app.bomb9X
            bomb9.centerY=app.bomb9Y
        if(bomb9.hitsShape(bomb10)==True):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
            bomb10.centerX=app.bomb10X
            bomb10.centerY=app.bomb10Y 
            
        if(bomb10.hitsShape(bomb1)==True):
            app.bomb2X = 20+randrange(0,10)*40
            app.bomb2Y = 20+randrange(0,10)*40
            bomb2.centerX=app.bomb2X
            bomb2.centerY=app.bomb2Y
        if(bomb10.hitsShape(bomb2)==True):
            app.bomb3X = 20+randrange(0,10)*40
            app.bomb3Y = 20+randrange(0,10)*40
            bomb3.centerX=app.bomb3X
            bomb3.centerY=app.bomb3Y
        if(bomb10.hitsShape(bomb3)==True):
            app.bomb4X = 20+randrange(0,10)*40
            app.bomb4Y = 20+randrange(0,10)*40
            bomb4.centerX=app.bomb4X
            bomb4.centerY=app.bomb4Y
        if(bomb10.hitsShape(bomb4)==True):
            app.bomb5X = 20+randrange(0,10)*40
            app.bomb5Y = 20+randrange(0,10)*40
            bomb5.centerX=app.bomb5X
            bomb5.centerY=app.bomb5Y
        if(bomb10.hitsShape(bomb5)==True):
            app.bomb6X = 20+randrange(0,10)*40
            app.bomb6Y = 20+randrange(0,10)*40
            bomb6.centerX=app.bomb6X
            bomb6.centerY=app.bomb6Y
        if(bomb10.hitsShape(bomb6)==True):
            app.bomb7X = 20+randrange(0,10)*40
            app.bomb7Y = 20+randrange(0,10)*40
            bomb7.centerX=app.bomb7X
            bomb7.centerY=app.bomb7Y
        if(bomb10.hitsShape(bomb7)==True):
            app.bomb8X = 20+randrange(0,10)*40
            app.bomb8Y = 20+randrange(0,10)*40
            bomb8.centerX=app.bomb8X
            bomb8.centerY=app.bomb8Y
        if(bomb10.hitsShape(bomb8)==True):
            app.bomb9X = 20+randrange(0,10)*40
            app.bomb9Y = 20+randrange(0,10)*40
            bomb9.centerX=app.bomb9X
            bomb9.centerY=app.bomb9Y
        if(bomb10.hitsShape(bomb9)==True):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
            bomb10.centerX=app.bomb10X
            bomb10.centerY=app.bomb10Y 
            
    Cover.opacity=50
    if(app.bomb1X==app.bomb2X):
        if(app.bomb1Y==app.bomb2Y):
            app.bomb2X = 20+randrange(0,10)*40
            app.bomb2Y = 20+randrange(0,10)*40
    elif(app.bomb2X==app.bomb3X):
        if(app.bomb2Y==app.bomb3Y):
            app.bomb3X = 20+randrange(0,10)*40
            app.bomb3Y = 20+randrange(0,10)*40
    elif(app.bomb3X==app.bomb4X):
        if(app.bomb3Y==app.bomb4Y):
            app.bomb4X = 20+randrange(0,10)*40
            app.bomb4Y = 20+randrange(0,10)*40
    elif(app.bomb4X==app.bomb5X):
        if(app.bomb4Y==app.bomb5Y):
            app.bomb5X = 20+randrange(0,10)*40
            app.bomb5Y = 20+randrange(0,10)*40
    elif(app.bomb5X==app.bomb6X):
        if(app.bomb5Y==app.bomb6Y):
            app.bomb6X = 20+randrange(0,10)*40
            app.bomb6Y = 20+randrange(0,10)*40
    elif(app.bomb6X==app.bomb7X):
        if(app.bomb6Y==app.bomb7Y):
            app.bomb7X = 20+randrange(0,10)*40
            app.bomb7Y = 20+randrange(0,10)*40
            
    elif(app.bomb7X==app.bomb8X):
        if(app.bomb7Y==app.bomb8Y):
            app.bomb8X = 20+randrange(0,10)*40
            app.bomb8Y = 20+randrange(0,10)*40
            
    elif(app.bomb8X==app.bomb9X):
        if(app.bomb8Y==app.bomb9Y):
            app.bomb9X = 20+randrange(0,10)*40
            app.bomb9Y = 20+randrange(0,10)*40
            
    elif(app.bomb9X==app.bomb10X):
        if(app.bomb9Y==app.bomb10Y):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
            
    elif(app.bomb10X==app.bomb1X):
        if(app.bomb10Y==app.bomb1Y):
            app.bomb10X = 20+randrange(0,10)*40
            app.bomb10Y = 20+randrange(0,10)*40
        
    if(app.ran==True):
        for number in numberGroup:
            for g in Cover:
                if(number.value==0):
                    if(g.hits(number.centerX-20,number.centerY) == True):
                        Cover.remove(g)
                        
                    if(g.hits(number.centerX+20,number.centerY) == True):
                        Cover.remove(g)
                    
                    if(g.hits(number.centerX,number.centerY-20) == True):
                        Cover.remove(g)
                        
                    if(g.hits(number.centerX,number.centerY+20) == True):
                        Cover.remove(g)
        
    bomb1.centerX=app.bomb1X
    bomb2.centerX=app.bomb2X
    bomb3.centerX=app.bomb3X
    bomb4.centerX=app.bomb4X
    bomb5.centerX=app.bomb5X
    bomb6.centerX=app.bomb6X
    bomb7.centerX=app.bomb7X
    bomb8.centerX=app.bomb8X
    bomb9.centerX=app.bomb9X
    bomb10.centerX=app.bomb10X
    bomb1.centerY=app.bomb1Y
    bomb2.centerY=app.bomb2Y
    bomb3.centerY=app.bomb3Y
    bomb4.centerY=app.bomb4Y
    bomb5.centerY=app.bomb5Y
    bomb6.centerY=app.bomb6Y
    bomb7.centerY=app.bomb7Y
    bomb8.centerY=app.bomb8Y
    bomb9.centerY=app.bomb9Y
    bomb10.centerY=app.bomb10Y
    
    if(len(Cover.children)<=10):
        if(len(Cover.children)>0):
            Cover.clear()
            win()
    
    Wins.value=app.wins
    Wins.left=262

def cover()  :      
    for i in range (0,400,40):
            for j in range(0,400,40):
                Cover.add(Rect(i,j,40,40,fill='grey',border='black',borderWidth=1))

cover()

def onMousePress(mouseX, mouseY):
    start(app.ran)
    app.ran=True
    for g in Cover:
        if(g.hits(mouseX,mouseY) == True):
            Cover.remove(g)
            
    for bomb in bombGroup:
        if(((mouseX >= bomb.centerX-20) and (mouseX <= bomb.centerX+20)) and ((mouseY >= bomb.centerY-20) and (mouseY <= bomb.centerY+20))):
            lose()
            
        if(bomb.hits(mouseX,mouseY)==True):
            lose()
            
def onKeyPress(key):
    if('enter'==key):
        Cover.clear()
        cover()
        lose1.opacity=0
        lose2.opacity=0
        lose3.opacity=0
        win1.opacity=0
        win2.opacity=0
        win1.opacity=0
        Wins.opacity=0
        Win.opacity=0
        grid.fill='lime'
        resetValue()
        app.bomb1X = 20+randrange(0,10)*40
        app.bomb2X = 20+randrange(0,10)*40
        app.bomb3X = 20+randrange(0,10)*40
        app.bomb4X = 20+randrange(0,10)*40
        app.bomb5X = 20+randrange(0,10)*40
        app.bomb6X = 20+randrange(0,10)*40
        app.bomb7X = 20+randrange(0,10)*40
        app.bomb8X = 20+randrange(0,10)*40
        app.bomb9X = 20+randrange(0,10)*40
        app.bomb10X = 20+randrange(0,10)*40
        
        app.bomb1Y = 20+randrange(0,10)*40
        app.bomb2Y = 20+randrange(0,10)*40
        app.bomb3Y = 20+randrange(0,10)*40
        app.bomb4Y = 20+randrange(0,10)*40
        app.bomb5Y = 20+randrange(0,10)*40
        app.bomb6Y = 20+randrange(0,10)*40
        app.bomb7Y = 20+randrange(0,10)*40
        app.bomb8Y = 20+randrange(0,10)*40
        app.bomb9Y = 20+randrange(0,10)*40
        app.bomb10Y = 20+randrange(0,10)*40
        
        if(app.bomb1X==app.bomb2X):
            if(app.bomb1Y==app.bomb2Y):
                app.bomb2X = 20+randrange(0,10)*40
                app.bomb2Y = 20+randrange(0,10)*40
            
        elif(app.bomb2X==app.bomb3X):
            if(app.bomb2Y==app.bomb3Y):
                app.bomb3X = 20+randrange(0,10)*40
                app.bomb3Y = 20+randrange(0,10)*40
                
        elif(app.bomb3X==app.bomb4X):
            if(app.bomb3Y==app.bomb4Y):
                app.bomb4X = 20+randrange(0,10)*40
                app.bomb4Y = 20+randrange(0,10)*40
                
        elif(app.bomb4X==app.bomb5X):
            if(app.bomb4Y==app.bomb5Y):
                app.bomb5X = 20+randrange(0,10)*40
                app.bomb5Y = 20+randrange(0,10)*40
                
        elif(app.bomb5X==app.bomb6X):
            if(app.bomb5Y==app.bomb6Y):
                app.bomb6X = 20+randrange(0,10)*40
                app.bomb6Y = 20+randrange(0,10)*40
                
        elif(app.bomb6X==app.bomb7X):
            if(app.bomb6Y==app.bomb7Y):
                app.bomb7X = 20+randrange(0,10)*40
                app.bomb7Y = 20+randrange(0,10)*40
                
        elif(app.bomb7X==app.bomb8X):
            if(app.bomb7Y==app.bomb8Y):
                app.bomb8X = 20+randrange(0,10)*40
                app.bomb8Y = 20+randrange(0,10)*40
                
        elif(app.bomb8X==app.bomb9X):
            if(app.bomb8Y==app.bomb9Y):
                app.bomb9X = 20+randrange(0,10)*40
                app.bomb9Y = 20+randrange(0,10)*40
                
        elif(app.bomb9X==app.bomb10X):
            if(app.bomb9Y==app.bomb10Y):
                app.bomb10X = 20+randrange(0,10)*40
                app.bomb10Y = 20+randrange(0,10)*40
                
        elif(app.bomb10X==app.bomb1X):
            if(app.bomb10Y==app.bomb1Y):
                app.bomb10X = 20+randrange(0,10)*40
                app.bomb10Y = 20+randrange(0,10)*40
        
        app.ran=False
        
lose1 = Label("KABOOM!",200,160,size=40,font='arial',bold=True,italic=False,fill='white',border='orangered',borderWidth=2,opacity=0,rotateAngle=0,align='center',visible=True)
lose2 = Label("Game Over",200,200,size=40,font='arial',bold=True,italic=False,fill='white',border='orangered',borderWidth=2,opacity=0,rotateAngle=0,align='center',visible=True)
lose3 = Label("Press Enter to Restart",200,280,size=35,font='arial',bold=True,italic=False,fill='white',border='orangered',borderWidth=2,opacity=0,rotateAngle=0,align='center',visible=True)
win1 = Label("KABOOM!",200,160,size=40,font='arial',bold=True,italic=False,fill='white',border='green',borderWidth=2,opacity=0,rotateAngle=0,align='center',visible=True)
win2 = Label("Game Over",200,200,size=40,font='arial',bold=True,italic=False,fill='white',border='green',borderWidth=2,opacity=0,rotateAngle=0,align='center',visible=True)
win3 = Label("Press Enter to Restart",200,280,size=35,font='arial',bold=True,italic=False,fill='white',border='green',borderWidth=2,opacity=0,rotateAngle=0,align='center',visible=True)
Wins = Label(0,262,240,size=40,font='arial',bold=True,italic=False,fill='white',border='black',borderWidth=2,opacity=0,rotateAngle=0,align='left',visible=True)
Win = Label("Wins =",183,240,size=40,font='arial',bold=True,italic=False,fill='white',border='black',borderWidth=2,opacity=0,rotateAngle=0,align='center',visible=True)

def lose():
    Cover.clear()
    Wins.border='orangered'
    Win.border='orangered'
    lose1.opacity=100
    lose2.opacity=100
    lose3.opacity=100
    Wins.opacity=100
    Win.opacity=100
    for bomb in bombGroup:
        for box in grid:
            if(box.hits(bomb.centerX,bomb.centerY)==True):
                box.fill='red'
                
def win():
    app.wins+=1
    Wins.border='green'
    Win.border='green'
    win1.opacity=100
    win2.opacity=100
    win3.opacity=100
    Wins.opacity=100
    Win.opacity=100

cmu_graphics.run()
