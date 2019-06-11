from collections import deque

class Solution:
    def print_debug(self, msg, dq=None, debug_dq=None, result=None, debug=True):
        if debug and dq is not None:
            print(msg + "dq={}, debug_dq={}, result={}".format(dq, debug_dq, result))
        elif debug:
            print(msg)

    def add_to_dq(self, dq, debug_dq, nums, end):
        while len(dq) and nums[dq[-1]] <= nums[end]:
            # Remove any smaller number from the back of the queue
            # To ensure that if nums[i] is the maximum for the window k,
            # Then it will move up to the first element
            dq.pop()
            debug_dq.pop()

        dq.append(end)
        debug_dq.append(nums[end])

    def add_to_result(self, dq, nums, result):
        if len(dq):
            result.append(nums[dq[0]])

    def remove_elements_out_of_window(self, dq, debug_dq, start):
        # Remove elements out of the window
        while len(dq) > 0 and dq[0] < start:
            dq.popleft()
            debug_dq.popleft()

    def maxSlidingWindow(self, nums, k):
        dq = deque()
        debug_dq = deque()
        debug = self.print_debug

        result = []

        # initial start window
        for i in range(k):
            self.add_to_dq(dq, debug_dq, nums, i)

        self.add_to_result(dq, nums, result)

        debug = lambda x: self.print_debug(x, dq, debug_dq, result)
        debug("Initial ")
        self.print_debug("")

        n, start, end = len(nums), 1, k
        number_of_iteration = n - k
        for i in range(number_of_iteration):

            debug("Start of loop {}, ".format(i+1))
            self.print_debug("start={}, end={}, window={}".format(start, end, nums[start:end+1]))
            self.remove_elements_out_of_window(dq, debug_dq, start)
            debug("Remove elements out of window: ")

            # deque is in descending order
            self.add_to_dq(dq, debug_dq, nums, end)

            x = "push current element nums[{}]={} into ".format(end, nums[end])
            debug(x)

            # Add result = max number of this sliding window k
            # The max number is the first element
            # Add the sliding window maximum to result
            self.add_to_result(dq, nums, result)
            debug("Add result ")
            self.print_debug("")

            start += 1
            end += 1

        print("nums = {} and k = {}, result={}".format(nums, k, result))
        return result
if __name__ == "__main__":
    x = Solution()

    k, l = 3, [1, 3, -1, -3, 5, 3, 6, 7]
    x.maxSlidingWindow(l, k)
    k, l = 3, [1, 3, -1, 10, -3, 5, 3, 6, 7]
    x.maxSlidingWindow(l, k)
