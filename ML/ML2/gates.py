import numpy as np


def NOT_percep(x):
    v = -1 * x + 0.5 #w = -1 , b = 0.5
    return 1 if v >= 0 else 0

def AND_percep(x):
    w, b= np.array([1, 1]), -1.5
    v = np.dot(w,x) + b
    return 1 if v >=0 else 0


def OR_percep(x):
    w, b = np.array([1, 1]) , -0.5
    v = np.dot(w,x) + b 
    return 1 if v>=0 else 0

def XOR_net(x):
    """"  FINAL OUTPUT = AND (NOT (AND(x , y)), OR(x,y) ) """
    # gate_1 = NOT_percep( AND_percep(x))
    # gate_2 = OR_percep(x)
    # new_x = np.array([gate_1, gate_2])
    # output = AND_percep(new_x)
    # return output

    return AND_percep(np.array([NOT_percep(AND_percep(x)),OR_percep(x)]))


# Test
example1 = np.array([0, 0])
example2 = np.array([0, 1])
example3 = np.array([1, 0])
example4 = np.array([1, 1])
print("The output of AND with weight w1=1 ,w2=1 and b=-1.5 is:-")
print(f"{0} | {0} --> {AND_percep(example1)}")
print(f"{0} | {1} --> {AND_percep(example2)}")
print(f"{1} | {0} --> {AND_percep(example3)}")
print(f"{1} | {1} --> {AND_percep(example4)}")

print("The output of OR with weight w1=1 ,w2=1 and b=-0.5 is:-")
print(f"{0} | {0} --> {OR_percep(example1)}")
print(f"{0} | {1} --> {OR_percep(example2)}")
print(f"{1} | {0} --> {OR_percep(example3)}")
print(f"{1} | {1} --> {OR_percep(example4)}")
print("The output of XOR  is:-")
print(f"{0} | {0} --> {XOR_net(example1)}")
print(f"{0} | {1} --> {XOR_net(example2)}")
print(f"{1} | {0} --> {XOR_net(example3)}")
print(f"{1} | {1} --> {XOR_net(example4)}")
