#!/usr/bin/env python3

# Given 2 words (start and end), and a wordlist:
    # find the length of the shortest transformation sequence from start to end, such that:
    # Only one letter can be changed at a time
    # Each intermediate word must exist in the dictionary
    # For example:
        # start = 'hit'
        # end = 'cog'
        # wordlist = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
        # return its length = 5 and return 0 if there is no such transformation sequence | all words have the same length and contain only lowercase alnum chars

class Enigma:
    # @param start, a string
    # @param end, a string
    # @param wordlist, a set of strings
    # @return a int

    def findlengthofladder(self, start, end, wordlist):
        distance, cur, visited = 0, [start], set([start])
        wordlist.add(end)
        alphabets = 'abcdefghijklmnopqrstuvwxyz'

        while cur:
            next = []
            for word in cur:
                if word == end:
                    return distance + 1
                for i in range(len(word)):
                    for j in alphabets:
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in dict:
                            next.append(candidate)
                            visited.add(candidate)
            distance += 1
            cur = next
        return 0

        if __name__ == "__main__":
            print(Solution().ladderlength("hit", "cog", set(["hot", "dot", "dog", "lot", "log"])))
