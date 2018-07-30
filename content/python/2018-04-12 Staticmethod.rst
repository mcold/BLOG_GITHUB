Staticmethod
############


:date: 2018-03-11 11:20
:modified: 2018-03-11 11:20
:tags: class, module, staticmethod
:category: python
:slug: staticmethod
:authors: Michael Cold
:summary: Реализация статических методов в классах 

Использование статического метода
=================================

Статический метод (обёрнутый декоратором staticmethod) в принципе соответствует статическим методам в C++ или Java
Классический способ использования статических методов

.. code-block:: py

    class MyClass():
    
        @staticmethod
        def pi():
            return 3.14

    if __name__ == "__main__":
        print(MyClass.pi())