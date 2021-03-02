from setuptools import setup

setup(
	name='evolution',
	version='0.1',
	install_requires=['numpy>=1.17',
					  'scipy>=1.3.1',
					  'pyexpokit',
					  'matplotlib>=3.1.1'],
	author='Johannes Kombe',
	description=('Time evoution using exact diagonalisation for quantum systems'),
	license='MIT',
	packages=['evolution'],
	classifiers=[
		'Intended Audience :: Science/Research',
		'License :: MIT License',
		'Progreamming Language :: Python :: 3.7'],
	python_requires='>=3.6')