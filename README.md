# Carla Agent Development

The ROS project for the CPSL carla development team.

We use ROS2 Humble for this project.

## Quickstart

Here's the procedure to run a simple test node to see how things work.

```
mkdir -p /your/path/to/project/src  # note the src at the end
cd /your/path/to/project/src
git clone https://github.com/cpsl-research/carla-agent.git
cd ..
colcon build --packages-select carla_agent_control carla_agent_bringup
source install/setup.zsh  # if your shell is zsh, install/setup.bash if bash
ros2 launch carla_agent_bringup test_launch.xml
```
