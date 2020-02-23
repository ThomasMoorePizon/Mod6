class Rectangle:
	"""This class creates rectangle objects"""
	
	def __init__ (self, location, w, h):
		"""Initialize the rectangle"""
		self.corner = location
		self.width = w
		self.height = h

	def __str__ (self):
		"""Prints the rectangle"""
		return "({0},{1},{2})".format(self.corner,self.width,self.height)

	def display (self):
		"""Prints the rectangle as a single string"""
		return(self.corner.get_x(),self.corner.get_y(),self.width,self.height)

	def get_corner (self):
		return (self.corner)

	def get_corner_x (self):
		return Point.get_x(self.corner)

	def set_corner_x (self, x):
		Point.set_x(self.corner,x)

	def set_corner_y (self, y):
		Point.set_y(self.corner,y)

	def get_corner_y (self):
		return Point.get_y(self.corner)

	def set_corner (self, x, y):
		Rectangle.set_corner_x(self,x)
		Rectangle.set_corner_y(self,y)

	def get_width (self):
		return self.width

	def get_height (self):
		return self.height

	def set_width (self, w):
		self.width = w

	def set_height (self, h):
		self.height = h

class Point:
	"""This class creates a point"""

	def __init__ (self,x,y):
		"""Initialize the point"""
		self.x = x
		self.y = y

	def __str__ (self):
		"""Prints the point"""
		return "({0},{1})".format(self.x,self.y)

	def display(self):
		"""Prints a point as a list"""
		return(self.x,self.y)

	def get_x (self):
		return self.x

	def get_y(self):
		return self.y

	def set_x (self, x):
		self.x = x

	def set_y (self, y):
		self.y = y


