class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = dict()
        for s in strs:
            sorted_s = sorted(s)
            if out.get(str(sorted_s), "") != "":
                out[str(sorted_s)].append(s)
            else:
                out[str(sorted_s)] = [s]
        return list(out.values())