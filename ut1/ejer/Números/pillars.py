# **********************
# POSTES EN LA CARRETERA
# **********************


def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    width = pillar_width * (num_pillars -2)
    distance = (num_pillars - 1) * (gap_pillars * 100)
    inter_distance = width + distance
    return inter_distance


if __name__ == '__main__':
    run(10, 5, 30)