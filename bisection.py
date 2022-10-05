# Defining Function
def f(x):
    return x**3-(7*x**2)+14*x-6

# Implementing Bisection Method
def bisection(x0,x1,e):
    step = 1
    print("itr.\tx1\t\tx2\t\txmid\t\tf(X1)\t\tf(x2)\t\tf(xmid)\t\tabs error")
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        #print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        print('%d\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t%0.6f'%(step,x0,x1,x2,f(x0),f(x1),f(x2),abs(x1-x2)))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired Root is : %0.8f' % x2)


# Input Section
x0 = input('x1: ')
x1 = input('x2: ')
e = input('Tolerable Error: ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

#Note: You can combine above two section like this
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and bisecting
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(x0,x1,e)