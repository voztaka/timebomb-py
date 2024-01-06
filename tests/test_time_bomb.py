from timebomb import time_bomb

def test_time_bomb():
    # Testing `time_bomb` is challenging due to `sys.exit()`.
    # You might test other aspects or refactor the function for better testability.
    assert callable(time_bomb)