import math
import numpy as np

from .data import nile_minima_data

from .calculate_numpyless import calculate_not_using_numpy


def get_possible_data_length(data):
    """
    Gets the maximum possible length of data with the length of 2^n from
    the given original data list.

    Args:
        data (list): A given original data list.

    Returns:
        The list maximum possible numbers of 2^n to obtain from given list,
        where n is natural number.
    """
    possible_data_length = []
    data_length = len(data)
    for i in range(1, round(math.log2(data_length)) + 1):
        number = 2**i
        if number <= data_length:
            possible_data_length.append(number)
        else:
            break
    return possible_data_length


def get_possible_segments_length(possible_data_length):
    """
    Calculates the dictionary with the elements of possible_data_length as
    keys and its possible combinations of power of 2 as values.

    Args:
        possible_data_length (list): A list of possible data length to
        obtain from a list of an original data list.

    Returns:
        The dictionary of a given list.
        e.g.: {2: [2], 4: [2, 4], 8: [2, 4, 8], ...}.
    """
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
    """
    Calculates the linear regressions Y[n]'s value for given X[n], a and b,
    where n is a natural number.

    Args:
        x (list): A list of X[n].
        a (float): A float number a.
        b (float): A float number b.

    Returns:
        A list of calculated Y[n].
    """
    return [a*x[i] + b for i in range(len(x))]


def split_list_into_segments(data_list, number_to_split):
    """
    Splits/Divides the original data list into N number of sub lists.

    Args:
        data_list (list): A list of original data.
        number_to_split (int): A number to split original data in.

    Returns:
        The list of N number split lists into segments.
    """
    count = 0
    each_segment = []
    segments_list = []

    for i in range(len(data_list)):
        each_segment.append(data_list[i])
        count += 1
        if count > 0 and count % number_to_split == 0:
            count = 1
            segments_list.append(each_segment)
            each_segment = [data_list[i]]
    return segments_list


def calculate_each_segments_f_l(segments_length, a, b, y):
    sum_of_y = 0
    for i in range(len(y)):
        sum_of_y += np.power((y[i] - a*i - b), 2)
    return np.sqrt(np.multiply((1/segments_length), sum_of_y))


def calculate_average_f_l(f_l_list):
    average_f_l = np.mean(f_l_list)
    return average_f_l


def get_classic_dfa_data(data_length, segments_length):
    # Stores the each segments data.
    calculated_data = []
    # Stores the calculated F(L) of each segments.
    f_l_list = []
    # Stores the formula y = a*x + b of each segments.
    formula_list = []
    # Taking the first N-th element and creating
    # a new list which is exponent of 2.
    sample_data = nile_minima_data[:(data_length + 1)]

    segments_number = round(data_length / segments_length)

    # Filtering levels out from sample data and storing them to a new list.
    x = filter_given_values_out_from(sample_data, 'year')
    y = filter_given_values_out_from(sample_data, 'level')

    segments_x = split_list_into_segments(x, segments_length + 1)
    segments_y = split_list_into_segments(y, segments_length + 1)

    # Getting the minimum and the maximum value of X series.
    min_x = np.min(x)
    max_x = np.max(x)

    # Getting the minimum and the maximum value of Y series.
    min_y = np.min(y)
    max_y = np.max(y)

    # Dividing the original series into segments.
    for i in range(segments_number):
        # First step: Calculating the average of Xn and Yn series.
        x_average = np.mean(segments_x[i])
        y_average = np.mean(segments_y[i])

        # Second step: Converting the series to a "Random Walk".
        # i.e.: Calculating the cumulative sums.
        x_cumulative_sum = np.cumsum(segments_x[i] - x_average)
        y_cumulative_sum = np.cumsum(segments_y[i] - y_average)

        # Third step: Dividing the series into segments of length L and
        # fitting a straight line within each segment.
        # a = x_cumulative_sum / y_cumulative_sum
        a = np.divide(
            np.sum(y_cumulative_sum),
            np.sum(x_cumulative_sum)
        )

        # b = y - a*x
        b = np.subtract(y_average, np.multiply(a, x_average))

        new_y = calculate_y(segments_x[i], a, b)

        # Fourth step: Calculating F(L) for each segments.
        f_l = calculate_each_segments_f_l(segments_length, a, b, new_y)
        f_l_list.append(f_l)

        # Saving each segment's formulas.
        formula_text = "{}. Y = {}*X + {} <strong>F(L) = {}</strong>"\
            .format(i + 1, a, b, f_l)

        for j in range(len(new_y)):
            segments_data = {
                'year' + str(i): segments_x[i][j],
                'level' + str(i): new_y[j]
            }
            calculated_data.append(segments_data)

            formula_text += "<br>&emsp;&emsp;Y[{}] = {}, X[{}] = {}"\
                .format(j + 1, new_y[j], j + 1, segments_x[i][j])

        formula_list.append(formula_text)

    # Fifth step: Calculating the average F^(L)
    # over all segments of the same length.
    f_l_average = calculate_average_f_l(f_l_list)

    # Sixth step: Calculating the alpha (Hurst Exponent).
    alpha = math.log(f_l_average, segments_length)

    return {
        'sample_data': sample_data,
        'calculated_data': calculated_data,
        'data_length': data_length,
        'segments_length': segments_length,
        'segments_number': segments_number,
        'formula_list': formula_list,
        'f_l_list': f_l_list,
        'f_l_average': f_l_average,
        'alpha': alpha,
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
