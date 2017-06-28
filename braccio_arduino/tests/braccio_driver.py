#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from moveit_msgs.msg import DisplayTrajectory
import moving_braccio_pc
import time

def callback(data):

    print "\n\nNew Position: "
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", DisplayTrajectory.trajectory)
    
    text = str(data.trajectory[0])

    text = text.split("\n")
    positions = []
    for line in text:
        if "positions" in line:
            positions.append(line)
    
    final_positions = []
    c = True                    # To Be Deleted
    for elem in positions:
        start = elem.index("[")
        end = elem.index("]")
        final_positions.append(elem[start+1:end].split(","))    # Useless if using next line
        to_be_appended = elem[start+1:end].split(",")
        command = ['__ignored__']
        for elem in to_be_appended:
            command = command + [abs(float(elem))*(57.2958)]      # Append degrees and not radians
            #command = command + [float(elem)*(57.2958)]

        if c:
            #command = ['__ignored__'] + ['180', '165', '0', '0', '180', '73']  # To Be Deleted
            c = False
        else:
            #command = ['__ignored__'] + ['100', '165', '0', '0', '140', '10']  # To Be Deleted
            c = True
        print "\n\n"
        print command
        moving_braccio_pc.main(command+['73'])      # Keep the gripper closed
        #time.sleep(3)
        
    
    #moving_braccio_pc.main(['__ignored__', '180', '165', '0', '0', '180', '73'])

''' 
This can probably be deleted

def publish_positions(final_positions):

    pub = rospy.Publisher('positions', String, queue_size=10)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        rospy.loginfo(final_positions)
        pub.publish(''.join(map(str, final_positions)))

        rate.sleep()
'''

def listener():

    rospy.init_node("Positions_parser", anonymous=True)
    rospy.Subscriber("/move_group/display_planned_path", DisplayTrajectory, callback)
    
    rospy.spin()

if __name__ == "__main__":
    listener()
