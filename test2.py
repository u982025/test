import pytest

@pytest.fixture
def passwd():
    with open("/etc/passwd") as f:
        yield f.readlines()

def test_has_lines(passwd):
    print('testing test has lines')
    assert len(passwd) >= 301

def test_nos_lines(passwd):
    print('testing test has no lines')
    assert len(passwd) >= 1
