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

#
# class Story():
#     """
#     Interface for story creation
#     """
#
#     def create_story(self):
#         pass
#
# class ConcreteStory(Story):
#     """
#     Implements interface Story
#     """
#
#     _story = "Creating story on ...\n"
#
#     def create_story(self):
#         return self._story
#
#
# # Since class StoryDecorator inherits Story this represents
# # "is-a" relatonship
# class StoryDecorator(Story):
#
#     """
#     base class for decorators
#     """
#
#     def __init__(self, decorated_story):
#         # this is for "has-a" relationship with Story class
#         self.decorated_story = decorated_story
#
#     def create_story(self):
#         return self.decorated_story.create_story()
#
# class Facebook(StoryDecorator):
#
#     _platform = "Facebook"
#
#     def __init__(self, decorated_story):
#         super().__init__(decorated_story)
#
#     def create_story(self):
#         return f"{self.decorated_story.create_story()}- {self._platform}\n"
#
# class Instagram(StoryDecorator):
#
#     _platform = "Instagram"
#
#     def __init__(self, decorated_story):
#         super().__init__(decorated_story)
#
#     def create_story(self):
#         return f"{self.decorated_story.create_story()}- {self._platform}\n"
#
# class Whatsapp(StoryDecorator):
#
#     _platform = "Whatsapp"
#
#     def __init__(self, decorated_story):
#         super().__init__(decorated_story)
#
#     def create_story(self):
#         return f"{self.decorated_story.create_story()}- {self._platform}\n"
#
# class Linkedin(StoryDecorator):
#
#     _platform = "Linkedin"
#
#     def __init__(self, decorated_story):
#         super().__init__(decorated_story)
#
#     def create_story(self):
#         return f"{self.decorated_story.create_story()}- {self._platform}\n"
#
# class Snapchat(StoryDecorator):
#
#     _platform = "Snapchat"
#
#     def __init__(self, decorated_story):
#         super().__init__(decorated_story)
#
#     def create_story(self):
#         return f"{self.decorated_story.create_story()}- {self._platform}\n"
#
# def show_off():
#     my_story = ConcreteStory()
#     my_story = Facebook(Instagram(Whatsapp(Linkedin(Snapchat(my_story)))))
#     print("Activating show off mode. Let's flood it on the platforms!")
#     print(my_story.create_story())
#
# def professional():
#     my_story = ConcreteStory()
#     my_story = Linkedin(my_story)
#     print("Let's keep it professional")
#     print(my_story.create_story())
#
# if __name__ == '__main__':
#     show_off()
#     professional()

#
# class College:
#     '''Resource-intensive object'''
#
#     def studyingInCollege(self):
#         print("Studying In College....")
#
#
# class CollegeProxy:
#     '''Relatively less resource-intensive proxy acting as middleman.
#      Instantiates a College object only if there is no fee due.'''
#
#     def __init__(self):
#
#         self.feeBalance = 1000
#         self.college = None
#
#     def studyingInCollege(self):
#
#         print("Proxy in action. Checking to see if the balance of student is clear or not...")
#         if self.feeBalance <= 500:
#             # If the balance is less than 500, let him study.
#             self.college = College()
#             self.college.studyingInCollege()
#         else:
#
#             # Otherwise, don't instantiate the college object.
#             print("Your fee balance is greater than 500, first pay the fee")
#
#
# """main method"""
#
# if __name__ == "__main__":
#     print(str(id(1))) #140587298777392
#
#     # Instantiate the Proxy
#     collegeProxy = CollegeProxy()
#
#     # Client attempting to study in the college at the default balance of 1000.
#     # Logically, since he / she cannot study with such balance,
#     # there is no need to make the college object.
#     collegeProxy.studyingInCollege()
#
#     # Altering the balance of the student
#     collegeProxy.feeBalance = 100
#
#     # Client attempting to study in college at the balance of 100. Should succeed.
#     collegeProxy.studyingInCollege()

#
# class AbstractHandler(object):
#     """Parent class of all concrete handlers"""
#
#     def __init__(self, nxt):
#         """change or increase the local variable using nxt"""
#
#         self._nxt = nxt
#
#     def handle(self, request):
#         """It calls the processRequest through given request"""
#
#         handled = self.processRequest(request)
#
#         """case when it is not handled"""
#
#         if not handled:
#             self._nxt.handle(request)
#
#     def processRequest(self, request):
#         """throws a NotImplementedError"""
#
#         raise NotImplementedError('First implement it !')
#
#
# class FirstConcreteHandler(AbstractHandler):
#     """Concrete Handler # 1: Child class of AbstractHandler"""
#
#     def processRequest(self, request):
#         '''return True if request is handled '''
#
#         if 'a' < request <= 'e':
#             print("This is {} handling request '{}'".format(self.__class__.__name__, request))
#             return True
#
#
# class SecondConcreteHandler(AbstractHandler):
#     """Concrete Handler # 2: Child class of AbstractHandler"""
#
#     def processRequest(self, request):
#         '''return True if the request is handled'''
#
#         if 'e' < request <= 'l':
#             print("This is {} handling request '{}'".format(self.__class__.__name__, request))
#             return True
#
#
# class ThirdConcreteHandler(AbstractHandler):
#     """Concrete Handler # 3: Child class of AbstractHandler"""
#
#     def processRequest(self, request):
#         '''return True if the request is handled'''
#
#         if 'l' < request <= 'z':
#             print("This is {} handling request '{}'".format(self.__class__.__name__, request))
#             return True
#
#
# class DefaultHandler(AbstractHandler):
#     """Default Handler: child class from AbstractHandler"""
#
#     def processRequest(self, request):
#         """Gives the message that the request is not handled and returns true"""
#
#         print("This is {} telling you that request '{}' has no handler right now.".format(self.__class__.__name__,
#                                                                                           request))
#         return True
#
#
# class User:
#     """User Class"""
#
#     def __init__(self):
#         """Provides the sequence of handles for the users"""
#
#         initial = None
#
#         self.handler = FirstConcreteHandler(SecondConcreteHandler(ThirdConcreteHandler(DefaultHandler(initial))))
#
#     def agent(self, user_request):
#         """Iterates over each request and sends them to specific handles"""
#
#         for request in user_request:
#             self.handler.handle(request)
#
#
# """main method"""
#
# if __name__ == "__main__":
#     """Create a client object"""
#     user = User()
#
#     """Create requests to be processed"""
#
#     string = "GeeksforGeeks"
#     requests = list(string)
#
#     """Send the requests one by one, to handlers as per the sequence of handlers defined in the Client class"""
#     user.agent(requests)


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

#
# class Instructor(Visitor):
#     def visit(self, crop):
#         crop.teaching(self)
#
#
# class Student(Visitor):
#     def visit(self, crop):
#         crop.studying(self)
#
#
# """creating objects for concrete classes"""
# sde = SDE()
# stl = STL()
# dsa = DSA()
#
# """Creating Visitors"""
# instructor = Instructor()
# student = Student()
#
# """Visitors visiting courses"""
# sde.accept(instructor)
# sde.accept(student)
#
# stl.accept(instructor)
# stl.accept(student)
#
# dsa.accept(instructor)
# dsa.accept(student)



# import math
#
# def find_roots(a, b, c):
#     x1_temp = -b + math.sqrt(b**2-4*a*c)
#     x1 = x1_temp/a*(1/2)
#     x2_temp = -b - math.sqrt(b**2-4*a*c)
#     x2 = x2_temp/a*(1/2)
#     if x1==x2:
#        return (x1)
#     else:
#        return (x1,x2)
#     return None
#
# print(find_roots(2, 10, 8));
#
# import collections
#
# Node = collections.namedtuple('Node', ['left', 'right', 'value'])
#
#
# def contains(root, value):
#     # [-10, -3, 0, 5, 9]
#     #
#     # def buildTree(left, right):
#     #     if left > right:
#     #         return None
#     #     m = (left + right) // 2
#     #     return TreeNode(nums[m], buildTree(left, m - 1), buildTree(m + 1, right))
#     #
#     # return buildTree(0, len(nums) - 1)
#     # if
#     pass
#
# n1 = Node(value=1, left=None, right=None)
# n3 = Node(value=3, left=None, right=None)
# n2 = Node(value=2, left=n1, right=n3)
#
# print(contains(n2, 3))


class TextInput:
    def __init__(self, input=None):
        self.input = input
        self.charstring = ''

    def add(self, character):
        self.charstring = charstring + character

    def get_value(self):
        return self.charstring


class NumericInput(TextInput):
    def __init__(self):
        super().__init__()

    def add(self, digits):
        if digits.isdigit():
            self.charstring = self.charstring + str(digits)


if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())





