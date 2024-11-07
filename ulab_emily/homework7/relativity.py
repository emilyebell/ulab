# relativity.py
import numpy as np

SPEED_OF_LIGHT = 299792458  # speed of light in screaming snake notation

def lorentz_factor(velocity):
   #calculate lorentz factor given an object's velocity
    if velocity >= SPEED_OF_LIGHT:
        print("The velocity cannot exceed the speed of light.")
        return None
    gamma = 1 / np.sqrt(1 - (velocity ** 2) / (SPEED_OF_LIGHT ** 2))
    return gamma

def time_dilation(proper_time, velocity):
    #calculate time dilation for an object at a given velocity
    gamma = lorentz_factor(velocity)
    dilated_time = gamma * proper_time
    return dilated_time

def length_contraction(proper_length, velocity):
    # calculate length contraction for given velocity
    gamma = lorentz_factor(velocity)
    contracted_length = proper_length / gamma
    return contracted_length

def lorentz_transformation(events, velocity):
    # transform position, time events from one inertial reference frame to another
    gamma = lorentz_factor(velocity)

    x = events[:, 0] #position
    t = events[:, 1] #time
    
    x_prime = gamma * (x - velocity * t) #lorentz transformation for position
    t_prime = gamma * (t - (velocity * x) / SPEED_OF_LIGHT**2) #time lorentz transformation
    
    transformed_events = np.column_stack((x_prime, t_prime)) # create new 2d array with transformed x,t
    return transformed_events
