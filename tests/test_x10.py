from .context import x10_controller
import unittest
import tempfile
import os

class X10TestSuite(unittest.TestCase):

    def test_grab(self):
        '''
        a lockfile must not exist before grabbing
        '''
        tr = x10_controller.X10Controller()
        ntf = tempfile.NamedTemporaryFile(delete=False)
        try:
            tr._grab_lockfile(ntf.name)
            assert False
        except:
            assert True

    def test_release(self):
        '''
        a lockfile must not exist after being released
        '''
        tr = x10_controller.X10Controller()
        ntf = tempfile.NamedTemporaryFile(delete=False)
        tr._release_lockfile(ntf.name)
        assert not os.path.isfile(ntf.name)

    def test_grab_and_release(self):
        '''
        grabbing and releasing the lockfile works appropriately
        '''
        tr = x10_controller.X10Controller()
        
        ntf = tempfile.NamedTemporaryFile(delete=False)
        os.remove(ntf.name)
        assert not os.path.isfile(ntf.name)
        tr._grab_lockfile(ntf.name)
        assert os.path.isfile(ntf.name)
        tr._release_lockfile(ntf.name)
        assert not os.path.isfile(ntf.name)

    def test_logging(self):
        
        tr = x10_controller.X10Controller()
        ntf = tempfile.NamedTemporaryFile(delete=False)
        app_name = x10_controller.get_logger_name()
        log = tr._setup_logger(ntf.name)
        log_msg = "testing logger"
        log(log_msg)
        f = open(ntf.name)
        file_contents = f.read()
        assert log_msg in file_contents
        assert app_name in file_contents
        
