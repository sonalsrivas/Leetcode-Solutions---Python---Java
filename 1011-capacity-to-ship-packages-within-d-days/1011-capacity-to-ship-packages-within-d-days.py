class Solution:
    def shipWithinDays(self, weights, days):
        lower, upper = max(weights), sum(weights)
        
        def can_hold_weight(cand_weight, weights):
            min_segments = 1
            cur_sum = 0
            for weight in weights:
                cur_sum += weight
                if cur_sum > cand_weight:
                    min_segments += 1
                    cur_sum = weight
            
            return min_segments <= days
        
        while lower < upper:
            weight_cand = (lower + upper) >> 1
            if can_hold_weight(weight_cand, weights):
                upper = weight_cand
            else:
                lower = weight_cand + 1
        
        return lower
        