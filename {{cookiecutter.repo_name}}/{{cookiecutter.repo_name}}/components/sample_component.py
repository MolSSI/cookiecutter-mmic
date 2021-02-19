"""
Components in {{cookiecutter.repo_name}}.
"""

from typing import List, Tuple, Optional

# Import the generic i.e. starting component from MMIC
from mmic.components.blueprints.generic_component import GenericComponent

# Import common functions from MMElemental
from mmelemental.util.decorators import require
from mmelemental.util.units import convert

# Import MMSchema models from MMElemental
from mmelemental.models.molecule import Molecule
from mmelemental.models.forcefield import ForceField

__all__ = ["SampleComponent"]


class SampleComponent(GenericComponent):
    """ A sample component that reads in a Molecule and returns a ForceField object. """

    @classmethod
    def input(cls):
        return Molecule

    @classmethod
    def output(cls):
        return ForceField

    @require("cookiecutter.code_name")
    def execute(
        self,
        inputs: Molecule,
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, ForceField]:
        import cookiecutter.code_name

        return True, ForceField(**kwargs)
