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
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add


@project_add
class GSettingsDesktopSchemas(Tarball, Meson):
    def __init__(self):
        Project.__init__(
            self,
            "gsettings-desktop-schemas",
            version="43.0",
            repository="https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas",
            archive_url="https://download.gnome.org/sources/gsettings-desktop-schemas/{major}/gsettings-desktop-schemas-{version}.tar.xz",
            hash="5d5568282ab38b95759d425401f7476e56f8cbf2629885587439f43bd0b84bbe",
            dependencies=["meson", "ninja", "pkgconf", "glib"],
        )
        if self.opts.enable_gi:
            self.add_dependency("gobject-introspection")
            enable_gi = "true"
        else:
            enable_gi = "false"

        self.add_param(f"-Dintrospection={enable_gi}")

    def build(self):
        Meson.build(self)

        self.install(r".\COPYING share\doc\gsettings-desktop-schemas")
