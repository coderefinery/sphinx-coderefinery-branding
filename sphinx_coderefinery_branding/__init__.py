"""Local branding module for CodeRefinery Sphinx projects
"""
from os import environ
from os.path import abspath, join, dirname

from ._version import __version__

def setup(app):

    def config_hook(app, config):
        """Hook to set the HTML favicon"""
        config.html_favicon = abspath(join(dirname(__file__), '_static', 'coderefinery.ico'))

    # Only add the hook if we think we are being built in an CodeRefinery
    # location:
    if (environ.get('GITHUB_REPOSITORY', '').lower().startswith('coderefinery')
          or 'CODEREFINERY' in environ):
        app.connect('config-inited', config_hook)
        app.setup_extension('sphinx_plausible')
        app.config.plausible_domain = 'coderefinery.github.io'

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
