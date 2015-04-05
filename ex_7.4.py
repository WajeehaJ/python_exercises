import math

def eval_loop():
    while True:
        input_val = raw_input("Please enter the string to evaluate\n")
        print input_val + " = ",
        if (input_val  == 'done'):
            break
        print eval(input_val)

    print 'Done'


eval_loop()
