import heapq
from datetime import datetime
from collections import defaultdict
from typing import List
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweet = defaultdict(list)
        self.followList = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet[userId].append((self.time, tweetId))
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        feed.extend(self.tweet[userId])
        for followee in self.followList[userId]:
            feed.extend(self.tweet[followee])
        feed.sort(reverse=True)
        ans = []
        for time, tweetId in feed[:10]:
            ans.append(tweetId)
        return ans
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].add(followeeId)
        return None
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)