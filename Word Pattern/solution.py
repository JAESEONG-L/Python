class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s += " "

        i=0 # Index going over the {pattern}.
        curr_idx=0  # Index going over the {s}.

        injection=dict()

        while i<len(pattern) and curr_idx<len(s):
            next_idx=s.find(" ", curr_idx)+1

            if pattern[i] in injection:
                if injection[pattern[i]]!=s[curr_idx:next_idx-1]:
                    return False

                pass
            else:
                if s[curr_idx:next_idx-1] in injection.values():
                    return False

                injection[pattern[i]]=s[curr_idx:next_idx-1]

            i += 1
            curr_idx= next_idx

        return bool((i==len(pattern)) & (curr_idx==len(s)))
