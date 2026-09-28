class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def str_sort(s):
            return ''.join(sorted(s))

        debug_flag = False

        d = dict()
        for item in strs:
            if str_sort(item) in d:
                d[str_sort(item)].append(item)
            else:
                d[str_sort(item)] = [item]
        if debug_flag:
            print(list(d.values()))
        return list(d.values())