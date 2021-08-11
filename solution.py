# idea: this is a graph problem where for each node (meeting)
#       you either add it to our answer or not
#
# you only add that node to the solution set if there are no violations of the rules
#
# at the end, given the valid solutions, take the one with highest involved

test_cases = [
    [[0,1,2],[1,2]],
    [[0,1],[0],[1]],
    [[0,1,2],[2,3]],
    [[4,10],[3,4,12],[0,8,9,10,13],[1,5,7],[2,6],[9,4,10,11,12],[11,13]],
    [[6,16,17],[8,9],[1],[7,14,9],[10,5],[2,7],[0,6,7,9],[10,11,5,13,15,16,17],[7,9],[5,9],[2,12,5,6,14,7,15,9],[10,5,14],[1,4,8],[1,3,9],[5]],
    [[9,16,34],[10,13,18,20,23,28,30,31,32],[4,7,8,11,16,17,19,25,29,36,37],[0,2,23,28],[1,3,7,8,14,15,19,24,25,26,32],[12,28],[16,21,24,33,34],[5,6,10,15,16,17,21,22,24,27,33,34,35]]
]

def helper(solutions, possible_solution, meetings, booked):
    if len(meetings) == 0:
        solutions.append((possible_solution, len(booked)))
        return

    # don't add the current meeting, but recurse
    helper(solutions, possible_solution, meetings[1:], booked)

    # possibly add the current meeting
    meeting_to_add = meetings[0]
    can_add = True

    # check if there are double booked
    for attendee in meeting_to_add:
        if attendee in booked:
            can_add = False
            break

    if can_add:
        # book the attendees
        for attendee in meeting_to_add:
            booked.add(attendee)
        # add this meeting to the possible solution
        possible_solution.append(meeting_to_add)
        # recurse on the next choice (don't need to recurse if we didn't add because we already did the alternative)
        helper(solutions, possible_solution, meetings[1:], booked)

# (repeated)
# idea: this is a graph problem where for each node (meeting)
#       you either add it to our answer or not
#
# you only add that node to the solution set if there are no violations of the rules
#
# at the end, given the valid solutions, take the one with highest involved
def solve(meetings):
    solutions = []
    
    # there is always at least one meeting
    possible_solution = [meetings[0]]
    booked = set(meetings[0])
    helper(solutions, possible_solution[:], meetings[1:], booked)

    # sort by involved
    solutions.sort(key=lambda x:x[1])
    solutions.reverse()

    # since reverse sorted by second element, the answer is on top
    ans = solutions[0][0]
    involved = solutions[0][1]

    return ans, involved
    
# print(test_cases)

for i, meetings in enumerate(test_cases):
    print(solve(meetings))
    # print("%s which has %d attendees" % str(ans), involved)
