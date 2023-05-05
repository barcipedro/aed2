def levenshtein_distance(s, t):
    # Initialize a matrix of zeros with dimensions (len(s)+1) x (len(t)+1)
    matrix = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    # Fill in the first row and column of the matrix
    for i in range(len(s) + 1):
        matrix[i][0] = i
    for j in range(len(t) + 1):
        matrix[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i-1] == t[j-1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            matrix[i][j] = min(matrix[i-1][j] + 1,  # deletion
                               matrix[i][j-1] + 1,  # insertion
                               matrix[i-1][j-1] + substitution_cost)  # substitution

    # The final answer is the bottom right element of the matrix
    return matrix[-1][-1]
    
s = "ERRO"
t = "ACERTO"
distance = levenshtein_distance(s, t)
print("Levenshtein distance between", s, "and", t, "is", distance)
