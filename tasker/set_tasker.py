# FIXME: No test coverage

from path import path

from .base import cachedprop
from .task import Tasker
from .storage import JSON
from .loader import use

class SetTasker(Tasker):
    """Tasker with convenient methods for handling taskers in subdirectories"""
    def __init__(self, *args, **kw):
        super(SetTasker, self).__init__(*args, **kw)

    def use(self, dirname, *args, **kw):
        """use() a directory with path relative to this one's"""
        return use(self.p / dirname, *args, **kw)

    @cachedprop
    def groups(self):
        """Dictionary of lists of relative paths to subdirectories."""
        return JSON(self.p / 'groups.json').read()

    def group_paths(self, groupname):
        """Get absolute paths of a named group of subdirectories"""
        return [path(t).abspath() for t in self.groups[groupname]]

    def grp(self, groupname, *args, **kw):
        """use() each directory in a named group"""
        return [use(self.p / dirname, *args, **kw) for dirname in self.groups[groupname]]

    @cachedprop
    def aliases(self):
        """Dictionary of aliases to relative paths of subdirectories."""
        return JSON(self.p / 'aliases.json').read()

    def alias_path(self, aliasname):
        """Get absolute path of an aliased subdirectory"""
        return [path(t).abspath() for t in self.aliases[aliasname]]

    def al(self, aliasname, *args, **kw):
        """use() an aliased subdirectory"""
        return use(self.p / self.aliases[aliasname], *args, **kw)

