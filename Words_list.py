# def words_list():
#     list = ["blue", "pink", "green", "aqua"]
#     print(list)

class Words:

    def __init__(self, head, body, arm_1, arm_2, leg_1, leg_2):
        self.__head = head
        self.__body = body
        self.__arm_1 = arm_1
        self.__arm_2 = arm_2
        self.__leg_1 = leg_1
        self.__leg_2 = leg_2

    def set_head(self, head):
        self.__head = head
    def set_body(self, body):
        self.__body = body
    def set__arm_1(self, arm_1):
        self.__arm_1 = arm_1
    def set__arm_2(self, arm_2):
        self.__arm_2 = arm_2
    def set__leg_1(self, leg_1):
        self.__leg_1 = leg_1
    def set__leg_2(self, leg_2):
        self.__leg_2 = leg_2

    def get_head(self):
        return self.__head
    def get_body(self):
        return self.__body
    def get_arm_1(self):
        return self.__arm_1
    def get_arm_2(self):
        return  self.__arm_2
    def get_leg_1(self):
        return self.__leg_1
    def get_leg_2(self):
        return self.__leg_2

