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
        start_date = '2020-07-01'
