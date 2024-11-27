import heapq
from collections import defaultdict, deque

class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(deque) 
        self.followees = defaultdict(set)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        if len(self.tweets[userId]) == 10:
            self.tweets[userId].popleft()
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        recent_tweets = []
        
        if userId in self.tweets:
            recent_tweets.extend(self.tweets[userId])
        
        for followee_id in self.followees[userId]:
            recent_tweets.extend(self.tweets[followee_id])
        
        return [tweet for _, tweet in heapq.nlargest(10, recent_tweets)]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)