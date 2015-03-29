import cv2


def RegionCheck(foo, ListPath):

    if (foo <= 130) and (ListPath[0] is not 0):
        ListPath[0] = 0
    if (foo > 130) and (foo <= 320) and (ListPath[1] is not 0):
        ListPath[1] = 0
    if (foo > 320) and (foo <= 510) and (ListPath[2] is not 0):
        ListPath[2] = 0
    if (foo > 510) and (ListPath[3] is not 0):
        ListPath[3] = 0

    return ListPath


def DirectBot():
    pass