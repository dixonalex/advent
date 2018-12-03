import inject
import pytest
from advent import Config, Claim
from advent.solutions import Solutions


class TestSolutions:
    @pytest.fixture()
    def frequencies(self) -> [str]:
        """The example input from advent of code 2018 day 1"""
        return [1, -2, 3, 1]

    @pytest.fixture()
    def ids(self) -> [str]:
        """The example input from advent of code 2018 day 2"""
        return ["abcdef", "bababc", "abbcde", "aacccd", "abcdee", "ababab"]

    @pytest.fixture()
    def claims(self) -> [str]:
        """Day 3"""
        return ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]

    @pytest.fixture(autouse=True)
    def setup(self, tmpdir, frequencies, ids, claims):
        p = tmpdir.join("day_1.txt")
        p.write("\n".join([str(f) for f in frequencies]))
        p2 = tmpdir.join("day_2.txt")
        p2.write("\n".join(ids))
        p3 = tmpdir.join("day_3.txt")
        p3.write("\n".join(claims))

        def configure(binder):
            cfg = Config(day_1=p.strpath, day_2=p2.strpath, day_3=p3.strpath)
            binder.bind(Config, cfg)

        inject.clear_and_configure(configure)

    def test_day_1(self):
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

    def test_day_2(self):
        # Arrange
        sut = Solutions()
        # Act
        part_1, part_2 = sut.day_2()
        # Assert
        assert part_1 == 12
        assert part_2 == "abcde"

    def test_day_3_claim(self):
        # Arrange
        line = "#1 @ 429,177: 12x27"
        # Act
        claim = Claim.from_elf(line)
        # Assert
        assert claim.id == 1
        assert claim.from_left == 429
        assert claim.from_top == 177
        assert claim.width == 12
        assert claim.height == 27

    def test_day_3(self):
        # Arrange
        sut = Solutions()
        # Act
        part_1, part_2 = sut.day_3()
        # Assert
        assert part_1 == 4
