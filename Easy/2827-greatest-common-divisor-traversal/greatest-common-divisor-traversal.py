class Solution:
    def dfs(self, index, visited_index, visited_prime):
        if visited_index[index]:
            return
        visited_index[index] = True

        for prime in self.index_to_prime[index]:
            if not visited_prime[prime]:
                visited_prime[prime] = True
                for index1 in self.prime_to_index[prime]:
                    if not visited_index[index1]:
                        self.dfs(index1, visited_index, visited_prime)

    def canTraverseAllPairs(self, nums):
        prime_to_index = defaultdict(list)
        index_to_prime = defaultdict(list)

        for i, num in enumerate(nums):
            temp = num
            for j in range(2, int(temp**0.5) + 1):
                if temp % j == 0:
                    prime_to_index[j].append(i)
                    index_to_prime[i].append(j)
                    while temp % j == 0:
                        temp //= j
            if temp > 1:
                prime_to_index[temp].append(i)
                index_to_prime[i].append(temp)

        visited_index = [False] * len(nums)
        visited_prime = defaultdict(bool)

        self.prime_to_index = prime_to_index
        self.index_to_prime = index_to_prime

        self.dfs(0, visited_index, visited_prime)

        return all(visited_index)