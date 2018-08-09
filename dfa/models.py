from django.db import models

from .data import nile_river_minima_data


# Taking the first N-th element and creating a new list which is exponent of 2.
sample_data = nile_river_minima_data[:32]


def calculate_average_level(data):
    """
    Calculates the arithmetic average of all levels in given <Xn> series.

    Args:
        data (list): A list of <Xn> series

    Returns:
        The calculated arithmetic average as float/double.
    """
    sum_of_levels = 0
    for data_dictionary in data:
        for key, value in data_dictionary.items():
            if key == 'level':
                sum_of_levels += value
    return sum_of_levels / len(data)


def get_classic_dfa_data():
    # First step: Calculating the average of <Xn>.
    average = calculate_average_level(sample_data)
    print("\nClassic DFA: "
          "\nThe average is = {}".format(average))
    return sample_data


def get_modified_dfa_data():
    # print("\n In get modified dfa data method!")
    return sample_data
