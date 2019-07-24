#from win32gui import *;
from tkinter import *;
from tkinter import messagebox;
from math import *;

class OtherFrame(Toplevel):
    def __init__(self, original):
        self.original_Window = original
        Toplevel.__init__(self)
        
    def onClose(self):
        self.destroy()
        self.original_frame.show()

class MyApp(object):
    sci_window=None;
    def __init__(self, parent):
        self.root = parent
        
    def hide(self):
        self.root.withdraw()

    def openWindow(self):
        self.hide()
        subFrame = OtherFrame(self)

    def show(self):
        self.root.update()
        self.root.deiconify()

window=Tk();
window.iconbitmap("icon.ico");
window.title("Calculator.py");
window.resizable(0,0);
window.geometry("295x275+600+200");  
    
def openSciWin():
    MyApp.sci_window=OtherFrame(window);
    m1=MyApp(window);
    m1.hide();
    MyApp.sci_window.title("Scientific Mode");
    MyApp.sci_window.iconbitmap("icon.ico");
    MyApp.sci_window.resizable(0,0);
    MyApp.sci_window.geometry("295x275+600+200");
    menubar1= Menu(MyApp.sci_window);
    menubar1.add_command(label="Normal mode",command=openNorWin);
    menubar1.add_command(label="Exit",command=closeWindow);
    MyApp.sci_window.config(menu=menubar1)
    t2=Entry(MyApp.sci_window,text="This is Scientific Widget2",bd=5,width="29",bg="powder blue",fg="black",font=('Arial',13,'bold'))
    t2.grid(column=0,row=0,columnspan=3);
    sci_list=['x!','exp','√x','deg','rad','log e','log 2','log 10','e','sin','cos','tan','sinh','cosh','tanh','gamma','π','e','floor','C','bkspace'];
    #print(len(sci_list))
    l2=[];
    for sci in sci_list:
        l2.append(Button(MyApp.sci_window,text=""+sci,width="10",bg="white",font=("Arial",12)));
    #print(sci);
    ind1=0;        
    if len(sci_list)%3==0:
        endRange1=(len(sci_list)//3)+(1)
    else:
        endRange1=(len(sci_list)//3)+(2)
    for m in range(1,endRange1):
        for n in range(0,3):
            l2[ind1].grid(column=n,row=m);
            l2[ind1].bind("<Button-1>", lambda event, obj=l2[ind1]: getscibutton(event, obj))
            ind1+=1;
        #print(l2);
    try:
        def getscibutton(event,obj):
        #print("Button Clicked is ....\t",event.widget);
            if(obj==l2[len(l1)-1]): #bkspace
                val=t2.get();
                t2.delete(0,END);
                #t2.insert(0,val[:(END-1)]);
                t2.insert(0,val[:(-1)]);   # This inserts val from (0:END-1)
            elif(obj==l2[0]):       #x!
                val=int(t2.get());
                #print(val);
                res=factorial(val);
                t2.delete(0,END);
                t2.insert(0,res)
            elif(obj==l2[1]):       #exp
                val=int(t2.get());
                #print(val);
                res=exp(val);
                t2.insert(0,res)
            elif(obj==l2[2]):       #sqrt
                val=int(t2.get());
                #print(val);
                res=sqrt(val);
                t2.insert(0,res)
            elif(obj==l2[3]):       #deg
                val=int(t2.get());
                #print(val);
                res=degrees(val);
                t2.insert(0,res)
            elif(obj==l2[4]):       #rad
                val=int(t2.get());
                #print(val);
                res=radians(val);
                t2.insert(0,res)
            elif(obj==l2[5]):       #log e
                val=int(t2.get());
                #print(val);
                res=log(val);
                t2.insert(0,res)
            elif(obj==l2[6]):       #log2
                val=int(t2.get());
                #print(val);
                res=log2(val);
                t2.insert(0,res)
            elif(obj==l2[7]):       #log 10
                val=int(t2.get());
                #print(val);
                res=log10(val);
                t2.insert(0,res)
            elif(obj==l2[8]):       #e
                #val=int(t2.get());
                #print(val);
                res=e;
                #print(res);
                t2.insert(END,res)
            elif(obj==l2[9]):       #sin
                val=int(t2.get());
                #print(val);
                res=sin(val);
                t2.insert(0,res)
            elif(obj==l2[10]):      #cos
                val=int(t2.get());
                #print(val);
                res=cos(val);
                t2.insert(0,res)
            elif(obj==l2[11]):      #tan
                val=int(t2.get());
                #print(val);
                res=tan(val);
                t2.insert(0,res)
            elif(obj==l2[12]):      #sinh
                val=int(t2.get());
                #print(val);
                res=sinh(val);
                t2.insert(0,res)
            elif(obj==l2[13]):      #cosh
                val=int(t2.get());
                #print(val);
                res=cosh(val);
                t2.insert(0,res)
            elif(obj==l2[14]):      #tanh
                val=int(t2.get());
                #print(val);
                res=tanh(val);
                t2.insert(0,res)
            elif(obj==l2[15]):      #gamma
                val=int(t2.get());
                #print(val);
                res=gamma(val);
                t2.insert(0,res)
            elif(obj==l2[16]):      #pi
                #val=int(t2.get());
                #print(val);
                res=pi;
                t2.insert(END,res)
            elif(obj==l2[17]):      #fabs
                val=int(t2.get());
                #print(val);
                res=fabs(val);
                t2.insert(0,res)
            elif(obj==l2[18]):      #floor
                val=float(t2.get());
                #print(val);
                res=floor(val);
                t2.delete(0,END);
                t2.insert(0,res)
            elif(obj==l2[19]):      #C
                #val=int(t2.get());
                #print(val);
                t2.delete(0,END);
    except Exception as e:
        messagebox.showinfo("Error", "pls check the value you have entered..!!!")
        print(e);
    finally:
        t2.focus();

        
    """
    sci_list=['x!','exp','√x','deg','rad','log e','log 2','log 10','e',
              'sin','cos','tan','sinh','cosh','tanh',
              'gamma','π','fabs','floor','C','close'];
    """

def openNorWin():
    window.update();
    window.deiconify();
    m2=MyApp(MyApp.sci_window);
    m2.hide();
    
def getbutton(event,obj):
    #print("Button Clicked is ....\t",event.widget);
    if(event.widget==l1[len(l1)-2]):   
        res=eval(t1.get());
        t1.delete(0,END);
        t1.insert(0,res)
    #elif(event.widget==b10):
    elif(obj==l1[10]):
       t1.delete(0,END);
    elif(obj==l1[len(l1)-1]):
        val=t1.get();
        t1.delete(0,END);
        t1.insert(0,val[:-1]);
    else:
        #t1.insert(END,event.widget['text'])
        t1.insert(END,obj['text'])

t1=Entry(window,text="This is Entry Widget1",bd=5,width="29",bg="powder blue",fg="black",font=('Arial',13,'bold'))

tlist=['0','1','2','3','4','5','6','7','8','9','C','00','+','-','*','/','//','%','**','=','bkspace'];
#print(len(tlist));
l1=[];

for i in tlist:
    l1.append(Button(window,text=""+i,width="10",bg="white",font=("Arial",12)));
    #print(i);
#print(l1);

def closeWindow():
        if(messagebox.askokcancel("Exit.py","Do you want to close the Calculator ?")):
            print("Closing the Application...");
            window.destroy();  

backButton=Button(MyApp.sci_window,bg="red",fg="black",text="Back",width="5",height="1")
menubar = Menu(window)
menubar.add_command(label="Scientific-Mode",command=openSciWin)
menubar.add_command(label="Exit",command=closeWindow);
window.config(menu=menubar);

t1.grid(column=0,row=0,columnspan=3);

ind=0;
count=0;

try:
    if len(tlist)%3==0:
        endRange=(len(tlist)//3)+(1)
    else:
        endRange=(len(tlist)//3)+(2)

    for i in range(1,endRange):
        for j in range(0,3):
            l1[ind].grid(column=j,row=i);
            l1[ind].bind("<1>", lambda event, obj=l1[ind]: getbutton(event, obj))
            ind+=1;
    #print(l1);

except Exception as e:
    print(e);
finally:
    window.mainloop();
