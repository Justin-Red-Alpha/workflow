def add(a, b):
    return a + b

def test():
    assert add(1,2) == 3, "test failed"
    assert add(3,4) == 7, "test failed"
    assert add(5,6) != 10, "test failed"

if __name__ == "__main__":
    print(add(2, 3))
