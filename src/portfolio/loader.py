import os
from .models import Position


def load_portfolio_from_env() -> list[Position]:
    """
    从环境变量 PORTFOLIO 读取持仓。

    格式：
    603986,100,675.20
    601208,500,67.39
    600487,300,116.05
    """
    raw = os.getenv("PORTFOLIO", "").strip()
    positions: list[Position] = []

    if not raw:
        return positions

    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue

        parts = [x.strip() for x in line.split(",")]
        if len(parts) != 3:
            continue

        code, shares, cost = parts

        try:
            positions.append(
                Position(
                    code=code,
                    shares=int(shares),
                    cost=float(cost),
                )
            )
        except ValueError:
            continue

    return positions
