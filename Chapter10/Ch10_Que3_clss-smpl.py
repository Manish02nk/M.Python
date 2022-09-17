# class Sample:
#     a = "Manish Nayak"

# object = Sample()
# object.a = "Rohan Sinodiya"

# print(Sample.a)
# print(object.a)   # It is does not change the name

#    ||
#    ||
#    ||
#   _||_
#   \  /
#    \/

class Sample:
    a = "Manish Nayak"


object = Sample()
object.a = "Rohan Sinodiya"
Sample.a = "Manish Pradhan"  # Now user can be change the name

print(Sample.a)
print(object.a)
