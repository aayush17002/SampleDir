from copy import *
class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return '('+self.x+','+self.y+')'
class Rectangle:
	def __init__(self,Pt1,Pt2):
		self.Pt1=deepcopy(Pt1)
		self.Pt2=deepcopy(Pt2)
		if Pt1.x>Pt2.x and Pt1.y>Pt2.y:
			self.Pt1=Pt2
			self.Pt2=Pt1
		elif Pt1.x>Pt2.x:
			self.Pt1.x=Pt2.x
			self.Pt1.y=Pt1.y
			self.Pt2.x=Pt1.x
			self.Pt2.y=Pt2.y
		elif Pt1.y>Pt2.y:
			self.Pt1.x=Pt1.x
			self.Pt1.y=Pt2.y
			self.Pt2.x=Pt2.x
			self.Pt2.y=Pt1.y
		else:
			pass
	def __add__(self,other):
		self.ptt1=deepcopy(self.Pt1)
		self.ptt2=deepcopy(self.Pt2)
		self.s1=min(self.Pt1.x,other.Pt1.x)
		self.s2=min(self.Pt1.y,other.Pt1.y)
		self.o1=max(self.Pt2.x,other.Pt2.x)
		self.o2=max(self.Pt2.y,other.Pt2.y)
		self.ptt1.x=self.s1
		self.ptt1.y=self.s2
		self.ptt2.x=self.o1
		self.ptt2.y=self.o2
		return Rectangle(self.ptt1,self.ptt2)
	def __str__(self):
		return '(('+str(self.Pt1.x)+','+str(self.Pt1.y)+')'+','+'('+str(self.Pt2.x)+','+str(self.Pt2.y)+'))'
def myfunc(L):
	return L.Pt1.x
if __name__ == '__main__':
	p1=Point(2,3)
	p2=Point(9,0)
	R1=Rectangle(p1,p2)
	p3=Point(1,2)
	p4=Point(6,6)
	R2=Rectangle(p3,p4)
	# print(R2)
	R3=R1+R2
	# print(R3)
	p5=Point(4,4)
	p6=Point(2,9)
	R4=Rectangle(p5,p6)
	# print(R4)
	L=[R1,R2,R3]
	for i in L:
		print(i)
	L.sort(key=myfunc)
	a=''
	for i in L:
		if a!='':
			a+=','+str(i)
		else:
			a+=str(i)
	print(a)