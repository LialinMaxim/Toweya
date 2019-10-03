"""
Implement a group_by_owners function that: Accepts a dictionary containing the file owner name for each file name. 
Returns a dictionary containing a list of file names for each owner name, in any order.  

For example, for dictionary
{'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

the group_by_owners function should return
{'Randy': ['Input.txt', 'Output.txt'], 'Stan': [‘Code.py’]}.

"""


def group_by_owners(data: dict) -> dict:
    result = {}
    for k, v in data.items():
        result[v] = result.get(v, []) + [k]
    return result


if __name__ == '__main__':
    expect = {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}

    assert expect == group_by_owners(
        {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
    )

    # with different order
    assert expect == group_by_owners(
        {'Code.py': 'Stan', 'Input.txt': 'Randy', 'Output.txt': 'Randy'}
    )
