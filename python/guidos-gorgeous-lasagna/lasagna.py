"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - the number of layers you want to add to the lasagna.
    :return: int - total preparation time (in minutes).

    Function that takes the number of layers as an argument and returns the time
    it takes to prepare them, assuming each layer takes 2 minutes.
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate total elapsed cooking time (prep + bake) in minutes.

    :param number_of_layers: int - the number of layers you want to add to the lasagna.
    :param elapsed_bake_time: int - elapsed baking time.
    :return: int - total elapsed cooking time (in minutes).

    Function that takes two parameters: the number of layers you want to add to
    the lasagna, and the elapsed baking time in minutes. It returns the total
    elapsed cooking time (in minutes) which is the sum of the preparation time
    and the elapsed baking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
