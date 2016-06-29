import unittest
import Introduction_to_algorithm.section_7.qucik_sort as quick_sort


class test_quick_sort(unittest.TestCase):
    def test_result(self):
        ary = [1, 4, 7, 2, 5, 8, 3, 6, 9]
        self.assertEqual(quick_sort.quick_sort(ary),
                         sorted(ary))


        self.assertEqual(quick_sort.quick_sort(ary),
                         sorted(ary))

        ary = [i for i in range(-10000, 10000)]
        self.assertEqual(quick_sort.quick_sort(ary),
                         sorted(ary))


if __name__ == "__main__":
    unittest.main()
