#!/usr/bin/env python3

import unittest


def flat_list(l):
    def nested_list_inside(l):
        for i in l:
            if isinstance(i, list):
                return True
        return False

    if not isinstance(l, list):
        raise TypeError

    res = []
    for elem in l:
        if isinstance(elem, list):
            res.extend(elem)
        else:
            res.append(elem)

    if nested_list_inside(res):
        res = flat_list(res)

    return res


class TestFlatList(unittest.TestCase):
    def setUp(self):
        self.test_vector = {
            'equal': [
                {
                    'before': [1, [2, [3, [4, 5]]]],
                    'after': [1, 2, 3, 4, 5]
                },
                {
                    'before': [1, [2, [3, [4, 5, []]]]],
                    'after': [1, 2, 3, 4, 5]
                },
                {
                    'before': [1, [2, None, [4, 5]]],
                    'after': [1, 2, None, 4, 5]
                },
                {
                    'before': [[1, 2, [3, []]], 4, 5],
                    'after': [1, 2, 3, 4, 5]
                },
                {
                    'before': [[[[[[[[[[[]]]]]]]]]]],
                    'after': []
                }
            ],
            'error': [
                {'value': None},
                {'value': '[ ]'},
                {'value': 720},
            ]
        }

    @staticmethod
    def hash_list(l):
        return hash(tuple(l))

    def test_equal(self):
        for vector in self.test_vector['equal']:
            after = vector['after']
            before = flat_list(vector['before'])
            self.assertEqual(self.hash_list(after),
                             self.hash_list(before))

    def test_error(self):
        for vector in self.test_vector['error']:
            self.assertRaises(TypeError, flat_list, vector['value'])


if __name__=='__main__':
    unittest.main()
