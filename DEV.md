# w0x7ce_bot
雷达 


TF即变换的英文单词TransForm的缩写。所以ROS和ROS2中的TF就是指和坐标变换相关的工具。

可以使用tf的坐标广播工具进行广播坐标关系，广播时需要三个数据：

父坐标系名称（字符串）
子坐标系名称（字符串）
父子之间的变换关系（平移关系和旋转关系）

发布B到C的位姿
父坐标系的名字就是B，子坐标系的名字是C，父子之间的平移关系是0 0 3,旋转关系是绕x轴旋转180度。
ros2 run tf2_ros static_transform_publisher 0 0 3 0 0 3.14 B C

发布C到P的位姿
ros2 run tf2_ros static_transform_publisher 2 1 2 0 0 0 C P

监听/获取TF关系
ros2 run tf2_ros tf2_echo B P



rqt_tf_tree
sudo apt install ros-humble-rqt-tf-tree

查看所有的发布者和频率。
tf2_monitor
ros2 run tf2_ros tf2_monitor 


rviz 设置默认坐标系 FixedFrame map 发布B到C的位姿后 发布C到P的位姿 可以固定frame 发布B到C的位姿 可以固定姿态B

添加 tf 插件 查看 tf 数据

URDF的组成介绍 一般情况下，URDF由声明信息和两种关键组件共同组成

声明信息包含两部分，第一部分是xml的声明信息，放在第一行 第二部分是机器人的声明，通过robot标签就可以声明一个机器人模型

```xml
<?xml version="1.0"?>
<robot name="fishbot">
     <link></link>
     <joint></joint>
  ......
</robot>
```

两种关键组件(Joint&Link) 而Link和Link之间的连接部分称之为Joint关节

```xml
```

可以简化为如下五个部件组成：

躯体

左右轮子

支撑轮

雷达激光

IMU模块

想要可视化模型需要三个节点参与

joint_state_publisher_gui 负责发布机器人关节数据信息，通过joint_states话题发布
robot_state_publisher_node负责发布机器人模型信息robot_description，并将joint_states数据转换tf信息发布
rviz2_node负责显示机器人的信息

这里我们用到了joint_state_publisher_gui和robot_state_publisher两个包，如果你的系统没有安装这两个包，可以手动安装:

sudo apt install ros-$ROS_DISTRO-joint-state-publisher-gui ros-$ROS_DISTRO-robot-state-publisher



# 创建 w0x7ce_bot

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

# 开启雷达

https://github.com/Slamtec/sllidar_ros2 ok
https://github.com/Slamtec/rplidar_ros not ok

ros2 launch rplidar_ros rplidar.launch.py

发布在 scan
link 为 laser

#

