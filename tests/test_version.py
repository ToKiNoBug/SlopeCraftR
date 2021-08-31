import unittest

from slopecraftr.utils import Version, PreRelease
from slopecraftr.utils.version import InvalidCall, LockedVersion


class VersionTest(unittest.TestCase):
    def test_version_cases(self):
        self.assertEqual(str(v0 := Version(11, 45, 14, p0 := PreRelease())), '11.45.14')
        self.assertEqual(str(va1 := Version(11, 45, 14, p0.alpha(1))), '11.45.14-alpha.1')
        self.assertEqual(str(vb2 := Version(11, 45, 14, p0.beta(2))), '11.45.14-beta.2')
        self.assertEqual(str(vrc3 := Version(11, 45, 14, p0.rc(3))), '11.45.14-rc.3')

        self.assertEqual(v0.pypi(), '11.45.14')
        self.assertEqual(va1.pypi(), '11.45.14a1')
        self.assertEqual(vb2.pypi(), '11.45.14b2')
        self.assertEqual(vrc3.pypi(), '11.45.14rc3')

        self.assertEqual(str(v0d0 := v0.dev(0)), '11.45.14+dev.0')
        self.assertEqual(str(va1d1 := va1.dev(1)), '11.45.14-alpha.1+dev.1')
        self.assertEqual(str(vb2d2 := vb2.dev(2)), '11.45.14-beta.2+dev.2')
        self.assertEqual(str(vrc3d3 := vrc3.dev(3)), '11.45.14-rc.3+dev.3')

        self.assertEqual(v0d0.pypi(), '11.45.14.dev0')
        self.assertEqual(va1d1.pypi(), '11.45.14a1.dev1')
        self.assertEqual(vb2d2.pypi(), '11.45.14b2.dev2')
        self.assertEqual(vrc3d3.pypi(), '11.45.14rc3.dev3')

    def test_error(self):
        self.assertRaises(InvalidCall, p0 := PreRelease(), 'nothing', 'no', 0)
        self.assertRaises(LockedVersion, p0.alpha(1).alpha, 1)
        self.assertRaises(LockedVersion, p0.beta(2).beta, 2)
        self.assertRaises(LockedVersion, p0.rc(3).rc, 3)


if __name__ == '__main__':
    unittest.main()
