def has_q(s):
    if 'q'in s:
        return True
    else:
        return False

if __name__ == "__main__":
  assert has_q("quick") == True
  assert has_q("math") == False
  print("All tests passed!")
