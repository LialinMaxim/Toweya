"""
Implement the unique_names method.
When passed two lists of names, it will return a list containing the names that appear in either or both lists.
The returned list should have no duplicates.  

For example, calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])
should return a list containing Ava, Emma, Olivia, and Sophia in ascending order. 
"""


class NameHandler:
    @staticmethod
    def unique_names(*args):
        return sorted(
            list(
                set(name for data_list in args for name in data_list)  # join all list from args
            )
        )

    @staticmethod
    def unique_names_and_validate(*args):
        result = set()
        for arg in args:
            if not isinstance(arg, list):
                raise ValueError(f"{arg} - Must be a list")
            else:
                for s in arg:
                    if not isinstance(s, str):
                        raise ValueError(f"{s} - Must be a sting")
                    else:
                        result.add(s)
        return sorted(list(result))


if __name__ == '__main__':
    nh = NameHandler()
    expect = ['Ava', 'Emma', 'Olivia', 'Sophia']

    # base test
    assert expect == nh.unique_names(
        ['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']
    )

    # base more similar argument
    assert expect == nh.unique_names(
        ['Ava', 'Emma', 'Emma', 'Olivia'], ['Ava', 'Olivia', 'Ava', 'Sophia', 'Emma']
    )

    # one list
    assert expect == nh.unique_names(
        ['Sophia', 'Ava', 'Emma', 'Olivia']
    )

    # many arguments
    assert expect == nh.unique_names(
        ['Ava', 'Emma', ], [], ['Emma', 'Olivia'], ['Ava', 'Olivia', 'Ava', 'Sophia', 'Emma'], []
    )
