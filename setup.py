from setuptools import setup

setup(
    name='tailwindpie',
    version='0.1.1',
    description='easiest way to configure tailwind in python',
    url='https://github.com/Abdulmumin1/tailwindpie',
    author='Abdulmumin Abdulkarim',
    author_email='avdorr12345@gmail.com',
    license='BSD 2-clause',
    packages=['tailwindpie'],
    install_requires=['rich'],
    entry_points={
        'console_scripts': [
            'tailwindpie = tailwindpie:parge',
        ]
    },

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
