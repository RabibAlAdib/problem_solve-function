# 14 check student varify

def valid(id):
    if id in student_list:
        return True
    else:
        return False


student_list = [2221001, 2221002, 2221003,222104]
id = int(input("Enter your Student Id: "))
print(valid(id))