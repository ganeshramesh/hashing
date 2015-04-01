from setuptools import setup

setup(name='hashing_library',
      version='0.1',
      description='A Hashing Library used for simhash and other tools.',
      url='http://github.com/ganeshramesh/hashing_library',
      author='Ganesh Ramesh',
      author_email='mr.ganesh.ramesh@gmail.com',
      license='MIT',
      packages=['hashing_library'],
      install_requires=[
	'hashlib','bitstring',
      ],
      zip_safe=False)
