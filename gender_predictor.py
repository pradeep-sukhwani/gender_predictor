from sex_machine.sexmachine.detector import Detector
from sys import argv
import unittest


def gender_predictor(name):
    """It is object of the class Detector defined in detector.py
    file. Here get_gender is function defined in detector.py file
    which checks whether the gender is male or female.
    """

    detector_obj = Detector()
    # To ensure the string has first character capitalised and all other chars in lower case
    name_translated = name.title()
    output = detector_obj.get_gender(name_translated)
    return output


def main():
    """checks the input if it has a name of a person, if it has then it is
    uses the builtin python function title() to make sure that the first
    letter is uppercase and rest are lowercase because that is the limitation
    of the API, the first letter should be in uppercase or else it will show
    as andy (it won't recognize the gender.) then it checks whether it is alphabet
    and then it finally gives the output.
    """

    if len(argv) == 2:
        input_name = argv[1]
        if input_name.isalpha():
            print gender_predictor(input_name)
        else:
            raise Exception('Please enter valid input')
    else:
        raise Exception('Please enter name')


class TestGenderPredictor(unittest.TestCase):
    """Not adding test cases for non alphabetical as they create exceptions."""

    def test_for_capitalized_letter_male(self):
        actual_output = gender_predictor('RAJU')
        self.assertEqual(actual_output, 'male', 'test failed')

    def test_for_capitalized_letter_female(self):
        actual_output = gender_predictor('PRIYA')
        self.assertEqual(actual_output, 'female', 'test failed')

    def test_for_normal_letter_male(self):
        actual_output = gender_predictor('Raju')
        self.assertEqual(actual_output, 'male', 'test failed')

    def test_for_normal_letter_female(self):
        actual_output = gender_predictor('PRIYA')
        self.assertEqual(actual_output, 'female', 'test failed')

    def test_for_small_letter_male(self):
        actual_output = gender_predictor('raju')
        self.assertEqual(actual_output, 'male', 'test failed')

    def test_for_small_letter_female(self):
        actual_output = gender_predictor('priya')
        self.assertEqual(actual_output, 'female', 'test failed')


if __name__ == "__main__":
    main()
