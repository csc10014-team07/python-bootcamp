def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Problem: Return the indices of two numbers whose sum equals target.
    Complete C++ Version:

    vector<int> two_sum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (seen.find(complement) != seen.end()) {
                return {seen[complement], i};
            }

            seen[nums[i]] = i;
        }

        return {};
    }

    One difference from C++ version
    Python uses 'in' for dictionary key lookup instead of C++'s find().

    Args:
        nums: List of integers to search.
        target: The sum the two numbers must add up to.

    Returns:
        A list ``[i, j]`` with the indices of the two numbers that add up to
        ``target``, or an empty list if no such pair exists.
    """
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []


if __name__ == "__main__":
    print("Trường hợp A:", two_sum([2, 7, 11, 15], 9))
    print("Trường hợp B:", two_sum([3, 2, 4], 6))
    print("Trường hợp C:", two_sum([3, 3], 6))
    print("Trường hợp D:", two_sum([1, 2, 3], 10))
