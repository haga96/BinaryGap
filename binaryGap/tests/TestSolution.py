from binaryGap import Solution


class TestSolution:
    def test_solution(self):
        s = Solution

        assert s.solution(32) == 0
        assert s.solution(9) == 2
        assert s.solution(20) == 1
        assert s.solution(15) == 0
        assert s.solution(1041) == 5
        assert s.solution(529) == 4
        assert s.solution(561892) == 3
        assert s.solution(74901729) == 4
        assert s.solution(1376796946) == 5
