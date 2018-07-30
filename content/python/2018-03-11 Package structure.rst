Peculiar properties of import packages
######################################

:date: 2018-03-11 11:20
:modified: 2018-03-11 11:20
:tags: modules
:category: python
:slug: modules
:authors: Michael Cold
:summary: Special features of importing packages


As you know in order to create a package you need to have executed the next condictions:
- create root directory
- create file __init__.py in root directory 

At first sign all is simple, but in more scrutinize look we can find some interesting cases which I want to research in this article
Let's to begin ...


Simple package construction
===========================

Suppose we have the next structure

::

    test.py
    │
    └───pack
            mod.py
            __init__.py

test.py         script for testing package pack
__init__.py     empty by default

mod.py

.. code-block:: py

    def mod_func():
        print("I'm module function!")


    if __name__ == '__main__':
        pass

Import module of package
========================

In order to execute function mod.mod_func() in test.py we need to do one of the next events:

* straight import module of package

test.py

.. code-block:: py

    from pack.mod import mod_func

    if __name__ == "__main__":
        mod_func()

* define in __init__.py variable __all__

__init__.py

.. code-block:: py

    __all__ = ['mod']

This way adds this module into namespace of package
So if we use instruction like

.. code-block:: py

    from pack.mod import *

It gives us the posibility to use all objects of module

test.py

.. code-block:: py

    from pack.mod import *

    if __name__ == "__main__":
        mod_func()

But if we don't use variable in __init__.py and have test.py with next code:

.. code-block:: py

    from pack.mod import *

    if __name__ == "__main__":
        mod_func()

The execution of script will be failed, because module mod is abscent in namespace of package

Import objects of package
=========================

Suppose we have a function into package

pack\__init__.py

.. code-block:: py

    def pack_func():
        print("Package function!")


Looksalike of previous point in order to execute this function in our test.py we need to use one of two methods:

* straight import of function

.. code-block:: py

    from pack import pack_func

    if __name__ == "__main__":
        pack_func()

another way

.. code-block:: py

    import pack

    if __name__ == "__main__":
        pack.pack_func()

* add function into __all__

pack\__init__.py

.. code-block:: py

    __all__ = ['mod', 'pack_func']


    def pack_func():
        print("Package function!")

As I mentioned before this way we added our package function into namespace of package and now we can use our function pretty simple

test.py

.. code-block:: py

    from pack import *

    if __name__ == "__main__":
        pack_func()

 