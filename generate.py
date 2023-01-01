#!/usr/bin/env python3

"""
Author:     jmdm
Date:       2022-12-30
OS:         macOS 12.6 (Monterey)
Hardware:   M1 chip

This code is provided "As Is"
"""

# Standard libraries
# Third-party libraries
import pyrosim.pyrosim as pyrosim

# Local libraries


def generate(name) -> None:
    """Generate a SDF file."""

    pyrosim.Start_SDF(f"{name}.sdf")
    p0_name = "Box"
    p0_x, p0_y, p0_z = 0, 0, 0
    p0_l, p0_w, p0_h = 1, 1, 1
    pyrosim.Send_Cube(name=p0_name, pos=[p0_x, p0_y, p0_z], size=[p0_l, p0_w, p0_h])
    pyrosim.End()


if __name__ == "__main__":
    generate("box")
