from TestCase import *

CASE_LIST = ["*"]


def getNum() -> tuple:
    caseLIst = []
    for case in CASE_LIST:
        caseLIst.extend([func for func in dir(case) if func.startswith("test")])

    nums = len(caseLIst)
    return nums, caseLIst


if __name__ == '__main__':
    print(getNum())
