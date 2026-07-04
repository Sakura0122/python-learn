def get_sum(num1, num2):
    assert isinstance(num1, (int, float)), "num1 必须是数字"
    assert isinstance(num2, (int, float)), "num2 必须是数字"

    return num1 + num2

get_sum(1,'123') 