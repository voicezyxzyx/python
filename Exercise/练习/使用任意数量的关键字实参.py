def build_profile(first, last, **user_info):
    """创建一个字典， 其中包含我们知道的有关用户的一切"""
    '''
形参 **user_info 中的两个星号让Python创建一个名为user_info 的空字典， 
并将收到的所有名称—值对都封装到这个字典中。 
在这个函数中， 可以像访问其他字典那样访问user_info 中的名称—值对。 
    '''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics')
print(user_profile)