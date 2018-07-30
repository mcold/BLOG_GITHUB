Inheritance
###########

:date: 2018-03-10 11:20
:modified: 2018-07-27 11:20
:tags: class
:category: python
:slug: inheritance
:authors: Michael Cold
:summary: Features of inheritance


Inheritance features of Python
==============================

Simple case of inheritance
==========================

Let's create a simple example of inheritance between two classes: child and parent:

.. code-block:: py

    class parent_class:

        def __init__(self):
            print("I'm parent!")

        def func(self):
            print("parent func")

        def parent_func(self):
            print("This function I've got from parent")


    class child_class(parent_class):

        def __init__(self):
            print("I'm child!")

        def func(self):
            print("child func")


    if __name__ == "__main__":
        item = child_class()
        item.func()
        item.parent_func()


::

    I'm child!
    child func
    This function I got from parent


In this example we see the next casualties:
- parent's function (func) is reloaded by child's function
- inherited function (parent_func) executed as it is in parent class


Inheritance from multiple parents
=================================


General case
------------

In general case of multiple inheritance all is pretty obious - functions which not repeated works as in parent classes
Let's have a look on case, when child have two parents. In our event it is classes with names 'mother' and 'father'

.. code-block:: py

    class father_class:

        def __init__(self):
            print("I'm father!")
            
        def father_func(self):
            print("Hay from father")


    class mother_class:
        
        def __init__(self):
            print("I'm mother!")


        def mother_func(self):
            print("Hay from mother")


    class child_class(father_class, mother_class):

        def __init__(self):
            print("I'm child!")


    if __name__ == "__main__":
        item = child_class()
        item.father_func()
        item.mother_func()

::

    I'm child!
    Hay from father
    Hay from mother

Reloaded functions
------------------

But what if we have two identical functions in two parents classes

.. code-block:: py

    class father_class:

        def __init__(self):
            print("I'm father!")

        def func(self):
            print("father func")

        def parent_func(self):
            print("This function I've got from father")


    class mother_class:
        
        def __init__(self):
            print("I'm mother!")

        def func(self):
            print("mother func")

        def parent_func(self):
            print("This function I've got from mother")


    class child_class(father_class, mother_class):

        def __init__(self):
            print("I'm child!")

        def func(self):
            print("child func")


    if __name__ == "__main__":
        item = child_class()
        item.func()
        item.parent_func()

::

    I'm child!
    child func
    This function I've got from father

We see that executes function (parent_func) which was founded first in list of parents classes

