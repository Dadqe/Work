def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))

test_var_kwargs(1, myarg2="two", myarg3=3)