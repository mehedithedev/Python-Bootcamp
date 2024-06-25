# def get_nr_items(names):
#
#     items = names.split(',')
#     return len(items)
# print(get_nr_items("Mehedi, Hasan"))
#


# def temp(value):
#     if value > 7:
#         return "Warm"
#     elif value <= 7:
#         return "Cold"
#
# print(temp(7))

def myPassword(password):
    if len(password) < 8:
        return False
    else:
        return True
myPassword("This is my password")

