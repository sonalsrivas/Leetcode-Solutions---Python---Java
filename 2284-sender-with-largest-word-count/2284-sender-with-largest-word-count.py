class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        maxNoOfWordsSent=0
        mapSenderNoOfWords=defaultdict(int)
        for message, sender in zip(messages, senders):
            mapSenderNoOfWords[sender]+=len(message.split())
            maxNoOfWordsSent=max(maxNoOfWordsSent, mapSenderNoOfWords[sender])
        
        senderOfLargestWordCount=''
        for sender, words in mapSenderNoOfWords.items():
            if words==maxNoOfWordsSent and sender>senderOfLargestWordCount:
                senderOfLargestWordCount=sender
        return senderOfLargestWordCount
                