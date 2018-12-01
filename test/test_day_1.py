import inject
import pytest
from advent import Config
from advent.solutions import Solutions


class Test2018Day1:
    @pytest.fixture()
    def frequencies(self) -> [str]:
        """The example input from advent of code 2018 day 1"""
        return [1, -2, 3, 1]

    @pytest.fixture(autouse=True)
    def setup(self, tmpdir, frequencies):
        p = tmpdir.join("day_1.txt")
        p.write("\n".join([str(f) for f in frequencies]))

        def configure(binder):
            cfg = Config(day_1={"input": p.strpath})
            binder.bind(Config, cfg)

        inject.clear_and_configure(configure)

    def test_solution(self):
        """
        input of [+1, -2, +3, +1] would result in
        0  + 1  -> 1
        1  + -2 -> -1
        -1 + 3  -> 2
        2  + 1  -> 3
        """
        # Arrange
        sut = Solutions()
        # Act
        part_1, part_2 = sut.day_1()
        # Assert
        assert part_1 == 3
        assert part_2 == 2
