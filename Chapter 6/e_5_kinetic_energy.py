# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:24:04 2022

@author: Ali

In physics, an object that is in motion is said to have kinetic energy (KE). 
The following formula can be used to determine a moving object’s kinetic energy:
KE= 1⁄2 * m * v**2
The variables in the formula are as follows: KE is the kinetic energy in joules, m is the
object’s mass in kilograms, and v is the object’s velocity in meters per second.
Write a function named kinetic_energy that accepts an object’s mass in kilograms and
velocity in meters per second as arguments. The function should return the amount of
kinetic energy that the object has. Write a program that asks the user to enter values for
mass and velocity, and then calls the kinetic_energy function to get the object’s kinetic
energy.
"""

def main():
    m, v = input_func()
    ke = kinetic_energy(m, v)
    display_func(ke)
    
    
def input_func():
    # Get the mass and velocity of object.

    m = float(input('Enter the object \'s mass (kg): '))
    # The unicode character for superscript **2 is '\u00b2'
    v = float(input('Enter the object \'s velocity (m/s\u00b2): '))
    return m,v

def display_func(value):
    print('The kinetic energy of the object is', format(value, ',.2f'), 'joules.')
    
def kinetic_energy(m, v):
    # ke = (1/2) * mass * (velocity ** 2)
    ke = (1/2) * m * (v ** 2)
    return ke

main()