Jinja Filters Changelog
=======================

2.1.0 - 2021-04-28
------------------

- **feature**: Add ``merge_date_url`` filter. See `Pull Request #12`_.
- **feature**: Add ``datetime_from_period`` filter. `Pull Request #12`_.
- **support**: Rework supporting ``tasks.py`` (for use with ``invoke``). See
  `Pull Request #8`_.
- **support**: Add test suite
- **support**: Support Pelican from version 3.0 on. See `Pull Request #10`_.

.. _Pull Request #8: https://github.com/pelican-plugins/jinja-filters/pull/8
.. _Pull Request #10: https://github.com/pelican-plugins/jinja-filters/pull/10
.. _Pull Request #12: https://github.com/pelican-plugins/jinja-filters/pull/12

2.0.0 - 2020-08-21
------------------

- **feature**: Initial release as namespace plugin. With Pelican 4.5,
  namespace plugins no longer need to be explicitly declared to be available to
  Pelican.
- **support**: Minimum version of Pelican is now 4.5
- **support**: Move plugin to the `Pelican Plugins`_ organization on GitHub. The
  code for the project is now at `pelican-plugins/jinja-filters`_
- **support**: First release to PyPI under `pelican-jinja-filters`_
- see `Pull Request #4`_.

1.1.0 - 2021-04-29
------------------

- **support**: Add warning message to point users to new plugin location at
  ``pelican-jinja-filters`` on PyPI. See `Issue #7`_.

.. _Issue #7: https://github.com/pelican-plugins/jinja-filters/issues/7

1.0.4 - 2017-04-17
------------------

- **bug**: Upgrade release machinery
- **bug**: Add Pelican trove classifier

1.0.1 - 2017-03-08
------------------

- **bug**: Provide universal wheels

1.0.0 - 2016-11-06
------------------

- **feature**: Copy existing code from personal website
- **support**: Add release machinery
- **support**: First release to PyPI under `minchin.pelican.jinja_filters`_
- **support**: Add 'setup.py', 'CHANGELOG.rst', 'README.rst'


.. _minchin.pelican.jinja_filters: https://pypi.org/project/minchin.pelican.jinja_filters/
.. _pelican-plugins/jinja-filters: https://github.com/pelican-plugins/jinja-filters
.. _pelican-jinja-filters: https://pypi.org/project/pelican-jinja-filters/
.. _Pelican Plugins: https://github.com/pelican-plugins
.. _Pull Request #4: https://github.com/pelican-plugins/jinja-filters/pull/4
