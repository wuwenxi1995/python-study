# -*- coding: utf-8 -*-
# @Time    : 2025/5/21 11:50
# @Author  : wuwenxi

def fund(a, b, c):
    print(a, b, c)  # ==> 输出: 1,2,3


# fund(1, 2)
# fund(1, b=2, 3)
# fund(b=1, a=2, c=3)

# def fund(a=1, b, c):
#     print()

# def f5(arg1, /, arg2, *, arg3):
#     print(arg1, arg2, arg3)
#
#
# f5(1, 2, 3, 4, 5)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    # kind 参数: 传入Limburger
    # arguments 参数传入:"It's very runny, sir.", "It's really very, VERY runny, sir."
    # keywords 参数传入：shopkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch"


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
cheeseshop("Limburger", *("It's very runny, sir.",
                          "It's really very, VERY runny, sir."),
           **{'shopkeeper': "Michael Palin",
              'client': "John Cleese",
              'sketch': "Cheese Shop Sketch"})


def f(name, /, **keymap):
    print(name in keymap)


f('name', **{'name': 23})
