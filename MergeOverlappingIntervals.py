# Merge Intervals
# Merge Overlapping Intervals
intervals = [[1,3],[2,6],[8,10],[15,18]]

# sorting in basis of start time
intervals.sort(key=lambda x: x[0])

merged = []
for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])