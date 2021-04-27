"""
``Jinja Filters`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``Jinja Filters`` provides a selection of functions (called *filters*) for
templates to use when building your website. They are packaged for Pelican, but
may prove useful for other projects that make use of Jinja.
"""

from __future__ import absolute_import

import logging

from pelican import signals
from pelican.plugins.jinja_filters import jinja_filters

# METADATA

__title__ = "minchin.pelican.jinja_filters"
__description__ = "Jinja Filters for Pelican."
__url__ = "https://github.com/MinchinWeb/minchin.pelican.jinja_filters"
__author__ = "William Minchin"
__email__ = "w_minchin@hotmail.com"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2016-21 William Minchin"

"""
This project uses the Semantic Versioning scheme in conjunction with PEP 0440:

    <http://semver.org/>
    <https://www.python.org/dev/peps/pep-0440>

Major versions introduce significant changes to the API, and backwards
compatibility is not guaranteed. Minor versions are for new features and other
backwards-compatible changes to the API. Patch versions are for bug fixes and
internal code changes that do not affect the API.

Version 0.x should be considered a development version with an unstable API,
and backwards compatibility is not guaranteed for minor versions.
"""
__version__ = "1.1.0-dev.3"


# Package Implementation

logger = logging.getLogger(__name__)

logger.warn(
    "This package name (`minchin.pelican.jinja_filters`) has been "
    "deprecated. Upgrade to `pelican-jinja-filters` on PyPI."
)


def add_all_filters(pelican):
    """Add (register) all filters to Pelican."""
    pelican.env.filters.update({"datetime": jinja_filters.datetime})
    pelican.env.filters.update({"article_date": jinja_filters.article_date})
    pelican.env.filters.update({"breaking_spaces": jinja_filters.breaking_spaces})
    pelican.env.filters.update({"titlecase": jinja_filters.titlecase})


def register():
    """Plugin registration."""
    signals.generator_init.connect(add_all_filters)