# -*- coding: utf-8 -*-

'''Here, we use a direct-sampling Monte Carlo simulation to calculate the value of π. 
   
   The conceptual model we have is of performing a number of uniformly-distributed trials inside a
   square, whose length we normalise to be 1. We imagine a circle of diameter one cocentric with the
   square, and we perform a number of trials (i.e. generate a number of points) inside the square.
   
   Since we know the ratio of the areas between the circle and the square is A_cir / A_sqr = π/4,
   and since the trials are uniformly distributed inside the square, we immediately have
   N_cir / N_sqr = π/4; reversing this gives the value of π as π = 4 N_cir / N_sqr.
   (Note that N_sqr is the number of trials: we don't count anything outside of the square.)'''
   
'''For this, we generate a number of (x, y) points in the range [-1, 1), which represents points in
   the square. To test whether they're inside the circle as well, we want to check x^2 + y^2; if
   x^2 + y^2 < 1, then the point is inside the circle. (This is why I'm generating points inside
   [-1, 1) rather than [0, 1): centering at the origin lets me check whether a point is inside the
   circle way more simply.)
   
   Since I only need to generate random points and check them, I don't actually need to store them
   anywhere.'''


# This section imports the libraries necessary to run the program.
import math
import random
import time

'''Note: I'm assuming people running this will have PyLab (with matplotlib) but not NumPy, so I'm
   going to avoid NumPy entirely.'''


# This section stores the time at the start of the program.
program_start_time = time.clock()

'''Since we're interested in the amount of time the program will run in, we'll store the time at the
   beginning of the program using time.clock(), and compare it to the time at the end (again using
   time.clock(), applied to a different variable name. time.clock() just takes the time at a given
   moment; it's up to us to store it properly.'''


# This section sets the number of Monte Carlo trials, as well as the number of times a single set of trials is run.
MC_trials = 1000000   # MC_trials is the number of Monte Carlo trials. 
runs = 50             # runs is the number of times the MC program is run.


# This section performs the trials, and counts the number of trials that fall inside the circle.
def MC_cir_count(trials):
    N_cir = 0
    for i in xrange(trials):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        if x**2 + y**2 <= 1.0:
            N_cir += 1
    return N_cir


# This function builds the array of the numbers of successes per run of the MC algorithm, as well as the associated statistics.
pi_val_array = [0]*runs

for i in xrange(runs):
    N_cir_run = MC_cir_count(MC_trials)
    pi_val_array[i] = 4.0*N_cir_run/MC_trials

mean_pi_val = sum(pi_val_array)/len(pi_val_array)
var_pi_val = sum((mean_pi_val - val) ** 2.0 for val in pi_val_array) / len(pi_val_array)
stdev_pi_val = var_pi_val ** 0.5
mse_pi_val = sum((math.pi - obj) ** 2.0 for obj in pi_val_array) / len(pi_val_array)
rms_pi_val = mse_pi_val ** 0.5


# To find out how long the program takes, we take the difference of time.clock() evaluated at the beginning of the program and at the end of the program. Here, we take the time at the end of the program, and define the total program time.
program_end_time = time.clock()
total_program_time = program_end_time - program_start_time

print "Approximation of pi: %6f ± %6f" % (mean_pi_val, rms_pi_val)
print "Variance:", var_pi_val
print "St. Dev.:", stdev_pi_val
print "RMS:", rms_pi_val
print "Program run time (s):", total_program_time
print "Run time per MC update (s):", total_program_time / (MC_trials * runs)