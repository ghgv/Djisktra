import struct

class node:
	
	def __init__(self,name):
		self.name=name
		self.child=[]
		
	def add_children(self,lista):
		self.num_children=len(lista)
		for key,value in lista.items():
			a,b=key,value
			#print(a)
			f=[a,b]
			self.child.append(f)
	def show_children(self):
		print("Number of childrem")
		print((len(self.child)))
		for i in range (len(self.child)):
			print(self.child[i])	
		
level={}
lista={}
visited=[]
nodes=[]
temp_site=""
adjacencia={
"a":{"b":4,"c":3,"d":2},
"b":{"a":4,"c":1,"e":7},
"c":{"a":3,"b":1,"d":3,"f":1},
"d":{"a":2,"c":3,"g":4},
"e":{"b":7,"f":1},
"f":{"e":1,"c":1,"g":5},
"g":{"f":5,"d":4}
}

print (adjacencia)
source=raw_input("Source Node")
destination=raw_input("Destination Node")

if __name__ =="__main__":
	print("\nStarting at node: " + source)
	print("\nDestination node: " + destination + " \n")
	print(adjacencia.get(source))
	level=adjacencia.get(source)
	level = sorted(level.items(), key=lambda kv: kv[1])
	print(level)
	#print(len(level))
	#for i in range( len(level)):
	temp_site,temp_cost=level.pop(0)
	print(temp_site)
	print(temp_cost)
	lista[temp_site]=temp_cost
	visited.append(temp_site)	
	lista = sorted(lista.items(), key=lambda kv: kv[1])
	print(lista)
	print(len(adjacencia))
	root=node(source)
	root.add_children(adjacencia.get(source))
	i=0	
	for keys,values in adjacencia.items():
			a=""
			a,b=keys,values
			f=node(a)
			f.add_children(b)			
			nodes.append(f)
			i=i+1
	len(nodes)
	nodes[0].show_children()
