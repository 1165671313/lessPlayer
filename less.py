import easygui
import cv2
import tkinter.messagebox as t
import re


def then():
    cap = cv2.VideoCapture(path)
    try:

        while cap.isOpened():
            ret, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow('Press Q key to end', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except:
        t.showinfo("播放完成", '播放结束|按确定键退出')
    cap.release()
    cv2.destroyAllWindows()


path = easygui.enterbox(msg='输入完整的视频地址', title='输入视频的地址')

if path is None:
    t.showinfo('退出', '您点击了退出')

else:
    res = '/'
    re = re.search(res, path)
    print(re)
    if re is None:
        t.showwarning('错误，请输入正确的地址', '请检查您的视频是否位于该程序的同级目录   或   再次输入')
    else:
        then()
