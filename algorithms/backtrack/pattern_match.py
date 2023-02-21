"""
Given a pattern and a string str,
find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
Notes:
You may assume both pattern and str contains only lowercase letters.
"""


def pattern_match(pattern, string, flags):
    """
    :type pattern: str
    :type string: str
    :rtype: bool
    """
    def backtrack(pattern, string, dic, flags):
        if len(pattern) == 0 and len(string) > 0:
            flags[0] = 1
            return False
        else:
            flags[1] = 1

        if len(pattern) == len(string) == 0:
            flags[2] = 1
            return True
        else:
            flags[3] = 1

        for end in range(1, len(string)-len(pattern)+2):
            if pattern[0] not in dic and string[:end] not in dic.values():
                flags[4] = 1
                dic[pattern[0]] = string[:end]
                if backtrack(pattern[1:], string[end:], dic, flags):
                    flags[5] = 1
                    return True
                else:
                    flags[6] = 1
                del dic[pattern[0]]
            elif pattern[0] in dic and dic[pattern[0]] == string[:end]:
                flags[7] = 1
                if backtrack(pattern[1:], string[end:], dic, flags):
                    flags[8] = 1
                    return True
                else:
                    flags[9] = 1
            else:
                flags[10] = 1
        flags[11] = 1
        return False
    return_value = backtrack(pattern, string, {}, flags)
    flags[12] = 1
    return return_value
