def is_valid_placement(grid, item, row, col):
    item_rows, item_cols = item
    for r in range(item_rows):
        for c in range(item_cols):
            if (
                row + r >= len(grid) or col + c >= len(grid[0])
                or grid[row + r][col + c] == 1
            ):
                return False
    return True

def place_items(grid, items, row=0, col=0):
    if row == len(grid):
        return grid

    if col == len(grid[0]):
        return place_items(grid, items, row + 1, 0)

    if not items:
        return grid

    for item in items:
        if is_valid_placement(grid, item, row, col):
            item_rows, item_cols = item
            for r in range(item_rows):
                for c in range(item_cols):
                    grid[row + r][col + c] = 1

            remaining_items = items[:]
            remaining_items.remove(item)

            result = place_items(grid, remaining_items, row, col + 1)
            if result is not None:
                return result

            for r in range(item_rows):
                for c in range(item_cols):
                    grid[row + r][col + c] = 0

    return None

# Example usage
grid_size = 8
grid = [[0] * grid_size for _ in range(grid_size)]
items = [(6, 2), (4, 4)]
solution = place_items(grid, items)

if solution is None:
    print("No valid solution found.")
else:
    print("Solution:")
    for row in solution:
        print(row)
