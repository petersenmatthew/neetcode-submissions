class Twitter:

    def __init__(self):
        # dict of account -> set(following)?
        self.following = {}
        # dict of user -> list of (time, tweetId)
        self.posts = {}
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.following:
            self.following[userId] = set()
            self.following[userId].add(userId)

        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        # i want the top k posts with the LARGEST time
        # use a min heap of size 10

        max_heap = []

        for following_user in self.following[userId]:
            for post in self.posts.get(following_user, []):
                heapq.heappush(max_heap, post)
                if len(max_heap) > 10:
                    heapq.heappop(max_heap)
        
        output = []
        while max_heap:
            output.append(heapq.heappop(max_heap)[1])
        return output[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
            self.following[followerId].add(followerId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId == followeeId:
            return
        self.following[followerId].discard(followeeId)