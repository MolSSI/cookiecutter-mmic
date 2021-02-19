""" Populate this file if your translator enables force field conversion """

from pydantic import Field, validator
from typing import Dict, Any, Optional
from mmelemental.models.base import ToolkitModel
from mmelemental.models.forcefield import ForceField
from mmelemental.util.decorators import require


__all__ = ["{{cookiecutter.model_name}}FF"]


class {{cookiecutter.model_name}}FF(ToolkitModel):
    """ A model for {{cookiecutter.code_name}} storing forcefield parameters. """

    @property
    @require("{{cookiecutter.code_name}}")
    def dtype(self):
        """ Returns the fundamental forcefield class in {{cookiecutter.code_name}}. """
        import {{cookiecutter.code_name}}

        raise NotImplementedError

    @validator("data")
    def valid_ff(cls, data):
        """ Validates the data object stored in ToolkitModel. """
        raise NotImplementedError

    @classmethod
    @require("{{cookiecutter.code_name}}")
    def from_file(
        cls, filename: str, dtype: str = None, **kwargs: Dict[str, Any]
    ) -> "{{cookiecutter.model_name}}FF":
        """
        Constructs an instance of {{cookiecutter.model_name}}FF object from file(s).

        Parameters
        ----------
        filename : str, optional
            The forcefield filename to read
        dtype: str, optional
            The type of file to interpret. If unset, {{cookiecutter.code_name}} attempts to discover dtype from the file extension.
        **kwargs
            Any additional keywords to pass to the constructor
        Returns
        -------
        ForceField
            MMSchema ForceField object.
        """
        import {{cookiecutter.code_name}}

        raise NotImplementedError

    @classmethod
    def from_schema(
        cls, data: ForceField, version: Optional[str] = None, **kwargs: Dict[str, Any]
    ) -> "{{cookiecutter.model_name}}FF":
        """
        Constructs a {{cookiecutter.model_name}}FF object from an MMSchema ForceField object.
        Parameters
        ----------
        data: ForceField
            Data to construct ForceField from.
        version: str, optional
            Schema version e.g. 1.0.1
        **kwargs
            Additional kwargs to pass to the constructors.
        Returns
        -------
        {{cookiecutter.model_name}}FF
            {{cookiecutter.code_name}} forcefield object.
        """
        raise NotImplementedError

    def to_file(self, filename: str, **kwargs):
        """Writes the forcefield to a file.
        Parameters
        ----------
        filename : str
            The filename to write to
        dtype : Optional[str], optional
        """
        raise NotImplementedError

    def to_schema(self, version: Optional[str] = None, **kwargs) -> ForceField:
        """Converts the {{cookiecutter.model_name}}FF to MMSchema ForceField.
        Parameters
        ----------
        version: str, optional
            Schema version e.g. 1.0.1
        **kwargs
            Additional kwargs to pass to the constructor.
        """
        raise NotImplementedError
