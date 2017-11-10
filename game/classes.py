class Place(object):
	def __init__(self, name, desc, neighbors=[]):
		self.name= name
		self.desc = desc
		self.neighbors = neighbors
		for n in self.neighbors:
			n.addneighbor(self)

	def addneighbor(self, neighbor):
		self.neighbors.append(neighbor)


Home = Place('Home','Place You Live')
Forest = Place('Forest','Place to Find Wood',[Home])
Mines = Place('Mines','Place You Get Ore',[Home,Forest])