def xor_sum(piles):
    xor_sum = 0
    for pile in piles:
        xor_sum ^= pile
    return xor_sum

def can_win(piles):
    def helper(piles):
        xor = xor_sum(piles)
        if xor == 0:
            return False

        for pile in piles:
            for k in range(1, min(pile, xor)+1):
                new_piles = [p-k if p == pile else p for p in piles]
                if not helper(new_piles):
                    return True
        return False
    
    return helper(piles)

# 示例：
piles = [1, 2, 3]
result = can_win(piles)
if result:
    print("Alice wins")
else:
    print("Bob wins")