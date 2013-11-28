import itertools
import numpy

# Brute force: compare every pair.
# O(n^2)
def has_sum1a(array, target):
  for aa_idx, aa in enumerate(array):
    for bb_idx, bb in enumerate(array):
      if aa + bb == target and aa_idx != bb_idx:
        return True
  return False

def has_sum1b(array, target, f=lambda x, y: x + y):
  for combination in itertools.combinations(array, 2):
    if combination[0] + combination[1] == target:
      return True
  return False

# Sort and binary search for complement.
# O(n log n) + (O(n) * O(log n)) = O(n log n)
def has_sum2(array, target):
  array.sort()  # O(n log(n))
  for aa_idx, aa in enumerate(array):
    complement = target - aa

    array[aa_idx] = None  # don't find yourself
    idx = numpy.searchsorted(array, complement)  # O(log n)
    array[aa_idx] = aa  # put self back

    is_found = idx < len(array)
    if is_found:
      return True
  return False

# Build hashmap of values to count of occurences, then iterate over values
# and check for each's complement.
# O(n) + (O(n) * O(1)) = O(n)
def has_sum3(array, target):
  counts = {}
  for aa in array:
    if aa in counts:
      counts[aa] = counts[aa] + 1
    else:
      counts[aa] = 1
  for aa in array:
    complement = target - aa
    if complement in counts:
      # Special case: complement is self but only one occurrence.
      if complement * 2 == target and counts[complement] == 1:
        continue
      return True
  return False

# Iterate over values, maintaining a set of seen values and checking for each
# value's complement as you go.
# O(n) * O(1) = O(n)
def has_sum4(array, target):
  seen = set()
  for aa in array:
    complement = target - aa
    if complement in seen:
      return True
    else:
      seen.add(aa)
  return False

def main():
  for has_sum in [has_sum1a, has_sum1b, has_sum2, has_sum3, has_sum4]:
    print has_sum.__name__,

    array = [3, 0, 1, 2, 3, 10, 3, -1]

    # verify 'normal' case
    assert has_sum(array, 5) == True
    # verify 3 is counted twice (for 6)
    assert has_sum(array, 6) == True
    # verify 10 is not counted twice
    assert has_sum(array, 20) == False
    # verify empty set returns false
    assert has_sum([], 1) == False
    # verify negatives are considered
    assert has_sum(array, 9) == True
    # verify zero is handled
    assert has_sum(array, 0) == True

    print 'OK'

if __name__ == "__main__":
    main()
