"""
ENGG1001 Assignment 1
Semester 1, 2021
"""

# Fill these in with your details
__author__ = "William Sawyer 46963608"
__email__ = "w.sawyer@uqconnnect.edu.au"
__date__ = "Friday 26 March, 20"

import math


def main():
    """
    Handles the top-level interaction with the user and calls other functions
    based off what the user wants to do.
    """

    want_to_do = ""

    while want_to_do != "q":
        print("")
        print("Please specify one of the following options:")
        print("     'q' - quit")
        print("     'i' - input initial conditions")
        print("     'c' - compute and plot trajectory")
        print("     'o' - print out optimum launch angle")
        want_to_do = input()

        if want_to_do == "i":
            x0, y0, v0, theta0, ax, ay, house_height, house_distance, delta_t \
                = get_initial_conditions()
        elif want_to_do == "c":
            kinetic_model(x0, y0, v0, theta0, ax, ay, house_height,
                          house_distance, delta_t)
        elif want_to_do == "o":
            optimum_angle(x0, y0, v0, ax, ay, delta_t)
    return


def get_initial_conditions():
    """
    Allows the user to input initial conditions for kinetic modelling.

    Return:
        tuple:           Initial conditions

    Note:
        The initial conditions returned are listed in the following order:
            xo, yo, vo, theta0, ax, ay, house_height, house_distance, delta_t
    """

    x0 = 0
    y0 = float(input("Input launch height (in meters): "))
    v0 = float(input("Input launch velocity (in meters/second): "))
    theta0 = float(input("Input the launch angle (in radians): "))
    ax = 0
    ay = -9.81
    house_height = float(input("Input height of master's house (in meters): "))
    house_distance = float(
        input("Input distance to house's furthest wall (in meters): "))
    delta_t = float(input("Input time increment for modelling (in seconds): "))
    return x0, y0, v0, theta0, ax, ay, house_height, house_distance, delta_t


def kinetic_model(x0, y0, v0, theta0, ax, ay, house_height, house_distance,
                  delta_t):
    """
    Calculates trajectory using initial conditions and motion equations.

    Parameters:
        x0              (float): Initial horizontal displacement.
        y0              (float): Initial vertical displacement.
        v0              (float): Initial speed.
        theta0          (float): Initial direction.
        ax              (float): Horizontal acceleration.
        ay              (float): Vertical acceleration.
        house_height    (float): Height of the master's house.
        house_distance  (float): Distance to furthest wall of master's house.
        delta_t         (float): Time period used for modelling.

    Return:
        tuple:          Tuples containing horizontal and vertical
                        displacements and velocities.

    Preconditions:
        All parameters must be defined by get_initial_conditions().
    """

    x_vec = ()
    y_vec = ()
    vx_vec = ()
    vy_vec = ()
    y = y0

    # i is used to iterate through time.
    i = 0

    # Begins making calculations if the loaf is above the ground.
    while y >= 0:
        # Calculates displacements and velocities to 2 decimal places.
        x = round(x0 + v0 * math.cos(theta0) * i * delta_t + 1 / 2 * ax *
                  (i * delta_t) ** 2, 2)
        y = round(y0 + v0 * math.sin(theta0) * i * delta_t + 1 / 2 * ay *
                  (i * delta_t) ** 2, 2)
        vx = round(v0 * math.cos(theta0) + ax * i * delta_t, 2)
        vy = round(v0 * math.sin(theta0) + ay * i * delta_t, 2)

        # Only accepts new values if the loaf is still above the ground.
        if y >= 0:
            x_vec += (x,)
            y_vec += (y,)
            vx_vec += (vx,)
            vy_vec += (vy,)
            i += 1
    return x_vec, y_vec, vx_vec, vy_vec


def optimum_angle(x0, y0, v0, ax, ay, delta_t):
    """
    Determines optimum launch angle to maximise horizontal displacement by
    numerically testing all integer angles from 0 to 90 degrees.

    Parameters:
        x0              (float): Initial horizontal displacement.
        y0              (float): Initial vertical displacement.
        v0              (float): Initial speed.
        ax              (float): Horizontal acceleration.
        ay              (float): Vertical acceleration.
        delta_t         (float): Time period used for modelling.

    Return:
        float:          Optimum launch angle.

    Preconditions:
        All parameters must be defined by get_initial_conditions().
    """

    x_max = 0
    theta_optimum = 0

    for theta in range(0, 90):
        # 'i' is used to iterate through time.
        i = 0
        y = 0

        theta = round(theta * math.pi / 180, 2)

        # Calculates trajectory.
        while y >= 0:
            x = round(x0 + v0 * math.cos(theta) * i * delta_t + 1 / 2 * ax * (
                    i * delta_t) ** 2, 2)
            y = round(y0 + v0 * math.sin(theta) * i * delta_t + 1 / 2 * ay * (
                    i * delta_t) ** 2, 2)
            i += 1

        if x > x_max:
            x_max = x
            theta_optimum = theta
    print(theta_optimum)
    return theta_optimum


if __name__ == "__main__":
    main()
