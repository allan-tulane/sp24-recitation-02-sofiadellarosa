from main import *
import math


def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650

  # added 3 additional tests below - Sofia
  assert simple_work_calc(10, 4, 2) == 126
  assert simple_work_calc(20, 2, 2) == 92
  assert simple_work_calc(30, 3, 2) == 300
  """ done. """


def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n * n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300

  # added 3 additional tests below - sofia
  assert work_calc(10, 2, 2, lambda n: n + 2) == 50
  assert work_calc(10, 2, 2, lambda n: n % 2) == 10
  assert work_calc(30, 1, 2, lambda n: n * 2) == 111
  #assert work_calc(1000, 1, 2, lambda n: n) == 10


def test_compare_work():
  # curry work_calc to create multiple work -> function inside function
  # functions that can be passed to compare_work

  # create work_fn1
  def work_fn1(n):
    return work_calc(n, 2, 4, lambda n: 1)

  # create work_fn2
  def work_fn2(n):
    return work_calc(n, 2, 4, lambda n: n * n)

  pass
  res = compare_work(work_fn1, work_fn2)
  #print(res)


def test_compare_span():
  # create work_fn1
  def span_fn1(n):
    return span_calc(n, 2, 4, lambda n: 1)

  # create work_fn2
  def span_fn2(n):
    return span_calc(n, 2, 4, lambda n: n * n)

  pass
  res = compare_span(span_fn1, span_fn2)
  pass
