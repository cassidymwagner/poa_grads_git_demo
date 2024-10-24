import numpy as np

def calc_mean(x):
    """Calculate the mean of an array of numbers.
    Parameters
    ----------
    x : array-like
        The array of numbers for which the mean is calculated.
    Returns
    -------
    mean : float
        The mean of the input array of numbers.
    
    """
    return np.mean(x)

def calc_median(x: np.ndarray) -> float:
    """Calculate the median of an array of numbers.
    Parameters
    ----------
    x : array-like
        The array of numbers for which the median is calculated.
    Returns
    -------
    median : float
        The median of the input array of numbers.
    
    """
    return np.median(x)

def calc_std(x):
    return np.std(x)

def calc_add(x, y):
    """Calculate the sum of two numbers.
    Parameters
    ----------
    x : float
        The first number.
    y : float
        The first number.
    Returns
    -------
    sum : float
        The sum of the two input numbers.
    """
    return x + y

def calc_sub(x, y):
    return x - y

def print_my_name(name):
    if not isinstance(name, str):
        raise ValueError("The input must be a string.")
    print("Hello, my name is", name)

def print_something_nice():
    print("You are doing a great job!")

def print_age(birth_year):
    print(f'I am {2024 - birth_year} years old.')


def print_favorite_animal(animal):
    if not isinstance(animal, str):
        raise ValueError("Input must be a string.")
    print("My favorite animal is", animal)