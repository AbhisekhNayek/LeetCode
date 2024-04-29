class Solution(object):
    def minOperations(self, nums, k):
        res_xor = 0
        for num in nums:
            res_xor ^= num

        final_xor = res_xor ^ k
        cnt_bits = 0

        while final_xor != 0:
            cnt_bits += final_xor & 1
            final_xor >>= 1

        return cnt_bits
