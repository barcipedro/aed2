def levenshtein_distance(s, t):
    # Define a recursive helper function
    def helper(i, j):
        if i == 0 or j == 0:
            # Base case: one string is empty
            return max(i, j)
        elif s[i-1] == t[j-1]:
            # Characters match, no operation needed
            return helper(i-1, j-1)
        else:
            # Characters don't match, choose the minimum of three operations
            deletion = helper(i-1, j) + 1
            insertion = helper(i, j-1) + 1
            substitution = helper(i-1, j-1) + 1
            return min(deletion, insertion, substitution)

    # Call the helper function with the indices of the last character in each string
    return helper(len(s), len(t))
s = "ERRO"
t = "ACERTO"
distance = levenshtein_distance(s, t)
print("Levenshtein distance between", s, "and", t, "is", distance)
