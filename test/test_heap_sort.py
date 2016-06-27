import unittest
import Introduction_to_algorithm.section_6.heap_sort as heap_sort


class test_heap_sort(unittest.TestCase):
    def test_sort_result(self):
        ary = [1, 4, 7, 8, 5, 2, 3, 6, 9]
        result = heap_sort.heap_sort(ary)
        self.assertEqual(sorted(ary), result)

    def test_build_max_heap(self):
        ary = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        result = heap_sort.build_max_heap(ary)
        self.assertEqual([16, 14, 10, 8, 7, 9, 3, 2, 4, 1], result)

    def test_max_heap(self):
        ary = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        result = heap_sort.max_heap(ary, 1, len(ary))
        self.assertEqual([16, 14, 10, 8, 7, 9, 3, 2, 4, 1], result)


if __name__ == "__main__":
    unittest.main()
