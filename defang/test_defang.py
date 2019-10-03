from defang import defang
import pytest

# make sure we're hooked up
def test_exists():
    assert defang

# test our standard ip
def test_vanilla():
    assert defang("1.1.1.1") == "1[.]1[.]1[.]1"

#Test for empty ip address passed in
def test_empty_string():
    with pytest.raises(ValueError, match='I am sorry, that ip address is empty.'):
        defang('')

# test for string without '.'
def test_no_periods():
    assert defang('1234') == '1234' 