import logging

logging.basicConfig(level=logging.DEBUG)


def run_tests():
    import unittest

    testsuite = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=3).run(testsuite)


if __name__ == "__main__":
    run_tests()
