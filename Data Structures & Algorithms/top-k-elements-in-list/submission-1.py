class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        return list(dict(sorted(counter.items(), key= lambda x: x[1], reverse=True)).keys())[:k]