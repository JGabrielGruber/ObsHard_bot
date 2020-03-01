
from distutils.core import setup

try:
	from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
	# 2.x
	from distutils.command.build_py import build_py

setup(
	name="obsgpu_bot",
	version="1.0.0",
	author="José Gabriel Gruber",
	author_email='jose_gabriel_gruber@hotmail.com',
	url="https://github.com/JGabrielGruber/ObsGPU_bot",
	download_url="https://github.com/JGabrielGruber/ObsGPU_bot",
	long_description="""GPU's prices reporter from e-commerces""",
	license="AGPL-3.0",
	packages=['bs4'],
	cmdclass={'build_py': build_py},
	classifiers=["Development Status :: 1 - Alpha",
				"Intended Audience :: Users",
				"License :: GNU Affero General Public License v3.0",
				"Programming Language :: Python",
				'Programming Language :: Python :: 3'
				],
)
