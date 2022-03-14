class Solution:  
    def largestNumber(self, nums: List[int]) -> str:
        num = [str(x) for x in nums]
        num.sort(key = functools.cmp_to_key(lambda b, a: ((a+b)>(b+a))-((a+b)<(b+a)) ))
        return ''.join(num).lstrip('0') or '0'