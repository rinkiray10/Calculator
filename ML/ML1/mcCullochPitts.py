import numpy as np

def activation_fn(z):
    return 1 if z >= 0 else 0

def main():
    # Taking inputs from txt file
    x = np.array([2,3,4,-1,-2,-2.4,2,-6,-3,5])
    w = np.array([-0.2,0.4,-0.2,2.1,-0.6,0.02,0.1,0.4,-0.2,-0.3])
    print(f'total input labels : {x.shape[0]}\nTotal weights : {w.shape[0]}')
    # calculating g(z)
    b = 1
    z = np.sum( np.dot(x.T,w)) + b
    print(f'total sum : {z}')
    # activation Function
    print(f'final output : {activation_fn(z)}')

main()