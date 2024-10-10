ip_version_priority = "ipv6"

source_urls = [
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Tianjin_liantong.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Zhejiang_dianxin.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Beijing_liantong.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Shanghai_dianxin.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Guangdong_dianxin.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Henan_liantong.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Sichuan_yidong.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Sichuan_dianxin.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Jiangsu_dianxin.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Anhui_dianxin.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Hubei_dianxin.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Chongqing_liantong.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Hunan_dianxin.txt",
    #"https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Yinni_PT.txt",
    "https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/Yuenan_FPT.txt",
    "https://github.com/zjykfy/fei/raw/main/GAT/GAT.m3u",
    "https://github.com/zjykfy/fei/raw/main/GAT/NEWTV.m3u",
    #"https://github.com/zjykfy/yangfeiyue/raw/main/speedtest/txt/KR_SK.txt",
    #"https://github.com/zjykfy/fei/raw/main/Yulin/Yulinzubo.m3u",
    #"https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/merged_output.txt"
]

url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "test.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn",
]

announcements = [
    {
        "channel": "公告",
        "entries": [
            {"name": "更新日期", "url": "https://live.yangfeiyue.cn/p/%E5%A4%A7%E7%8F%AD.MP4", "logo": "https://live.yangfeiyue.cn/p/端午节.png"},
            {"name": None, "url": "https://live.yangfeiyue.cn/p/%E5%A4%A7%E7%8F%AD.MP4", "logo": "https://live.yangfeiyue.cn/p/端午节1.png"},
  ]
    }
]

epg_urls = [
    "https://assets.livednow.com/epg.xml",
    "http://epg.51zmt.top:8000/e.xml",
]