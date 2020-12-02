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

    """def __str__(self):
        return ’<Commandx=" ’ +str(self.x) +’"y=" ’ +str(self.y) + \
                '"width=" ’ +str(self.width) ¡"width=" ’ +str(self.width) \
               +’"color="’ + self.color  +’">GoTo </Command>’"""     
         

class CircleCommand:

    def __init__(self,radius,width=1,color="black"):
        self.radius = radius
        self.width = width
        self.color = color 

    def draw(self,turtle): 
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)

    """def __str__(self):
        return ’<Commandradius=" ’ +str(self.radius) +’"width="’ + \
                str(self.width) +’"color="’+ self.color +’">Circle</Command>’"""

class BeginFillCommand:

    def __init__(self,color):
        self.color = color

    def draw(self,turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    """def __str__(self):
        return ’<Command_color="’+ self.color +’">BeginFill</Command>’"""

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

    def buildWindow(self):
        self.master.title("Draw")
        bar = tkinter.Menu(self,master)
        fileMenu = tkinter.Menu(bar,tearoff=0)

        def newWindow():
            theTurtle.clear()
            theTurtle.penup()
            theTurtle.goto(0,0)
            theTurtle.pendown()
            screen.update()
            screen.listen()
            self.graphicsCommands = PyList()

        fileMenu.add_command(label="New",command=newWindow)

        def parse(filename):
            xmldoc = xml.dom.minidom.parse(filename)

            graphicsCommandsElement = xmldoc.getElementsByTagName("GraphicsCommands")[0]
            graphicsCommands = graphicsCommandsElement.getElementsByTagName("command") 

            for commandElement in graphicsCommands:
                print(type(commandElement))
                command = command.firstChild.data.strip()
                attr = commandElement.attributes
                if command == "GoTo":
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    width = float(atrr["width"].value)
                    color = atrr["color"].value.strip()
                    cmd = GoToCommand(x,y,width,color)

                elif command == "Circle":
                    radius = float(attr["radius"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd =CircleCommand(radius,width,color)

                elif command == "BeginFill":
                    color = attr["color"].value.strip()
                    cmd = BeginFillCommand(color)

                elif command == "EndFill":
                    cmd = EndFillCommand()

                elif command == "PenUp":
                    cmd = PenUpCommand()

                elif command == "PenDown":
                    cmd = PenDownCommand()

                else:
                    raise RuntimeError("Unknow_Command:" + command)

                self.graphicsCommands,append(cmd)

        def loadFile():
            filename = tkinter.filedialog.askopenfilename(title="Select_a_Graphic_File")
            newWindow()
            self.graphicsCommands = PyList()
            parse(filename)

            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)

            screen.update()

        fileMenu.add_command(label="Load...",command=loadFile)

        def addToFile():
            filename = tkinter.filedialog.askopenfilename(title="Slect_a_Graphic_File")

            theTurtle,penup()
            theTurtle.goto(0,0)
            theTurtle.pendown()
            theTurtle.pencolor("#000000")
            theTurtle.fillcolor("#000000")
            cmd = PenUpCommand()
            self.graphicsCommands.append(cmd)
            cmd = GoToCommand(0,0,1,"#000000")
            self.graphicsCommands.append(cmd)
            cmd = PenDownCommand
            self.graphicsCommands.append(cmd)
            screen.update()
            parse(filename)

            for cmd in self.graphicsCommands:
                cmd.drwa(theTurtle)
                screen.update()

        fileMenu.add_command(label="Load_Into..",command=addToFile)

        def write(filename):
            file = open( filename , "w")
            file.write('<?xmlversion ="1.0"encoding="UTF−8"standalone="no"?>')
            file.write('<GraphicsCommands >')
            for cmd in self.graphicsCommands:
                file.write(''+str(cmd)+"\n")
            file. write('</GraphicsCommands >')
            file.close()

        def saveFile():
            filename = tkinter.asksaveasfilename(title="Save Picture As")
            write(filename)

        fileMenu.add_command(label="SaveAs...",command=saveFile) 
        fileMenu.add_command(label="Exit",command=self.master.quit)
        bar.add_cascade(label="File",menu=fileMenu) 
        self.master.config(menu=bar)
        canvas = tkinter.Canvas(self,width=600,height=600)
        canvas.pack(side=tkinter.LEFT)
        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.shape("circle")
        screen = theTurtle.getscreen()
        screen.tracer(0)
        sideBar = tkinter.Frame(self,padx=5,pady=5)
        sideBar.pack(side=tkinter.RIGHT,fill=tkinter.BOTH)
        pointLabel = tkinter.Label(ideBar,text="Width")
        pointLabel.pack()
        widthSize = tkinter.StringVar()
        widthEntry = tkinter.Entry(sideBar,textvariable=widthSize)
        widthEntry.pack()
        widthSize.set(str(1))

        radiusLabel = tkinter.Label(sideBar,text="Radius")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar,textvariable=radiusSize)
        radiusSize.set(str(10))

        def circleHandler():

            cmd = CircleCommand(float(radiusSize.get()),float( widthSize.get()),penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()
            
        circleButton = tkinter.Button(sideBar,text ="DrawCircle",command=circleHandler)
        circleButton.pack(fill=tkinter.BOTH)
        screen .colormode(255)
        penLabel = tkinter.Label(sideBar,text="PenColor")
        penLabel.pack()
        penColor = tkinter.StringVar()
        penEntry = tkinter.Entry(sideBar,textvariable=penColor)
        penEntry.pack()
        penColor.set("#000000")

        def getPenColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                #penColor.set(str(color)[−9:−2])
                pass

        penColorButton = tkinter.Button(sideBar, text="PickPenColor",command=getPenColor)
        penColorButton.pack(fill=tkinter.BOTH)
        fillLabel = tkinter.Label(sideBar,text="FillColor")
        fillLabel.pack()
        fillColor = tkinter.StringVar()
        fillEntry = tkinter.Entry(sideBar,textvariable=fillColor)
        fillEntry.pack()
        fillColor.set("#000000")

        def getFillColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                #fillColor.set(str(color)[−9:−2])
                pass

        fillColorButton = \
            tkinter.Button(sideBar, text="PickFillColor",command=getFillColor)
        fillColorButton.pack(fill=tkinter.BOTH) 

        def beginFillHandler():
            cmd = BeginFillCommand(fillColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd) 

        beginFillButton = tkinter.Button(sideBar,text="BeginFill",command=beginFillHandler )
        beginFillButton.pack(fill=tkinter.BOTH)

        def endFillHandler():
            cmd = EndFillCommand()
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd) 

        endFillButton = tkinter.Button(sideBar,text="EndFill",command=endFillHandler)
        endFillButton.pack(fill=tkinter.BOTH)
        penLabel = tkinter.Label(sideBar,text="PenIsDown")
        penLabel.pack()

        def penUpHandler():
            cmd = PenUpCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="PenIsUp")
            self.graphicsCommands.append(cmd)

        penUpButton = tkinter.Button(sideBar, text ="PenUp",command=penUpHandler) 
        penUpButton.pack(fill=tkinter.BOTH)

        def penDownHandler():
            cmd = PenDownCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="PenIsDown")
            self.graphicsCommands.append(cmd)

        penDownButton = tkinter.Button(sideBar, text="PenDown",command=penDownHandler) 
        penDownButton.pack(fill=tkinter.BOTH)

        def clickHandler(x,y):
            cmd = GoToCommand (x,y,float(widthSize.get()),penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        screen.onclick(clickHandler)

        def dragHandler(x,y):
            cmd = GoToCommand(x,y,float(widthSize.get()),penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        theTurtle.ondrag(dragHandler)

        def undoHandler():
            if len(self.graphicsCommands)>0:
                self.graphicsCommands.removeLast()
                theTurtle.clear()
                theTurtle.penup()
                theTurtle.goto(0,0)
                theTurtle.pendown()
                for cmd in self.graphicsCommands:
                    cmd.draw(theTurtle)
                screen.update()
                screen.listen()

        screen.onkeypress(undoHandler, "u")
        screen.listen()

def main():
    root = tkinter.Tk()
    drawingApp = DrawingApplication(root)

    drawingApp.mainloop()
    print("ProgramExecutionCompleted.")

if __name__ == "__main__":
    main()                                                                    
             






