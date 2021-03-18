"""
Components in {{cookiecutter.repo_name}}.
"""

from typing import List, Tuple, Optional
from mmic.components.blueprints.generic_component import GenericComponent
from ..models import *

__all__ = ["Component"]


class Component(GenericComponent):
    """ A sample component that defines the 3 required methods. """

    @classmethod
    def input(cls):
        return InputModel

    @classmethod
    def output(cls):
        return OutputModel

    def execute(
        self,
        inputs: InputModel,
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, OutputModel]:

        # Convert input dictionary to model
        if isinstance(inputs, dict):
            inputs = self.input()(**inputs)

        # Populate kwargs from inputs
        return True, OutputModel(**kwargs)
