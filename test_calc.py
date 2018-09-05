import pytest
from calc import soma

@pytest.mark.parametrize('a,b,esp', [(1,1,2),(1,2,3),(2,3,5)])
def test_soma(a,b,esp):
 assert soma(a,b) == esp
 
