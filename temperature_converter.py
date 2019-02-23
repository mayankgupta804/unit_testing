def c_to_f(t_in_celcius):
    assert type(t_in_celcius) == float or type(t_in_celcius) == int
    return float(t_in_celcius * 9/5 + 32)

def f_to_c(t_in_fahrenheit):
    assert type(t_in_fahrenheit) == float or type(t_in_fahrenheit) == int
    return float((t_in_fahrenheit - 32) * 5/9)
 