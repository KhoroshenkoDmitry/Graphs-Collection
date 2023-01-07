from MVC import *

model = Model()
controller = Controller(model)
view = View(controller)
model.subscribe_observer(view)
view.mainloop()