import unittest

from dserial.dserial import TypeCheckingDictSerializer


class TestTypesStrict(TypeCheckingDictSerializer):
    int_val: int
    str_val: str

    def is_strict_check(self) -> bool:
        return True


class TestDefaultTypeStrict(unittest.TestCase):
    def should_success_convert_dict_to_data_class(self):
        test_dict = {
            'int_val': 1,
            'str_val': 'string'
        }
        TestTypesStrict(test_dict)

    def should_fail_unsatisfied_element_exists(self):
        with self.assertRaises(TypeError):
            test_dict = {
                'int_val': 1
            }
            TestTypesStrict(test_dict)

    def should_success_type_cast_able(self):
        test_dict = {
            'int_val': '1',
            'str_val': 1
        }
        TestTypesStrict(test_dict)

    @staticmethod
    def get_test_suites():
        suite = unittest.TestSuite()
        test_list = [
            'should_success_convert_dict_to_data_class',
            'should_fail_unsatisfied_element_exists',
            'should_success_type_cast_able',
        ]
        for test_case in test_list:
            suite.addTest(TestDefaultTypeStrict(test_case))
        return suite
