from setuptools import setup


setup(
    name="nb-tensorspace-playground",
    packages= ['nb_tensorspace_playground'],
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'jupyter-server-proxy',
        'notebook'
    ],
    url="https://github.com/innovationOUtside/nb_tensorspace_server_proxy",
    author="",
    description="tony.hirst@gmail.com",
    entry_points={
        'jupyter_serverproxy_servers': [
            'nb_tensorspace_playground = nb_tensorspace_playground:setup_nb_tensorspace_playground',
        ]
    }
)