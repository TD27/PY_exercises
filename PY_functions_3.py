def shut_down(s):
  if s == "yes":
    s="Shutting down"
  elif s == "no":
  	s="Shutdown aborted"
  else:
    s="Sorry"
  return s


print (shut_down ("no"))

