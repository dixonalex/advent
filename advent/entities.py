from dataclasses import dataclass
import itertools


@dataclass
class Claim:
    id: int
    from_left: int
    from_top: int
    width: int
    height: int

    @property
    def coordinates(self) -> [(int, int)]:
        x_coords = [x + self.from_left for x in range(0, self.width)]
        y_coords = [y + self.from_top for y in range(0, self.height)]
        return set(itertools.product(x_coords, y_coords))

    @classmethod
    def from_elf(cls, line):
        _id, _, offset, area = line.split(" ")
        _id = _id.replace("#", "")
        from_left, from_top = offset.replace(":", "").split(",")
        width, height = area.split("x")
        props = [_id, from_left, from_top, width, height]
        props = [int(p) for p in props]
        return cls(*props)
