from esgflib.data.datasets import get_melbourne_data, split_train_test_data


def test_get_melbourne_data():
    '''
    Test the get_melbourne_data function.
    '''
    # Get the data
    data = get_melbourne_data()
    # Check dataset is not empty
    assert len(data) > 0


def test_split_train_test_data():
    '''
    Test the split_train_test_data function.
    '''
    # Get the data
    data = get_melbourne_data()
    # Split the data
    train, test = split_train_test_data(data, split_year="1986")
    # Check the train and test data are not empty
    assert len(train) > 0
    assert len(test) > 0
