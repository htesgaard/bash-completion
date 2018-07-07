import pytest


class TestIperf3(object):

    @pytest.mark.complete("iperf3 ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("iperf3 --bind ")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("iperf3 --client foo --")
    def test_3(self, completion):
        assert completion.list and "--daemon" not in completion.list

    @pytest.mark.complete("iperf3 --server --")
    def test_4(self, completion):
        assert "--daemon" in completion.list