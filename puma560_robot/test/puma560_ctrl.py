#! /usr/bin/env python
import rospy
from threading import Thread
import trajectory_msgs.msg as tm
import sensor_msgs.msg as sm
import geometry_msgs.msg as gm

class TopicListener(object):
    # "stores last message"
    last_msg = None

    def __init__(self, topic_name, msg_type):

        self.sub = rospy.Subscriber(topic_name, msg_type, self.callback)

        rospy.loginfo('esperando por el primer mensaje: %s' % topic_name)
        while self.last_msg is None: rospy.sleep(.01)
        rospy.loginfo('ok: %s' % topic_name)

    def callback(self, msg):
        self.last_msg = msg

class JustWaitThread(Thread):
    def __init__(self, duration):
        Thread.__init__(self)
        self.wants_exit = False
        self.duration = duration

    def run(self):
        t_done = rospy.Time.now() + rospy.Duration(self.duration)
        while not self.wants_exit and rospy.Time.now() < t_done and not rospy.is_shutdown():
            rospy.sleep(.01)        

class Puma560(object):

    def __init__(self):
        self.home_position = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.zero_position = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.ns = '/puma560'
        self.joints = []

    def get_ns(self):
        return self.ns

    def goto_position_goal(self, position_goal):
        pass

class TrajectoryControllerWrapper(object):

    def __init__(self, puma560, controller_name):
        self.puma560 = puma560
        self.controller_name = controller_name
        self.joints = rospy.get_param('/{}/{}/joints'.format(self.puma560.get_ns(), self.controller_name))
           

def main():
    pass

if __name__ == "__main__":
    pass