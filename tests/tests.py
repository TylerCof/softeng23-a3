import pytest, os

from pmgr.project import Project, TaskException

@pytest.fixture(scope="function")
def testproj():
    tproj = Project('mytestproj')
    yield tproj
    tproj.delete()

def test_init_file(testproj):
    assert os.path.isfile(testproj.filepath)

def test_add(testproj):
    testproj.add_task('dosomething')
    assert 'dosomething' in testproj.get_tasks()

def test_remove(testproj):
    testproj.add_task('do this')
    testproj.remove_task('do this')
    assert 'do this' not in testproj.get_tasks()

def test_remove_fail(testproj):
    with pytest.raises(TaskException):
        testproj.remove_task('something')

def test_add_fail(testproj):
    testproj.add_task('this thing')
    with pytest.raises(TaskException):
        testproj.add_task('this thing')

def test_add_edge(testproj):
    testproj.add_task('dosomething')
    with pytest.raises(TaskException):
        testproj.add_task('dosomething')
        testproj.remove_task('dosomething')
    assert 'dosomething' not in testproj.get_tasks()

def test_add_whitespace(testproj):
    testproj.add_task('dothis')
    testproj.add_task('dothis\n')
    testproj.remove_task('dothis')    
    assert 'dothis' not in testproj.get_tasks()


