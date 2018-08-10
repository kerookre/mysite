import numpy
import math
from .data import nile_minima_data

from .calculate_numpyless import calculate_not_using_numpy


def filter_given_values_out_from(json_data, given_key):
    """
    Filters out only values with keys "level" from sample data json
    and stores them in a new list.

    Args:
        json_data (list): A list of dictionaries.
        given_key (str): A string determining the key type.

    Returns:
        The new list storing the values of levels.
    """
    return [value
            for dictionary in json_data
            for key, value in dictionary.items()
            if key == given_key]


def minus_average(values, average):
    return [value - average for value in values]


def calculate_levels_by_years(levels, years):
    result = []
    for i in range(len(levels)):
        result.append(levels[i] * years[i])
    return result


def calculate_y(x, a, b):
    return [a*x[i] + b for i in range(len(x))]


def get_classic_dfa_data(segmenth_length):
    # Taking the first N-th element and creating
    # a new list which is exponent of 2.
    sample_data = nile_minima_data[:128]
    # Filtering levels out from sample data and storing them to a new list.
    x = filter_given_values_out_from(sample_data, 'year')
    y = filter_given_values_out_from(sample_data, 'level')

    # First step: Calculating the average of Xn and Yn series.
    x_average = numpy.mean(x)
    y_average = numpy.mean(y)
    print("\nAve. of X = {},\nAve. of Y = {}".format(x_average, y_average))

    # Second step: Converting the series to a "Random Walk".
    # i.e.: Calculating the cumulative sums.
    x_cumulative_sum = numpy.cumsum(x - x_average)
    y_cumulative_sum = numpy.cumsum(y - y_average)

    print("\nThe cumulative sum of X = \n{} \nThe sum of cumulative sum = {}"
          .format(x_cumulative_sum, numpy.sum(x_cumulative_sum)))

    print("\nThe cumulative sum of Y = \n{} \nThe sum of cumulative sum = {}"
          .format(y_cumulative_sum, numpy.sum(y_cumulative_sum)))

    # a = x_cumulative_sum / y_cumulative_sum
    a = numpy.divide(numpy.sum(y_cumulative_sum), numpy.sum(x_cumulative_sum))

    # b = y - a*x
    b = numpy.subtract(y_average, numpy.multiply(a, x_average))

    new_y = calculate_y(x, a, b)

    for i in range(len(new_y)):
        sample_data.append({'year1': x[i], 'level1': new_y[i]})

    for d in sample_data:
        print(d)
    # print("\ny = a*x + b:\ny = {}*x + {}".format(a, b))
    # print("\nClassic DFA: "
    #       "\nThe average is = {}"
    #       "\nThe cumulative sum is = \n{}".format(average, cumulative_sum))
    return {'data': sample_data}


def get_modified_dfa_data(segmenth_length):
    # Taking the first N-th element and creating
    # a new list which is exponent of 2.
    sample_data = nile_minima_data[:32]
    # print("\n In get modified dfa data method!")
    return {'data': sample_data}
