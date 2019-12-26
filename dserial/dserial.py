from abc import ABC, abstractmethod


class TypeCheckingDictSerializer:
    def __init__(self, arg):
        kwargs = {**arg}
        for attr, type_ in self.__annotations__.items():
            if attr not in kwargs:
                if hasattr(self, attr):
                    setattr(self, attr, getattr(self, attr))
                elif self.is_strict_check():
                    # Only if strict check, not passed, no default values
                    raise TypeError(f'Missing required attribute: {attr}')
            else:
                if kwargs[attr] is not None:
                    try:
                        if issubclass(type_, TypeAnnotatedList):
                            list_element_type = type_.get_type()
                            value = [list_element_type(elem) for elem in kwargs[attr]]
                        else:
                            value = type_(kwargs[attr])
                    except (TypeError, ValueError):
                        raise TypeError(
                            f'{self.__class__.__name__}.{attr} ' +
                            f'should be {type_} not {type(kwargs[attr])}'
                        )
                else:
                    value = kwargs[attr]

                setattr(self, attr, value)

    def is_strict_check(self) -> bool:
        return False

    def to_dict(self):
        def adjust_type(target):
            if issubclass(type(target), TypeCheckingDictSerializer):
                return target.to_dict()
            return target

        raw_dict = vars(self)
        return_dict = {}
        for key, value in raw_dict.items():
            if issubclass(type(value), list):
                return_dict[key] = [adjust_type(x) for x in value]
            else:
                return_dict[key] = adjust_type(value)

        return return_dict


class TypeAnnotatedList(list, ABC):
    @staticmethod
    @abstractmethod
    def get_type(): pass
