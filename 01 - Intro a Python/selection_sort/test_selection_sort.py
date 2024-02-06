from selection_sort import selection_sort
import unittest


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort_derecho(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(selection_sort([5, 2, 2, 10, 6, 5, 3], reverse=False), [
                         2, 2, 3, 5, 5, 6, 10])

    def test_selection_reves(self):
        self.assertEqual(selection_sort(
            [5, 4, 3, 2, 1], reverse=True), [5, 4, 3, 2, 1])
        self.assertEqual(selection_sort([5, 2, 2, 10, 6, 5, 3], reverse=True), [
                         10, 6, 5, 5, 3, 2, 2])
