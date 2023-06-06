# import inc_dec    # The code to test
from inc_dec import increment, decrement

def test_increment():
    assert increment(3) == 4

# This test is designed to fail for demonstration purposes.
def test_decrement():
    assert decrement(3) == 4
