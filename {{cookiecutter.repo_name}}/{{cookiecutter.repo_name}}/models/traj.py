""" Populate this file if your translator enables trajectory conversion """

from pydantic import Field, validator
from typing import Dict, Any, Optional
from mmelemental.models.base import ToolkitModel
from mmelemental.models.molecule import Molecule
from mmelemental.models.collect import Trajectory
from mmelemental.util.decorators import require


__all__ = ["{{cookiecutter.model_name}}Traj"]


class {{cookiecutter.model_name}}Traj(ToolkitModel):
    """ A model for {{cookiecutter.code_name}} storing a trajectory. """

    @property
    @require("{{cookiecutter.code_name}}")
    def dtype(self):
        """ Returns the fundamental molecule class in {{cookiecutter.code_name}}. """
        import {{cookiecutter.code_name}}

        raise NotImplementedError

    @validator("data")
    def valid_traj(cls, data):
        """ Validates the data object stored in ToolkitModel. """
        raise NotImplementedError

    @classmethod
    @require("{{cookiecutter.code_name}}")
    def from_file(
        cls, filename: str, top_filename: str = None, dtype: str = None, **kwargs: Dict[str, Any]
    ) -> "{{cookiecutter.model_name}}Traj":
        """
        Constructs an instance of {{cookiecutter.model_name}}Traj object from file(s).

        Parameters
        ----------
        filename : str, optional
            The trajectory filename to read
        top_filename: str, optional
            The topology filename to read
        dtype: str, optional
            The type of file to interpret. If unset, {{cookiecutter.code_name}} attempts to discover dtype from the file extension.
        **kwargs
            Any additional keywords to pass to the constructor
        Returns
        -------
        Trajectory
            MMSchema Trajectory object.
        """
        import {{cookiecutter.code_name}}

        raise NotImplementedError

    @classmethod
    def from_schema(
        cls, data: Trajectory, version: Optional[str] = None, **kwargs: Dict[str, Any]
    ) -> "{{cookiecutter.model_name}}Traj":
        """
        Constructs a {{cookiecutter.model_name}}Traj object from an MMSchema Trajectory object.
        Parameters
        ----------
        data: Trajectory
            Data to construct Molecule from.
        version: str, optional
            Schema version e.g. 1.0.1
        **kwargs
            Additional kwargs to pass to the constructors.
        Returns
        -------
        {{cookiecutter.model_name}}Traj
            {{cookiecutter.code_name}} trajectory object.
        """
        raise NotImplementedError

    def to_file(self, filename: str, **kwargs):
        """Writes the trajectory to a file.
        Parameters
        ----------
        filename : str
            The filename to write to
        dtype : Optional[str], optional
        """
        raise NotImplementedError

    def to_schema(self, version: Optional[str] = None, **kwargs) -> Trajectory:
        """Converts the {{cookiecutter.model_name}}Traj to MMSchema Trajectory.
        Parameters
        ----------
        version: str, optional
            Schema version e.g. 1.0.1
        **kwargs
            Additional kwargs to pass to the constructor.
        """
        raise NotImplementedError
