# this contains imports plugins that configure py.test for astropy tests.
# by importing them here in conftest.py they are discoverable by py.test
# no matter how it is invoked within the source tree.

try:
    from astropy.tests.plugins.display import (pytest_report_header,
                                               PYTEST_HEADER_MODULES,
                                               TESTED_VERSIONS)
except ImportError:
    # When using astropy 2.0
    from astropy.tests.pytest_plugins import (pytest_report_header,
                                              PYTEST_HEADER_MODULES,
                                              TESTED_VERSIONS)

try:
    # This is the way to get plugins in astropy 2.x
    from astropy.tests.pytest_plugins import *
except ImportError:
    # Otherwise they are installed as separate packages that pytest
    # automagically finds.
    pass


## Uncomment the following line to treat all DeprecationWarnings as
## exceptions
# enable_deprecations_as_exceptions()

## Uncomment and customize the following lines to add/remove entries from
## the list of packages for which version numbers are displayed when running
## the tests. Making it pass for KeyError is essential in some cases when
## the package uses other astropy affiliated packages.
# try:
#     PYTEST_HEADER_MODULES['Astropy'] = 'astropy'
#     PYTEST_HEADER_MODULES['scikit-image'] = 'skimage'
#     del PYTEST_HEADER_MODULES['h5py']
# except (NameError, KeyError):  # NameError is needed to support Astropy < 1.0
#     pass

## Uncomment the following lines to display the version number of the
## package rather than the version number of Astropy in the top line when
## running the tests.
# import os
#
## This is to figure out the affiliated package version, rather than
## using Astropy's
# try:
#     from .version import version
# except ImportError:
#     version = 'dev'
#
# try:
#     packagename = os.path.basename(os.path.dirname(__file__))
#     TESTED_VERSIONS[packagename] = version
# except NameError:   # Needed to support Astropy <= 1.0.0
#     pass
