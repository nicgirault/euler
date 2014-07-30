#idee: faire un graph ou chaque nombre represente un noeud
#et ou deux nombres consecutifs representent une relation.
#je creer le graph associe et je supprime les relations en trop
#c'est a dire la situation: 3->1->9 et 3->9, on peut supprimer
#la relation 3->9
#cela donne finalement qu'une seule possibilité (par chance)
class Node:
	def __init__(self, value):
		self.value = value
		self.childs = []
	def addChild(self, node):
		if node not in self.childs:
			self.childs.append(node)
		return
	def removeChild(self, v):
		for node in self.childs:
			if node.value == v:
				self.childs.remove(node)
			
	def getChilds(self):
		return self.childs
	def getChildValues(self):
		return [c.value for c in self.childs]

def grandChilds(node):
	grandChilds = []
	for child in node.getChilds():
		for grandChild in child.getChilds():
			if grandChild not in grandChilds:
				grandChilds.append(grandChild)
	return grandChilds

def getNode(v, nodes):
	for node in nodes:
		if node.value == v:
			return node

def buildStruct(v1, v2, nodes):
	if v1 not in [x.value for x in nodes]:
		Nv1 = Node(v1)
		nodes.append(Nv1)
	else:
		Nv1 = getNode(v1, nodes)
	if v2 not in [x.value for x in nodes]:
		nodes.append(Node(v2))
	if v2 not in Nv1.getChildValues():
		Nv1.addChild(getNode(v2, nodes))
	return nodes

f = open('79.txt')

nodes = []
for line in f.readlines():
	nodes = buildStruct(line[0], line[1], nodes)
	nodes = buildStruct(line[1], line[2], nodes)

for node in nodes:
	for cvalue in node.getChildValues():
		if cvalue in [x.value for x in grandChilds(node)]:
			node.removeChild(cvalue)

for node in nodes:
	print node.value, [x.value for x in node.childs]

