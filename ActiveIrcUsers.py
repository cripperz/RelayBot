# This class stores the usernames of the users who join through IRC, and the timestamp of their last message or activity
# This information is used in the SilentJoinPart class (in relaybot.py) to decide whether to relay/pass the message to the flowdock channel or not
# The purpose is to send as little quit/leave/rename messages to flowdock as possible

import time, re
class ActiveIrcUsers:
    def __init__(self):
        self.users = {}

    def add(self, username):
        self.users[username] = int(time.time())

    def remove(self, username):
        if username in self.users:
            del self.users[username]

    def getUsernameFromMessage(self, message):
        regex = re.compile("\[([^\]]+)")
        match = regex.match(message)
        if match:
            return match.group(1)
        return False

    # a user is active if he/she sent a message or renamed their nick in the last 30 minutes (1800 seconds)
    def isUserStillActive(self, username):
        if username in self.users:
            lastTimestamp = self.users[username]
            currentTimestamp = int(time.time())
            return abs(currentTimestamp - lastTimestamp) < 1800
        return False
