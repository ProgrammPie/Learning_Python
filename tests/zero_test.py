from hello.main import greet


def test_greet_basic() -> None:
    assert greet("World") == "Hello, World!"


def test_greet_empty() -> None:
    assert greet("") == "Hello, !"
