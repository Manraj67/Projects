class Employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print('Making Object...')
    x = Employee()
    print('function end...')
    return x

print('Calling Create_obj() function...')

a = Create_obj()
print('Program End...')
print(a)