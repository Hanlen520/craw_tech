import platform

from conf import logger
from base import scheduled
from crawler import juejin, cnblog, kf_toutiao, tuiku, importnew
from util import myos


def start():
    # linux下开起定时任务  其他就直接全部执行
    # if myos.is_linux():
    #     scheduled.start()
    # else:
    juejin.JueJin().start()
    tuiku.TuiKu().start()
    kf_toutiao.KaiFaTouTiao().start()
    importnew.ImportNew().start()
    cnblog.CnBlog().start()


if __name__ == '__main__':
    # log配置
    logger.init()
    # 启动
    start()
