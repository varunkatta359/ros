from setuptools import find_packages, setup

package_name = 'my_pkgpy'

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
    maintainer='varun',
    maintainer_email='varun@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = my_pkgpy.node1:main",
            "robot_news_station = my_pkgpy.robot_news_station:main",
            "smartphone = my_pkgpy.smartphone:main",
            "number_publish= my_pkgpy.number_publisher:main",
            "Add_two_integers_server = my_pkgpy.add_two_ints_server:main",
            "Add_two_integers_client_no_opp = my_pkgpy.add_two_ints_client_no_opp:main",
            "Add_two_integers_client = my_pkgpy.add_two_ints_client_opp:main",
            "number_counter=my_pkgpy.number_counter:main",
            "Hw_status_publihser=my_pkgpy.hw_status_publisher:main",
            "Led_states_publisher=my_pkgpy.led_panel:main",
            "battery_client=my_pkgpy.battery_client:main"
            
        ],
    },
)
