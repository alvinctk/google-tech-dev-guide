class Solution:
    def nextClosestTime(self, time):
        """
        1. Start from the last digit, find the first digit that is increase-able,
        that is, we can increase this digits without violating the following condition -
              minutes < 60 and hours < 24

        2. If we cannot increase this digit, then we set digit to be the minimum number
        and try to increase the next digit.

        Time complexity: O(n log n) since dominated by .sort O(n log n)

        Space complexity: O(n) using list and sets to store data.
        Runtime: 32 ms, faster than 96.81% of Python3 online submissions for Next Closest Time.
        Memory Usage: 13.8 MB, less than 16.67% of Python3 online submissions for Next Closest Time.
        """
        time = list(time)

        digits = list(set(time[:2] + time[3:]))

        if len(digits) == 1:
            return "".join(time)

        digits.sort()

        h1, h0 = (0, "2"), (1, ["9", "3"][time[0] == "2"])
        m1, m0 = (3, "5"), (4, "9")

        for i, limit in [m0, m1, h0, h1]:
            min_closest_digits = [d for d in digits if time[i] < d <= limit]
            if min_closest_digits:
                time[i] = min_closest_digits[0]
                break
            else:
                time[i] = digits[0]

        return "".join(time)

if __name__ == "__main__":
    s = Solution()
    test = ["18:42", "19:34", "13:29", "10:59", "23:59"]
    answer = ["18:44", "19:39", "13:31", "11:00", "22:22"]
    for t, a in zip(test, answer):
        time = s.nextClosestTime(t)
        assert time == a, print("{} != {}".format(time, a))
        print("nextClosestTime({}) = {}".format(t, s.nextClosestTime(t)))
