from esgflib.data.datasets import get_melbourne_data


def test_get_melbourne_data():
    '''
    Test the get_melbourne_data function.
    '''
    # Get the data
    data = get_melbourne_data()
    # Check dataset is not empty
    assert len(data) > 0
