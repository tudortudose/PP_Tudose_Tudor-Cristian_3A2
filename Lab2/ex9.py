def getBadLocations(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    bad_locations = []
    for c in range(cols):
        tallest = 0
        for r in range(rows):
            if matrix[r][c] <= tallest:
                bad_locations += [(r, c)]
            else:
                tallest = matrix[r][c]
    return bad_locations
