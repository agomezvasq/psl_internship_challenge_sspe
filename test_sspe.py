import unittest
import sspe


class TestSSPE(unittest.TestCase):

    def test_to_binary(self):
        string = ' _ '
        binary = sspe.to_binary(string)

        self.assertEqual(binary, '010')

    def test_to_digit(self):
        string = ' _ ' + \
                 ' _|' + \
                 '|_ '
        binary = sspe.to_binary(string)
        digit = sspe.to_digit(binary)

        self.assertEqual(digit, 2)

    def test_lines(self):
        string = '     _   _       _   _   _   _   _   _  \n' + \
                 '  |  _|  _| |_| |_  |_    | |_| |_| | | \n' + \
                 '  | |_   _|   |  _| |_|   | |_|   | |_| '
        digits = sspe.parse(string)

        self.assertEqual(digits, '1234567890')

    def test_file(self):
        with open('test.txt', 'r') as f:
            digits = sspe.parse(f.read())

            self.assertEqual(digits, '1234567890')


if __name__ == '__main__':
    unittest.main()
