# 1079. Letter Tile Possibilities
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = 0
        t_list = list(tiles)
        t_list.sort()
        new_t = "".join(t_list)

        def backtrack(t, cur, k):
            if len(cur) == k:
                nonlocal res
                res += 1
                return
            for i in range(len(t)):
                if i > 0 and t[i] == t[i - 1]:
                    continue
                backtrack(t[:i] + t[i + 1 :], cur + t[i], k)

        for i in range(1, len(new_t) + 1):
            backtrack(new_t, "", i)
        return res


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        def backtrack(t, cur, k):
            if k == len(cur):
                res.add(cur)
                return
            for i in range(len(t)):
                backtrack(t[:i] + t[i + 1 :], cur + t[i], k)

        for i in range(1, len(tiles) + 1):
            backtrack(tiles, "", i)

        print(res)
        return len(res)


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        char_list = list(tiles)
        char_list.sort()

        def backtrack(chars, cur):
            if not chars and cur:
                res.add(cur)
                return

            for i in range(len(chars)):
                if i > 0 and chars[i] == chars[i - 1]:
                    continue
                backtrack(chars[:i] + chars[i + 1 :], cur + chars[i])
                backtrack(chars[:i] + chars[i + 1 :], cur)

        backtrack(char_list, "")
        return len(res)
