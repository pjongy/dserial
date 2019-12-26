import unittest

from tests.test_default_type import TestDefaultType
from tests.test_default_type_strict import TestDefaultTypeStrict
from tests.test_nested_type import TestNestedType
from tests.test_nested_type_strict import TestNestedTypeStrict
from tests.test_repeated_nested_type import TestRepeatedNestedType
from tests.test_repeated_type import TestRepeatedType

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(TestDefaultType.get_test_suites())
    runner.run(TestDefaultTypeStrict.get_test_suites())
    runner.run(TestNestedType.get_test_suites())
    runner.run(TestNestedTypeStrict.get_test_suites())
    runner.run(TestRepeatedType.get_test_suites())
    runner.run(TestRepeatedNestedType.get_test_suites())
