def test_outcome(test_name: str, value: any, expectation: any) -> None:
    if (value != expectation):
        print("FAIL: " + test_name)
        print("Expected: " + expectation)
        print("Received: " + value)
        exit(1)
    else:
        print(test_name.upper() + " TESTS PASS!")