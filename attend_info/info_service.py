import collections
from datetime import timedelta,datetime

class InfoService:
    """서비스"""

    def __init__(self, dao):
        self.dao = dao
        self.id = ''
        self.rule_in = '09:10'

    def sign_in(self, name, phone):
        info = self.dao.sign_in(name, phone)
        if info == 'teacher':
            return info
        elif not info:
            return False
        else:
            self.id = info.id
            return info

    def teacher_search(self, date):
        # print(date)
        names = self.dao.selectByDate_t(date)
        print(names)
        return names

    # student
    def searchAttend(self):
        attendInfo = []
        allInfo = self.dao.selectById(self.id)
        for in_date in allInfo:
            in_time = in_date.split(' ')[1]
            hour = in_time.split(':')[0]
            minute = in_time.split(':')[1]
            # 입실 시각 < 규정 입실 시각
            if int(hour) < int(self.rule_in.split(':')[0]):
                print(hour, "/", self.rule_in.split(':')[0])
                attendInfo.append(in_date)
            # 입실 시각 == 규정 입실 시각 and 입실 분 <= 규정 입실 분
            elif int(hour) == int(self.rule_in.split(':')[0]) and int(minute) <= int(self.rule_in.split(':')[1]):
                attendInfo.append(in_date)
        print('atttendInfo:', attendInfo)
        return attendInfo

    def searchLate(self):
        lateInfo = []
        allInfo = self.dao.selectById(self.id)
        for in_date in allInfo:
            in_time = in_date.split(' ')[1]
            hour = in_time.split(':')[0]
            minute = in_time.split(':')[1]
            # 입실 시각 > 규정 입실 시각
            if int(hour) > int(self.rule_in.split(':')[0]):
                lateInfo.append(in_date)
            # 입실 시각 == 규정 입실 시각 and 입실 분 > 규정 입실 분
            elif int(hour) == int(self.rule_in.split(':')[0]) and int(minute) > int(self.rule_in.split(':')[1]):
                lateInfo.append(in_date)
        print('lateInfo:', lateInfo)
        return lateInfo

    def searchAbsent(self):
        startDate = datetime.strptime('2020-07-01', '%Y-%m-%d')  # 시작일
        endDate = datetime.today()  # 오늘
        allInfo = self.dao.selectById(self.id)  # 해당 id 모든 입실시간 정보
        attendDate = collections.deque()  # date 타입의 입실시간 정보
        absentInfo = []  # 결석한 날짜 정보
        flag = True
        # str 타입의 입실시간 정보 datetime 타입으로 변환
        for in_date in allInfo:
            d = datetime.strptime(in_date.split(' ')[0], '%Y-%m-%d')
            attendDate.append(d)  # datetime 타입으로 append
        # 결석한 날짜 찾기
        while flag:
            # startDate와 endDate가 일치하면 반복문 종료
            if str(startDate).split(' ')[0] == str(endDate).split(' ')[0]:
                flag = False
                break
            # attendDate의 요소가 존재할 경우
            if len(attendDate) > 0 and startDate < attendDate[0]:
                absentInfo.append(str(startDate).split(' ')[0])
                startDate += timedelta(days=1)
            elif len(attendDate) > 0 and startDate == attendDate[0]:
                attendDate.pop(0)
            # attendDate의 요소가 존재하지 않을 경우
            elif len(attendDate) == 0:
                absentInfo.append(str(startDate).split(' ')[0])
        print('absentInfo:', absentInfo)
        return absentInfo
