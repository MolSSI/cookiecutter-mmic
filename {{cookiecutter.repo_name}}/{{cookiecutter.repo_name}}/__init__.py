"""
{{cookiecutter.project_name}}
{{cookiecutter.description}}
"""

# Add imports here
from .{{cookiecutter.first_module_name}} import *
from . import models, components

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions


# The molecule file extensions supported by
# the reader and writers in {{cookiercutter.repo_name}}
molread_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

molwrite_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

# The trajectory file extensions supported by
# the reader and writers in {{cookiercutter.repo_name}}
trajread_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

trajwrite_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

# The force field file extensions supported by
# the readers and writers in {{cookiercutter.repo_name}}
ffread_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

ffwrite_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

# Name to model map for MMElemental
_classes_map = {
    "Molecule": models.{{cookiecutter.model_name}}Mol,
    "Trajectory": models.{{cookiecutter.model_name}}Traj,
    "ForceField": models.{{cookiecutter.model_name}}FF,
}
