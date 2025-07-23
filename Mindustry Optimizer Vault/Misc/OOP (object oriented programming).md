#### Inheritance

Inheritance is a core OOP concept that allows you to create a new class (the **child class** or subclass) that inherits attributes and methods from an existing class (the **parent class** or superclass).

- **Defining a Child Class:** You define a child class by putting the parent class's name in parentheses after the child class's name.

	```python
    class Parent:
        # Parent's attributes and methods
        pass
    
    class Child(Parent):
        # Child now has access to everything in Parent
        pass
    ```
- **Method Overriding:** A child class can provide its own specific implementation of a method that is already defined in its parent class. This is called method overriding. The most common method to override is __init__().
    
- **Extending Functionality with super():** When you override a method, you often still want to run the code from the parent's version of that method. The super() function allows the child class to call methods from its parent class.
    
    You create your own __init__() method in the child to define its unique attributes. Within that method, you use super().__init__() to execute the parent's __init__() method. This ensures that the object is properly initialized according to both the parent's and the child's logic. After the super() call, you add the new attributes and methods specific to the child class.

    ```python
    class Net(nn.Module):
        def __init__(self):
            # First, run the __init__ of the parent (nn.Module)
            super().__init__()
    
            # Now, add the new attributes unique to the Net class
            self.conv1 = nn.Conv2d(1, 6, 5)
            self.fc1 = nn.Linear(16 * 5 * 5, 120)
    ```
#### Why does super() sometimes look like super(Net, self)?

You asked specifically about the super(Net, self).__init__() syntax. That is the older, more explicit syntax used in Python 2.

- super(Net, self): This explicitly tells Python, "Start searching for methods in the parent class of Net, and apply this method to the current object instance, self."
    
- super(): Since Python 3, you can use the simpler, zero-argument version. When you use super() inside a method, Python automatically figures out which class you're in (like Net) and which object instance you're working with (self). It is the modern and preferred syntax.