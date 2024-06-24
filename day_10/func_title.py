
def func_title(f_name, l_name):
    """return the title case version of f_name and l_name"""
    return f"{f_name.title()} {l_name.title()}"


f_name = "first_name"
l_name = "last_name"
print(func_title(f_name, l_name))