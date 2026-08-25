#def set_name():
 #   name = "Aryna"

# print(name)
# NameError: name 'name' is not defined

def outer():

    def set_name():
        name = "Aryna"
        return name
    return set_name()

name = outer()
print(name)