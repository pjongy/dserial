import unittest

from dserial.dserial import TypeCheckingDictSerializer


class TestTypes(TypeCheckingDictSerializer):
    int_val: int


class TestDefaultType(unittest.TestCase):
    def should_success_convert_dict_to_data_class(self):
        test_dict = {
            'int_val': 1
        }
        TestTypes(test_dict)

    def should_fail_declared_int_type_passed_string_type(self):
        with self.assertRaises(TypeError):
            test_dict = {
                'int_val': 'string_type'
            }
            TestTypes(test_dict)

    def should_success_type_cast_able(self):
        test_dict = {
            'int_val': '1'
        }
        TestTypes(test_dict)

    @staticmethod
    def get_test_suites():
        suite = unittest.TestSuite()
        test_list = [
            'should_success_convert_dict_to_data_class',
            'should_fail_declared_int_type_passed_string_type',
            'should_success_type_cast_able',
        ]
        for test_case in test_list:
            suite.addTest(TestDefaultType(test_case))
        return suite
