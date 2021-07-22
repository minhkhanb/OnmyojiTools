from gameLib.fighter import Fighter
from tools.game_pos import YuhunPos
import tools.utilities as ut

import logging


class GoryouFight(Fighter):
    '''单人御魂战斗，参数done, emyc'''

    def __init__(self, done=1, emyc=0):
        # 初始化
        Fighter.__init__(self)

    def start(self):
        '''单人战斗主循环'''
        mood1 = ut.Mood()
        mood2 = ut.Mood()
        mood3 = ut.Mood(3)
        while self.run:
            # Phát hiện xem quá trình giải quyết có thành công ở bước trước hay không và ngăn chặn các bất thường do máy rung không được phát hiện trong giây lát
            maxVal, maxLoc = self.yys.find_multi_img(
                'img/SHENG-LI.png', 'img/TIAO-DAN.png', 'img/JIN-BI.png', 'img/JIE-SU.png')

            if max(maxVal) > 0.9:
                self.get_reward(mood3, 1)

            # Nhấp vào nút "Thử thách" trong menu chính của Evo Material, bạn cần sử dụng "khóa đội hình"!
            self.yys.wait_game_img_knn('img\\CHALLENGE.png', max_time=self.max_win_time)

            mood1.moodsleep()
            self.click_until_knn('Nút thử thách', 'img\\CHALLENGE.png',
                                 *YuhunPos.tiaozhan_btn, appear=False, thread=20)

            logging.info('Check battle')
            # Kiểm tra xem có tham gia trận chiến hay không
            self.check_battle()

            # Trong trận chiến, tự động nhấp vào đổ lỗi
            self.click_monster()

            # Kiểm tra xem nó đã hoàn thành chưa
            state = self.check_end()
            mood2.moodsleep()

            # Dàn xếp trận chiến
            self.get_reward(mood3, state)
            logging.info("Quay lại giao diện lựa chọn")

            # Kiểm tra số lượng trò chơi
            self.check_times()
