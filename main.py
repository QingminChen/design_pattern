# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# class Subject:
#     """Represents what is being observed"""
#
#     def __init__(self):
#
#         """create an empty observer list"""
#
#         self._observers = []
#
#     def notify(self, modifier=None):
#
#         """Alert the observers"""
#
#         for observer in self._observers:
#             if modifier != observer:
#                 observer.update(self)
#
#     def attach(self, observer):
#
#         """If the observer is not in the list,
#         append it into the list"""
#
#         if observer not in self._observers:
#             self._observers.append(observer)
#
#     def detach(self, observer):
#
#         """Remove the observer from the observer list"""
#
#         try:
#             self._observers.remove(observer)
#         except ValueError:
#             pass
#
#
# class Data(Subject):
#     """monitor the object"""
#
#     def __init__(self, name=''):
#         Subject.__init__(self)
#         self.name = name
#         self._data = 0
#
#     @property
#     def data(self):
#         return self._data
#
#     @data.setter
#     def data(self, value):
#         self._data = value
#         self.notify()
#
#
# class HexViewer:
#     """updates the Hexviewer"""
#
#     def update(self, subject):
#         print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))
#
#
# class OctalViewer:
#     """updates the Octal viewer"""
#
#     def update(self, subject):
#         print('OctalViewer: Subject' + str(subject.name) + 'has data ' + str(oct(subject.data)))
#
#
# class DecimalViewer:
#     """updates the Decimal viewer"""
#
#     def update(self, subject):
#         print('DecimalViewer: Subject % s has data % d' % (subject.name, subject.data))
#
#
# """main function"""
#
# if __name__ == "__main__":
#     """provide the data"""
#
#     obj1 = Data('Data 1')
#     obj2 = Data('Data 2')
#
#     view1 = DecimalViewer()
#     view2 = HexViewer()
#     view3 = OctalViewer()
#
#     obj1.attach(view1)
#     obj1.attach(view2)
#     obj1.attach(view3)
#
#     obj2.attach(view1)
#     obj2.attach(view2)
#     obj2.attach(view3)
#
#     obj1.data = 10
#     obj2.data = 15



# '''State Pattern'''
# class State:
#     """Base state. This is to share functionality"""
#
#     def scan(self):
#         """Scan the dial to the next station"""
#         self.pos += 1
#
#         """check for the last station"""
#         if self.pos == len(self.stations):
#             self.pos = 0
#         print("Visiting... Station is {} {}".format(self.stations[self.pos], self.name))
#
#
# """Separate Class for AM state of the radio"""
#
#
# class AmState(State):
#     """constructor for AM state class"""
#
#     def __init__(self, radio):
#         self.radio = radio
#         self.stations = ["1250", "1380", "1510"]
#         self.pos = 0
#         self.name = "AM"
#
#     """method for toggling the state"""
#
#     def toggle_amfm(self):
#         print("Switching to FM")
#         self.radio.state = self.radio.fmstate
#
#
# """Separate class for FM state"""
#
#
# class FmState(State):
#     """Constriuctor for FM state"""
#
#     def __init__(self, radio):
#         self.radio = radio
#         self.stations = ["81.3", "89.1", "103.9"]
#         self.pos = 0
#         self.name = "FM"
#
#     """method for toggling the state"""
#
#     def toggle_amfm(self):
#         print("Switching to AM")
#         self.radio.state = self.radio.amstate
#
#
# """Dedicated class Radio"""
#
#
# class Radio:
#     """A radio. It has a scan button, and an AM / FM toggle switch."""
#
#     def __init__(self):
#         """We have an AM state and an FM state"""
#         self.fmstate = FmState(self)
#         self.amstate = AmState(self)
#         self.state = self.fmstate
#
#     """method to toggle the switch"""
#
#     def toggle_amfm(self):
#         self.state.toggle_amfm()
#
#     """method to scan """
#
#     def scan(self):
#         self.state.scan()
#
#
# def try_method():
#     print('try_method for executing method')
#
# """ main method """
# if __name__ == "__main__":
#
#     """ create radio object"""
#     radio = Radio()
#     actions1 = [radio.scan] * 3
#     actions2 = [radio.toggle_amfm]
#     actions3 = [radio.scan] * 3
#     actions = actions1 + actions2 + actions3
#     # actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
#     actions *= 2
#
#     '''No use, just for having a try'''
#     # try_method_actions = [try_method]*4
#     # print('try Over')
#     #
#     # for try_method in try_method_actions:
#     #     try_method()
#
#
#     for action in actions:
#         action()


# # Strategy Pattern
# class Item:
#     """Constructor function with price and discount"""
#
#     def __init__(self, price, discount_strategy=None):
#
#         """take price and discount strategy"""
#
#         self.price = price
#         self.discount_strategy = discount_strategy  # it just assigns the function name, but haven' executed it yet
#         print('456')
#
#     """A separate function for price after discount"""
#
#     def price_after_discount(self):
#
#         if self.discount_strategy:
#             discount = self.discount_strategy(self)  # this is the exact actual line to execute the function
#         else:
#             discount = 0
#
#         return self.price - discount
#
#     def __repr__(self):
#
#         statement = "Price: {}, price after discount: {}"
#         return statement.format(self.price, self.price_after_discount())
#
#
# """function dedicated to On Sale Discount"""
#
#
# def on_sale_discount(order):
#     return order.price * 0.25 + 20
#
#
# """function dedicated to 20 % discount"""
#
#
# def twenty_percent_discount(order):
#     return order.price * 0.20
#
#
# class Bunny:
#     def __init__(self, name, hobby):
#         self.name = name
#         self.hobby = hobby
#
#     def __repr__(self): # Be invoked automatically
#         statement = "Bunny: {}, likes: {}"
#         return statement.format(self.name, self.hobby)
#
#
# """main function"""
# if __name__ == "__main__":
#     print(Bunny('Monica','Rest'))
#
#     print(Item(20000))
#
#     """with discount strategy as 20 % discount"""
#     print(Item(20000, discount_strategy=twenty_percent_discount))
#
#     """with discount strategy as On Sale Discount"""
#     print(Item(20000, discount_strategy=on_sale_discount))

# Visitor Method
class Courses_At_GFG:

    def accept(self, visitor):
        visitor.visit(self)

    def teaching(self, visitor):
        print(self, "Taught by ", visitor)

    def studying(self, visitor):
        print(self, "studied by ", visitor)

    def __str__(self):
        return self.__class__.__name__


"""Concrete Courses_At_GFG class: Classes being visited."""


class SDE(Courses_At_GFG): pass


class STL(Courses_At_GFG): pass


class DSA(Courses_At_GFG): pass


""" Abstract Visitor class for Concrete Visitor classes:
 method defined in this class will be inherited by all
 Concrete Visitor classes."""


class Visitor:

    def __str__(self):
        return self.__class__.__name__


""" Concrete Visitors: Classes visiting Concrete Course objects.
 These classes have a visit() method which is called by the
 accept() method of the Concrete Course_At_GFG classes."""


class Instructor(Visitor):
    def visit(self, crop):
        crop.teaching(self)


class Student(Visitor):
    def visit(self, crop):
        crop.studying(self)


"""creating objects for concrete classes"""
sde = SDE()
stl = STL()
dsa = DSA()

"""Creating Visitors"""
instructor = Instructor()
student = Student()

"""Visitors visiting courses"""
sde.accept(instructor)
sde.accept(student)

stl.accept(instructor)
stl.accept(student)

dsa.accept(instructor)
dsa.accept(student)





