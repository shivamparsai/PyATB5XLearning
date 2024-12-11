import  time

# Note - 1.if we need to use the multiple dacorators then write the return wrapper without () and explicitly call the function
# in this case testUI1() and testUI2() were called

# 2.We are not going to create the dacorators but we only need to use them like for reports, logs etc
# Allure report - html report - we need to call the @allure - so allure report is generated
# in Api automation - @file_details  - csv file or data

def masureTime(func):
    def wrapper():
        startTime = time.time()
        print("Start time is ", startTime)
        func()
        endTime = time.time()
        print("End Time is ", endTime)
        print("Total time taken is ", endTime-startTime)
    return wrapper

def printLogs(func):
    def wrapper():
        print("print logs start")
        func()
        print("print logs end")
    return wrapper

@printLogs
@masureTime
def testUI1():
    print("calling testUI1()")
    time.sleep(2)

testUI1()

@printLogs
@masureTime
def testUI2():
    print("Calling testUI2")
    time.sleep(5)

testUI2()