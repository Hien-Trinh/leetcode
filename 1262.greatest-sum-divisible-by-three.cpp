/*
 * @lc app=leetcode id=1262 lang=cpp
 *
 * [1262] Greatest Sum Divisible by Three
 */

// @lc code=start
#include <vector>
using namespace std;
class Solution {
 public:
    int maxSumDivThree(vector<int>& nums) {
    vector<int> dp(3);
    for (int i : nums) {
      for (int j : vector<int>(dp)) {
        dp[(i + j) % 3] = max(dp[(i + j) % 3], i + j);
      }
    }
    return dp[0];
  }
};
// @lc code=end
