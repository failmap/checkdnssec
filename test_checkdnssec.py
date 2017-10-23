"""Verify basic functionality of this package."""

# run with: python setup.py test

from checkdnssec import get_dnssec

# domain name with and without DNSSEC
GOOD = 'faalkaart.nl'
BAD = 'example.com'


def test_good():
    """Test known positive."""
    assert get_dnssec(GOOD)


def test_bad():
    """Test known negative."""
    assert not get_dnssec(BAD)
