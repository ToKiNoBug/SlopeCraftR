from semver import VersionInfo


class InvalidCall(RuntimeError):
    pass


class LockedVersion(RuntimeError):
    pass


class PreRelease:
    def __init__(self):
        self._locked = False
        self._level = None
        self._level_abbr = None
        self._pre_ver = None

    def __call__(self, level: str, level_abbr: str, pre_ver: int, _valid: bool = False) -> 'PreRelease':
        if not _valid:
            raise InvalidCall(f'Invalid way to call {self}')
        if self._locked:
            raise LockedVersion(f'{self} is locked')
        new = self.__class__()
        new._locked = True
        new._level = level
        new._level_abbr = level_abbr
        new._pre_ver = pre_ver
        return new

    def alpha(self, ver) -> 'PreRelease':
        return self('alpha', 'a', ver, _valid=True)

    def beta(self, ver) -> 'PreRelease':
        return self('beta', 'b', ver, _valid=True)

    def rc(self, ver) -> 'PreRelease':
        return self('rc', 'rc', ver, _valid=True)

    def __str__(self):
        return f'{self._level}.{self._pre_ver}' if self._locked else ''

    def to_pypi_format(self) -> str:
        return f'{self._level_abbr}{self._pre_ver}' if self._locked else ''


class Version(VersionInfo):
    def __init__(self, major: int, minor: int = 0, patch: int = 0, prerelease: PreRelease = PreRelease()):
        self._pypi_pre = prerelease.to_pypi_format()
        self._pypi_build = ''
        super().__init__(
            major=major,
            minor=minor,
            patch=patch,
            prerelease=str(prerelease)
        )

    def dev(self, dev_ver: int) -> 'Version':
        new = self.__class__(self.major, self.minor, self.patch)
        new._prerelease = self._prerelease
        new._pypi_pre = self._pypi_pre
        new._build = f'dev.{dev_ver}'
        new._pypi_build = f'.dev{dev_ver}'
        return new

    def pypi(self) -> str:
        major, minor, patch = self.major, self.minor, self.patch
        pre = self._pypi_pre
        dev = self._pypi_build
        return f'{major}.{minor}.{patch}{pre}{dev}'
