from main import checkPwd


def test_checkPwd():
    assert checkPwd('AZsdfgh123!!') == [True]


def test_Checkpwd1():
    res = checkPwd('nhrhdjske')
    assert res[0] == False


def test_checkPwd2():
    res = checkPwd('qsdfgAZE123')
    assert res[0] == False


def test_checkPwd3():
    assert checkPwd('dflgmptvfg3SAZ!') == [True]

def test_checkPwd4():
    res = checkPwd('12000009')
    assert res[0] == False

def test_checkPwd5():
    res = checkPwd('!!!!::::22')
    assert res[0] == False