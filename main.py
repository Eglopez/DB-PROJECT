import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom

class GoToCommand:

    def __init__(self,x,y,width=1,color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color


    def draw(self,turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x,self.y)

    def __str__(self):
        return ’<Commandx=" ’ +str(self.x) +’"y=" ’ +str(self.y) + \
                '"width=" ’ +str(self.width) ¡"width=" ’ +str(self.width) \
                +’"color="’ + self.color  +’">GoTo </Command>’      

class CircleCommand:

    def __init__(self,radius,width=1,color="black"):
        self.radius = radius
        self.width = width
        self.color = color 

    def draw(self,turtle): 
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)

    def __str__(self):
        return ’<Commandradius=" ’ +str(self.radius) +’"width="’ + \
                str(self.width) +’"color="’+ self.color +’">Circle</Command>’

class BeginFillCommand:

    def __init__(self),color:
        self.color = color

    def draw(self,turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    def __str__(self):
        return ’<Command_color="’+ self.color +’">BeginFill</Command>’

class EndFillCommand:

    def __init__(self):
        pass

    def draw(self,turtle):
        turtle.end_fill()

    def __str__(self):
        return "<Command>EndFill</Command>"

class PenUpCommand:

    def __init__(self):
        pass

    def draw(self,turtle):
        turtle.penup()

    def __str__(self):
        return "<Command>PenUp</Command>"                

class PenDownCommand:

    def __init__(self):
        pass

    def draw(self,turtle):
        turtle.pendown()

    def __str__(self):
        return "<Command>PenDown</Command>"
        

class PyList:

    def __init__(self):
        self.gcList = []

    def append(self,item):
        self.gcList = self.gcList + [item]

    def removeLast(self):
        self.gcList = self.gcList[:-1]

    def __iter__(self):
        for c in self.gcList:
            yield c

    def __len__(self):
        return len(self.gcList)

class DrawingApplication(tkinter.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.graphicsCommands = PyList()                  

