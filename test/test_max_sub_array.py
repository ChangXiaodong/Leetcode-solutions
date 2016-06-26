import unittest
import max_sub_array


class test_max_sub_array(unittest.TestCase):
    def setUp(self):
        self.A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -222, 15, 50, -100]

    def test_two_algorithm_equal(self):
        recursive = max_sub_array.find_max_array(self.A, 0, len(self.A) - 1)
        liner = max_sub_array.find_max_sub_array_liner(self.A)
        self.assertEqual(recursive, liner)

    def test_recursive_algorithm(self):
        self.assertEqual(max_sub_array.find_max_array(self.A, 0, len(self.A) - 1),
                         (13, 14, 65)
                         )

    def test_liner_algorithm(self):
        self.assertEqual(max_sub_array.find_max_sub_array_liner(self.A),
                         (13, 14, 65)
                         )


if __name__ == "__main__":
    unittest.main()
