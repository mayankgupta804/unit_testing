import unittest
from temperature_converter import c_to_f, f_to_c

class TestTemperatureConverter(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTemperatureConverter, self).__init__(*args, **kwargs)

    def test_c_to_f_with_integers_and_float_arguments(self):
        input1 = 12.123 
        input2 = 44

        expected_output1 = 53.8214 
        expected_output2 = 111.2
        
        self.assertEqual(c_to_f(input1), expected_output1, "Temperature in Fahrenheit does not match!")
        self.assertEqual(c_to_f(input2), expected_output2, "Temperature in Fahrenheit does not match!")

    def test_f_to_c_with_invalid_arguments(self):
        input1 = "12"
        input2 = [123,12]

        with self.assertRaises(AssertionError):
            f_to_c(input1)

        with self.assertRaises(AssertionError):
            f_to_c(input2)     