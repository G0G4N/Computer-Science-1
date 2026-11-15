from cmu_graphics import *

app.background = rgb(5,220,0)
Label('Score:',40,20,size=20,bold=True)
score = Label(0,80,21,size=20,bold=True)
score.left=75
control=Line(200,0,200,400,fill=None)
head=Circle(200,250,25,fill='blue')
part1=Circle(200,290,25,fill=rgb(0,11,199))
part2=Circle(200,330,25,fill=rgb(0,14,145))
part3=Circle(200,370,25,fill=rgb(0,13,95))
part4=Circle(200,410,25,fill=rgb(0,0,50))
Net = Group(
    Line(40,50,40,80,fill='saddlebrown',lineWidth=5),
    Polygon(40,0,40,50,-12,28,fill='white'),
    Oval(40,25,30,50,fill='white',border='blue',borderWidth=3),
    )
Net.top=3
Net.centerX=22+randrange(340)
Net.rotateAngle=45
Net.speed=0
menu=Rect(0,0,400,400,fill='blue')
titleText=Label("Snake Game",200,40,size=50,fill='White',bold=True)
menuText=Label("Pick a dificulty.",200,100,size=20,fill='White',bold=True)
menuText2=Label("Move with the arrow or WASD keys.",200,120,size=20,fill='White',bold=True)
menuText3=Label("Don't get caught by the net!",200,140,size=20,fill='White',bold=True)
easy=Rect(200,200,100,40,align='center')
easyText=Label("Easy",200,200,fill='white',size=20,bold=True)
medium=Rect(200,280,100,40,align='center')
mediumText=Label("Medium",200,280,fill='white',size=20,bold=True)
hard=Rect(200,360,100,40,align='center')
hardText=Label("Hard",200,360,fill='white',size=20,bold=True)
loss=Rect(0,0,400,400,fill='blue')
lossText=Label("You've Lost",200,120,size=50,fill='White',bold=True)
goMenu=Rect(200,200,100,40,align='center')
goMenuText=Label("Menu",200,200,fill='white',size=20,bold=True)
Loss=Group(
    )
Loss.add(loss)
Loss.add(lossText)
Loss.add(goMenu)
Loss.add(goMenuText)
Loss.centerX=600
Menu=Group(
    )
Menu.add(menu)
Menu.add(titleText)
Menu.add(menuText)
Menu.add(menuText2)
Menu.add(menuText3)
Menu.add(easy)
Menu.add(easyText)
Menu.add(medium)
Menu.add(mediumText)
Menu.add(hard)
Menu.add(hardText)
def onMousePress(mouseX,mouseY):
    if(easy.hits(mouseX,mouseY)==True):
        Net.speed=3
        Menu.centerX=600
        Net.centerX=29+randrange(341)
        Net.bottom=-10
        Net.width=68
        Net.height=80
    if(medium.hits(mouseX,mouseY)==True):
        Net.speed=5
        Menu.centerX=600
        Net.centerX=29+randrange(341)
        Net.bottom=-10
        Net.width=78
        Net.height=90
    if(hard.hits(mouseX,mouseY)==True):
        Net.speed=9
        Menu.centerX=600
        Net.centerX=29+randrange(341)
        Net.bottom=-10
        Net.width=98
        Net.height=110
    if(goMenu.hits(mouseX,mouseY)==True):
        Menu.centerX=200
        Loss.centerX=600
def onKeyHold(keys):
    if(control.centerX<375):
        if('right' in keys):
            control.centerX+=5
    if(control.centerX>25):
        if('left' in keys):
            control.centerX-=5
    if(control.centerX<375):
        if('d' in keys):
            control.centerX+=5
    if(control.centerX>25):
        if('a' in keys):
            control.centerX-=5
def onStep():
    head.centerX=control.centerX
    if(part1.centerX<head.centerX):
        if(part1.centerX>head.left+10):
            part1.centerX+=2
        else:
            part1.centerX=head.left+11
    if(part1.centerX>head.centerX):
        if(part1.centerX<head.right-10):
            part1.centerX-=2
        else:
            part1.centerX=head.right-11
    if(part2.centerX<part1.centerX):
        if(part2.centerX>part1.left+10):
            part2.centerX+=2
        else:
            part2.centerX=part1.left+11
    if(part2.centerX>head.centerX):
        if(part2.centerX<part1.right-10):
            part2.centerX-=2
        else:
            part2.centerX=part1.right-11
    if(part3.centerX<part2.centerX):
        if(part3.centerX>part2.left+10):
            part3.centerX+=2
        else:
            part3.centerX=part2.left+11
    if(part3.centerX>head.centerX):
        if(part3.centerX<part2.right-10):
            part3.centerX-=2
        else:
            part3.centerX=part2.right-11
    if(part4.centerX<part3.centerX):
        if(part4.centerX>part3.left+10):
            part4.centerX+=2
        else:
            part4.centerX=part3.left+11
    if(part4.centerX>head.centerX):
        if(part4.centerX<part3.right-10):
            part4.centerX-=2
        else:
            part4.centerX=part3.right-11
    Net.centerY+=Net.speed
    if(Net.top>410):
        Net.bottom=-10
        Net.centerX=29+randrange(341)
        score.value+=1
        score.left=75
    if(Net.left<0):
        Net.left=0
    if(Net.right>400):
        Net.right=400
    if(head.hitsShape(Net)==True):
        Net.speed=0
        Loss.centerX=200
        Net.bottom=-10

cmu_graphics.run()
