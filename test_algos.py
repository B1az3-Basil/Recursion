import unittest
import super_algos

class MyTestCase(unittest.TestCase):
    def test_find_min(self):
        check = super_algos.find_min([1 , 1 , 1 , 1 , 1])
        self.assertEqual(1 ,check)
        check = super_algos.find_min([1 , 'b', 'f', 5, 3])
        self.assertEqual(-1 ,check)
        check = super_algos.find_min([1 , 1, -1, 5, 3])
        self.assertEqual(-1 ,check)
        check = super_algos.find_min([1 , 1, -1, -5, 3])
        self.assertEqual(-5 ,check)
        check = super_algos.find_min([5])
        self.assertEqual(5 ,check)


    def test_sum_all(self):
        check = super_algos.sum_all(['a', 2 , 6 , 7, 'b'])
        self.assertEqual(-1, check)
        check = super_algos.sum_all([])
        self.assertEqual(-1 , check)
        check = super_algos.sum_all([5])
        self.assertEqual(5 , check)
        check = super_algos.sum_all([100, 3 , 5 , 10 , 6, 10 , 3, 20 , 100 , 4 , 200 , 600])
        self.assertEqual(1061, check)
        check = super_algos.sum_all([-100, -200, 200 , 100])
        self.assertEqual(0 , check)
        check = super_algos.sum_all([-100, -100])
        self.assertEqual(-200, check)
    
    def test_find_possible_strings(self):
        check = super_algos.find_possible_strings(['a', 'b', 'c'], 4)
        self.assertEqual(['aaaa', 'aaab', 'aaac', 'aaba', 'aabb', 'aabc', 'aaca', 'aacb', 'aacc', 'abaa', 'abab', 'abac', 'abba', 'abbb', 'abbc', 'abca', 'abcb', 'abcc', 'acaa', 'acab', 'acac', 'acba', 'acbb', 'acbc', 'acca', 'accb', 'accc', 'baaa', 'baab', 'baac', 'baba', 'babb', 'babc', 'baca', 'bacb', 'bacc', 'bbaa', 'bbab', 'bbac', 'bbba', 'bbbb', 'bbbc', 'bbca', 'bbcb', 'bbcc', 'bcaa', 'bcab', 'bcac', 'bcba', 'bcbb', 'bcbc', 'bcca', 'bccb', 'bccc', 'caaa', 'caab', 'caac', 'caba', 'cabb', 'cabc', 'caca', 'cacb', 'cacc', 'cbaa', 'cbab', 'cbac', 'cbba', 'cbbb', 'cbbc', 'cbca', 'cbcb', 'cbcc', 'ccaa', 'ccab', 'ccac', 'ccba', 'ccbb', 'ccbc', 'ccca', 'cccb', 'cccc'], check)
        check = super_algos.find_possible_strings(['a', 5, 6 ,'g'] , 2)
        self.assertEqual([], check)
        check = super_algos.find_possible_strings(['3', '5', 6], 7)
        self.assertEqual([], check)
        check = super_algos.find_possible_strings(['a','b', 'c'], 1)
        self.assertEqual(['a', 'b', 'c'], check)
        check = super_algos.find_possible_strings(['a','b'], 3)
        self.assertEqual(['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'], check)