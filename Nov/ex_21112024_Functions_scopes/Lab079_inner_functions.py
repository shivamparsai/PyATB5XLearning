# outer function variable can be used by the inner functions

def outerFunction():
    var1 = 30      # local variable

    def innerFunction1():
        var2 = 50
        print(var1)

    def innerFunction2():
        print(var1)

    innerFunction1()
    innerFunction2()
    # print(var2)   # not allowed

# innerFunction1()    # not possible to call

outerFunction()