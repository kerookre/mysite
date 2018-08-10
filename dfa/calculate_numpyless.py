# These functions are no longer used, because the
# end results are not as much precise as like in
# numpy library.


def calculate_average_level(levels_list):
    """
    Calculates the arithmetic average of all levels in given series.

    Args:
        levels_list (list): A list of levels (Xn series).

    Returns:
        The calculated arithmetic average as float.
    """
    sum_of_levels = 0
    for level in levels_list:
        sum_of_levels += level
    return sum_of_levels / len(levels_list)


def calculate_cumulative_sum(levels, average):
    """
    Calculates the cumulative sum for each given fragment of levels
    (Xn series) and its arithmetic average.

    Args:
        levels (list): A fragment or whole list of levels.
        average (float): A pre-calculated arithmetic average.

    Returns:
        A cumulative sum of elements from X1 to Xn.
    """
    # Variable with value 0, which will store the results.
    fragment_cumulative_sum = 0
    # For every numbers in each fragment list.
    for level in levels:
        # Calculating sum by subtracting the arithmetic average.
        fragment_cumulative_sum += (level - average)
    return fragment_cumulative_sum


def get_cumulative_sum(levels, average):
    """
    Calculates the cumulative sum using the list of levels (Xn series)
    and its arithmetic average.

    Args:
        levels (list): A list of levels (Xn series).
        average (float): A pre-calculated arithmetic average.

    Returns:

    """
    # Empty list, which will store the results.
    cumulative_sum = []
    # In other to send the fragments like:
    # 1. [x1]
    # 2. [x1, x2]
    # ... ...
    # n. [x1, x2, x3, ..., xn], starting the for loop from 1 to n + 1
    # and finally slicing the list in each loop.
    for i in range(1, len(levels) + 1):
        # Appending to a list, the calculated cumulative sums of each fragment.
        cumulative_sum.append(calculate_cumulative_sum(levels[:i], average))
    return cumulative_sum


def calculate_not_using_numpy(levels):
    """

    :param levels:
    :return:
    """
    # First step: Calculating the average of <Xn>.
    average = calculate_average_level(levels)
    # Second step: Converting the series to a "random walk".
    # i.e.: Calculating the cumulative sums.
    cumulative_sum = get_cumulative_sum(levels, average)
    return average, cumulative_sum
