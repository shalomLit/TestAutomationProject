import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest():
    print("test base")
    pass