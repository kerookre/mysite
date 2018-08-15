import math
import numpy
import pprint
from .data import nile_minima_data

from .calculate_numpyless import calculate_not_using_numpy


def get_possible_data_length():
    possible_data_length = []
    data_length = len(nile_minima_data)
    for i in range(1, round(math.log2(data_length)) + 1):
        number = 2**i
        if number <= data_length:
            possible_data_length.append(number)
        else:
            break
    return possible_data_length


def get_possible_segments_length(possible_data_length):
    possible_segments = {}
    for number in possible_data_length:
        possible_segments[number] = [
            2**i for i in range(1, round(math.log2(number)) + 1)
        ]
    return possible_segments


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


def calculate_y(x, a, b):
    return [a*x[i] + b for i in range(len(x))]


def split_list_into_segments(data_list, number_to_split):
    count = 0
    small_list = []
    result = []

    for i in range(len(data_list)):
        small_list.append(data_list[i])
        count += 1

        if count > 0 and count % number_to_split == 0:
            count = 1
            result.append(small_list)
            small_list = [data_list[i]]

    return result


def get_classic_dfa_data(data_length, segments_length):
    print("\n data_length = ", data_length, type(data_length))
    print("\n segments_length = ", segments_length, type(segments_length))
    # Taking the first N-th element and creating
    # a new list which is exponent of 2.
    sample_data = nile_minima_data[:(data_length + 1)]
    calculated_data = []

    segments_number = round(data_length / segments_length)
    print("\nSegments number = ", segments_number)

    # Filtering levels out from sample data and storing them to a new list.
    x = filter_given_values_out_from(sample_data, 'year')
    y = filter_given_values_out_from(sample_data, 'level')

    segments_x = split_list_into_segments(x, segments_length + 1)
    segments_y = split_list_into_segments(y, segments_length + 1)

    print("\nsegments_x = ", segments_x)
    print("\nsegments_y = ", segments_y)

    # Getting the minimum and the maximum value of X series.
    min_x = numpy.min(x)
    max_x = numpy.max(x)

    # Getting the minimum and the maximum value of Y series.
    min_y = numpy.min(y)
    max_y = numpy.max(y)

    print("\nmin_y = {}, max_y = {}".format(min_y, max_y))
    print("\nmin_x = {}, max_x = {}".format(min_x, max_x))

    for i in range(segments_number):
        # First step: Calculating the average of Xn and Yn series.
        x_average = numpy.mean(segments_x[i])
        y_average = numpy.mean(segments_y[i])
        # print("\nAve. of X = {},\nAve. of Y = {}".format(x_average, y_average))

        # Second step: Converting the series to a "Random Walk".
        # i.e.: Calculating the cumulative sums.
        x_cumulative_sum = numpy.cumsum(segments_x[i] - x_average)
        y_cumulative_sum = numpy.cumsum(segments_y[i] - y_average)

        # print("\nThe cumulative sum of X = \n{} \nThe sum of cumulative sum = {}"
        #       .format(x_cumulative_sum, numpy.sum(x_cumulative_sum)))
        #
        # print("\nThe cumulative sum of Y = \n{} \nThe sum of cumulative sum = {}"
        #       .format(y_cumulative_sum, numpy.sum(y_cumulative_sum)))

        # Third step: Dividing the series into segments of length L and
        # fitting a straight line within each segment.
        # a = x_cumulative_sum / y_cumulative_sum
        a = numpy.divide(
            numpy.sum(y_cumulative_sum),
            numpy.sum(x_cumulative_sum)
        )

        # b = y - a*x
        b = numpy.subtract(y_average, numpy.multiply(a, x_average))

        new_y = calculate_y(segments_x[i], a, b)
        print(segments_x[i])
        print(new_y)
        print("\nY[{}] = a*X[{}]+ b:\ny = {}*x + {}".format(i, i, a, b))

        for j in range(len(new_y)):
            sample_data.append({
                'year' + str(i): segments_x[i][j],
                'level' + str(i): new_y[j]
            })

            calculated_data.append({
                'year' + str(i): segments_x[i][j],
                'level' + str(i): new_y[j]
            })

    # print("\nClassic DFA: "
    #       "\nThe average is = {}"
    #       "\nThe cumulative sum is = \n{}".format(average, cumulative_sum))
    return {
        'sample_data': sample_data,
        'calculated_data': calculated_data,
        'segments_number': segments_number,
        'min_x': int(min_x),
        'max_x': int(max_x),
        'min_y': min_y,
        'max_y': max_y
    }


def get_modified_dfa_data(segments_length):
    # Taking the first N-th element and creating
    # a new list which is exponent of 2.
    sample_data = nile_minima_data[:32]
    # print("\n In get modified dfa data method!")
    return {'data': sample_data}
