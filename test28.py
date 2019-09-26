Getting Started with Pytest:

#test1.py
def test_passing():
   assert (1,2,3)==(1,2,3)

cmd:pytest test1.py
pytest -v test1.py

#test2.py
def test_failing():
   assert (1,2,3)==(3,2,1)

cmd:pytest test2.py
pytest -v test_two.py #verbose form


Tests:

from collections import namedtuple

Task=namedtuple('Task',['summary','owner','done','id'])
Task.__new__.__defaults__=(None,None,False,None)

def test_defaults():
    t1=Task()
    t2=Task(None,None,False,None)
    assert t1==t2

def test_member_access():
    """Checking member values"""
    t=Task("Buy milk","brian")
    assert t.summary=="Buy milk"
    assert t.owner=="brian"
    assert (t.done,t.id)==(False,None)

def test_asdict():
    t_task=Task('do something','okken',True,21)
    t_dict=t_task._asdict()
    expected={'summary':'do something','owner':'okken','done':True,'id':21}
    assert t_dict==expected

def test_replace():
    t_before=Task('finish book','brian',False)
    t_after=t_before._replace(id=10,done=True)
    t_expected=Task('finish book','brian',True,10)
    assert t_after==t_expected


pytest -v test_namedtuple.py
The filenames should either start with test_  or _test.py

if all the test are in the directory named task

cmd:pytest task

Using Options:



Test discovery
pytest itself find the tests residing in the directory.

Test functions should be named
test_<Something>
Test classes should be named
Test<Something>
Test files should be named
<something>_test.py


What are the outcomes of pytest?
The outcomes of pytest are:
1.Passed
2.Fail
3.skipped
4.xfail
5.xpass
6.Error

How to run only one of the test in pytest?

pytest -v test_file.py::test_summary

This is the way to run only one of the test in test file.

pytest -k "asdict or defaults"
pytest -v -k "asdict or defaults"

import pytest

@pytest.mark.run_these
def test_fun():
   pass

pytest -m run_these

#Stopping the entire test as soon as the test fails.
pytest -x

pytest --maxfail=2

pytest -lf






















