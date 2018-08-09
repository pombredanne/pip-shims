# -*- coding=utf-8 -*-
from __future__ import absolute_import

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "_strip_extras",
    "cmdoptions",
    "Command",
    "ConfigOptionParser",
    "DistributionNotFound",
    "FAVORITE_HASH",
    "FormatControl",
    "get_installed_distributions",
    "index_group",
    "InstallRequirement",
    "is_archive_file",
    "is_file_url",
    "is_installable_dir",
    "Link",
    "make_abstract_dist",
    "make_option_group",
    "PackageFinder",
    "parse_requirements",
    "parse_version",
    "path_to_url",
    "pip_version",
    "PipError",
    "RequirementPreparer",
    "RequirementSet",
    "RequirementTracker",
    "Resolver",
    "SafeFileCache",
    "url_to_path",
    "USER_CACHE_DIR",
    "VcsSupport",
    "Wheel",
    "WheelCache",
]

from .shims import shimmed_imports
import sys
sys.modules["{0}.shims".format(__name__)] = shimmed_imports
shims = shimmed_imports
