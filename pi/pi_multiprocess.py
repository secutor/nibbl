import random
from multiprocessing import Pool

"""
Simple application of multiprocessor mapping to calculate Pi with all your CPUs. 
"""

def generate_pi(nil):
    n = 10**7
    pi = 0
    for i in xrange(n):
        if random.random()**2 + random.random()**2 < 1:
            pi+=1
    return 4.0*pi/n

if __name__ == "__main__":

    reps = range(10) #only used for number of repetitions
    pool = Pool()
    results = pool.map(generate_pi, reps) #returns list of 10 values calculated by generate_pi (hack for no input parameter with "nil")
    pool.close()
    pool.join()

    print sum(results)/len(results)
    

    