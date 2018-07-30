# *topping可以代表多个数量的形参  一个“pepperoni”可以
# 三个'mushrooms', 'green peppers', 'extra cheese'也可以

def make_pizza(*topping):
    print(topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

