def rotate_left3(nums):
  front = nums[0]
  new = nums[1:]
  new.append(front)
  return new