#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
                continue

            is_destroyed = False
            while stack and stack[-1] > 0:
                if stack[-1] > -a:
                    is_destroyed = True
                    break
                elif stack[-1] == -a:
                    is_destroyed = True
                    stack.pop()
                    break

                stack.pop()

            if not is_destroyed:
                stack.append(a)

        return stack
# @lc code=end

