from tools.game_pos import TansuoPos, YuhunPos

import time
from tools.logsystem import MyLog
import cv2


class GameScene():
    def __init__(self):
        self.deep = 0
        self.log = MyLog.mlogger

    def get_scene(self):
        '''
        Xác định cảnh hiện tại
             : return: Trả lại tên cảnh:
             1- sân trong;
            2-Khám phá giao diện;
            3-Giao diện chương;
            4-Khám phá bên trong;
            5-Soul Menu;
            6-Soul Start
            7-Fire Start
            8-Himiko Start
        '''
        # 拒绝悬赏
        self.yys.rejectbounty()

        # 分别识别庭院、探索、章节页、探索内
        maxVal, maxLoc = self.yys.find_multi_img(
            'img/JIA-CHENG.png', 'img/SCENE-EXPLORE.png', 'img/BTN-EXPLORE.png', 'img/YING-BING.png', 'img/SOULS-MENU.png', 'img/TIAO-ZHAN.png')

        scene_cof = max(maxVal)
        if scene_cof > 0.9:
            scene = maxVal.index(scene_cof)
            return scene + 1
        else:
            return 0

    def switch_to_scene(self, scene):
        '''
        Chuyển cảnh
             : param scene: Cảnh được chuyển sang: 1-8
             : return: Trả về True nếu chuyển đổi thành công; Thoát trực tiếp nếu chuyển đổi không thành công
        '''
        scene_now = self.get_scene()
        self.log.info('Current scene：' + str(scene_now))

        if scene_now == 0:
            self.log.info('The scene is not recognized yet, try again after 2s')
            time.sleep(2)
            scene_now = self.get_scene()
            self.log.info('Current scene：' + str(scene_now))

        if scene_now == scene:
            return True
        if scene_now == 1:
            # Trong sân
            if scene in [2, 3, 4, 5, 6, 7, 8]:
                # Đầu tiên hãy vẽ giao diện ở ngoài cùng bên phải
                self.slide_x_scene(800)
                time.sleep(2)
                self.slide_x_scene(800)

                # Bấm vào lồng đèn thám hiểm để vào giao diện khám phá
                self.click_until('Khám phá đèn lồng', 'img/JUE-XING.png', *
                                 TansuoPos.tansuo_denglong, 2)

                # 递归
                self.switch_to_scene(scene)

        elif scene_now == 2:
            # Khám phá giao diện
            if scene == 3 or scene == 4:

                # Check reward in Chapter scene
                result = self.yys.find_game_img_knn('img\\CHEST.png', thread=30)
                self.log.info('Bấm vào ' + str(result))

                # Bấm vào chương cuối cùng
                self.click_until('Chương cuối cùng', 'img/BTN-EXPLORE.png',
                                 *TansuoPos.last_chapter, 2)
                # 递归
                self.log.info('chuong cuoi cung scene: ' + str(scene))
                self.switch_to_scene(scene)
            elif scene in [5, 6, 7, 8]:
                # 点击御魂按钮
                self.click_until('Soul Menu', 'img/BA-QI-DA-SHE.png',
                                 *YuhunPos.yuhun_menu, 2)
                # 递归
                self.switch_to_scene(scene)

        elif scene_now == 3:
            # 章节界面
            if scene == 4:
                # 点击探索按钮
                self.click_until('Nút khám phá', 'img/YING-BING.png',
                                 *TansuoPos.tansuo_btn, 2)
                # 递归
                self.switch_to_scene(scene)
            elif scene in [5, 6, 7, 8]:
                self.click_until('Thoát chương', 'img/JUE-XING.png',
                                 *TansuoPos.quit_last_chapter, 2)
                self.switch_to_scene(scene)

        elif scene_now == 4:
            # 探索内
            if scene in [2, 3]:
                # 点击退出探索
                self.click_until_multi('Nút thoát', 'img/QUE-REN.png', 'img/BTN-EXPLORE.png', 'img/SCENE-EXPLORE.png',
                                 pos=TansuoPos.quit_btn[0], pos_end=TansuoPos.quit_btn[1], step_time=0.5)

                # 点击确认
                self.click_until('Nút xác nhận', 'img\\QUE-REN.png',
                                 *TansuoPos.confirm_btn, 2, False)
                # 递归
                self.switch_to_scene(scene)

        elif scene_now == 5:
            # 御魂菜单内
            if scene == 6:
                # 点击御魂
                self.click_until_knn('Orochi', 'img/TIAO-ZHAN.png',
                                     *YuhunPos.yuhun_btn, 2, thread=20)
                # 递归
                self.switch_to_scene(scene)
            elif scene == 7:
                # 点击业原火
                self.click_until_knn('Fire', 'img/TIAO-ZHAN.png',
                                     *YuhunPos.yeyuanhuo_btn, 2, thread=20)
                # 递归
                self.switch_to_scene(scene)
            elif scene == 8:
                # 点击卑弥呼
                self.click_until_knn('Himiko', 'img/TIAO-ZHAN.png',
                                     *YuhunPos.beimihu_btn, 2, thread=20)
                # 递归
                self.switch_to_scene(scene)
