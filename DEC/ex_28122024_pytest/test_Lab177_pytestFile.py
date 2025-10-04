# ### Rules with PyTest
# 1. Test Name (starts with test_) test_file_name.py -> test_file.py
# 2. create a method with the name (starts with test_) test_main_name()
# 3. You can add Assertion ?
#     1. Expected Result == Actual Result
#     2. Fail or Pass.
# 4. F- Fail
# 5. . - Green Dot**. - Pass ( Passed)
# 6. You cam mark your Testcase
#     1. @pytest.mark.name
#     2. @pytest.mark.pyatb4x
# 7. to run the TCs - cmd - pytest <filename>
# Assertion - means statement, ex = 5 == 5, True == True/False
# pip install pytest-html
# --html=report.html--self-contained-html
# cmd for generate report: pytest --html=report.html <file name>

def method1():      # not a pytest method. rule no.2
    print("hello")

def test_method1():
    print("hello 1")
    assert True == False

def test_method2():
    print("hello 2")
    assert 1+1 == 3

def test_method3():
    print("hello 3")
    assert 1+1 == 2
