""" Populate this file if your translator enables molecule conversion """

from typing import Dict, Any, Optional
from mmelemental.models.base import ToolkitModel
from mmelemental.models.molecule import Molecule
from mmelemental.util.decorators import require


__all__ = ["{{cookiecutter.model_name}}Mol"]


class {{cookiecutter.model_name}}Mol(ToolkitModel):
    """ A model for {{cookiecutter.code_name}} storing a molecule. """

    @property
    @require("{{cookiecutter.code_name}}")
    def dtype(self):
        """ Returns the fundamental molecule class in {{cookiecutter.code_name}}. """
        import {{cookiecutter.code_name}}

        raise NotImplementedError

    @classmethod
    def isvalid(cls, data):
        """ Validates the data object stored in ToolkitModel. """
        raise NotImplementedError

    @classmethod
    @require("{{cookiecutter.code_name}}")
    def from_file(
        cls, filename: str, top_filename: str = None, dtype: str = None, **kwargs: Dict[str, Any]
    ) -> "{{cookiecutter.model_name}}Mol":
        """
        Constructs an instance of {{cookiecutter.model_name}}Mol object from file(s).

        Parameters
        ----------
        filename : str, optional
            The molecule filename to read
        top_filename: str, optional
            The topology filename to read
        dtype: str, optional
            The type of file to interpret. If unset, {{cookiecutter.code_name}} attempts to discover dtype from the file extension.
        **kwargs
            Any additional keywords to pass to the constructor
        Returns
        -------
        Molecule
            MMSchema Molecule object.
        """
        import {{cookiecutter.code_name}}

        raise NotImplementedError

    @classmethod
    def from_schema(
        cls, data: Molecule, version: Optional[str] = None, **kwargs: Dict[str, Any]
    ) -> "{{cookiecutter.model_name}}Mol":
        """
        Constructs a {{cookiecutter.model_name}}Molecule object from an MMSchema Molecule object.
        Parameters
        ----------
        data: Molecule
            Data to construct Molecule from.
        version: str, optional
            Schema version e.g. 1.0.1
        **kwargs
            Additional kwargs to pass to the constructors.
        Returns
        -------
        {{cookiecutter.model_name}}Mol
            {{cookiecutter.code_name}} molecule object.
        """
        raise NotImplementedError

    def to_file(self, filename: str, **kwargs):
        """Writes the molecule to a file.
        Parameters
        ----------
        filename : str
            The filename to write to
        dtype : Optional[str], optional
        """
        raise NotImplementedError

    def to_schema(self, version: Optional[str] = None, **kwargs) -> Molecule:
        """Converts the {{cookiecutter.model_name}}Mol to MMSchema Molecule.
        Parameters
        ----------
        version: str, optional
            Schema version e.g. 1.0.1
        **kwargs
            Additional kwargs to pass to the constructor.
        """
        raise NotImplementedError
