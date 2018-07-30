Global & local variables
########################

:date: 2018-03-12 11:20
:modified: 2018-03-12 11:20
:tags: modules, local, global
:category: python
:slug: variables
:authors: Michael Cold
:summary: Namespace scopes


.. code-block:: py

    def f():
        s = "Local var"
        print(s)

    if __name__ == "__main__":
        s = "Global var"
        f()
        print(s)

::

    Local var
    Global var

global
======

.. code-block:: py

    def f():
        global s
        s = "Local var"
        print(s)

    if __name__ == "__main__":
        s = "Global var"
        f()
        print(s)

::

    Local var
    Local var


.. code-block:: py

    def f():
        global s
        s = "Local var"
        print(s)

    if __name__ == "__main__":
        f()
        print(s)
