"""
Return config on servers to start for nb_handwritten_digit
See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import pkg_resources

def setup_nb_tensorspace_playground():
    fpath = pkg_resources.resource_filename('nb_tensorspace_playground', 'static/')
    return {
        'command': ["python", "-m", "http.server", "--directory", fpath, "{port}"],
        'environment': {},
        'launcher_entry': {
            'title': 'nb_tensorspace_playground',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'nb_tensorspace_playground.svg')
        }
    }