import math

def calc(x, y):
    fabs = math.fabs(x - y)    # 绝对值计算 fabs方法返回绝对值
    divisor_one = math.pow(3, x)   # pow方法返回第一个参数的第二个参数次方
    divisor_two = math.sin(y)    # sin方法返回正弦值
    result = math.pow(math.e, fabs) / (divisor_one + divisor_two)
    return result


var_x = input("请您输入第一个数x:")
var_y = input("请您输入第二个数y:")
result = calc(int(var_x), int(var_y))
print("结果是", str(result))
