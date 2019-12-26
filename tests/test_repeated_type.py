import unittest

from dserial.dserial import TypeCheckingDictSerializer, TypeAnnotatedList


class TestRepeatedPrimitiveType(TypeCheckingDictSerializer):
    class PrimitiveList(TypeAnnotatedList):
        @staticmethod
        def get_type():
            return int

    repeated_val: PrimitiveList


class TestRepeatedType(unittest.TestCase):
    def should_success_convert_dict_to_data_class(self):
        test_dict = {
            'repeated_val': [1, 2, 3]
        }
        TestRepeatedPrimitiveType(test_dict)

    def should_success_convert_dict_to_data_class_type_cast(self):
        test_dict = {
            'repeated_val': ['1', 2, '3']
        }
        TestRepeatedPrimitiveType(test_dict)

    def should_fail_declared_list_element_wrong_type(self):
        with self.assertRaises(TypeError):
            test_dict = {
                'repeated_val': ['1', {2: 1}, '3']
            }
            TestRepeatedPrimitiveType(test_dict)

    @staticmethod
    def get_test_suites():
        suite = unittest.TestSuite()
        test_list = [
            'should_success_convert_dict_to_data_class',
            'should_success_convert_dict_to_data_class_type_cast',
            'should_fail_declared_list_element_wrong_type',
        ]
        for test_case in test_list:
            suite.addTest(TestRepeatedType(test_case))
        return suite
