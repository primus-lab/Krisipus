# KRISIPUS - Lakointeligentni generator tautologija

from random import random, choice
from formula import Atom
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import  Frame, Label, Entry, Radiobutton, Button, Style, Combobox 

class Krisipus(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()
	
	def initUI(self):
		self.parent.title("Χρύσιππος")
		self.pack(fill=BOTH, expand=True)
		
		global value
		value = 0
		
		
		
		global num
		num = StringVar()
		
		
		global res
		res = StringVar()

        
		
        
      
		frame1 = Frame(self,style='My.TFrame')
		frame1.pack(fill=X)
		
		lbl1 = Label(frame1, text="Izaberi broj iskaznih slova :", width=25,foreground='white',background='royal blue')
		lbl1.pack(side=LEFT, padx=5, pady=5)
		
		option = Combobox(frame1, textvariable=num, width='3')
		option['values'] =('1','2','3','4')
		option.current(1)
		option.pack(side=LEFT, padx=5, pady=1)
		
		
		
		frame2 = Frame(self,style='My.TFrame')
		frame2.pack(fill=X)
		
		lbl2 = Label(frame2, text="Tautologija :", width=12,foreground='white',background='royal blue')
		lbl2.pack(side=LEFT, padx=5, pady=5)
		
		result = Entry(frame2, textvariable=res, width=85,background='royal blue')
		result.pack(side=LEFT, padx=5, pady=1)
		
		frame3 = Frame(self,style='My.TFrame')
		frame3.pack(fill=X)
		
		btngenerate = Button(frame3, text="Generiši", width=10, command=self.test,style='My.TButton')
		btngenerate.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
		btnclose = Button(frame3, text="Zatvori", width=10, command=self.quit,style='My.TButton')
		btnclose.pack(side=RIGHT, anchor=N, padx=5, pady=5)
		
		btnclear = Button(frame3, text="Izbriši", width=10, command=self.clear,style='My.TButton')
		btnclear.pack(side=RIGHT, anchor=N, padx=5, pady=5)
		
		
		
	def errorMsg(self,msg):
		if msg == 'error':
			tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
		elif msg == 'errc':
			tkinter.messagebox.showerror('Error!', 'Number must be greater than two')
	
	def test(self):
		try:
			i=int(num.get())
			p = Atom('p')
			q = Atom('q')
			r = Atom('r')
			s = Atom('s')
			UNARIES = ["~%s"]
			BINARIES = ["%s | %s", "%s & %s", "%s >> %s", "%s << %s"]
			PROP_PARANTHESIS = 0.3
			PROP_BINARY = 0.7
			
			def condition(i,ex):
				if i==1:
					return('p' in ex and len(ex)<15)
				elif i==2:
					return('p' in ex and 'q' in ex and len(ex)<25)
				elif i==3:
					return('p' in ex and 'q' in ex and 'r' in ex and len(ex)<35)
				elif i==4:
					return('p' in ex and 'q' in ex and 'r' in ex and 's' in ex and len(ex)<42)
				
			if i==1:
				scope=[c for c in "p"]
			elif i==2:
				scope=[c for c in "pq"]
			elif i==3:
				scope=[c for c in "pqr"]
			elif i==4:
				scope=[c for c in "pqrs"]
			
			l=list(scope)
			j=0
			
			for _ in range(1000):
				if j==1:
					break
				else:
					scope=l
					scope = list(scope) # make a copy first, append as we go
					for _ in range(70000):
						if random() < PROP_BINARY: # decide unary or binary operator
							ex = choice(BINARIES) % (choice(scope), choice(scope))
							if random() < PROP_PARANTHESIS:
								ex = "(%s)" % ex
							if condition(i,ex):	
								if eval(ex).t()==None:
									value=str(eval(ex))[1:-1]
									res.set(self.makeAsItIs(value))
									j=1
									break
							scope.append(ex)
						else:
							ex = choice(UNARIES) % choice(scope)
							if condition(i,ex):
								if eval(ex).t()==None:
									value=str(eval(ex))[1:-1]
									res.set(self.makeAsItIs(value))
									j=1
									break
							scope.append(ex)
		except:
			self.errorMsg('error')
			
	def clear(self):
		try:
			res.set('')
			
		
		except:
			self.errorMsg('error')
	
	def makeAsItIs(self, value):
		return value

			
def main():
    root = Tk()
    root.resizable(0,0)
    s = Style()
    s.configure('My.TFrame', background='royal blue')
    s.configure('My.TButton', background='light gray')
    s.configure('My.TEntry', fieldbackground='light gray')
    s.configure('My.TRadiobutton', background='royal blue')
    s.map('My.TRadiobutton', background=[('active', '#FFC133')])
    root.geometry("480x88")
    krisipus = Krisipus(root)
    root.mainloop()

if __name__ == '__main__':
	main()

