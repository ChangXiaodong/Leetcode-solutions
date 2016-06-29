import unittest
import Introduction_to_algorithm.section_9.randomized_select as select


class test_randomized_select(unittest.TestCase):

    def test_find_ist_number(self):
        i = 5
        ary = [1, 4, 7, 2, 5, 8, 3, 6, 9, 0]
        self.assertEqual(select.find_ist_number(ary, i),
                         sorted(ary)[i - 1])

    def test_randomized_partition(self):
        ary = [1, 4, 7, 2, 5, 8, 3, 6, 9, 0]
        origin = (1, 4, 7, 2, 5, 8, 3, 6, 9, 0)
        random, partition = select.random_partition(
            ary,
            0,
            len(ary) - 1
        )
        self.assertEqual(origin[random], partition)


if __name__ == "__main__":
    unittest.main()
