class Solution:
    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, start, end):
        n = len(start)
        meetings = []

        # Store (end_time, start_time) for each meeting
        for i in range(n):
            meetings.append((end[i], start[i]))

        # Sort meetings by their end times
        meetings.sort()

        count = 1           # We can always select the first meeting
        last_end = meetings[0][0]

        for i in range(1, n):
            if meetings[i][1] > last_end:
                count += 1
                last_end = meetings[i][0]

        return count


start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
print(Solution().maximumMeetings(start, end))
