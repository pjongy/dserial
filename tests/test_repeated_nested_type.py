import unittest

from dserial.dserial import TypeCheckingDictSerializer, TypeAnnotatedList


class ComplexDataType(TypeCheckingDictSerializer):
    int_val: int
    str_val: str


class TestRepeatedComplexDataType(TypeCheckingDictSerializer):
    class ComplexDataList(TypeAnnotatedList):
        class ComplexDataType(TypeCheckingDictSerializer):
            int_val: int
            str_val: str

        @staticmethod
        def get_type():
            return ComplexDataType

    repeated_val: ComplexDataList


class TestRepeatedNestedType(unittest.TestCase):
    def should_success_convert_dict_to_data_class(self):
        test_dict = {
            'repeated_val': [
                {
                    'int_val': 1,
                },
                {
                    'int_val': 1,
                    'str_val': 2,
                },
            ]
        }
        TestRepeatedComplexDataType(test_dict)

    def should_success_convert_dict_to_data_class_type_cast(self):
        test_dict = {
            'repeated_val': [
                {
                    'int_val': '1',
                },
                {
                    'int_val': 1,
                    'str_val': '2',
                },
            ]
        }
        TestRepeatedComplexDataType(test_dict)

    def should_fail_declared_list_element_wrong_type(self):
        with self.assertRaises(TypeError):
            test_dict = {
                'repeated_val': {'int_val': '1'}
            }
            TestRepeatedComplexDataType(test_dict)

    @staticmethod
    def get_test_suites():
        suite = unittest.TestSuite()
        test_list = [
            'should_success_convert_dict_to_data_class',
            'should_success_convert_dict_to_data_class_type_cast',
            'should_fail_declared_list_element_wrong_type',
        ]
        for test_case in test_list:
            suite.addTest(TestRepeatedNestedType(test_case))
        return suite
