import pytest


class Test(object):

    @pytest.mark.complete("nc -")
    def test_dash(self, completion):
        assert completion.list