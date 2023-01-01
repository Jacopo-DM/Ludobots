#!/usr/bin/env python3

"""
Author:     jmdm
Date:       2022-12-30
OS:         macOS 12.6 (Monterey)
Hardware:   M1 chip

This code is provided "As Is"
"""

# Standard libraries
import time

# Third-party libraries
import pybullet as p

# Local libraries
from generate import generate
from utils.setup import setup

# Constants
STEPS = 1000
TIME = 1 / 240


def main(sdf_name) -> None:
    """Main function"""

    physicsClient = p.connect(p.GUI)

    p.loadSDF(sdf_name + ".sdf")

    for __ in range(STEPS):
        p.stepSimulation()
        time.sleep(TIME)

    p.disconnect(physicsClient)


if __name__ == "__main__":
    setup()
    sdf_name = "box"
    generate(sdf_name)
    main(sdf_name)

""" Utilities
Create 'requirements.txt'
    pip install pipreqs
    pipreqs /path/to/project
Use 'requirements.txt'
    pip install -r /path/to/requirements.txt
"""

""" Function Definitions
def func(param1: str, param2: int) -> bool:
    Parameters
    ----------    
    param1
        The first parameter.
    param2
        The second parameter.

    Returns
    -------
        The return value. True for success, False otherwise.
"""
