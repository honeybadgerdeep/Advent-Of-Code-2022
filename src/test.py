def test_outcome(test_name: str, value: any, expectation: any) -> None:
    if (value != expectation):
        print("FAIL: " + test_name)
        print("Expected: " + str(expectation))
        print("Received: " + str(value))
        exit(1)
    else:
        print(test_name.upper() + " TESTS PASS!")