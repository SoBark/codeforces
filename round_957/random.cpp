#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

int main()
{
    int n;
    std::cin >> n;

    std::vector<long long> nums(n);

    for (int i = 0; i < n; ++i)
        std::cin >> nums[i];

    std::sort(nums.begin(), nums.end(), std::less<long long>());

    long long res = 0;
    int i = 0;
    int j = n - 2;
    bool flag = false;

    while ( i < j ){

        if (nums[j+1] - nums[j] >= (nums[i+1] - nums[i])*(i+1) ){
            res += (nums[i+1] - nums[i])*(i+1);
            i++;
        }
        else{
            res += nums[j+1] - nums[j];
            nums[j] += nums[j+1] - nums[j];
            j--;
        }
    }

    std::cout << res;

    return 0;
}