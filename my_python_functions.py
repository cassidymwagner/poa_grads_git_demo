import numpy as np


def calc_mean(x: np.ndarray) -> float:
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


def calc_std(x: np.ndarray) -> float:
    return np.std(x)


def calc_add(x: float, y: float) -> float:
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


def calc_sub(x: float, y: float) -> float:
    """Calculate the difference between 2 numbers

    Parameters
    ----------
    x : float
        The first number
    y : float
        The second number

    Returns
    -------
    float
        The difference
    """
    return x - y


def print_my_name(name: str) -> None:
    if not isinstance(name, str):
        raise ValueError("The input must be a string.")
    print("Hello, my name is", name)


def print_something_nice() -> None:
    print("You are doing a great job!")


def print_age(birth_year: float) -> None:
    print(f"I am {2024 - birth_year} years old.")
