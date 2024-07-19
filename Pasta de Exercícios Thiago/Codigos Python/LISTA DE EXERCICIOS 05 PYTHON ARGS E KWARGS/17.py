def fun(**kwargs):
    x = 0
    for value in kwargs.values():
        print(value)
        x += 1
        

fun(firstname='First name is John',lastname='Lastname is Wood',email='Email is johnwood@nomail.com',country='Country is Wakanda',age='Age is 25',phone='Phone is 9876543210')