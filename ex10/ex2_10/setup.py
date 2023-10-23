from setuptools import find_packages, setup

package_name = 'ex2_10'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='solmir',
    maintainer_email='v.chelondaev@g.nsu.ru',
    description='movement of turtle by phrases',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'text_to_cmd_vel = ex2_10.text_to_cmd_vel:main'
        ],
    },
)
