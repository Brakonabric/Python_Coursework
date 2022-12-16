def showPosition(pos):
    x = pos.x
    y = pos.y
    print("Pointer is currently at %d, %d" % (x, y))
#root.bind('<Double-1>', callback)
root.bind('<Motion>', showPosition)
