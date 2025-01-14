#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> numStrings;
        for (int num : nums) {
            numStrings.push_back(to_string(num));
        }
        auto compare = [](const string& a, const string& b) {
            return a + b > b + a;
        };
        sort(numStrings.begin(), numStrings.end(), compare);
        if (numStrings[0] == "0") {
            return "0";
        }
        string result;
        for (const string& numStr : numStrings) {
            result += numStr;
        }
        return result;
    }
};
