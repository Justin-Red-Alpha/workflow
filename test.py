from main import subtract

def test():
    assert subtract(2, 1) == 1, "test failed"
    assert subtract(5, 3) == 2, "test failed"
    assert subtract(9, 5) != 5, "test failed"

if __name__ == "__main__":
    test()