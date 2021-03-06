from algorithms import bfs
from facebook import FacebookClient
from constants import TARGET

cookies = None

class FBTree:
    solution_required = 1  # NUMBER MUTUAL FRIENDS REQUIRED
    client = FacebookClient(cookies)

    def __init__(self):
        self.root = self.client.get_myself_username()
        self.goals = None

    def get_root(self):
        return self.root

    def set_goals(self, username):
        """
        Get the friends of the target
        """
        children = self.client.get_friends(username)
        self.goals = [child.username for child in children]
        print 'goals: ', self.goals

    def is_goal(self, username):
        """
        Check if the new user is in the goals set
        """
        return username in self.goals

    def get_children(self, username):
        return self.client.get_friends(username)


if __name__ == '__main__':
    tree = FBTree()
    tree.set_goals(TARGET)
    results = bfs(tree)

    print '------------------------------------------'
    print "RESULT PATHS: %s\n" % '\n'.join(results)
    print '------------------------------------------'
