""" Populate this file if your component requires its own models """

from mmelemental.models.base import ProtoModel

__all__ = ["InputModel", "OutputModel"]


class InputModel(ProtoModel):
    """ An input model for {{cookiecutter.repo_name}}. """

    ...


class OutputModel(ProtoModel):
    """ An output model for {{cookiecutter.repo_name}}. """

    ...
