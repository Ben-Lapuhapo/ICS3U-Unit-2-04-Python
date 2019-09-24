#!/usr/bin/env python3

# Created by: Ben lapuhapo
# Created on: Sep 23 2019
# This program calculates the cost of pizza

import constants


def main():
    # This Function calculates the cost of pizza

    # Input
    diameter = int(input("Enter the diameter of the pizza you would " +
                         "like (inch): "))

    # Process
    sub_total = constants.LABOR + constants.RENT + \
        (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    # Output
    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
