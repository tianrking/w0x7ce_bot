# w0x7ce_bot
�״� 


TF���任��Ӣ�ĵ���TransForm����д������ROS��ROS2�е�TF����ָ������任��صĹ��ߡ�

����ʹ��tf������㲥���߽��й㲥�����ϵ���㲥ʱ��Ҫ�������ݣ�

������ϵ���ƣ��ַ�����
������ϵ���ƣ��ַ�����
����֮��ı任��ϵ��ƽ�ƹ�ϵ����ת��ϵ��

����B��C��λ��
������ϵ�����־���B��������ϵ��������C������֮���ƽ�ƹ�ϵ��0 0 3,��ת��ϵ����x����ת180�ȡ�
ros2 run tf2_ros static_transform_publisher 0 0 3 0 0 3.14 B C

����C��P��λ��
ros2 run tf2_ros static_transform_publisher 2 1 2 0 0 0 C P

����/��ȡTF��ϵ
ros2 run tf2_ros tf2_echo B P



rqt_tf_tree
sudo apt install ros-humble-rqt-tf-tree

�鿴���еķ����ߺ�Ƶ�ʡ�
tf2_monitor
ros2 run tf2_ros tf2_monitor 


rviz ����Ĭ������ϵ FixedFrame map ����B��C��λ�˺� ����C��P��λ�� ���Թ̶�frame ����B��C��λ�� ���Թ̶���̬B

��� tf ��� �鿴 tf ����

URDF����ɽ��� һ������£�URDF��������Ϣ�����ֹؼ������ͬ���

������Ϣ���������֣���һ������xml��������Ϣ�����ڵ�һ�� �ڶ������ǻ����˵�������ͨ��robot��ǩ�Ϳ�������һ��������ģ��

```xml
<?xml version="1.0"?>
<robot name="fishbot">
     <link></link>
     <joint></joint>
  ......
</robot>
```

���ֹؼ����(Joint&Link) ��Link��Link֮������Ӳ��ֳ�֮ΪJoint�ؽ�

```xml
```

���Լ�Ϊ�������������ɣ�

����

��������

֧����

�״Ｄ��

IMUģ��

��Ҫ���ӻ�ģ����Ҫ�����ڵ����

joint_state_publisher_gui ���𷢲������˹ؽ�������Ϣ��ͨ��joint_states���ⷢ��
robot_state_publisher_node���𷢲�������ģ����Ϣrobot_description������joint_states����ת��tf��Ϣ����
rviz2_node������ʾ�����˵���Ϣ

���������õ���joint_state_publisher_gui��robot_state_publisher��������������ϵͳû�а�װ���������������ֶ���װ:

sudo apt install ros-$ROS_DISTRO-joint-state-publisher-gui ros-$ROS_DISTRO-robot-state-publisher



# ���� w0x7ce_bot

ros2 pkg create w0x7ce_bot_description --build-type ament_python

cd w0x7ce_bot_description && mkdir urdf 
vim urdf/w0x7ce_base.urdf

```xml
<?xml version="1.0"?>
<robot name="w0x7ce_bot">
    
  <!-- base link -->
  <link name="base_link">
      <visual>
      <origin xyz="0 0 0.0" rpy="0 0 0"/>
      <geometry>
        <cylinder length="0.12" radius="0.10"/>
      </geometry>
    </visual>
  </link>
    
  <!-- laser link -->
  <link name="laser">
      <visual>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <cylinder length="0.02" radius="0.02"/>
      </geometry>
      <material name="black">
          <color rgba="0.0 0.0 0.0 0.8" /> 
      </material>
    </visual>
  </link>
    
  <!-- laser joint -->
    <joint name="laser_joint" type="fixed">
        <parent link="base_link" />
        <child link="laser" />
        <origin xyz="0 0 0.075" />
    </joint>

</robot>

```

mkdir launch
touch display_rviz2.launch.py

```python
import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    package_name = 'w0x7ce_bot_description'
    urdf_name = "w0x7ce_base.urdf"

    ld = LaunchDescription()
    pkg_share = FindPackageShare(package=package_name).find(package_name) 
    urdf_model_path = os.path.join(pkg_share, f'urdf/{urdf_name}')

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        arguments=[urdf_model_path]
        )

    joint_state_publisher_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        arguments=[urdf_model_path]
        )

    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        )

    ld.add_action(robot_state_publisher_node)
    ld.add_action(joint_state_publisher_node)
    ld.add_action(rviz2_node)

    return ld
```

setup.py

```python
from setuptools import setup
from glob import glob
import os

package_name = 'w0x7ce_bot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/**')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='me@w0x7ce.eu',
    description='w0x7ce: Package description',
    license='w0x7ce: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
```

# w0x7ce_bot

# rp2040 

https://github.com/tianrking/MicroROS_RP2040

# �����״�

https://github.com/Slamtec/sllidar_ros2 ok
https://github.com/Slamtec/rplidar_ros not ok

ros2 launch rplidar_ros rplidar.launch.py

������ scan
link Ϊ laser

#

