from distutils.core import setup
import os

if os.path.exists("MANIFEST"):
    os.unlink("MANIFEST")

# Borrowed and modified from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)


def build_package(dirpath, dirnames, filenames):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames and 'steps.py' not in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[10:]  # Strip "armstrong<dir separator>"
        for f in filenames:
            # Ignore all dot files and any compiled
            if f.startswith(".") or f.endswith(".pyc"):
                continue
            data_files.append(os.path.join(prefix, f))


[build_package(dirpath, dirnames, filenames) for dirpath, dirnames, filenames
        in os.walk('armstrong/apps/articles')]


setup(
    name='armstrong.apps.articles',
    version='0.1',
    description='Provides the Article within Armstrong',
    author='Bay Citizen & Texas Tribune',
    author_email='info@armstrongcms.org',
    url='http://github.com/armstrongcms/armstrong.apps.articles/',
    packages=packages,
    package_data={"armstrong": data_files},
    namespace_packages=["armstrong", "armstrong.apps", ],
    install_requires=[
        'armstrong.apps.content',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
