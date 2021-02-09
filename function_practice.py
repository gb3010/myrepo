#Simple function

def fun():
    print("Hello world!")

#fun()


#Function with unknown number of arguments

def fun_with_args(*fruits):
    print("{var} is one of my favourite fruits".format(var=fruits[1]))

#fun_with_args('mango','apple','banana')


#Function with args of key value relationship
def fun_with_kw(**empdetails):
    print("{e} is from {s}".format(e=empdetails['name'],s=empdetails['state']))

fun_with_kw(name='john',state='AZ')