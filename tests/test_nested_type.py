import unittest

from dserial.dserial import TypeCheckingDictSerializer


class TestNestedTypeParent(TypeCheckingDictSerializer):
    class Child(TypeCheckingDictSerializer):
        child_val: int
        child_val_2: str

    parent_val: int
    child_type: Child


class TestNestedType(unittest.TestCase):
    def should_success_convert_dict_to_data_class(self):
        test_dict = {
            'parent_val': 1,
            'child_type': {
                'child_val': 1,
                'child_val_2': 2
            }
        }
        TestNestedTypeParent(test_dict)

    @staticmethod
    def get_test_suites():
        suite = unittest.TestSuite()
        test_list = [
            'should_success_convert_dict_to_data_class',
        ]
        for test_case in test_list:
            suite.addTest(TestNestedType(test_case))
        return suite
