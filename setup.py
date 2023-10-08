from setuptools import setup, find_packages

with open('requirements.txt') as f:
	requirements = f.readlines()

long_description = 'Sample Package made for a demo \
	of its making for the GeeksforGeeks Article.'

setup(
		name ='qcheck',
		version ='1.0.0',
		author ='kutumbarao Nidamarthi',
		author_email ='nidamarthi.kr@gmail.com',
		url ='https://github.com/nidamarthikr/qcheck',
		description ='Quality parameters for cryoEM',
		license ='MIT',
		packages = find_packages(),
		classifiers =(
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
		),
		keywords ='CryoEm 3D maps Reconstrunction Statistics Quality matrics',
		install_requires = requirements,
		zip_safe = False
)
