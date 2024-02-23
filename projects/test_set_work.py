import projects.set_work
import pytest


def test_element_list():
    assert projects.set_work.element_list() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def test_for_length_of_list():
    assert projects.set_work.length_of_list() == 15


def test_for_duplicate_of_list():
    assert projects.set_work.duplicate_of_list() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def test_removal_of_duplicate_of_list():
    assert projects.set_work.removal_of_duplicate_of_list() ==[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
