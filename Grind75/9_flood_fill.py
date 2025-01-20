from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc] == color:
        return image
    old_color = image[sr][sc]
    return replace_old_color_in_neighbours(image,sr,sc,color, old_color)

def replace_old_color_in_neighbours(image: List[List[int]], sr: int, sc: int, new_color: int, old_color: int=None) -> List[List[int]]:
    if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != old_color:
        return image

    image[sr][sc] = new_color

    replace_old_color_in_neighbours(image, sr - 1, sc, new_color, old_color)
    replace_old_color_in_neighbours(image, sr + 1, sc, new_color, old_color)
    replace_old_color_in_neighbours(image, sr, sc - 1, new_color, old_color)
    replace_old_color_in_neighbours(image, sr, sc + 1, new_color, old_color)

    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 0))
print(floodFill([[0,0,0],[0,0,0]], sr = 1, sc = 0, color = 2))

