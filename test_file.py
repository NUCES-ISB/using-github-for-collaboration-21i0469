from app import add
import pytest


def test_add():
    assert add(1, 3) == 4  
    assert add(2, 2) == 4  
    assert add(-1, 5) == 4  
    assert add(0, 0) == 0 
    
    
if __name__ == "__main__":
    test_add()
