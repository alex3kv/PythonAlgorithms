'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''
from collections import Counter
from operator import itemgetter

class Huffman:
    def __init__(self, message):
        self._message = message
        self._elements = {}
        self._node = self._make_node()
        self._node.walk(self._elements, [])

    def _make_leaves(self, string):
        new_counted = {}

        for key, val in dict(Counter(string)).items():
            new_counted[self.Leaf(key)] = val

        return list(new_counted.items())

    def _make_node(self):
        items = self._make_leaves(self._message)

        while len(items) >= 2:
            left_leaf = items.pop()
            right_leaf = items.pop()

            leaf_count = left_leaf[1] + right_leaf[1]
            items.append((self.Node(left=left_leaf[0], right=right_leaf[0]), leaf_count))
            items.sort(key=itemgetter(1), reverse=True)

        return items.pop()[0]

    class Node:
        def __init__(self, left=None, right=None):
            self._left = left
            self._right = right

        def walk(self, code, value):
            self._left.walk(code, value + ['0'])
            self._right.walk(code, value + ['1'])

    class Leaf:
        def __init__(self, char):
            self._char = char

        def walk(self, code, value):
            code[self._char] = value    

    @property
    def elements(self):
        return self._elements

    def __str__(self):
        coded_string = []

        for i in self._message:
            coded_string += self._elements[i] + [' ']

        return ''.join(coded_string)


a = Huffman('тест текст тет')
print(a.elements)
print(a)
