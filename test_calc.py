import pytest
from calc import soma, sub, multi, divi

@pytest.mark.parametrize('a,b,esp', [(1,1,2),(1,2,3),(2,3,5)])
def test_soma(a,b,esp):
 assert soma(a,b) == esp

@pytest.mark.parametrize('a,b,esp',[(1,1,0),(1,2,-1),(2,3,-1)])
def test_sub(a,b,esp):
 assert sub(a,b) == esp

@pytest.mark.parametrize('a,b,esp',[(1,1,1),(1,2,2),(2,3,6)])
def test_multi(a,b,esp):
 assert multi(a,b) == esp

@pytest.mark.parametrize('a,b,esp',[(1,1,1),(1,2,0.5),(2,3,0.6666666666666666)])
def test_divi(a,b,esp):
 assert divi(a,b) == esp


