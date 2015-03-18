import random
import matplotlib.pyplot as plt

"""
Matplotlib visualization of the Monte Carlo process used to estimate Pi (http://en.wikipedia.org/wiki/Pi#Geometry_and_trigonometry).
"""

def generate_pi(s, reps = 10):
    random.seed()
    n = 10**reps
    pi = 0
    ixs = []
    iys = []
    oxs = []
    oys = []
    for i in xrange(int(n)):
        x = random.random() 
        y = random.random() 
        
        if x**2 + y**2 < 1:
            ixs.append(x)
            iys.append(y)
            pi+=1
        else:
            oxs.append(x)
            oys.append(y)
    
    fig = plt.figure(figsize=(8,8))
    plt.plot(ixs,iys, color= "r", marker = "o", linestyle = "None", mew=0, alpha = .5)
    plt.plot(oxs,oys, color= "darkblue", marker = "o", linestyle = "None", mew=0, alpha = .5)
    resultpi = 4.0*pi/n
    plt.title("Pi estimated with {} random numbers: {}".format(int(n), resultpi))
    plt.show()
    
    return 4.0*pi/n


if __name__ == "__main__":
        
    for i in range(3,9):
        generate_pi(0, reps = i)
    