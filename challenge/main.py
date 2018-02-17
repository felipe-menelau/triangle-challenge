def solve(triangle = []):
    if not triangle:
        raise RuntimeError('Should have a triangle')

    bottom_up_navigation_range = reversed(range(len(triangle) - 1))

    for i in bottom_up_navigation_range:
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return str(triangle[0][0])



if __name__ == "__main__":
    triangle = [
            [6],
            [3,5],
            [9,7,1],
            [4,6,8,4]
    ]
    print(solve(triangle))
