from hello import hello

    # if the hello() function had a print statement
    # this wouldnt work because the function
    # hello() doesnt return a value

def test_argument():

    assert hello("David") == "hello, David"

    # using a loop and list
    for name in ["hermione", "harry", "ron"]:
        assert hello(name) ==f"hello, {name}"


def test_default():
    assert hello() == "hello, world"
