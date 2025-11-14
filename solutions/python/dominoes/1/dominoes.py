from typing import List, Tuple, Optional

Domino = Tuple[int, int]

def can_chain(dominoes: List[Domino]) -> Optional[List[Domino]]:
    if not dominoes:
        return []

    def build_chain(path: List[Domino], remaining: List[Domino]) -> Optional[List[Domino]]:
        if not remaining:
            if path[0][0] == path[-1][1]:
                return path
            return None

        for i, domino in enumerate(remaining):
            rest = remaining[:i] + remaining[i+1:]
            if path[-1][1] == domino[0]:
                result = build_chain(path + [domino], rest)
                if result:
                    return result
            elif path[-1][1] == domino[1]:
                result = build_chain(path + [(domino[1], domino[0])], rest)
                if result:
                    return result
        return None

    for i, start in enumerate(dominoes):
        rest = dominoes[:i] + dominoes[i+1:]
        result = build_chain([start], rest)
        if result:
            return result
        flipped_start = (start[1], start[0])
        result = build_chain([flipped_start], rest)
        if result:
            return result

    return None
