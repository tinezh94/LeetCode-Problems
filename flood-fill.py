"""

733. Flood Fill

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

modified image = [
    [2, 2, 2],
    [2, 2, 0],
    [2, 0, 1]
]

"""

def floodFill(image, sr, sc, color):
    row, col = len(image), len(image[0])
    startColor = image[sr][sc]
    
    if startColor == color: return image

    def dfs(r, c):
        if image[r][c] == startColor:
            image[r][c] = color
            if r >= 1: dfs(r - 1, c)
            if r + 1 < row: dfs(r + 1, c)
            if c >= 1: dfs(r, c - 1)
            if c + 1 < col: dfs(r, c + 1)
    dfs(sr, sc)
    return image



print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))