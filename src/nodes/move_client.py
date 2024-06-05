#!/usr/bin/env python3
import sys
import rospy
from geometry_msgs.msg import Pose, Point, Quaternion
from ur5_robot.srv import MoveToPose, MoveToPoseRequest

def move_robot_to_pose(pose):
    rospy.wait_for_service('move_to_pose')
    try:
        move_to_pose = rospy.ServiceProxy('move_to_pose', MoveToPose)
        resp = move_to_pose(pose)
        return resp.success
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def main():
    rospy.init_node('move_robot_client')

    # Example pose
    example_pose = Pose()
    example_pose.position = Point(0.2, 0.3, 0.1)  # Example position in meters
    example_pose.orientation = Quaternion(0, 0, 0, 1)  # Example orientation as a quaternion

    result = move_robot_to_pose(example_pose)
    if result:
        print("Robot moved successfully!")
    else:
        print("Failed to move robot.")
    rospy.sleep(5)
    example_pose = Pose()
    example_pose.position = Point(0.2, 0.3, 0.4)  # Example position in meters
    example_pose.orientation = Quaternion(0, 0, 0, 1)  # Example orientation as a quaternion
    result = move_robot_to_pose(example_pose)
    if result:
        print("Robot moved successfully!")
    else:
        print("Failed to move robot.")
if __name__ == "__main__":
    main()
