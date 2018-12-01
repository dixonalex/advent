from advent import Config
import inject
import itertools


class Solutions:

    cfg = inject.attr(Config)

    def device_readings(self) -> [int]:
        with open(self.cfg.day_1["input"], "r") as f:
            for s in f.readlines():
                yield int(s)

    def day_1(self) -> tuple:
        """Day 1 challenges
	
            part_1: resulting frequency after all changes are applied
            part_2: the first frequency your device reaches twice

        Returns:
             part_1, part_2 (tuple)
         """

        frequencies = list(self.device_readings())
        part_1 = sum(frequencies)
        part_2_list = list()
        for i, f in enumerate(itertools.cycle(frequencies)):
            if i > 1000000:
                raise ValueError("Giving up after 1 million tries")
            part_2 = part_2_list[i - 1] + f if i > 0 else f
            if part_2 in part_2_list:
                # first freq read twice
                return part_1, part_2
            else:
                part_2_list.append(part_2)
