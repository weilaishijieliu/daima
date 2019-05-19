import unittest
# suite=unittest.TestLoader().discover('../jiaqidebao')
suite=unittest.defaultTestLoader.discover('../jiaqidebao')
unittest.TextTestRunner().run(suite)