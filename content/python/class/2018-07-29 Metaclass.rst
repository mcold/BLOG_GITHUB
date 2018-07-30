Metaclass
#########

:date: 2018-07-29 15:20
:modified: 2018-07-29 15:20
:tags: class
:category: python
:slug: metaclass
:authors: Michael Cold
:summary: Используем метаклассы

Py2 & Py3
=========

Версии Python по разному регламентируют синтаксис метакласса

Python2:

.. code-block:: py

    from abc import ABCMeta, abstractmethod

    class A(metaclass=ABCMeta):
        pass



Python3:

.. code-block:: py

    class A():
        __metaclass__ = ABCMeta 
        pass