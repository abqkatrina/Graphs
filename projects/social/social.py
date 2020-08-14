import random
from util import Stack, Queue
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    #  want a way to get friend ids
    def get_friend(self, user_id):
        return self.friendships[user_id]

    # want a way to make a path of friendships (bfs)
    def bfs(self, user_id, friend_id):
        q = Queue()
        q.enqueue([user_id])
        visited = set()
        while q.size() > 0:
            p = q.dequeue()
            last = p[-1]
            if last == friend_id:
                return p
            if last not in visited:
                visited.add(last)
                for f in self.get_friend(last):
                    copy = p.copy()
                    copy.append(f)
                    q.enqueue(copy)


    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # placeholder array for shuffling
        potentials = []

        # create new user
        for x in range(num_users):
            # use add method with user name as argument -- user_id in this case
            self.add_user(f"User {x + 1}")

        # for each user id, add friend ids
        for user in self.users:
            for friend_id in range(user + 1, self.last_id + 1):
                # add relationship object to list of friendships
                potentials.append((user, friend_id))

        # shuffle list of friendships
        random.shuffle(potentials)

        # for each user, add friendships with connections
        for x in range(num_users * avg_friendships // 2):
            # add random friendship to user -- use add method with edge to next user(friend)
            friendship = potentials[x]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        s = Stack()
        s.push(user_id)
        # while there's something in the stack, make current the popped item
        while s.size() > 0:
            v = s.pop()
            # if current hasn't been used, mark used and 
            # create a path between starting user and current
            # using the visited list
            if v not in visited:
                path = self.bfs(user_id, v)
                visited[v] = path
                # for each friend of the current, add to stack and start again
                for f in self.get_friend(v):
                    s.push(f)
        # when all connected user ids have been visited and the stack is empty, return the list
        return visited
        # TODO first user/ unconnected users show path to self as self. Change to return nothing?

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
