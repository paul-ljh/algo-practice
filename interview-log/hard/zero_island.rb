require 'pp'

=begin
Imagine we have an image. We'll represent this image as a simple 2D array where every pixel is a 1 or a 0.

The image you get is known to have potentially many distinct rectangles of 0s on a background of 1s. Write a function that takes in the image and returns the coordinates of all the 0 rectangles -- top-left and bottom-right; or top-left, width and height.

image1 = [
  [0, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [1, 1, 1, 1, 1, 1, 0],
]

findRectangles(image1) =>
  // (using top-left-row-column and bottom-right):
  [
    [[0,0],[0,0]],
    [[2,0],[2,0]],
    [[2,3],[3,5]],
    [[3,1],[5,1]],
    [[5,3],[6,4]],
    [[7,6],[7,6]],
  ]
  // (using top-left-x-y and width/height):
  [
    [[0,0],[1,1]],
    [[0,2],[1,1]],
    [[3,2],[3,2]],
    [[1,3],[1,3]],
    [[3,5],[2,2]],
    [[6,7],[1,1]],
  ]

image2 = [
  [0],
]

findRectangles(image2) =>
  // (using top-left-row-column and bottom-right):
  [
    [[0,0],[0,0]],
  ]

  // (using top-left-x-y and width/height):
  [
    [[0,0],[1,1]],
  ]

image3 = [
  [1],
]

findRectangles(image3) => []

image4 = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1],
]

findRectangles(image4) =>
  // (using top-left-row-column and bottom-right or top-left-x-y and width/height):
  [
    [[1,1],[3,3]],
  ]
=end

def find_rectangles(image)
  row, col = image.length, image[0].length
  top_left_dict = Hash.new
  result = []
  
  0.upto(row-1) do |r|
    tlr, tlc = nil, nil
    0.upto(col-1) do |c|
      if image[r][c] == 0
        # top left
        if (r.zero? || image[r-1][c] == 1) && (c.zero? || image[r][c-1] == 1)
          tlr, tlc = r, c
        end

        # top right
        if (r.zero? || image[r-1][c] == 1) && (c == col-1 || image[r][c+1] == 1)
          top_left_dict[c] = [tlr, tlc]
        end
        
        # bottom right
        if (r == row-1 || image[r+1][c] == 1) && (c == col-1 || image[r][c+1] == 1)
          result.push([top_left_dict[c], [r, c]])
          top_left_dict.delete(c)
        end
      end
    end
  end
  pp result
  return result
end

def test
  image1 = [
    [0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0],
  ]
  
  image2 = [
    [0],
  ]
  
  image3 = [
    [1],
  ]
  
  image4 = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
  ]

  find_rectangles(image1)
  find_rectangles(image2)
  find_rectangles(image3)
  find_rectangles(image4)
end

      
      
        
      
    
  
