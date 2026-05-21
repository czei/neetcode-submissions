class Solution:
    def isValid(self, s: str) -> bool:

        p_map = {")":"(","}":"{","]":"["}
        parens = []

        for p in s:
            if p in p_map.values():
                parens.append(p)
            else:
                if len(parens) == 0:
                    return False
                if parens[-1] == p_map[p]:
                    parens.pop()
                else:
                    return False
        return len(parens) == 0
        