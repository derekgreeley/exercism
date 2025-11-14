EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    """
    Return preparation time in minutes
 
    :param number_of_layers: int number of layers
    :return: int preparation time in minutes
    """
    return number_of_layers * PREPARATION_TIME
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed time in minutes
 
    :param number_of_layers: int number of layers
    :param elapsed_bake_time: int elapsed bake time
    :return: int elapsed time in minutes
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time