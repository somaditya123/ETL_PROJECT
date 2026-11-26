#set is an unordered collection
#mutable # return the unique value #
test_cases = ["Login", "Search", "Checkout"]

for test in test_cases:
    value = input(f"Enter result for {test}: ")

    if value == test:
        print(test, "- Passed")
    else:
        print(test, "- Failed")
