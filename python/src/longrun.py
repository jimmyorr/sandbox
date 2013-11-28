import unittest

def longest_run(iterable):
  """
  Takes an iterable and returns the item in that iterable with the longest
  consecutive run. If iterable is empty, return None.
  
  Example: "aabbbaa", returns 'b' (longest run of 3).
  """
  previous = None
  longest_run = None
  current_count = 0
  max_count = 0

  for current in iterable:
    if current == previous:
      current_count += 1
    else:
      current_count = 1

    # tie goes to the first occurrence
    if current_count > max_count:
      max_count = current_count
      longest_run = current

    previous = current

  return longest_run


class LongestRunTestCase(unittest.TestCase):

  def test_front(self):
    self.assertEquals(longest_run('bbbaa'), 'b')

  def test_middle(self):
    self.assertEquals(longest_run('aabbbaa'), 'b')

  def test_end(self):
    self.assertEquals(longest_run('aabbb'), 'b')

  def test_single(self):
    self.assertEquals(longest_run('a'), 'a')

  def test_unicode_input(self):
    s = 'aa' + ''.join([unichr(num) for num in xrange(50000)])
    self.assertEquals(longest_run(s), 'a')

  def test_tie1(self):
    self.assertEquals(longest_run('ab'), 'a')

  def test_tie2(self):
    self.assertEquals(longest_run('aabb'), 'a')

  def test_empty_string(self):
    self.assertEquals(longest_run(''), None)

  def test_list(self):
    self.assertEquals(longest_run([1, 2, 2, 3]), 2)

if __name__ == '__main__':
  unittest.main()
