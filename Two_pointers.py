def trap42(height):
    l = 0
    r = len(height) - 1
    l_max = 0
    r_max = 0
    res = 0


    while r > l:
        if height[r] > height[l]:
            if height[l] > l_max:
                l_max = height[l]
            else:
                res += l_max - height
            l += 1
        else:
            if height[r] >= r_max:
                r_max = height[r]
            else:
                res += r_max - height[r]
            r -= 1
    return res


def removeDuplicates26(nums):
    if len(nums) < 1:
        return 0
    k = 1
    i = 0
    for j in range(1, len(nums)):
        if nums[i] == nums[j]:
            nums[j] = "_"
        else:
            k += 1
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    return k

def removeElement27(nums, val):
    i = 0
    for j in nums:
        if j != val:
            nums[i] = j
            i += 1
        else:
            continue
    return [nums, i]


def strStr28(haystack, needle):
    i = 0
    j = 0
    n = len(haystack)
    m = len(needle)

    while n > i:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
        
        if j == m:
            return i - j
    return -1



def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    return nums1





