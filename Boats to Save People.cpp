#include <vector>
#include <algorithm>

class Solution {
public:
    int numRescueBoats(std::vector<int>& people, int limit) {
        int ans = 0;
        
        std::sort(people.begin(), people.end());
        
        for (int i = 0, j = people.size() - 1; i <= j; ++ans) {
            int remain = limit - people[j--];
            if (people[i] <= remain)
                ++i;
        }
        
        return ans;
    }
};
