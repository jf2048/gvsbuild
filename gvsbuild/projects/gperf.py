#  Copyright (C) 2016 - Yevgen Muntyan
#  Copyright (C) 2016 - Ignacio Casal Quinteiro
#  Copyright (C) 2016 - Arnavion
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from gvsbuild.utils.base_builders import Meson
from gvsbuild.utils.base_expanders import GitRepo
from gvsbuild.utils.base_project import Project, project_add


@project_add
class Gperf(GitRepo, Meson):
    def __init__(self):
        Project.__init__(
            self,
            "gperf",
            repo_url="https://gitlab.freedesktop.org/tpm/gperf.git",
            fetch_submodules=False,
            tag="705c85fee6254ac5eb0df7de6a8ca6f567f34472",
            dependencies=["ninja"],
        )

    def build(self):
        Meson.build(self)
        self.install(r"COPYING share\doc\gperf")
