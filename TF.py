import Thomas

def create_point (x,y):
	return Thomas.Point(x,y)

def str_point (dot):
	return dot.display()

def shift_rectangle (shape, movex, movey):
	newx = Thomas.Rectangle.get_corner_x(shape) + movex
	newy = Thomas.Rectangle.get_corner_y(shape) + movey
	Thomas.Rectangle.set_corner_x(shape,newx)
	Thomas.Rectangle.set_corner_y(shape,newy)

def offset_rectangle (shape, movex, movey):
	newx = Thomas.Rectangle.get_corner_x(shape) + movex
	newy = Thomas.Rectangle.get_corner_y(shape) + movey
	w = Thomas.Rectangle.get_width(shape)
	h = Thomas.Rectangle.get_height(shape)
	return create_rectangle(newx,newy,w,h)

def create_rectangle (x,y,w,h):
	return Thomas.Rectangle(create_point(x,y),w,h)

def str_rectangle (shape):
	return shape.display()



