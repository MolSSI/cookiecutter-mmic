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


# Main component used by MMIC class I components
_mainComponent = components.Component
