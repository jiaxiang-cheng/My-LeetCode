class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 1
        n = len(numbers)
        while index1 < n - 1:
            if numbers[index1] == numbers[index1 - 1]:
                continue
            head = index1 + 1
            tail = n - 1
            while tail - head != 1:
                if numbers[index1] + numbers[int((head + tail) / 2)] > target:
                    tail = int((head + tail) / 2)
                elif numbers[index1] + numbers[int((head + tail) / 2)] < target:
                    head = int((head + tail) / 2)
                else:
                    break

            if numbers[index1] + numbers[head] == target:
                index2 = head
                break
            elif numbers[index1] + numbers[tail] == target:
                index2 = tail
                break
            else:
                index1 += 1
        return [index1 + 1, index2 + 1]
