import pytest
import fonctions as f

def test_1():
	assert f.puissance(2,3) == 8
	assert f.puissance(-2,-2) == 0.25
	assert f.puissance(-5,0) == 1
	assert f.puissance(0,58) == 0



