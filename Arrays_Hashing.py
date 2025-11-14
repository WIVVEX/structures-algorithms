
def containsDuplicate217(nums):
    seq = {}

    for i in nums:
        if i in seq and seq[i] == 1:
            return True
        seq[i] = 1
    return False

def isAnagram242(s, t):
    dict1, dict2 = {}, {}
    for i in s:
        dict1[i] = dict1.get(i, 0) + 1
    for i in t:
        dict2[i] = dict2.get(i, 0) + 1
    
    return dict1 ==  dict2  

def twoSum1(arr, target):
    seq = {}
    for index, value in enumerate(arr):            
        if target - value in seq:
            return [index, seq[target - value]]
        seq[value] = index

def groupAnagrams49(strs):
    sorted_words = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in sorted_words:
            sorted_words[sorted_word] = []
        sorted_words[sorted_word].append(word)
    
    return list(sorted_words.values())

def topKFrequent347(nums, k):
    count = {}

    freq = [[] for _ in range(len(nums) + 1)]

    for i in nums:
        count[i] = count.get(i, 0) + 1
    
    for value, index in count.items():
        freq[index].append(value)
    
    res = []

    for i in range(len(freq) -1, -1, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res 


def encode(strs: list[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(s: str) -> list[str]:
    res = []
    i = 0

    while i < len(s):
        j = i 
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return res


from collections import defaultdict

def isValidSudoku36(board):
    rows = defaultdict(set)
    columns = defaultdict(set)
    boxes = defaultdict(set)
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue


            if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in boxes[i // 3, j // 3]:
                return False
            

            rows[i].add(board[i][j])
            columns[j].add(board[i][j])
            boxes[(i // 3, j // 3)].add(board[i][j])
    

    return True




            

         








