#-*- coding: utf-8 -*-

"""在校园招聘的季节里，为了能让学生们更好地了解微软亚洲研究院各研究组的情况，HR部门计划为每一个研究组举办一次见面会，
让各 个研究组的员工能跟学生相互了解和交流。已知有n位学生，他们分别对m个研究组中的若干个感兴趣。为了满足所有学生的要求，HR希望每
个学生都能参加自己感兴趣的所有见面会。如果每个见面会的时间为t，那么，如何安排才能够使得所有见面会的总时间最短？ 最简单的办法，
就是把m个研究组的见面会时间依次排开，那我们就要用m * t的总时间，我们有10多个研究小组，时间会拖得很长，能否进一步提高效率？"""

"""可以将已知问题转换为着色问题"""

squences = [1, 2, 3, 4, 5, 6]   # 会议安排场次的顺序
meetings = ['A', 'B', 'C', 'D', 'E','F']

neighbors = {}                  # 定义一个空字典
neighbors['A'] = ['B', 'C']     # B,C会议不可以和A同时开
neighbors['B'] = ['A']
neighbors['C'] = ['A']
neighbors['D'] = ['F', 'E']
neighbors['E'] = ['F','D']
neighbors['F'] = ['D','E']

squences_of_meetings = {}       # 定义一个关于会议:场次顺序的字典


def main():
    temp = []
    for meeting in meetings:
        squences_of_meetings[meeting] = get_squence_for_meeting(meeting)
        temp.append(get_squence_for_meeting(meeting))

    time = len(set(temp))
    print squences_of_meetings
    print "The minimum time is %dt." %(time)                  # 返回总共需要的最少时间


def get_squence_for_meeting(meeting):
    for squence in squences:
        if promising(squence, meeting):
            return squence              # 返回会议的场次顺序


def promising(squence, meeting):    # 定义会议的场次顺序不能等于有时间冲突的场次
    for neighbor in neighbors.get(meeting):
        squence_of_neighbor = squences_of_meetings.get(neighbor)
        if squence_of_neighbor == squence:
            return False

    return True

main()



