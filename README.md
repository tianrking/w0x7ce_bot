<!--
 * @作�?: 小鱼
 * @�?众号: 鱼�?�ROS
 * @QQ交流�?: 2642868461
 * @描述: README
-->


## What's w0x7ce_bot


## How to use

### Download & Compile


```
git clone --recursive https://github.com/tianrking/w0x7ce_bot -b cool_single_radar coool_single_radar
cd coool_single_radar
rosdep install --from-paths src -y
colcon build
```

### Use

#### Build map

```
source install/setup.bash
ros2 launch fishbot_cartographer cartographer.launch.py
```

#### Nav2
```
source install/setup.bash
ros2 launch fishbot_navigation2 navigation2.launch.py use_sim_time:=True
```

Error

```bash
None of the required 'cairo>=1.12.16' found
```

Solution

```bash
export PKG_CONFIG_PATH="/usr/share/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig:$PKG_CONFIG_PATH"
```