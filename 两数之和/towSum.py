# 整体思路还是较为简单的，遍历数组，通过给定的target减去遍历的值得到一个差，然后再去数组里寻找这个差，
# 找到则成功，没有找到就继续遍历。这里的重点是如何寻找这个差
# 方法2是再次遍历数组
# 方法3是先转换成字典，也可以理解是hashmap，然后再进行上述过程，由于hashmap查找的效率无限接近与O(1),所以耗时短
# 方法4是在第三种方法的基础上不需要再对整个dict进行寻找，再加入一个新的键值对之前，判断是否满足条件，
# 满足之后就直接返回，不满足就继续

# 这样，这个题其实是考察耗时最短的查找方法

##暴力法 超时
class Solution_1:
    def twoSum(self, nums, target):
        answer = []
        for i in range(0,len(nums)):
            flag = False
            for j in range(0,len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    answer.append(i)
                    answer.append(j)
                    flag = True
                    break
            if flag == True:
                break
        return answer
## 第二种暴力方法 使用target减去当前值得到差，然后去数组里查找是否有这个值
## 通过
class Solution_2:
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            if nums.count(target - nums[i]) != 0:
                left = nums.index((target - nums[i]),0,len(nums))
                if left != -1 and left != i:
                    return sorted([i, left])

## 第三种方法，对nums进行转换，方便我们快速获得值对应的下标
class Solution_3:
    def twoSum(self, nums, target):
        num = {}
        ##将list 转成dict
        for i in range(0, len(nums)):
            num[nums[i]] = i

        for i in range(0, len(nums)):
            left = num.get(target - nums[i])
            if left != i and left is not None:
                return [i,left]

## 第四种方法， 进行转换时查找
class Solution_4:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(0, len(nums)):
            if hashmap.get(target - nums[i]) is not None:
                return [i, hashmap.get(target - nums[i])]
            hashmap[nums[i]] = i

if __name__ == "__main__":
    so = Solution_4()
    an = so.twoSum([3,2,3], 6)
    print(an)