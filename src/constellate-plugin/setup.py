from setuptools import setup

setup(
    name='constellate-plugin',
    version='0.0.1',
    author='Constellate team',
    author_email='tdm@ithaka.org',
    packages=[
        'constellate_plugin',
    ],
    url='https://github.com/ithaka/tdm-notebooks',
    license='MIT',
    package_data={
        'constellate_plugin': ['constellate_plugin/static/main.js'],
    },
    description='Constellate utilities',
    install_requires=[
        'notebook',
    ],
    data_files=[(
            'share/jupyter/nbextensions/constellate-plugin', [
                'constellate_plugin/static/main.js'
        ]),
        ('etc/jupyter/nbconfig/notebook.d' , ['constellate_plugin.json'])
    ],
    zip_safe=False,
    include_package_data=True,
)