import time
def average_time_taken(method, target=None):
  sumTimeTaken = 0
  TEST_CYCLES =10
  for _ in range(TEST_CYCLES):
    start = time.process_time()
    if target == None:
      method()
    else:
      method(target)
    sumTimeTaken += time.process_time() - start
  if target == None:
    print("Average time taken is {}s. Result: {}".format(sumTimeTaken / float(TEST_CYCLES), method()))
  else:
    print("Average time taken for {} is {}s. Result: {}".format(target, sumTimeTaken / float(TEST_CYCLES), method(target)))

def average_time_taken_no_result(method, target=None):
  sumTimeTaken = 0
  TEST_CYCLES =10
  for _ in range(TEST_CYCLES):
    start = time.process_time()
    method(target)
    sumTimeTaken += time.process_time() - start
  print("Average time taken for {} is {}s".format(target, sumTimeTaken / float(TEST_CYCLES)))

def average_time_taken_multiple_args(method, *argv):
  sumTimeTaken = 0
  TEST_CYCLES =10
  for _ in range(TEST_CYCLES):
    start = time.process_time()
    method(*argv)
    sumTimeTaken += time.process_time() - start
  print("Average time taken is {}s. Result: {}".format(sumTimeTaken / float(TEST_CYCLES), method(*argv)))
  