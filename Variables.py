"""
Created on Jun 16, 2016

@author: MarcoXZh
"""

cssFF = [
    # Background
    "background-color",           "background-image",
    # Border
    "border-bottom-color",        "border-bottom-style",         "border-bottom-width",
    "border-left-color",          "border-left-style",           "border-left-width",
    "border-right-color",         "border-right-style",          "border-right-width",
    "border-top-color",           "border-top-style",            "border-top-width",
    "outline-color",              "outline-style",               "outline-width",
    "border-bottom-left-radius",  "border-bottom-right-radius",
    "border-top-left-radius",     "border-top-right-radius",     "box-shadow",
    # Text - paragraph
    "direction",                  "letter-spacing",              "line-height",
    "text-align",                 "text-decoration",             "text-indent",
    "text-transform",             "vertical-align",              "white-space",
    "word-spacing",               "text-overflow",               "text-shadow",
    "word-break",                 "word-wrap",
    # Text - column
    "-moz-column-count",         #"column-count",                "-webkit-column-count"
    "-moz-column-gap",           #"column-gap",                  "-webkit-column-gap",
    "-moz-column-rule-color",    #"column-rule-color",           "-webkit-column-rule-color",
    "-moz-column-rule-style",    #"column-rule-style",           "-webkit-column-rule-style",
    "-moz-column-rule-width",    #"column-rule-width",           "-webkit-column-rule-width",
    "-moz-column-width",         #"column-width",                "-webkit-column-width",
    # Text - list
    "list-style-image",           "list-style-position",         "list-style-type",
    # Text - font
    "font-family",                "font-size",                   "font-weight",
    #"font-size-adjust",# Only Firefox supports this property
    "font-style",                 "font-variant",                "color"
] # cssFF = [ ... ]
cssCH = [
    # Background
    "background-color",           "background-image",
    # Border
    "border-bottom-color",        "border-bottom-style",         "border-bottom-width",
    "border-left-color",          "border-left-style",           "border-left-width",
    "border-right-color",         "border-right-style",          "border-right-width",
    "border-top-color",           "border-top-style",            "border-top-width",
    "outline-color",              "outline-style",               "outline-width",
    "border-bottom-left-radius",  "border-bottom-right-radius",
    "border-top-left-radius",     "border-top-right-radius",     "box-shadow",
    # Text - paragraph
    "direction",                  "letter-spacing",              "line-height",
    "text-align",                 "text-decoration",             "text-indent",
    "text-transform",             "vertical-align",              "white-space",
    "word-spacing",               "text-overflow",               "text-shadow",
    "word-break",                 "word-wrap",
    # Text - column
    "-webkit-column-count",      #"-moz-column-count",          "column-count",
    "-webkit-column-gap",        #"-moz-column-gap",            "column-gap",
    "-webkit-column-rule-color", #"-moz-column-rule-color",     "column-rule-color",
    "-webkit-column-rule-style", #"-moz-column-rule-style",     "column-rule-style",
    "-webkit-column-rule-width", #"-moz-column-rule-width",     "column-rule-width",
    "-webkit-column-width",      #"-moz-column-width",          "column-width",
    # Text - list
    "list-style-image",           "list-style-position",         "list-style-type",
    # Text - font
    "font-family",                "font-size",                   "font-weight",
    "font-style",                 "font-variant",                "color"
] # cssCH = [ ... ]

urls = [
    # 1
    "http://virtual-dj.softonic.com",
    # 2
    "https://trello.com/",
    # 3
    "http://world.taobao.com//tw.taobao.com/market/tw/pt-index.php?spm=a213z.1224559.20150331FF08.1.xnGWsz",
    # 4
    "http://www.flipkart.com/q/dell-laptops",
    # 5
    "http://video.sina.com.cn/",
    # 6
    "http://rutracker.wiki/",
    # 7
    "http://www.nih.gov/",
    # 8
    "http://cache.ltn.com.tw/app/program/click.php?ano=2016011183",
    # 9
    "http://news.rambler.ru/politics/32414463/",
    # 10
    "http://market.envato.com/",
    # 11
    "http://xuite.net/",
    # 12
    "http://www.webmdhealthservices.com/",
    # 13
    "http://www.independent.co.uk/arts-entertainment/music/news/brit-awards-amy-winehouse-nominated-for-british-female-solo-artist-four-years-after-her-death-a6813001.html",
    # 14
    "http://www.google.de/history/optout?hl=de",
    # 15
    "http://mil.huanqiu.com/china/2016-01/8377121.html",
    # 16
    "http://voice.hupu.com/soccer/1993099.html",
    # 17
    "http://blog.jp/",
    # 18
    "http://www.dailymail.co.uk/video/femail/video-1243576/The-quick-easy-way-peel-hard-boiled-egg.html",
    # 19
    "http://www.flickr.com/photos/jellyfire/23984358359/in/explore-2016-01-13/lightbox",
    # 20
    "http://www.google.se/",
    # 21
    "http://amazon.it/Brooks-Brothers-Saxxonn-Biella-Maglia/dp/B00YJ1GWZ8",
    # 22
    "http://www.snapdeal.com/products/musical-instruments-classical/filters/Type_s~Tabla?sort=plrty",
    # 23
    "http://product.auto.163.com/rank/lowPrice_paoche.html",
    # 24
    "http://www.oracle.com/us/support/software/premier/my-oracle-support-068523.html",
    # 25
    "http://dictionary.reference.com/slideshows/baby-animals",
    # 26
    "http://www.xfinity.com/",
    # 27
    "http://www.oracle.com/index.html",
    # 28
    "http://product.yesky.com/product/949/949664/param.shtml",
    # 29
    "http://shop.nordstrom.com/c/space?dept=8000001&origin=topnav",
    # 30
    "https://uk.news.yahoo.com/video/painter-no-fingers-creates-incredible-141025259.html",
    # 31
    "http://www.google.dz/",
    # 32
    "http://www.spiegel.de/reise/europa/",
    # 33
    "http://www.bitauto.com/zhuanti/8/bbspopularthemes/baoguang.shtml",
    # 34
    "http://cd.house.ifeng.com/sale/search/21057/_/_/0_184_0_0_0_0_0_0_0_0_0_0_0_0.shtml?keyword=_",
    # 35
    "https://watsons.world.tmall.com//watsons.tmall.com/category-669621742.htm?search=y&parentCatId=423860678&parentCatName=%CB%F9%D3%D0%C6%B7%C5%C6+ALL+Brands&catName=%C5%CB%E6%C3",
    # 36
    "http://car.bitauto.com/huabeijunfeng/",
    # 37
    "http://www.tudou.com/home/_520147384/",
    # 38
    "https://www.alipay.com",
    # 39
    "https://rewards.americanexpress.com/myca/loyalty/us/rewards/mracctmgmt/acctsumm?request_type=authreg_mr&Face=en_US&intlink=US-Homepage-MembershipRewards-NOJS",
    # 40
    "http://www.1905.com/vod/info/968423.shtml",
    # 41
    "http://www.ign.com/?setccpref=NO",
    # 42
    "http://gizmodo.com/",
    # 43
    "https://www.discover.com/credit-cards/compare/index.html",
    # 44
    "http://www.milliyet.com.tr/isid-uc-gun-yas-ilan-etti/dunya/detay/2179132/default.htm",
    # 45
    "http://www.tripadvisor.com/",
    # 46
    "http://www.google.es/advanced_search?hl=es&authuser=0",
    # 47
    "http://us.battle.net/en/",
    # 48
    "https://archive.org/details/audio",
    # 49
    "http://www.firmy.cz/?q=person%C3%A1ln%C3%AD+agentury",
    # 50
    "http://www.w3schools.com/",
    # 51
    "http://health.lady8844.com/946552/",
    # 52
    "http://www.bestbuy.com/",
    # 53
    "http://www.qq.com/",
    # 54
    "http://news.bitauto.com/sum/20140325/1706380317-3.html",
    # 55
    "http://pinterest.com/categories/kids/",
    # 56
    "http://bbs.lady8844.com/thread-1760932-1-1.html",
    # 57
    "http://www.shopclues.com/",
    # 58
    "https://ca.godaddy.com/site-map.aspx",
    # 59
    "http://www.google.com.sg/setprefs?sig=0_He38FLXKs_M8-9AlsEjDzHbAc3c%3D&hl=ta&source=homepage",
    # 60
    "https://kat.cr/blog/post/new-site-rules/",
    # 61
    "http://www.cnet.com/internet-speed-test/",
    # 62
    "http://japanpost.jp/",
    # 63
    "http://hdfcbank.com/",
    # 64
    "http://www.theladbible.com/",
    # 65
    "http://hupo.baike.com/",
    # 66
    "http://www.google.at/",
    # 67
    "https://www.rt.com//ruptly.tv/",
    # 68
    "http://minneapolis.about.com",
    # 69
    "http://www.google.com.tw/",
    # 70
    "http://www.ppomppu.co.kr/zboard/zboard.php?id=science",
    # 71
    "http://opinion.china.com.cn/event_4445_1.html",
    # 72
    "http://www.huffingtonpost.ca/british-columbia/",
    # 73
    "http://sports.gmw.cn/2016-01/14/content_18492735.htm",
    # 74
    "http://www.xe.com/ibancalculator/",
    # 75
    "http://gallery.artron.net/xuyuan/",
    # 76
    "http://www.asos.com/men/t-shirts/cat/pgecategory.aspx?cid=7616&via=top",
    # 77
    "http://tv.cntv.cn/videoset/C37717",
    # 78
    "http://www.reimageplus.com/support-partners/",
    # 79
    "https://www.etsy.com/teams/?ref=ftr",
    # 80
    "http://search.nicovideo.jp/video/search/",
    # 81
    "http://www.fedex.com/bb/",
    # 82
    "http://www.samsung.com/ca/support/category/cameracamcorder/camera/",
    # 83
    "http://news.goo.ne.jp/article/thetv/entertainment/thetv-70952.html",
    # 84
    "http://dmm.com/",
    # 85
    "http://www.google.de/",
    # 86
    "https://kat.cr/david-bowie-1973-07-03-london-england-sbd-flac-t11890210.html",
    # 87
    "http://shop374140507.kouclo.com/",
    # 88
    "http://www.vice.com/en_ca",
    # 89
    "http://zt.mama.cn/x2/index.php?p=au&c=mini",
    # 90
    "http://amazon.it/gp/prime?ie=UTF8&ref=BillBrd_Pr_Memb_Parm",
    # 91
    "http://blog.caijing.com.cn/expert_article-151316-69266.shtml",
    # 92
    "http://car.bitauto.com/guangqiriye/",
    # 93
    "http://www.nfl.com/voting/clutch-performer/2015/YEAR/0?module=HP11_content_stream_voting_gmc",
    # 94
    "http://www.macys.com/catalog/index.ognc?CategoryID=32144&cm_sp=intl_hdr-_-flytrackingbreadcrumb-_-32144_7-for-all-mankind_COL4",
    # 95
    "http://www.gap.com/profile/customer_value.do",
    # 96
    "http://news.163.com/photoview/00AO0001/108284.html",
    # 97
    "https://www.adcash.com/en/index.php",
    # 98
    "http://quotes.wsj.com/index/DJIA",
    # 99
    "http://hebei.ifeng.com/news/zbc/detail_2016_01/14/4740235_0.shtml",
    # 100
    "http://www.qq.com/icp.shtml",
    # 101
    "http://www.google.com.mx/",
    # 102
    "http://www.ebay.pl",
    # 103
    "http://www.softonic.com/",
    # 104
    "http://revista.zapimoveis.com.br/decoracao-de-quartos-dos-famosos-serve-de-inspiracao/",
    # 105
    "https://instagram.com/kohls/",
    # 106
    "https://www.etsy.com/c/craft-supplies-and-tools/patterns-and-tutorials/woodworking?ref=catnav-562",
    # 107
    "http://emotion.lady8844.com/lohas/2015-10-14/1696661.html",
    # 108
    "https://kat.cr/",
    # 109
    "http://jib.xywy.com/il_sii_1979.htm",
    # 110
    "http://www.reuters.com/news/oddlyEnough",
    # 111
    "http://gizmodo.com/the-la-gas-leak-is-scarier-than-we-thought-1752935526",
    # 112
    "http://us.playstation.com/support/protection-plan/",
    # 113
    "http://dc.yesky.com/459/99462459.shtml",
    # 114
    "http://www.sears.com/appliances-dishwashers/b-1020017",
    # 115
    "http://www.taipeitimes.com/",
    # 116
    "http://www.kohls.com/catalog/marc-anthony-clearance.jsp?CN=4294737585+4294736457&cc=clearance-TN2.0-S-marcanthony",
    # 117
    "http://www.tripadvisor.com/Hotels-g293974-Istanbul-Hotels.html",
    # 118
    "http://stackoverflow.com/",
    # 119
    "http://product.yesky.com/product/864/864914/",
    # 120
    "http://www.theguardian.com/football/tables",
    # 121
    "http://tieba.baidu.com/",
    # 122
    "http://v.qq.com/cover/7/7rk99b2lgnl9pse/d00199mj7eo.html",
    # 123
    "http://uae.souq.com/ae-en/suunto/fitness-technology-498/new/a-t-c/s/?sortby=sr",
    # 124
    "http://www.google.co.th/preferences?hl=th",
    # 125
    "http://www.oeeee.com/api/channel.php?s=/index/index/channel/sd",
    # 126
    "http://edmonton.craigslist.ca/",
    # 127
    "http://ettoday.net/social/latest-comments.htm",
    # 128
    "http://www.urdupoint.com/advertisement_urdu",
    # 129
    "http://www.reuters.com/article/us-indonesia-blast-idUSKCN0US0BS20160114",
    # 130
    "http://elpais.com/tag/salud/a/",
    # 131
    "http://www.avg.com/ca-en/partners-contactus",
    # 132
    "http://udn.com/news/story/5/1441122",
    # 133
    "http://www.kaskus.co.id/forum/173/?ref=homelanding&med=forum_categories",
    # 134
    "http://www.tmall.com//trade.taobao.com/trade/itemlist/list_bought_items.htm",
    # 135
    "http://www.google.com.ua/",
    # 136
    "http://bbs.hupu.com/acg",
    # 137
    "http://interview.gmw.cn/node_81312.htm",
    # 138
    "http://money.163.com/special/view619/",
    # 139
    "http://www.rottentomatoes.com/terms",
    # 140
    "http://extratorrent.cc/category/795/2+Broke+Girls+Torrents.html",
    # 141
    "http://www.sabah.com.tr/spor",
    # 142
    "http://money.163.com/16/0114/08/BD9BUSTM00252H36.html",
    # 143
    "http://www.weather.com/",
    # 144
    "http://www.accuweather.com/en/ca/scarborough/m1s/hourly-weather-forecast/55049",
    # 145
    "http://product.rakuten.co.jp/200162/",
    # 146
    "http://beian.cqwa.gov.cn/open/showRecord?id=50019950500075",
    # 147
    "http://www.gearbest.com/about/terms-and-conditions.html",
    # 148
    "https://www.etsy.com/c/toys-and-games/toys/wind-up-toys?ref=catnav-2961",
    # 149
    "http://cnnic.cn/",
    # 150
    "http://www.macys.com/catalog/index.ognc?CategoryID=55971&cm_sp=intl_hdr-_-flytrackingbreadcrumb-_-55971_home-decor_COL3",
    # 151
    "http://guilin.bitauto.com/",
    # 152
    "http://bbs.hupu.com/15240795.html",
    # 153
    "http://www.alibaba.com/catalogs/products/CID100006919",
    # 154
    "http://www.babytree.com/",
    # 155
    "http://beijing.china.org.cn/chinese/index.htm",
    # 156
    "http://ofsajd.onet.pl/",
    # 157
    "http://www.usatoday.com/",
    # 158
    "http://wordreference.com/",
    # 159
    "http://amazon.es/Rowenta-Air-Force-Extreme-Aspiradora/dp/B009ET1CUK",
    # 160
    "https://watsons.world.tmall.com//watsons.tmall.com/category-423842968.htm?search=y&parentCatId=423842967&parentCatName=Men%26%2339%3Bs+Grooming+%C4%D0%CA%BF%BB%A4%C0%ED&catName=Cleanser+%BD%E0%C3%E6",
    # 161
    "http://envios.mercadolivre.com.br/",
    # 162
    "https://watsons.world.tmall.com//watsons.tmall.com/category-1167522407.htm?search=y&catName=%C4%EA%C4%A9%B4%F3%C7%E5%B2%D6",
    # 163
    "http://www.zillow.com/mortgage-rates/wa/",
    # 164
    "http://www.xfinity.com/",
    # 165
    "http://www.douyutv.com/",
    # 166
    "http://www.google.com.ph/intl/en/services/",
    # 167
    "http://amazon.it/Brooks-Brothers-Saxxon-V-Neck-Biella/dp/B00YJ2KMI0",
    # 168
    "https://eksisozluk.com/",
    # 169
    "http://www.rakuten.co.jp/",
    # 170
    "http://ad8.adfarm1.adition.com/redi?sid=3088031&kid=1214230&bid=3966013",
    # 171
    "http://putlocker.is/genre/fantasy/1",
    # 172
    "http://www.google.com.pk/",
    # 173
    "http://www.twitch.tv//www.facebook.com/twitch",
    # 174
    "http://www.snapdeal.com/products/books-competitive-exams",
    # 175
    "http://www.indiatimes.com/",
    # 176
    "http://web.de/magazine/politik/fluechtlingskrise-in-europa/de-maiziere-gabriel-fluechtlingszuzug-spuerbar-reduzieren-31276926",
    # 177
    "http://www.homedepot.com/c/project_how_to",
    # 178
    "http://shop.deviantart.com",
    # 179
    "http://www.t-online.de/tv/tv-highlights/pro7sat1/id_76635566/ort-ist-nach-einem-kleidungstueck-benannt.html",
    # 180
    "https://www.playstation.com/en-ca/",
    # 181
    "https://www.irctc.co.in/eticketing/loginhome.jsf",
    # 182
    "http://kakaku.com/hikkoshi/",
    # 183
    "http://maps.google.fr/maps?hl=fr&tab=wl",
    # 184
    "http://mall.360.com/preorder/che?utm_source=guding_360guanwang _syproduct03_0804&utm_medium=inside",
    # 185
    "http://www.sabah.com.tr/cumartesi",
    # 186
    "http://code.google.com/intl/de/chrome/chromeframe/",
    # 187
    "http://amazon.de/Die-Tribute-von-Panem-Mockingjay/dp/B0182LRM22",
    # 188
    "http://guminba.17ok.com/fund/index/ba_display.php?pid=295606",
    # 189
    "http://www.milliyet.com.tr/yagli-sac-nasil-temiz-gorunur--pembenar-galeri-sacbakimi-2178784/",
    # 190
    "http://kakaku.com/",
    # 191
    "https://www.grouponworks.com/",
    # 192
    "http://twitter.com/intent/tweet?text=",
    # 193
    "http://www.amazon.in/b?_encoding=UTF8&node=8907206031",
    # 194
    "http://huanqiu.com/",
    # 195
    "http://extratorrent.cc/torrent_download/4645141/YouTube+Secrets+How+To+Make+%241%2C000%2B+Per+Month.torrent",
    # 196
    "http://beijing.bitauto.com/cheshi/shijingshanqu/",
    # 197
    "https://watsons.world.tmall.com/",
    # 198
    "http://www.kohls.com/catalog/entryway-and-mud-room-furniture-furniture-and-decor.jsp?CN=4294709983+4294719761+4294719779&cc=furniture-TN1.0-S-EntrywayFurniture",
    # 199
    "http://www.kinopoisk.ru/film/734349/",
    # 200
    "http://www.ltn.com.tw/",
    # 201
    "http://elpais.com/elpais/2016/01/14/inenglish/1452766827_378501.html",
    # 202
    "http://hf.yesky.com/",
    # 203
    "http://www.dailymail.co.uk/tvshowbiz/article-3396570/Pixie-Lott-Penelope-Pitstop-boyfriend-Oliver-Cheshire-dons-Scooby-Doo-costume-fancy-dress-birthday-party.html",
    # 204
    "http://oldman.39.net/a/160101/4751935.html",
    # 205
    "http://www.yeah.net/",
    # 206
    "http://www.novinky.cz/denni-tisk",
    # 207
    "http://www.macys.com/catalog/index.ognc?CategoryID=71123&cm_sp=intl_hdr-_-flytrackingbreadcrumb-_-71123_heels_COL1",
    # 208
    "http://web.de/magazine/politik/fluechtlingskrise-in-europa/altkanzler-gerhard-schroeder-kritisiert-angela-merkels-fluechtlingspolitik-31277002",
    # 209
    "http://www.google.no/",
    # 210
    "http://event.rakuten.co.jp/borderless/?scid=wi_jpn_footer_global_border",
    # 211
    "http://www.kaskus.co.id/forum/476/?ref=homelanding&med=forum_categories",
    # 212
    "http://www.zuhause.de/gartenkalender-welche-gartenarbeit-steht-wann-an-/id_61270508/index",
    # 213
    "http://www.wsj.com/articles/bhp-billitons-onshore-u-s-assets-hurt-by-downturn-in-energy-prices-1452811902",
    # 214
    "http://kdp.amazon.fr/",
    # 215
    "http://d.1905.com/space/8953224",
    # 216
    "http://cn.wsj.com/gb/index.asp",
    # 217
    "http://www.haosou.com?src=haosou.com",
    # 218
    "http://www.usatoday.com/news/politics/",
    # 219
    "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=12&ct=1452550905&rver=6.4.6456.0&wp=mbi_ssl_shared&wreply=https:%2f%2fmail.live.com%2fdefault.aspx%3frru%3dinbox&lc=1033&id=64855&mkt=en-us&cbcxt=mai",
    # 220
    "http://www.salesforce.com/platform/solutions/mobile/",
    # 221
    "http://sportdaten.t-online.de/fussball/infos/verein/fortuna-koeln/id_35_0_1751/",
    # 222
    "http://www.cnet.com/news/spacex-will-try-to-land-a-used-rocket-on-a-drone-barge-again-sunday/",
    # 223
    "http://wikia.com/",
    # 224
    "https://www.pixnet.net/",
    # 225
    "http://amazon.co.uk/",
    # 226
    "http://www.reuters.com/news/politics",
    # 227
    "http://gora.golf.rakuten.co.jp/",
    # 228
    "http://www.gamefaqs.com/boards/678050-final-fantasy-xiv-online-a-realm-reborn/73146654",
    # 229
    "http://putlocker.is/featured/1",
    # 230
    "http://car.bitauto.com/xuebaox80/",
    # 231
    "https://www.americanexpress.com/",
    # 232
    "https://adidas.world.tmall.com//adidas.tmall.com/category.htm?orderType=defaultSort&viewType=grid&catId=235127627&keyword=%D0%AC&scene=taobao_shop",
    # 233
    "http://www.tmall.com//mai.taobao.com/seller_admin.htm",
    # 234
    "http://amazon.es/Samsung-Galaxy-Tab-T-Shark2-Android/dp/B016DCF0RQ",
    # 235
    "http://www.dailymail.co.uk/tvshowbiz/article-3398362/Anybody-need-shops-Ellie-Goulding-jokes-skimpy-wardrobe-shows-gym-honed-figure-leather-leotard-tour-prep.html",
    # 236
    "http://youm7.com/",
    # 237
    "http://workathomemoms.about.com",
    # 238
    "http://jck.39.net/jiancha/wuli/fsxhs/4e9f4.html",
    # 239
    "http://store.steampowered.com/sub/79867/?snr=1_4_4__tab-Specials",
    # 240
    "http://www.super.cz/403964-anorekticku-s-29-kily-od-smrti-delily-hodiny-je-k-nevire-jak-se-dala-dohromady.html",
    # 241
    "http://news.china.com.cn/node_7184192.htm",
    # 242
    "http://www.shopclues.com/car-and-bike-accessories/car-accessories/car-spare-parts.html",
    # 243
    "http://www.shopclues.com/jewelry-and-watches/gold-store-special/gold-coins-8.html",
    # 244
    "http://stackoverflow.com/users",
    # 245
    "http://www.imdb.com/news/ns0000159?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1920909362&pf_rd_r=1JY4J1T5VXD1VBEY3CS8&pf_rd_s=center-3&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_nw_mv2_src",
    # 246
    "http://www.free.fr/adsl/index.html",
    # 247
    "http://www.fx120.net",
    # 248
    "https://watsons.world.tmall.com//watsons.tmall.com/category-1122785725.htm?search=y&parentCatId=1122785721&parentCatName=%D0%CD%C4%D0&catName=%E3%E5%D4%A1%C2%B6",
    # 249
    "http://www.tlbb8.com/",
    # 250
    "https://adidas.world.tmall.com//adidas.tmall.com/category-1146053974.htm?search=y&parentCatId=939733174&parentCatName=%D6%F7%CD%C6%CF%B5%C1%D0&catName=own+the+city",
    # 251
    "http://z.xywy.com/yiyuan-nfyy.htm",
    # 252
    "http://www.gsmarena.com/",
    # 253
    "http://www.naver.com/",
    # 254
    "http://www.google.com.br/",
    # 255
    "http://www.chinadaily.com.cn/index.html",
    # 256
    "http://film.onet.pl/kinga-preis-o-swojej-metamorfozie-odejscie-z-na-dobre-i-na-zle-flesz-filmowy/w03tn3",
    # 257
    "http://www.cnet.com/",
    # 258
    "http://www.kinopoisk.ru/photos/film/804666/",
    # 259
    "http://avito.ru/rossiya/zapchasti_i_aksessuary",
    # 260
    "http://uae.souq.com/ae-en/perfume/perfumes---and---fragrances-478/gucci/new/a-t-7-c/s/?page=1",
    # 261
    "http://mulher.uol.com.br/horoscopo/escorpiao/previsao-diaria/",
    # 262
    "http://bbs.zol.com.cn/diybbs/",
    # 263
    "http://foodnetwork.com/",
    # 264
    "http://www.uptodown.com/",
    # 265
    "http://21cn.com/",
    # 266
    "https://account.bilibili.com/login?act=exit",
    # 267
    "http://www.teepr.com/",
    # 268
    "http://www.kinopoisk.ru/tv/",
    # 269
    "http://www.yodobashi.com/%E3%82%B5%E3%82%A6%E3%83%B3%E3%83%89%E3%83%88%E3%83%A9%E3%83%83%E3%82%AF/ct/91226_216520000000000000/",
    # 270
    "http://slickdeals.net/",
    # 271
    "https://www.att.com/shop/wireless/accessories/accessorieslist.html",
    # 272
    "https://www.etsy.com/",
    # 273
    "http://opinion.udn.com",
    # 274
    "http://resume.naukri.com/resume-quality-score?fftid=101003",
    # 275
    "http://edu.qq.com/photo/",
    # 276
    "http://www.dailymail.co.uk/tvshowbiz/article-3396174/She-s-knockout-Creed-star-Tessa-Thompson-puts-leggy-display-thigh-high-split-gown-joins-Sylvester-Stallone-London-premiere.html",
    # 277
    "http://s.kouclo.com/search.php?c=4457,%E7%8E%B0%E4%BB%A3%E8%A3%85%E9%A5%B0%E7%94%BB",
    # 278
    "http://pinimg.com/",
    # 279
    "http://www.flipkart.com/",
    # 280
    "http://business.sohu.com/20160115/n434581721.shtml",
    # 281
    "http://www.pixiv.net/",
    # 282
    "http://www.booking.com/",
    # 283
    "http://onedio.com/is-dunyasi-haberleri",
    # 284
    "http://www.foxnews.com/travel/2016/01/14/turkey-ruffles-feathers-about-emotional-support-animals-on-flights/?intcmp=latestnews",
    # 285
    "http://www.ebay.co.uk",
    # 286
    "http://siteadvisor.com/",
    # 287
    "http://shop.nordstrom.com/c/sale?dept=8000001&origin=topnav",
    # 288
    "http://corporate.ancestry.com/careers/",
    # 289
    "http://liputan6.com/",
    # 290
    "http://news.bitauto.com/peixun/20160115/1706577825.html",
    # 291
    "http://www.t-online.de/",
    # 292
    "http://grants.nih.gov/grants/ElectronicReceipt/index.htm",
    # 293
    "http://rd.rakuten.co.jp/s/?R2=http%3A%2F%2Ftravel.rakuten.co.jp%2Fcoupon%2Fspecial%2Fshop%2F201512%2F%3Fscid%3Dwi_grp_gmx_trv_ich_top_grpcpn_onsencpn2015&D2=3.8611.68708.907371.32111361&C3=6bbdc11b02e189c2cdb7a98ed6d83518cb6002a3",
    # 294
    "http://www.mama.cn/z/559/",
    # 295
    "http://ettoday.net/news/20160114/630879.htm",
    # 296
    "https://ask.fm/",
    # 297
    "http://www.indeed.com/",
    # 298
    "http://www.laiwang.com/",
    # 299
    "http://about.ask.fm/blog/?lang=en",
    # 300
    "http://www.kohls.com/catalog/mens-accessories-accessories.jsp?CN=4294723349+4294719516+4294717956&cc=mens-TN1.0-S-accessoriesmore",
    # 301
    "http://sportdaten.t-online.de/fussball/infos/verein/fiorentina/id_35_0_125/",
    # 302
    "http://www.iqiyi.com/",
    # 303
    "http://www.1905.com/newgallery/hdpic/968112.shtml",
    # 304
    "http://4travel.jp/insurance/",
    # 305
    "http://v.china.com.cn/news/2016-01/14/content_37577039.htm",
    # 306
    "http://www.slideshare.net/login?from_source=%2FCEWGeorgetown%2Fcareer-clusters-forecasting-demand-for-high-school-through-college-jobs-20082018%3Ffrom_action%3Dsave&from=download&layout=foundation",
    # 307
    "http://www.xinhuanet.com/yuqing/2014/xbyqpx/zhuanti/02.htm",
    # 308
    "http://tabelog.com/kushiage/rank/",
    # 309
    "http://amazon.fr/JBL-Edition-Enceinte-portable-Bluetooth/dp/B01689TIP4",
    # 310
    "https://www.kickstarter.com/discover/categories/art?ref=home_featured",
    # 311
    "http://udn.com/news/index",
    # 312
    "http://jbk.39.net/byby/",
    # 313
    "http://www.indiatimes.com/news/sports/chris-lynn-almost-pulls-off-a-yuvraj-singh-smashes-5-sixes-in-an-over-in-big-bash-league-249454.html",
    # 314
    "http://redir.xuite.net/redir/xuite/www/index/log/photoBlock^http://photo.xuite.net/photo/19333626/853.jpg",
    # 315
    "http://bbs.hupu.com/15230793.html",
    # 316
    "http://uae.souq.com/ae-en/casio-men/watches-490/new/a-t-c/s/?sortby=sr&page=1",
    # 317
    "http://www.thesaurus.com/",
    # 318
    "http://i100.co.uk/?utm_source=indy&utm_medium=top5header&utm_campaign=i100",
    # 319
    "https://plus.google.com/u/0/112638281780859343687",
    # 320
    "http://auto.china.com/zhuanzai/daogou/11162371/20160114/21139610.html",
    # 321
    "https://www.capitalone.com/credit-cards/business/?Log=1&EventType=Link&ComponentType=T&LOB=MTS%3A%3AL0RT6ME8Z&PageName=Home+Page+Dynamic&ComponentName=primary_nav&ContentElement=b-br-2%3BSmall+Business+Credit+Cards&TargetLob=MTS%3A%3ALCTMMQC4S&TargetPageName=Spark+Business+Credit+Cards+%7C+Capital+&referer=https%3A%2F%2Fwww.capitalone.com%2Fhomepage-dynamic",
    # 322
    "http://www.yelp.co.uk/sf",
    # 323
    "http://www.gap.com/browse/home.do?cid=5058&mlink=39813,10323290,GFOL_MainNav_GOLHP,visnav&clink=10323290",
    # 324
    "http://glutenfreecooking.about.com",
    # 325
    "http://detail.zol.com.cn/digital_camera_index/subcate15_list_1.html",
    # 326
    "http://www.booking.com/region/gb/new-forest.html",
    # 327
    "http://www.fandango.com/13hours:thesecretsoldiersofbenghazi_185036/movieoverview",
    # 328
    "http://uyelikyonetim.hurriyet.com.tr/",
    # 329
    "http://www.google.com.pe/",
    # 330
    "http://www.xe.com/",
    # 331
    "http://mashable.com/2013/07/",
    # 332
    "http://www.about.com/",
    # 333
    "http://www.chip.de/",
    # 334
    "http://www.costco.com/hardware.html",
    # 335
    "http://domodi.pl/?utm_source=serwisy_WP&utm_medium=wp.pl&utm_campaign=nformatsg",
    # 336
    "http://www.kohls.com/",
    # 337
    "http://www.ebay.com.au/chp/Nail-Care-Polish-/47945",
    # 338
    "http://item.yhd.com/item/57430961?tp=222.32895_0.212.2_105.21.L7ONdWD-11-8jryB&ti=S5V4",
    # 339
    "http://money.17ok.com/news/441/2016/0114/2511127.html",
    # 340
    "http://detail.zol.com.cn/motherboard/maxsun/",
    # 341
    "http://appdirectory.hootsuite.com/",
    # 342
    "http://disease.39.net/a/160113/4757637.html",
    # 343
    "http://photo.accuweather.com",
    # 344
    "http://www.ancestry.com/",
    # 345
    "http://www.shopclues.com/fashion/pv-trendz-special.html",
    # 346
    "http://www.google.se/imghp?hl=sv&tab=wi",
    # 347
    "https://www.lowes.ca//www.lowes.ca/1/3/indexf1.html",
    # 348
    "http://tech.sina.com.cn/t/2016-01-14/doc-ifxnqrkc6360858.shtml",
    # 349
    "http://www.harpercollins.com/",
    # 350
    "http://www.1905.com/",
    # 351
    "http://www.eyny.com/video.php?mod=video&vid=1264159",
    # 352
    "http://car.bitauto.com/rely/",
    # 353
    "http://www.yaolan.com/",
    # 354
    "https://suche.web.de/newshp?src=hp_start",
    # 355
    "http://video.ltn.com.tw/",
    # 356
    "http://udn.com/news/cate/6644",
    # 357
    "http://business.comcast.com/triple-play-bundle",
    # 358
    "http://foodnetwork.com/",
    # 359
    "http://news.sina.com.cn/c/2016-01-14/doc-ifxnkvtn9957303.shtml",
    # 360
    "http://yqk.39.net/gxzzzzq/yaochang/69b89.html",
    # 361
    "https://www.seznam.cz/mobilni-aplikace/",
    # 362
    "http://www.iqiyi.com/a_19rrhb9b6p.html",
    # 363
    "http://www.marca.com/",
    # 364
    "http://bbs.hupu.com/15233740.html",
    # 365
    "http://f.iqiyi.com",
    # 366
    "http://elpais.com/autor/abril_mulato_salinas/a/",
    # 367
    "http://mens.tasclap.jp/a1126",
    # 368
    "https://www.dell.com/identity/v2/discovery?cht=login",
    # 369
    "http://my.ebay.co.uk/wishlistsearch",
    # 370
    "http://cd.house.ifeng.com/sale",
    # 371
    "http://www.google.com.co/",
    # 372
    "http://ph.priceprice.com/",
    # 373
    "http://pad.zol.com.cn/",
    # 374
    "http://www.bitauto.com/chaozhou/",
    # 375
    "http://kakaku.com/rexcard/?lid=rex_tb04",
    # 376
    "http://wunderground.com/",
    # 377
    "http://hotel.jd.com/",
    # 378
    "http://amazon.co.uk/Video-Games-Sony-14070-Bloodborne-PS4/dp/B00KL3WD2Y",
    # 379
    "http://educacao.uol.com.br/noticias/2016/01/14/sisu-tem-mais-de-25-milhoes-de-inscritos-sao-dez-candidatos-por-vaga.htm",
    # 380
    "http://www.naukri.com/tieups/tieups.php?othersrcp=14588",
    # 381
    "http://sabine62.deviantart.com/art/What-s-the-dIFS-Lifted-537940917",
    # 382
    "http://www.liveinternet.ru/users/3324853/profile/",
    # 383
    "http://blog.39.net/yuanxifuyz/a_16652572.html",
    # 384
    "http://www.speedtest.net/",
    # 385
    "http://www.kaskus.co.id/forum/633/?ref=homelanding&med=forum_categories",
    # 386
    "http://www.gearbest.com/",
    # 387
    "https://evernote.com/",
    # 388
    "http://www.nba.com/",
    # 389
    "http://espn.go.com/video/clip?id=14569527",
    # 390
    "http://www.icicibank.com/Personal-Banking/loans/loans.page?",
    # 391
    "http://www.kaskus.co.id/",
    # 392
    "http://www.shopclues.com/appliances-5/kitchen-appliances-5/chimney-and-hoods.html",
    # 393
    "http://stock.caijing.com.cn/20160114/4053702.shtml",
    # 394
    "http://www.google.co.id/",
    # 395
    "http://ettoday.net/news/20160114/630473.htm",
    # 396
    "http://open.163.com/movie/2011/10/R/A/M7GFK24P5_M7GHKMRRA.html",
    # 397
    "http://imgur.com/",
    # 398
    "http://lifehacker.com/",
    # 399
    "http://www.independent.co.uk/news/uk/home-news/uk-weather-ice-sleet-and-lows-of-8c-possible-as-arctic-air-blows-through-uk-a6808456.html",
    # 400
    "http://forum.china.com.cn/forum-146-1.html",
    # 401
    "http://www.rambler.ru/",
    # 402
    "http://www.urdupoint.com/",
    # 403
    "http://tabelog.com/rstLst/cond04-00-00/",
    # 404
    "https://www.chase.com",
    # 405
    "http://www.spiegel.de/schulspiegel/ausland/",
    # 406
    "http://elpais.com/internacional/2016/01/14/actualidad/1452740228_369263.html",
    # 407
    "http://www.foxnews.com/world/2016/01/14/massive-explosion-gunfire-heard-in-indonesian-capital-jakarta.html?intcmp=latestnews",
    # 408
    "http://www.tmall.com//chaoshi.tmall.com/paper/list.htm",
    # 409
    "http://www.ebay.com",
    # 410
    "http://auslogics-registry-cleaner.uptodown.com",
    # 411
    "http://www.spiegel.de/wirtschaft/service/versicherung-check-fuer-haftpflicht-hausrat-berufsunfaehigkeit-a-960380.html",
    # 412
    "http://www.deviantart.com/",
    # 413
    "http://www.naukri.com/tieups/tieups.php?othersrcp=14811",
    # 414
    "http://www.asos.com/discover/magazine/?ctaref=HP|gen|bottom|magazine",
    # 415
    "http://www.sina.com.cn/",
    # 416
    "http://www.reference.com/",
    # 417
    "http://www.kompas.com",
    # 418
    "http://www.mama.cn/z/1151/",
    # 419
    "http://www.caijing.com.cn/",
    # 420
    "http://desk.zol.com.cn/",
    # 421
    "http://fi.yelp.fi/sf",
    # 422
    "http://blog.caijing.com.cn/fuweigang",
    # 423
    "http://bbs.lady8844.com/zt/gkk17/",
    # 424
    "http://www.onclickads.net",
    # 425
    "http://ebates.com/",
    # 426
    "http://www.yodobashi.com/%E3%82%BB%E3%83%AB%E3%82%B9%E3%82%BF%E3%83%BC-AR-282GA-ASSURA-3-7%E3%82%A4%E3%83%B3%E3%83%81%E4%B8%80%E4%BD%93%E5%9E%8B%E3%83%AC%E3%83%BC%E3%83%80%E3%83%BC/pd/100000001002766047/",
    # 427
    "http://www.sc.xinhuanet.com/",
    # 428
    "http://pic.news.sohu.com/group-708375.shtml",
    # 429
    "http://count.shopping.t-online.de/RE?ID=76627312&CID=40576530&SI=64756648&TI=40867578&lg=1&URL=http%3A%2F%2Fwww.t-online.de%2Fshopping%2Fid_19374836%2Fexklusive-markenmode-und-designermode.html&SEC=z8hroj8oCDNIr0yCwu230g%3D%3D",
    # 430
    "http://www.yodobashi.com/ec/feature/470005/index.html",
    # 431
    "http://www.google.cz/",
    # 432
    "http://9gag.com/privacy",
    # 433
    "http://www.hurriyet.com.tr/her-30-saniyede-bir-kisi-diyabetten-bacagini-kaybediyor-40039948",
    # 434
    "http://www.fedex.com/sy/",
    # 435
    "http://www.yaolan.com/zhishi/dnfsdyfdyx/",
    # 436
    "http://www.slideshare.net/",
    # 437
    "https://slack.com/",
    # 438
    "https://www.etsy.com/c/accessories/belts-and-suspenders?ref=catnav-2938",
    # 439
    "https://aws.amazon.com/documentation/devicefarm/?icmpid=docs_menu",
    # 440
    "https://www.lowes.ca/account/subscriptionMgmt.aspx?coupon=yes",
    # 441
    "http://www.dailymail.co.uk/tvshowbiz/article-3400037/Liam-Hemsworth-showcases-comedic-talents-guest-appearance-Workaholics.html",
    # 442
    "http://jejuin.tistory.com/1764",
    # 443
    "https://www.bukalapak.com/c/kamera/cctv",
    # 444
    "http://www.sears.com/tvs-electronics-portable-audio-electronics-portable-audio-electronics-accessories-mp3-player-accessories-mp3-speakers-docks/b-1231480196",
    # 445
    "http://apps.chip.de/?utm_source=chiphomepage&utm_medium=footerteaser&utm_campaign=chipapps",
    # 446
    "https://www.bukalapak.com/rajawali_dedy123",
    # 447
    "http://www.ebay.de/itm/Candy-GCH-981-NA2T-Waschetrockner-8-KG-EEK-A-/252075294140?_trkparms=%26rpp_cid%3D51e728904708d64d754427de%26rpp_icid%3D51e727a01789bd84b1a00fe5&_trksid=p2057337.m2592&_trkparms=",
    # 448
    "http://conservativetribune.com/",
    # 449
    "http://slickdeals.net/coupons/buydig/",
    # 450
    "http://www.nba.com/playerfile/ricky_rubio/?ls=iref:nbahpstats",
    # 451
    "https://www.discover.com/",
    # 452
    "http://yyk.39.net/hospital/676b2_labs.html",
    # 453
    "http://photobucket.com/",
    # 454
    "http://torrentz.eu/torrentz.btsearch",
    # 455
    "https://ca.answers.yahoo.com/",
    # 456
    "http://netforbeginners.about.com/od/internet101/ss/The-Best-Search-Engines-of-2016.htm",
    # 457
    "http://www.google.com.eg/",
    # 458
    "http://www.shopclues.com/amour-engineered-wood-open-book-shelf.html",
    # 459
    "http://www.google.com.ar/preferences?hl=es-419",
    # 460
    "http://www.babytree.com/learn/specialtopic/diluchujun",
    # 461
    "http://nametests.com/",
    # 462
    "http://servicios.elpais.com/programacion-tv/",
    # 463
    "http://www.engadget.com/about/tips/",
    # 464
    "http://www.addthis.com/get/social",
    # 465
    "http://car.bitauto.com/oumake/",
    # 466
    "http://www.goodreads.com/genres/science-fiction",
    # 467
    "http://academia.stackexchange.com/users/35129/coderinnetwork",
    # 468
    "http://www.samsung.com/ca/support/category/pcperipheralsprinter/printer/",
    # 469
    "http://www.cbsinteractive.com/terms_of_use.php",
    # 470
    "http://www.dailymail.co.uk/tvshowbiz/article-3395526/David-Gest-kisses-Jeremy-McConnell-s-CBB.html",
    # 471
    "https://watsons.world.tmall.com//watsons.tmall.com/category-1122785377.htm?spm=a220o.1000855.w5842-12089783554.50.GCz73s&search=y&parentCatId=1122785358&parentCatName=%B2%CA%D7%B1&catName=%D1%DB%B2%BF%D7%B1%C8%DD",
    # 472
    "http://top.zol.com.cn/compositor/notebook.html",
    # 473
    "http://www.xywy.com/",
    # 474
    "https://www.mixer.cz/34/1766",
    # 475
    "http://extratorrent.cc/torrent_download/4644984/Panic+At+The+Disco-Death+Of+A+Bachelor+%282016%29.torrent",
    # 476
    "http://megapolitan.kompas.com/read/2016/01/14/11211971/Ledakan.Sarinah.Polisi.Sempat.Baku.Tembak.dengan.Beberapa.Orang?utm_source=WP&utm_medium=box&utm_campaign=Kpopwp",
    # 477
    "http://www.aliexpress.com/category/200002458/hair-care-styling.html?g=y",
    # 478
    "http://www.imdb.com/",
    # 479
    "http://sh.eastday.com/m/20160115/u1a9180547.html",
    # 480
    "http://www.kaskus.co.id/classified/328/?ref=homelanding&med=fjb_categories",
    # 481
    "http://extremesports.about.com",
    # 482
    "http://car.bitauto.com/leikesasies/",
    # 483
    "http://ogloszenia.wp.pl/motoryzacja",
    # 484
    "http://pic.yesky.com/98/99942598.shtml",
    # 485
    "http://kuchnia.wp.pl/kat,1038395,title,Pomysly-na-pulpety-w-kilku-odslonach,wid,18101910,wiadomosc.html",
    # 486
    "https://www.etsy.com/c/weddings/accessories/something-blue?ref=catnav-1633",
    # 487
    "http://big5.xinhuanet.com/gate/big5/www.news.cn/",
    # 488
    "https://vid.me/StefanBucher",
    # 489
    "http://car.bitauto.com/ounuo/",
    # 490
    "http://food.lady8844.com/142/",
    # 491
    "http://hangye.baike.com/?prd=shouye_hangyebaike",
    # 492
    "http://stackoverflow.com/questions/tagged/kvm",
    # 493
    "http://changsha.auto.sohu.com/20140102/n392737626.shtml/?pvid=e482cafb21d9ca99",
    # 494
    "http://www.weather.com/home-garden",
    # 495
    "http://www.tudou.com/list/ach3a-2b131c-2d-2e-2f-2g-2h-2i-2j-2k-2l-2m-2n-2sort2.html",
    # 496
    "http://www.snapdeal.com/",
    # 497
    "http://www.sears.com/en_us/dap/baby-basics.html",
    # 498
    "https://www.groupon.com/coupons/stores/nutrisystem.com",
    # 499
    "http://kidsparties.about.com",
    # 500
    "http://www.cntv.cn",
    # 501
    "http://extratorrent.cc/torrent_download/4645014/B.B.+King+-+Live+In+Cook+County+Jail+%282015%29+%5B24-96+HD+FLAC%5D.torrent",
    # 502
    "http://www.aliexpress.com/category/200000161/wedding-engagement-jewelry.html",
    # 503
    "http://elpais.com/deportes/2016/01/14/actualidad/1452810502_286240.html",
    # 504
    "http://transit.goo.ne.jp/",
    # 505
    "http://www.bbc.com/sport/cricket",
    # 506
    "http://ent.news.cn/mx.htm",
    # 507
    "http://rottentomatoes.com/",
    # 508
    "http://stock.17ok.com/news/815/2016/0114/2511276.html",
    # 509
    "http://www.tmall.com//chaoshi.tmall.com/activity/hub.htm?t=nianhuojie&acm=lb-zebra-24212-587641.1003.8.640809&scm=1003.8.lb-zebra-24212-587641.ITEM_145134336366715_640809",
    # 510
    "https://twitter.com/Independent",
    # 511
    "http://leaguepasssupport.nba.com/?ls=iref:nba:gnav",
    # 512
    "http://www.gap.com/browse/category.do?cid=6189",
    # 513
    "http://bbs.hupu.com/15239687.html",
    # 514
    "http://ettoday.net/news/20160114/630964.htm",
    # 515
    "http://www.att.com/esupport/main.jsp?cv=801&RIAConsoleLogLevel=4000&wtSlotClick=1-006XQP-0-3",
    # 516
    "http://www.spiegel.de/wirtschaft/zinsen-wie-fed-und-ezb-die-wirtschaft-beeinflussen-a-1067806.html",
    # 517
    "http://www.att.com/esupport/main.jsp?cv=808&RIAConsoleLogLevel=4000",
    # 518
    "http://comment.163.com/sports_bbs/BDADKP3P00051C8L.html?type=GTwww_NewsTie",
    # 519
    "http://bateria.about.com",
    # 520
    "https://accounts.google.com/servicelogin?service=blogger&hl=en_gb&passive=1209600&continue=https://www.blogger.com/home",
    # 521
    "http://foodnetwork.com/shows/cake-wars/photos/the-winning-creations-from-cake-wars-season-2.html",
    # 522
    "http://uae.souq.com/ae-en/michael-kors-everest-for-men-black-dial-silicone-band-watch-mk8365-7632162/i/",
    # 523
    "http://jbk.39.net/ynsz/",
    # 524
    "http://www.marca.com/deporte/central-de-datos/baloncesto/acb/calendario.html",
    # 525
    "http://www.huffingtonpost.ca/2016/01/14/kevin-oleary-conservative-leadership-race_n_8978852.html",
    # 526
    "http://www.cnews.ru/",
    # 527
    "http://ettoday.net/news/20160114/630911.htm",
    # 528
    "http://www.yodobashi.com/ec/store/0023/index.html",
    # 529
    "http://deadspin.com",
    # 530
    "https://archive.org/",
    # 531
    "http://www.teepr.com/category/%e8%97%9d%e8%a1%93/%e8%a8%ad%e8%a8%88/",
    # 532
    "https://yandex.ua/images/search?text=%D1%81%D0%B0%D0%B4%D0%BE%D0%B2%D0%B8%D0%B9%20%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD&source=images_garden",
    # 533
    "http://slide.tech.sina.com.cn/d/slide_5_453_66456.html",
    # 534
    "http://www.google.ca/",
    # 535
    "http://uae.souq.com/ae-en/swimwears/men/new/a-6356-c/l/?page=1",
    # 536
    "http://finance.southcn.com/",
    # 537
    "http://2ch.net/",
    # 538
    "https://wordpress.com/",
    # 539
    "http://amazon.fr/gp/bestsellers/electronics/14059601",
    # 540
    "http://eces.t-online.de/ati/mhit.php?kurl=https://www.telekom.de/hilfe/hilfe-bei-stoerungen&param_xtor=xto=AD-1068-[stoerungen-1507]-[telco-stagee]-[text]-[t-online.de]-[]-[71206152]",
    # 541
    "http://www.wikihow.com/main-page",
    # 542
    "http://wz.wen.oeeee.com/Content/204679.htm",
    # 543
    "http://travel.ettoday.net/article/629935.htm",
    # 544
    "http://ebates.com/stores/all/index.htm?navigation_id=22831",
    # 545
    "http://www.newegg.com/",
    # 546
    "https://www.tumblr.com/",
    # 547
    "http://gu.qq.com/sh000847",
    # 548
    "http://www.hurriyet.com.tr/",
    # 549
    "http://www.google.es/",
    # 550
    "http://notebook.yesky.com/116/99890116.shtml",
    # 551
    "http://yandex.ru/",
    # 552
    "http://www.google.ch/",
    # 553
    "http://job.goo.ne.jp/search/arbeit/spec26?rf=gtr167-33",
    # 554
    "http://amazon.ca/ASUS-C201-11-6-Chromebook-Rockchip/dp/B00VUV0MG0",
    # 555
    "http://www.tudou.com/albumplay/Qss__Gky9ts.html",
    # 556
    "http://tech.sina.com.cn/mobile/n/g/2016-01-14/doc-ifxnkkuy8005558.shtml",
    # 557
    "http://eces.t-online.de/ati/mhit.php?kurl=https://kundencenter.telekom.de/kundencenter/rechnung/&param_xtor=xto=AD-16-[rechnung-online-1507]-[telco-stage]-[text]-[t-online.de]-[]-[64531214]",
    # 558
    "http://www.about.com/education/",
    # 559
    "http://nasional.kompas.com",
    # 560
    "http://www.avg.com/ca-en/homepage",
    # 561
    "http://bbs.gmw.cn/thread-3494577-1-1.html",
    # 562
    "http://bleacherreport.com/",
    # 563
    "http://jiaxiao.jxedt.com",
    # 564
    "http://wulumuqi.zol.com.cn/",
    # 565
    "http://jobsearch.naukri.com/jobs-in-bangalore",
    # 566
    "http://www.xfinity.com/xfinity-vs-competition",
    # 567
    "http://shanghai.craigslist.com.cn",
    # 568
    "http://net.ce.cn/wz1/index.shtml",
    # 569
    "http://www.lady8844.com/topic/fashion/1726430.html",
    # 570
    "http://sfrom.net/http://youtube.com/watch?v=u7deClndzQw",
    # 571
    "http://www.shopclues.com/help.html",
    # 572
    "http://putlocker.is/genre/sci-fi/1",
    # 573
    "http://www.uptodown.com/buscar/router-keygen-para-windows-phone",
    # 574
    "http://www.milliyet.com.tr/",
    # 575
    "http://bkuma.hatena.ne.jp/",
    # 576
    "http://ok.ru/",
    # 577
    "http://blog.ce.cn/index.php/uid-617660-action-viewspace-itemid-1926524",
    # 578
    "http://www.money.pl/gospodarka/ngospodarka/ebiznes/artykul/t-mobile-polska-ukarane-przez-uokik-wazna,120,0,1997432.html",
    # 579
    "http://www.google.com.bd/",
    # 580
    "http://www.amazon.cn/gp/product-reviews/B00UW7QW8A",
    # 581
    "http://game.china.com/picnews/11128819/20160114/21139225.html",
    # 582
    "http://intl.target.com/",
    # 583
    "http://www.gap.com/browse/category.do?cid=1019160",
    # 584
    "http://www.gap.com/browse/category.do?cid=6437",
    # 585
    "https://adidas.world.tmall.com/",
    # 586
    "http://diply.com/",
    # 587
    "https://www.google.com/url?q=https://www.google.com/maps/%40-13.1650709,-72.5447154,3a,75y,352.16h,70.03t/data%3D!3m6!1e1!3m4!1smD4ThA4SthLifTAdt0lb4A!2e0!7i13312!8i6656&source=hpp&id=5083286&ct=3&usg=AFQjCNFf2GwpLom5gCAO3eo5JxzHjrWImQ",
    # 588
    "http://open.soft.360.cn/report.htm",
    # 589
    "https://www.discover.com/online-banking/cd/?ICMPGN=HDR_ALLPS_BANK_CD",
    # 590
    "http://www.xfinity.com/upgrade-center/customer-deals",
    # 591
    "http://sports.163.com/16/0114/15/BDA3C6DK00051C89.html",
    # 592
    "http://events.xiyou.cntv.cn/xcp/index.shtml?url=http://xiyou.cntv.cn/v-f272112c-b997-11e5-bcda-ecf4bbe6b3cc.html",
    # 593
    "http://www.macys.com/",
    # 594
    "http://edmonton.craigslist.ca//geo.craigslist.org/iso/kw",
    # 595
    "http://www.google.ie/setprefdomain?prefdom=US&sig=__0-iSqe4TpUxSikrh8UTr7ZQm3jw%3D",
    # 596
    "https://watsons.world.tmall.com//watsons.tmall.com/category-1122785766.htm?spm=a220o.1000855.w4010-6665696770.127.BQuHoq&search=y&parentCatId=1122785748&parentCatName=%BD%A1%BF%B5+%BB%A4%C0%ED&catName=%C9%ED%CC%E5%CD%E2%D3%C3%BB%A4%C0%ED",
    # 597
    "http://www.aliexpress.com/category/200000256/instruments.html",
    # 598
    "http://9gag.com/",
    # 599
    "https://www.groupon.com/coupons/stores/ae.com",
    # 600
    "http://uae.souq.com/ae-en/account_lists.php",
    # 601
    "http://totaltech.it?ref=libero&id=VTOTECH_921720",
    # 602
    "http://www.yodobashi.com/ec/store/0085/index.html",
    # 603
    "http://www.google.co.ve/",
    # 604
    "http://finance.china.com.cn/money/",
    # 605
    "http://amazon.fr/Sicario-steelbook-Benicio-Del-Toro/dp/B017TL763G",
    # 606
    "http://car.bitauto.com/shengdafei/",
    # 607
    "http://www.shopclues.com/wholesale/computers-19/laptops-19.html",
    # 608
    "http://liveadexchanger.com/",
    # 609
    "http://www.google.co.uk/",
    # 610
    "http://www.goodreads.com/user/show/51536104-ryley-balon",
    # 611
    "http://dating.independent.co.uk/?utm_source=dating&utm_campaign=dating&utm_term=independent",
    # 612
    "http://www.google.com.pe/intl/es-419/about.html",
    # 613
    "http://www.dailymail.co.uk/tvshowbiz/article-3395823/Charlotte-Crosby-shares-saucy-photo-posts-cheeky-belfie-Instagram-account.html",
    # 614
    "http://elpais.com/elpais/portada_america.html",
    # 615
    "http://finance.ifeng.com/mrztbfp/special/ztbfp160114/",
    # 616
    "http://www.ltn.com.tw/news/local/paper/949530",
    # 617
    "http://shop.nordstrom.com/c/space-handbags?dept=8000001&origin=topnav",
    # 618
    "http://www.chip.de/Tipps-Tools_13101526.html",
    # 619
    "http://www.alibaba.com/",
    # 620
    "http://car.bitauto.com/lingya-2422/",
    # 621
    "http://www.goodreads.com/user/show/4850141-vicki",
    # 622
    "http://www.news.cn/fashion/suxing2015.htm",
    # 623
    "http://www.daum.net/",
    # 624
    "http://www.1905.com/newgallery/list/c35.html",
    # 625
    "http://www.google.sk/",
    # 626
    "http://www.yaolan.com/zhishi/buruqikeyitangtoufama/",
    # 627
    "https://www.google.de/intl/de/options/",
    # 628
    "http://dmm.com/digital/-/basket/",
    # 629
    "http://web.de/",
    # 630
    "http://www.google.fi/",
    # 631
    "https://www.kickstarter.com/team?ref=footer",
    # 632
    "http://dc.yesky.com/4/99785504.shtml",
    # 633
    "http://www.espncricinfo.com/other/content/site/207463.html",
    # 634
    "https://adidas.world.tmall.com//adidas.tmall.com/category-939733174.htm?search=y&catName=%D6%F7%CD%C6%CF%B5%C1%D0",
    # 635
    "http://slickdeals.net/article/buying-guide/jewelry-buying-guide",
    # 636
    "http://www.ppomppu.co.kr/zboard/zboard.php?id=hobby",
    # 637
    "http://www.varzesh3.com/",
    # 638
    "http://www.bbc.co.uk/",
    # 639
    "http://www.huffingtonpost.com/2016/01/13/el-chapo-texts_n_8972852.html?ir=WorldPost",
    # 640
    "https://www.paypal.com/ca/webapps/mpp/home",
    # 641
    "http://money.17ok.com/list.php?id=592",
    # 642
    "https://support.office.com/article/What-s-new-in-Word-2016-4219dfb5-23fc-4853-95aa-b13a674a6670",
    # 643
    "http://www.google.co.za/setprefs?sig=0_17ixKmsb-ahjGqnDobKKXjJJf3c%3D&hl=tn&source=homepage",
    # 644
    "http://www.alibaba.com/catalogs/products/CID1715",
    # 645
    "http://redir.xuite.net/redir/xuite/www/index/log/photoBlock^http://photo.xuite.net/dong928/19727050/33.jpg",
    # 646
    "http://www.digitaltransformationlondon2016.com",
    # 647
    "http://www.google.com.sa/",
    # 648
    "https://www.rt.com/",
    # 649
    "http://stackexchange.com/",
    # 650
    "http://badoo.com/el/",
    # 651
    "http://bbs.oeeee.com/thread-17673936-1-1.html",
    # 652
    "http://d.1905.com/space/8497220",
    # 653
    "http://www.kohls.com/catalog/gaiam.jsp?CN=4294873092&cc=wms-TN2.0-S-gaiam",
    # 654
    "http://car.bitauto.com/maibahe57/",
    # 655
    "http://uae.souq.com/ae-en/polo-ralph-lauren-men/new/a-c/s/",
    # 656
    "http://siviaggia.it/viaggi/italia-viaggi/foto/itinerari-a-piedi-i-cammini-piu-belli-da-fare-in-italia/126158/",
    # 657
    "http://travel.china.com/happy/11167036/20160108/21102878.html",
    # 658
    "http://steamcommunity.com/",
    # 659
    "http://www.58188.com/",
    # 660
    "http://terraclicks.com/",
    # 661
    "http://g.csdn.net/5290943",
    # 662
    "http://www.zillow.com/browse/homes/nj/",
    # 663
    "http://www.mama.cn/z/1236/",
    # 664
    "http://opinion.huanqiu.com/special/wgyb2015/index.html",
    # 665
    "http://donghua.cntv.cn/2015/11/03/VIDA1446519432097398.shtml",
    # 666
    "http://discovery.163.com/",
    # 667
    "http://www.livejournal.com/",
    # 668
    "https://www.playstation.com/en-ca/explore/games/browse-games/",
    # 669
    "http://advertising.washingtonpost.com/index.php",
    # 670
    "http://sberbank.ru/ru/person",
    # 671
    "http://www.kohls.com/catalog/ncaa-sports-fan.jsp?CN=4294708148+4294718600&cc=sportsfan-TN2.0-S-ncaa",
    # 672
    "http://finance.caijing.com.cn/index.html",
    # 673
    "http://www.dailymail.co.uk/tvshowbiz/article-3399141/Danny-Dyer-admits-petrified-forthcoming-summer-nuptials-long-term-love-Joanne-Mas.html",
    # 674
    "http://hao123.com/",
    # 675
    "https://www.kickstarter.com/artbasel",
    # 676
    "http://www.yodobashi.com/ec/store/0081/index.html",
    # 677
    "http://china.com/",
    # 678
    "https://www.mediafire.com/",
    # 679
    "http://www.icicibank.com/stayconnected.page?",
    # 680
    "http://lady.163.com/special/womenview/",
    # 681
    "http://www.google.co.in/intl/en/policies/terms/",
    # 682
    "http://www.naukri.com/tieups/tieups.php?othersrcp=21256",
    # 683
    "http://bbs.hupu.com/15114713.html",
    # 684
    "http://baby.39.net/yeyp/yfnf/",
    # 685
    "http://drug.39.net/xjj/60/index.html",
    # 686
    "http://espn.go.com/esports/story/_/id/14551519/esports-having-moment",
    # 687
    "https://www.youtube.com/user/BroScienceLife",
    # 688
    "http://www.answers.com/page/businesssolutions",
    # 689
    "http://www.google.co.jp/",
    # 690
    "https://play.google.com/store/apps/details?id=com.mercadolibre&hl=pt_BR",
    # 691
    "http://bbs.cntv.cn/forum-31100-1.html",
    # 692
    "http://www.rediff.com/getahead/report/money-how-to-get-your-cibil-score-soar-high-this-makar-sankranti/20160114.htm",
    # 693
    "http://product.astro.sina.com.cn/?top=1009",
    # 694
    "http://business.chip.de/artikel/NEU-Das-CHIP-Software-Verzeichnis_57685093.html",
    # 695
    "http://www.zhihu.com/roundtable",
    # 696
    "http://www.dailymail.co.uk/news/article-3399646/He-really-wants-goats-Watch-astonishing-moment-farmer-uses-bare-hands-squeeze-two-animals-stomach-live-PYTHON.html",
    # 697
    "https://products.office.com/en-US/business/compare-office-365-for-business-plans",
    # 698
    "http://shop.goo.ne.jp/",
    # 699
    "http://ht.zol.com.cn/",
    # 700
    "http://news.livedoor.com/topics/detail/11065604/",
    # 701
    "http://www.caijing.com.cn/zhuantibaodao/index.shtml",
    # 702
    "https://www.capitalone.com/credit-cards/?Log=1&EventType=Link&ComponentType=T&LOB=MTS::L0RT6ME8Z&SubLob=&PageName=Home Page Dynamic&PortletLocation=5&ComponentName=footer&ComponentStrategy=&ContentElement=1%3BPersonal+Credit+Cards&TargetLob=MTS%3A%3ALCTMMQC4S&TargetPageName=Credit+Cards+Home&linkid=&email_delivery_id=&referer=https://www.capitalone.com/homepage-dynamic&external_id=&mediacode=",
    # 703
    "http://news.xywy.com/news/hyzx/2014/1110/735118.html",
    # 704
    "http://walmart.com/",
    # 705
    "http://qnife.deviantart.com/",
    # 706
    "http://www.indiatimes.com/news/sports/",
    # 707
    "http://www.tudou.com/list/",
    # 708
    "http://uae.souq.com/ae-en/slip-ons-or-lakee/casual---and---dress-shoes-481/skechers|cocos|rock|soludos|carolina-boix|class-man|ceyo|mel-by-melissa|response|san-marco|bata|dockers|garvalin|ramble|toms|bobell|adora|agatha-ruiz-de-la-prada|reflex|calvin-klein|comfy|convince|crocs|fabio-morello|k--shoes|zane|carrera|geox|lakee|lower-east-side|ryderwear|something-borrowed|timberland|zalora/flat|ballerinas|loafers|slip-ons/new/a-t-7-6453-c/s/",
    # 709
    "http://money.rbc.ru/",
    # 710
    "http://www.webmd.com/",
    # 711
    "http://www.chip.de/News_29559209.html?tid1=38715&tid2=0",
    # 712
    "http://www.google.com.ng/",
    # 713
    "http://uae.souq.com/ae-en/michael-kors-men-s-black-dial-stainless-steel-band-chronograph-watch-mk8316-6857559/i/",
    # 714
    "http://amazon.ca/OGIO-Ascent-Pack-International-Carry-On/dp/B00OPOO12K",
    # 715
    "http://www.addthis.com/contact",
    # 716
    "http://www.snapdeal.com/products/kids-footwear-girls?sort=plrty",
    # 717
    "http://www.onet.pl/",
    # 718
    "http://buzz.marca.com/?cid=MENUPROD35603&s_kw=marcabuzz",
    # 719
    "https://sports.bwin.es/es/sports?sb=1&wm=4420906&zoneId=1665790",
    # 720
    "http://news.eastday.com/c/20160115/u1a9180538.html",
    # 721
    "http://www.ppomppu.co.kr/zboard/zboard.php?id=china",
    # 722
    "http://www.cnn.com/2016/01/12/opinions/axelrod-debates-preview-desperation/index.html",
    # 723
    "http://wyleczto.wp.pl",
    # 724
    "http://car.bitauto.com/haifeng/",
    # 725
    "http://www.google.ru/",
    # 726
    "http://car.bitauto.com/612scaglietti/",
    # 727
    "http://cctv.cntv.cn/lm/dilizhongguo/index.shtml",
    # 728
    "http://www.sears.com//www.sears.com/shc/s/dealscenter?storeId=10153&fromLandingPage=true&WcUseHttps=true&catalogId=12605",
    # 729
    "http://www.google.ie/",
    # 730
    "http://history.huanqiu.com/china/2016-01/8381550.html",
    # 731
    "http://blog.csdn.net/mindfloating/article/details/49902867",
    # 732
    "https://www.pixnet.net//www.pixnet.net/regulation",
    # 733
    "http://www.booking.com/airport",
    # 734
    "http://detail.zol.com.cn/printer/ricoh/",
    # 735
    "http://mashable.com/lifestyle/",
    # 736
    "http://twitter.com/dictionarycom/",
    # 737
    "http://www.fedex.com/vc/",
    # 738
    "http://product.yesky.com/dv/sport/",
    # 739
    "https://www.youtube.com//www.youtube.com/yt/dev/",
    # 740
    "http://carro.mercadolivre.com.br/MLB-732981952-volkswagen-voyage-10-mi-8v-_JM",
    # 741
    "http://amazon.fr/Desigual-London-Sac-bandouli%C3%A8re-Carmin/dp/B00VCAW78K",
    # 742
    "http://www.snapdeal.com/products/laptop-skins?sort=plrty",
    # 743
    "http://rottentomatoes.com/m/norm_of_the_north/",
    # 744
    "http://www.detik.com//hot.detik.com",
    # 745
    "http://www.china.org.cn/chinese/china_key_words/index.htm",
    # 746
    "http://salesforce.com/ca/iot-cloud/",
    # 747
    "http://homebusiness.about.com",
    # 748
    "http://flickr.com/",
    # 749
    "https://wordpress.com/",
    # 750
    "http://www.yodobashi.com/%E3%82%AC%E3%83%BC%E3%83%87%E3%83%8B%E3%83%B3%E3%82%B0%E7%94%A8%E5%93%81/ct/72125_500000000000000211/",
    # 751
    "http://slickdeals.net/coupons/best-buy/",
    # 752
    "http://www.entwine-wines.com/",
    # 753
    "http://www.sears.com/clothing-shoes-jewelry-shoes-men-s-shoes-men-s-boots/b-1325057470",
    # 754
    "https://www.capitalone.com/about/?Log=1&EventType=Link&ComponentType=T&LOB=MTS::L0RT6ME8Z&SubLob=&PageName=Home Page Dynamic&PortletLocation=5&ComponentName=footer&ComponentStrategy=&ContentElement=12%3BAbout+Capital+One&TargetLob=MTS%3A%3ALCTMJBE8Z&TargetPageName=About+Capital+One&linkid=&email_delivery_id=&referer=https://www.capitalone.com/homepage-dynamic&external_id=&mediacode=",
    # 755
    "https://paytm.com/",
    # 756
    "http://www.ebay.in/usr/home.curator",
    # 757
    "http://world.taobao.com//world.taobao.com/search/search.htm?spm=a215z.1510359.a214x9l.7&_ksTS=1446622630103_35&search_type=0&_input_charset=utf-8&navigator=all&json=on&q=iphone6s%E6%89%8B%E6%9C%BA%E5%A3%B3&cna=aWCrDjq8ZFsCASp4Slwt8ZyI&callback=__jsonp_cb&abtest=_AB-LR854-PV854_2100",
    # 758
    "http://tabelog.com/",
    # 759
    "http://uyghur.news.cn/",
    # 760
    "http://sourceforge.net/blog/",
    # 761
    "http://g.csdn.net/5286443",
    # 762
    "http://amazon.de/The-Hateful-Blu-ray-Samuel-Jackson/dp/B019QBI62M",
    # 763
    "http://www.disneystore.com/toys/mn/1000208/?cmp=OTL-Dcom&att=GO_Toys",
    # 764
    "http://www.google.pt/",
    # 765
    "http://art.china.com/ywz11.html",
    # 766
    "http://www.apple.com/",
    # 767
    "http://www.xda-developers.com/xda-developers-privacy-policy/",
    # 768
    "http://www.yelp.com/c/sf/active",
    # 769
    "http://www.mama.cn/baby/art/20151119/778008.html",
    # 770
    "http://rd.nicovideo.jp/cc/nicotop_blomaga/userblmgarlist",
    # 771
    "http://mexicanfood.about.com",
    # 772
    "http://www.forbes.com/sites/janetnovack/",
    # 773
    "http://www.speedtest.net/results.php",
    # 774
    "http://udn.com/news/story/6885/1440890",
    # 775
    "http://oppnet.nih.gov/",
    # 776
    "http://www.zhihu.com/",
    # 777
    "http://amazon.com/Tide-Pods-Powder-Dash-Button/dp/B00WJ12MQ8",
    # 778
    "https://www.capitalone.com/",
    # 779
    "http://sportowefakty.wp.pl/la",
    # 780
    "http://bbs.zol.com.cn/dcbbs/d16_434270.html",
    # 781
    "http://www.homedepot.com/",
    # 782
    "http://www.enet.com.cn/",
    # 783
    "http://amazon.ca/25-Adele/dp/B00L98V4UW",
    # 784
    "http://www.milliyet.com.tr/evdeki-gundelikciye-100-tl-devlet/ekonomi/ydetay/2178490/default.htm",
    # 785
    "http://avito.ru/",
    # 786
    "http://mashable.com/",
    # 787
    "http://www.sabah.com.tr/spor/futbol/2016/01/14/atletico-madrid-ve-real-madride-transfer-yasagi",
    # 788
    "https://www.lowes.ca/articles/projects-diy-toolkit_a1019.html",
    # 789
    "http://lux.17ok.com/news/802/2016/0114/2511299.html",
    # 790
    "http://wen.oeeee.com/channel/5072.html",
    # 791
    "http://www.1905.com/mdb/film/1969420/",
    # 792
    "http://www.chip.de/news/Zum-Glueck-gezwungen-Danke-fuer-Windows-10-Microsoft_88202771.html",
    # 793
    "http://news.cntv.cn/2016/01/14/VIDEliqaIb2RqvBMIS62yRFC160114.shtml",
    # 794
    "http://www.booking.com/hostels/city/th/bangkok.html",
    # 795
    "http://www.voc.com.cn/",
    # 796
    "http://www.espncricinfo.com/ci/content/video_audio/index.html?genre=131",
    # 797
    "http://www.cnet.com/topics/internet/how-to/",
    # 798
    "http://ameblo.jp/",
    # 799
    "http://xinhuanet.com/",
    # 800
    "http://www.yahoo.co.jp/",
    # 801
    "http://www.milliyetemlak.com/uzman-soru-cevap?qid=7195",
    # 802
    "http://ent.china.com/star/news/11052670/20160114/21139702.html",
    # 803
    "http://www.foxnews.com/politics/2016/01/14/10-yemeni-detainees-sent-from-gitmo-to-oman-in-troubling-transfer.html?intcmp=latestnews",
    # 804
    "http://kinogo.co/5559-tretiy-lishniye-2-2015.html",
    # 805
    "http://www.speedtest.net/partner-with-ookla",
    # 806
    "http://www.asos.com/",
    # 807
    "http://www.maxima.fm/",
    # 808
    "http://www.dell.com/en-ca/",
    # 809
    "http://pinterest.com/categories/diy_crafts/",
    # 810
    "http://www.macys.com/shop/handbags-accessories/impulse-brands?id=53610&edge=hybrid&cm_sp=intl_hdr-_-flytrackingbreadcrumb-_-contemporary-handbags_COL1",
    # 811
    "http://i.baike.com/u/GdwFRBHZmVGRYYUR0/index",
    # 812
    "http://www.naukri.com/tieups/tieups.php?othersrcp=19825",
    # 813
    "http://www.adobe.com/ie/",
    # 814
    "http://life.ce.cn/",
    # 815
    "http://www.spiegel.de/wirtschaft/",
    # 816
    "https://www.etsy.com/c/vintage/clothing/womens-clothing/shorts-and-skorts?ref=catnav-2963",
    # 817
    "http://spasibosberbank.ru/actions/yarkoe-puteshestvie-ng-2016/",
    # 818
    "http://www.baike.com/",
    # 819
    "http://www.huffingtonpost.ca/",
    # 820
    "http://www.fun.tv/channel/500281",
    # 821
    "http://www.jabong.com/maybelline/",
    # 822
    "https://www.bukalapak.com/c/motor-471/outwear-motor",
    # 823
    "http://amazon.de/Fiskars-115560-Teleskop-Schneidgiraffe-Schwarz/dp/B0002TTRMQ",
    # 824
    "http://data.auto.qq.com/car_serial/1002/",
    # 825
    "https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://www.google.com.au/",
    # 826
    "https://www.washingtonpost.com/",
    # 827
    "http://www.ebay.de/rpp/tv-home-entertainment",
    # 828
    "http://www.shopclues.com/support",
    # 829
    "http://amazon.fr/",
    # 830
    "https://adidas.world.tmall.com//adidas.tmall.com/p/technology.htm?scene=taobao_shop",
    # 831
    "http://product.yesky.com/edict/",
    # 832
    "http://yyk.39.net/doctors/pifuke/",
    # 833
    "http://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fbv.ms%2F2020Hqs",
    # 834
    "https://secure.bankofamerica.com/login/enroll/entry/olbEnroll.go",
    # 835
    "http://widhawati.blogdetik.com/2016/01/14/netizen-hebohhastag-terkait-bom-sarinah-jakarta-bikin-rupiah-melemah",
    # 836
    "http://www.icicibank.com/Personal-Banking/offers/provogue-stay-trendy-offer.page?",
    # 837
    "http://support.xbox.com/browse/xbox-on-other-devices?xr=shellnav",
    # 838
    "http://www.gamefaqs.com/",
    # 839
    "http://www.360.com",
    # 840
    "http://eyny.com/",
    # 841
    "http://ekhanei.com/",
    # 842
    "http://column.caijing.com.cn/20141127/3759923.shtml",
    # 843
    "http://www.google.pt/intl/pt-PT/services/",
    # 844
    "http://www.firmy.cz/",
    # 845
    "http://www.youtube-mp3.org/",
    # 846
    "http://www.kohls.com/catalog/toys-episode-vii-the-force-awakens.jsp?CN=4294720971+4294696309&cc=toys-TN2.0-S-episodevii",
    # 847
    "http://www.google.co.jp/intl/ja/about.html",
    # 848
    "http://themeforest.net/follow_feed",
    # 849
    "http://www.thestar.com/authors.david_olive.html",
    # 850
    "http://jbk.39.net/sjs/ysbj/",
    # 851
    "http://www.snapdeal.com/products/girls-clothing",
    # 852
    "http://otomotif.liputan6.com/read/2411787/bom-jakarta-peluncuran-all-new-pajero-sport-belum-pasti",
    # 853
    "https://medium.com/",
    # 854
    "http://www.snapdeal.com/products/computers-laptops/?q=Type_s%3ATablet%20(2%20in%201)%7C&sort=plrty",
    # 855
    "http://www.sogou.com/?rfrom=soso",
    # 856
    "http://news.ifeng.com/a/20160115/47076816_0.shtml",
    # 857
    "http://www.leboncoin.fr/annonces/offres/provence_alpes_cote_d_azur/",
    # 858
    "http://www.nytimes.com/",
    # 859
    "http://pediatrics.about.com",
    # 860
    "http://gonewzealand.about.com",
    # 861
    "http://imbc.pixnet.net/blog/post/288638983-%e3%80%8e%e6%98%a5%e5%ad%a3%e8%b3%bd%e3%80%8fmsi%e6%9c%ab%e7%af%80%e7%88%86%e7%99%bc%ef%bc%8c%e5%be%8c%e9%80%9f%e8%b2%a2%e8%8b%a6%e8%bf%bd%e7%84%a1%e6%9e%9c",
    # 862
    "http://ypk.39.net/yaopin/jsjnfmyy/ydsjxty/7a8aa.html",
    # 863
    "http://www.nytimes.com/pages/magazine/index.html",
    # 864
    "http://www.dailymail.co.uk/video/news/video-1243887/Onlookers-film-explosion-central-Jakarta.html",
    # 865
    "http://www.nyaa.se/",
    # 866
    "http://cadde.milliyet.com.tr",
    # 867
    "http://news.china.com.cn/node_7232860.htm",
    # 868
    "https://www.groupon.com/coupons/stores/iolo.com",
    # 869
    "http://www.aliexpress.com/category/200000181/parking-assistance.html",
    # 870
    "http://resultados.elpais.com/mercados/indices/eurostoxx_50/1321/",
    # 871
    "http://salesforce.com/",
    # 872
    "http://detail.zol.com.cn/402/401594/pic.shtml",
    # 873
    "http://www.buzzfeed.com/business",
    # 874
    "http://www.flipkart.com/sunglasses/pr?p[]=facets.ideal_for[]=Boys&p[]=facets.ideal_for[]=Girls&sid=26x",
    # 875
    "http://www.google.co.in/",
    # 876
    "http://visualbasic.about.com",
    # 877
    "https://www.oracle.com/corporate/careers/index.html",
    # 878
    "http://extratorrent.cc/torrent/4644327/Kept.Woman.2015.HDRip.XviD.AC3-EVO.html",
    # 879
    "http://sannong.cntv.cn/2016/01/13/VIDEWVprgIQ2JNfY9ucxAeRq160113.shtml",
    # 880
    "http://www.mama.cn/",
    # 881
    "http://www.mama.cn/z/555/",
    # 882
    "http://www.yelp.com/",
    # 883
    "http://www.fedex.com/mv/",
    # 884
    "http://tupian.zol.com.cn/",
    # 885
    "http://www.techtudo.com.br/dicas-e-tutoriais/noticia/2016/01/colordrop-muda-cor-de-sites-como-google-e-o-facebook-colorido.html",
    # 886
    "http://detail.zol.com.cn/price_cate_10.html",
    # 887
    "http://v.youku.com/v_show/id_XOTY0NTA1MTY0.html",
    # 888
    "http://www.macys.com/catalog/index.ognc?CategoryID=69907&cm_sp=intl_hdr-_-flytrackingbreadcrumb-_-69907_thalia-sodi_COL3",
    # 889
    "https://watsons.world.tmall.com//watsons.tmall.com/category-1122785743.htm?search=y&parentCatId=1122785738&parentCatName=%BF%DA%C7%BB&catName=%B6%F9%CD%AF%D1%C0%B7%DB",
    # 890
    "http://www.google.ae/",
    # 891
    "http://douban.com/",
    # 892
    "http://miamidolphins.about.com",
    # 893
    "http://app.sina.com.cn/?f=p_binfen&w=p_binfen",
    # 894
    "http://www.salesforce.com/cn/",
    # 895
    "http://www.marca.com/baloncesto/nba/2016/01/14/5697799b22601dd3088b45aa.html",
    # 896
    "http://bbs.17ok.com/forum-2259-1.html",
    # 897
    "http://www.amazon.in/Fitbit-Wireless-Activity-Sleep-Tracker/dp/B0095PZHPE",
    # 898
    "http://amazon.com/gp/redirect.html?ie=UTF8&location=http%3A%2F%2Fwww.amazon.jobs%2Fgp%2Fredirect.html%3Flocation%3D%252F&source=standards&token=25117E9F01C8F0AB1D649F37EDDD2DEBE047C3A6",
    # 899
    "http://fuwu.sogou.com/product/jingjia/index.html?sohu=sohushangji",
    # 900
    "http://www.1688.com/",
    # 901
    "http://www.naukri.com/tieups/tieups.php?othersrcp=20204",
    # 902
    "http://moto.onet.pl/raporty/najbardziej-bezawaryjne-auta-z-rocznika-2004/vej14c",
    # 903
    "http://www.imdb.com/search?ref_=ft_sr",
    # 904
    "http://shop341140329.kouclo.com/index/index/1/all/all",
    # 905
    "http://www.naukri.com/tieups/tieups.php?othersrcp=20224",
    # 906
    "http://leboncoin.fr/",
    # 907
    "http://www.telegraph.co.uk/",
    # 908
    "http://www.bild.de/news/leserreporter/leserreporter/tierische-taeuschungen-39979610.bild.html",
    # 909
    "http://jbk.39.net/zq/shiliao/jbys/nfmst/",
    # 910
    "http://www.verizonwireless.com/",
    # 911
    "http://www.aliexpress.com/",
    # 912
    "http://www.xbox.com/en-ca/",
    # 913
    "http://extratorrent.cc/torrent/4645488/%5BRyuusei%5D+Clannad+After+Story+-+%28BDRip+1080p+x264+AAC+5.1%29+%5Brich_jc%5D.html",
    # 914
    "https://www.bukalapak.com/c/buku/parenting",
    # 915
    "https://www.wellsfargo.com/",
    # 916
    "http://www.costco.com/gasoline.html",
    # 917
    "http://www.xe.com/currency/usd-us-dollar",
    # 918
    "http://yandex.ua/",
    # 919
    "http://www.wikihow.com/wikiHow:Language-Projects",
    # 920
    "http://www.sabah.com.tr/galeri/yasam/hangi-ayda-ne-tuketilmeli",
    # 921
    "https://yabs.yandex.ua/count/4LWOiePL9mu40000gOA0ZhotWca5KPKAcm5jZeYvyY471wQ42Ogtq5Qq0we4fQRv1WMHlD19P0QJZmYYNqAkzi47QuPjKoa5iG6oe0000hlxjudqEzJYomJ1__________yFql__________3zF__________mzx3G00",
    # 922
    "http://pinterest.com/",
    # 923
    "http://credit.alibaba.com/buyer.htm",
    # 924
    "http://github.io/",
    # 925
    "http://car.bitauto.com/aodia3/",
    # 926
    "http://french.china.com/",
    # 927
    "http://www.fengjr.com/tuiguang/clean?c=pcfscjwzl",
    # 928
    "http://uae.souq.com/ae-en/diesel-men/eyewear-433%7Cwatches-490%7Chandbags-472%7Ctops-488%7Caccessories-466%7Cwallets-533%7Ccasual---and---dress-shoes-481%7Cpants-477%7Cslippers-485/new/a-t-c/s/?sortby=sr&page=1",
    # 929
    "http://www.sears.com/kids-clothing-boys-clothing-boys-suits-dresswear/b-1282030444",
    # 930
    "http://amazon.es/",
    # 931
    "http://www.alimama.com/",
    # 932
    "https://www.bukalapak.com/hourglass",
    # 933
    "http://www.tudou.com/listplay/tMozKHU0WX4/rqYFLKvDyXc.html",
    # 934
    "http://wunderground.com/marine-weather/",
    # 935
    "https://www.groupon.com/",
    # 936
    "https://www.etsy.com/c/vintage/toys-and-games/sports-and-outdoor-games?ref=catnav-2963",
    # 937
    "http://www.urdupoint.com/technology/detail/mobile-and-gadgets/three-new-smartphones-introduced-by-sharp-2164.html",
    # 938
    "http://z.xywy.com/zhuanye-erke.htm",
    # 939
    "https://watsons.world.tmall.com//watsons.tmall.com/category-423839221.htm?search=y&parentCatId=423839218&parentCatName=Skincare+%BB%A4%B7%F4&catName=Exfoliating+%BD%C7%D6%CA%BB%A4%C0%ED",
    # 940
    "http://www.yodobashi.com/%E6%9D%B1%E8%8A%9D-TOSHIBA-SD-WD032G-SDHC%E3%83%A1%E3%83%A2%E3%83%AA%E3%82%AB%E3%83%BC%E3%83%89-32GB-FlashAir-CLASS10-W-02/pd/100000001001941110/",
    # 941
    "http://www.personalmarkt.de/source-links/spiegel/serviceangebotebox.html",
    # 942
    "http://www.bild.de/",
    # 943
    "http://www.nyaa.se/?cats=2_12",
    # 944
    "https://ss.knet.cn/verifyseal.dll?sn=e13073044010041807hcer000000&ct=df&a=1&pa=0.9170622944366187",
    # 945
    "http://casavogue.globo.com/",
    # 946
    "https://aws.amazon.com/marketplace/pp/B00EQE493U/ref=mkt_ste_l2_Backup_f2?nc2=h_l3_bsa",
    # 947
    "http://et.21cn.com/star/pic/a/2016/0113/16/30482871.shtml?flag=true",
    # 948
    "http://www.xe.com/currencycharts/?from=GBP&to=USD",
    # 949
    "http://www.google.com.ph/",
    # 950
    "http://netadreg.gzaic.gov.cn/ntmm/WebSear/WebLogoPub.aspx?logo=440108108022006041100041",
    # 951
    "http://www.lasapuestasdeas.com",
    # 952
    "http://extratorrent.cc/",
    # 953
    "http://www.engadget.com/2016/01/14/darpa-photon-project/",
    # 954
    "http://kanasoku.info/articles/79528.html",
    # 955
    "http://youm7.com/%D8%AD%D9%88%D8%A7%D8%AF%D8%AB-203",
    # 956
    "http://www.kohls.com/catalog/clearance-kids.jsp?CN=4294736457+4294732649&cc=kids-TN1.0-S-kidsclearance",
    # 957
    "http://jiangsu.china.com.cn/",
    # 958
    "http://www.detik.com/",
    # 959
    "http://www.shopclues.com/sunday-flea-market.html",
    # 960
    "http://s.kouclo.com/search.php?c=2778,%E5%85%B6%E5%AE%83",
    # 961
    "http://www.macys.com/catalog/index.ognc?CategoryID=8380&cm_sp=intl_hdr-_-flytrackingbreadcrumb-_-8380_waterford_COL2",
    # 962
    "http://www.ppomppu.co.kr/zboard/zboard.php?id=market_phone",
    # 963
    "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn",
    # 964
    "http://www.slideshare.net/CEWGeorgetown",
    # 965
    "https://www.kickstarter.com/discover/places/orlando-fl?ref=city",
    # 966
    "http://cba.hupu.com/",
    # 967
    "http://mailchimp.com/",
    # 968
    "https://www.capitalone.com/legal/terms-conditions/?Log=1&EventType=Link&ComponentType=T&LOB=MTS::L0RT6ME8Z&SubLob=&PageName=Home Page Dynamic&PortletLocation=5&ComponentName=footer&ComponentStrategy=&ContentElement=31%3BTerms+%26+Conditions&TargetLob=MTS%3A%3ALCTMJBE8Z&TargetPageName=Terms+and+Conditions&linkid=&email_delivery_id=&referer=https://www.capitalone.com/homepage-dynamic&external_id=&mediacode=",
    # 969
    "http://dmm.co.jp/",
    # 970
    "http://www.sears.com/home-improvement-bathroom/b-1270630373",
    # 971
    "http://www.directrev.com/",
    # 972
    "http://www.amazon.cn/",
    # 973
    "http://yuehui.163.com/searchphoto.do?from=wsdh",
    # 974
    "http://www.alibaba.com/catalogs/products/CID282901",
    # 975
    "http://ent.ltn.com.tw/news/breakingnews/1572713",
    # 976
    "http://www.mama.cn/z/967/",
    # 977
    "http://tech.huanqiu.com/diginews/2016-01/8379300.html",
    # 978
    "http://kouclo.com/help/index/14",
    # 979
    "http://web.de/magazine/unterhaltung/lifestyle/miss-internet/",
    # 980
    "http://www.bitauto.com/",
    # 981
    "http://www.jabong.com/online-sale/",
    # 982
    "http://uae.souq.com/ae-en/receiver-amplifier/l/?rpp=48&amp;sortby=",
    # 983
    "http://www.chinadaily.com.cn/",
    # 984
    "http://shop.nordstrom.com/",
    # 985
    "http://m.vk.com/",
    # 986
    "https://www.ups.com/",
    # 987
    "https://www.oracle.com/applications/customer-experience/sales/roles/index.html",
    # 988
    "http://www.google.pl/",
    # 989
    "https://kat.cr/user/figer/",
    # 990
    "http://jib.xywy.com/il_sii_77.htm",
    # 991
    "http://www.foxnews.com/",
    # 992
    "https://www.doubleclickbygoogle.com//services.google.com/fb/forms/revenuemanagementen/",
    # 993
    "http://www.kaskus.co.id/forum/579/?ref=homelanding&med=forum_categories",
    # 994
    "http://www.alibaba.com/catalogs/products/CID100000300",
    # 995
    "http://stackoverflow.com/questions/tagged/angularjs-scope",
    # 996
    "http://product.yesky.com/product/875/875383/price.shtml",
    # 997
    "http://doublepimp.com/",
    # 998
    "http://www.google.co.za/",
    # 999
    "http://badoo.com/install/?ref=web-direct-footer&d=WindowsPhone",
    # 1000
    "http://photo.xuite.net/photo/18673846",
    # 1001
    "http://gouwu.360.cn/",
    # 1002
    "https://www.adobe.com/products/photoshop-lightroom.html?promoid=KLXLX",
    # 1003
    "http://www.youtube-mp3.org/jp",
    # 1004
    "http://ca.ign.com/",
    # 1005
    "https://uk.news.yahoo.com/video/modern-caveman-man-builds-230-122622275.html",
    # 1006
    "http://www.macys.com/catalog/index.ognc?CategoryID=63913&cm_sp=intl_hdr-_-flytrackingbreadcrumb-_-63913_michael-kors_COL3",
    # 1007
    "http://www.kohls.com/catalog/womens-athletic-shoes-sneakers-shoes.jsp?CN=4294720878+4294711897+4294719777&cc=wms-TN2.0-S-athleticshoes",
    # 1008
    "http://www.audible.com/",
    # 1009
    "http://data.auto.qq.com/car_serial/103/",
    # 1010
    "http://shop.nordstrom.com/c/jewelry?dept=8000001&origin=topnav",
    # 1011
    "http://www.taoche.com/aodiq5-2855/",
    # 1012
    "http://xl415.com/",
    # 1013
    "http://www.snapdeal.com/products/jewelry-bangles-bracelets?sort=plrty",
    # 1014
    "http://product.yesky.com/product/773/773915/param.shtml",
    # 1015
    "https://www.bankofamerica.com/",
    # 1016
    "http://www.rediff.com/getahead/slide-show/slide-show-1-specials-festivals-in-pics-how-rural-tamil-nadu-celebrates-pongal/20140114.htm",
    # 1017
    "http://tvpot.daum.net",
    # 1018
    "http://ad8.adfarm1.adition.com/redi?sid=3076396&kid=1503404&bid=5108800",
    # 1019
    "http://www.t-online.de/unterhaltung/partnersuche/",
    # 1020
    "http://www.webmd.com/parenting/default.htm",
    # 1021
    "http://www.flipkart.com/panasonic-th-32c350dx-81-cm-32-led-tv/p/itmecek5bfyrqfyt?pid=TVSECEK5GXGRMKVY",
    # 1022
    "https://adidas.world.tmall.com//adidas.tmall.com/category.htm?orderType=defaultSort&viewType=grid&keyword=%C5%DC%B2%BD&scene=taobao_shop",
    # 1023
    "https://aws.amazon.com/tools/?nc2=h_mo",
    # 1024
    "http://vod.pl/filmy-i-bajki-dla-dzieci",
    # 1025
    "http://news.china.com.cn/node_7226521.htm",
    # 1026
    "http://hd.mama.cn/sz/detail/4117405",
    # 1027
    "https://www.taboola.com/",
    # 1028
    "http://technowinki.onet.pl/windows-10-czy-darmowa-aktualizacja-zmotywowala-was-do-instalacji/g2qex8",
    # 1029
    "https://login.microsoftonline.com/",
    # 1030
    "http://www.sympatiaplus.pl/glowna/ikona?utm_source=onet.pl&utm_medium=banner&utm_campaign=ikona",
    # 1031
    "http://www.adobe.com//www.adobe.com/privacy.html",
    # 1032
    "http://www.baike.com/shouye/xukezheng/wangluowenhua.html",
    # 1033
    "http://www.milliyet.com.tr/gundem",
    # 1034
    "http://www.360.com/",
    # 1035
    "http://mens.tasclap.jp/a1105",
    # 1036
    "https://www.instagram.com/",
    # 1037
    "http://top.51.la/se.htm",
    # 1038
    "http://www.ikea.com/ca/en/",
    # 1039
    "http://encruceros.about.com",
    # 1040
    "http://www.yodobashi.com/ec/promotion/newtopics/detail/10000000000000033471/index.html",
    # 1041
    "http://likes.com/art/10-pallet-projects-you-re-going-to-want-to-try-this-spring-summer",
    # 1042
    "http://shop296140221.kouclo.com/",
    # 1043
    "http://www.shopclues.com/home-garden/kitchen-en/kitchen-essentials.html",
    # 1044
    "http://gshow.globo.com/programas/programa-do-jo/",
    # 1045
    "http://sberbank.ru/ru/person/pensioner/get?utm_source=mainp4_2",
    # 1046
    "http://sportdaten.t-online.de/fussball/uefa-europa-league/2015-2016/spiel-bilanz/spieltag-7/id_33_0_27078_839798/",
    # 1047
    "http://www.bbc.com/",
    # 1048
    "http://daily.urdupoint.com/livenews/2016-01-14/news-572110.html",
    # 1049
    "http://japanpost.jp/ir/stock/index02.html",
    # 1050
    "https://pasangmata.detik.com/contribution/189155",
    # 1051
    "http://www.nfl.com/news/author?id=09000d5d82036444",
    # 1052
    "http://shop.nordstrom.com/c/womens-swimsuits-shop?dept=8000001&origin=topnav",
    # 1053
    "http://resume.naukri.com/job-alerts-on-mobile-mail?fftid=101011",
    # 1054
    "https://wordpress.org/",
    # 1055
    "http://www.ce.cn/cysc/fdc/",
    # 1056
    "http://www.answers.com/",
    # 1057
    "http://www.1905.com/mdb/film/2229392/prevue/",
    # 1058
    "http://amazon.ca/gp/help/customer/display.html?ie=UTF8&nodeId=915404",
    # 1059
    "http://www.tmall.com//pages.tmall.com/wow/act/15303/jkbjnh2016?acm=lb-zebra-24212-587641.1003.8.640809&scm=1003.8.lb-zebra-24212-587641.ITEM_14513456721595_640809",
    # 1060
    "http://www.mama.cn/z/1102/",
    # 1061
    "http://www.costco.com/",
    # 1062
    "http://www.google.com.sg/",
    # 1063
    "http://sberbank.ru/ru/person/bank_inshure/insuranceprogram/life/accident",
    # 1064
    "http://www.yesky.com/",
    # 1065
    "http://tech.huanqiu.com/diginews/2016-01/8379308.html",
    # 1066
    "http://aws.amazon.com/workmail/?hp=tile",
    # 1067
    "http://foodnetwork.com/topics/whiskey.html",
    # 1068
    "http://war.163.com/photoview/4T8E0001/108250.html",
    # 1069
    "http://media.tumblr.com/",
    # 1070
    "http://link.1905.com/link/?&fr=wwwhome_sryywindow_4.0&redirect_url=http%3A%2F%2Fdownpay.m1905.cn%2Fpc%2Fsoft%2F4.0.3%2FM1905-Player19050000.exe",
    # 1071
    "http://www.tudou.com/albumplay/fQV_ahPQu5A/rkvzxIznnG4.html",
    # 1072
    "http://www.forbes.com/home_usa/",
    # 1073
    "http://news.nandu.com/media/",
    # 1074
    "http://tangshan.auto.sohu.com/20140102/n392740391.shtml?pvid=e482cafb21d9ca99",
    # 1075
    "http://pages.ebay.in/help/confidence/overview.html",
    # 1076
    "http://onedio.com/haber/real-madrid-ve-atletico-madrid-e-2-donem-transfer-yasagi-658989",
    # 1077
    "http://ftpd.youth.cn/",
    # 1078
    "http://ecredit.alibaba.com/ecl/buyer.htm?tracelog=beacon_credit_140704",
    # 1079
    "http://www.sears.com/tools-tool-storage-tool-chest-combos/b-1025212",
    # 1080
    "http://www.cntv.cn/special/guanyunew/PAGE13818868795101872/index.shtml",
    # 1081
    "http://www.ce.cn/cysc/ny",
    # 1082
    "http://www.yaolan.com/birth/",
    # 1083
    "https://www.doubleclickbygoogle.com/",
    # 1084
    "http://www.sears.com/clothing-shoes-jewelry-shoes-men-s-shoes-men-s-casual-shoes/b-1325057492",
    # 1085
    "http://photo.hupu.com/nba/p26736.html",
    # 1086
    "http://www.hm.com/ca/subdepartment/LADIES?Nr=4294866545",
    # 1087
    "http://uae.souq.com/ae-en/philips-hp-8103-salon-dry-compact-4864620/i/",
    # 1088
    "https://news.yandex.ru/yandsearch?cl4url=ria.ru/culture/20160114/1359772489.html&lang=ru&lr=20806",
    # 1089
    "http://livingrooms.about.com",
    # 1090
    "http://www.sabah.com.tr/",
    # 1091
    "http://car.bitauto.com/sanlingpajieluo/tupian/",
    # 1092
    "http://www.naukri.com/tieups/tieups.php?othersrcp=14741",
    # 1093
    "https://www.mozilla.org/en-us/",
    # 1094
    "http://finance.17ok.com/list.php?id=2050",
    # 1095
    "http://www.forbes.com/video/4516437683001/",
    # 1096
    "http://sh.house.ifeng.com/pic/2016_01/14/38871402_0.shtml",
    # 1097
    "http://www.orange.fr/",
    # 1098
    "http://www.wsj.com/articles/arizona-mansion-aims-for-record-35-million-price-1452788968",
    # 1099
    "http://likes.com/",
    # 1100
    "http://www.bitauto.com/puer/",
    # 1101
    "http://amazon.it/gp/help/customer/display.html?ie=UTF8&nodeId=200522630",
    # 1102
    "http://rd.da.netease.com/redirect?t=75z7vH&p=ByiZoO&proId=1024&target=http%3A%2F%2Fwww.kaola.com",
    # 1103
    "http://www.snapdeal.com/products/bags-clutches?sort=plrty",
    # 1104
    "https://www.discover.com/credit-cards/index.html?ICMPGN=HDR_ALLPS_CC_ALL",
    # 1105
    "http://www.yaolan.com/zhishi/shqzysx/",
    # 1106
    "http://www.39.net/",
    # 1107
    "http://www.gap.com/",
    # 1108
    "http://dl.360safe.com/instmobilemgr.exe",
    # 1109
    "http://www.sears.com/",
    # 1110
    "https://www.etsy.com/c/electronics-and-accessories/video-games?ref=catnav-2961",
    # 1111
    "https://eksisozluk.com/basliklar/populer",
    # 1112
    "http://edu.qq.com/a/20160114/010668.htm",
    # 1113
    "http://www.hupu.com/",
    # 1114
    "http://dcdv.zol.com.cn/",
    # 1115
    "http://daily.urdupoint.com/livenews/2016-01-14/news-572408.html",
    # 1116
    "http://blog.sina.com.cn/s/blog_48b3b0120102x3ii.html?tj=fina",
    # 1117
    "http://ent.ltn.com.tw/news/breakingnews/1572698",
    # 1118
    "https://aws.amazon.com/marketplace/pp/B00N44P7L6/ref=mkt_ste_l2_hls_f3?nc2=h_l3_hl",
    # 1119
    "http://car.bitauto.com/surui/",
    # 1120
    "http://ent.v.sina.cn/show/vMPWwBKR~z3QAtvzswdBuQ__.htm",
    # 1121
    "http://car.bitauto.com/sangtana/",
    # 1122
    "http://produto.mercadolivre.com.br/MLB-732610245-lampada-quente-cermica-e14-3w-bivol-1-lote-com-5-unidades-_JM",
    # 1123
    "https://www.pixnet.net/",
    # 1124
    "http://www.kohls.com/catalog/teen-guys-tops-clothing.jsp?CN=4294718789+4294719805+4294719810&cc=mens-TN2.0-S-ymshirtstees",
    # 1125
    "http://www.wix.com/",
    # 1126
    "http://licaishi.sina.com.cn/web/planList?s=2&rs=0&d=0&o=c_r&ow=1&fr=stock_top",
    # 1127
    "http://global.rakuten.com/zh-cn/?scid=wi_jpn_footer_global_cn",
    # 1128
    "http://baa.bitauto.com/polo/thread-3488845.html",
    # 1129
    "https://kat.cr/request/",
    # 1130
    "https://eksisozluk.com/istatistik",
    # 1131
    "http://blog.sina.com.cn/lm/pic/",
    # 1132
    "http://www.youth.cn/",
    # 1133
    "http://www.tudou.com/home/xiaohuoban/",
    # 1134
    "http://jbk.39.net/yxmc/shengwuyixue/rstz",
    # 1135
    "http://oshiete.goo.ne.jp/watch/introduction/ffc1e22380ee79c7e73a052c243b3f1e?from=osw_gootop",
    # 1136
    "http://money.17ok.com/list.php?id=435",
    # 1137
    "http://finance.haiwainet.cn/",
    # 1138
    "http://www.sohu.com/",
    # 1139
    "http://dining.rakuten.co.jp/",
    # 1140
    "http://car.bitauto.com/jiayumpv/",
    # 1141
    "https://twitter.com/",
    # 1142
    "http://book.sina.com.cn/news/a/2016-01-13/0924787884.shtml",
    # 1143
    "http://uae.souq.com/ae-en/tops/women/levi\'s%7Creflex%7Credtag%7Clacoste%7Cyellow-fashion%7Cdina-zaki%7Cralph-lauren%7Cmng%7Cguess%7Cwal-g%7Clois%7Cd-muse-by-dressberry/new/a-6356-7-c/l/?page=1",
    # 1144
    "http://www.news.cn/house/sh/zt/140901_youyhz/index.html",
    # 1145
    "http://corp.rakuten.co.jp/",
    # 1146
    "http://www.kohls.com/catalog/nfl-denver-broncos-sports-fan.jsp?CN=4294708579+4294708467+4294718600&cc=sportsfan-TN2.0-S-denverbroncos",
    # 1147
    "http://popcash.net/",
    # 1148
    "https://online.citi.com/us/welcome.c",
    # 1149
    "http://cnzz.com/",
    # 1150
    "http://www.milliyet.com.tr/hamile-kalmak-icin-ne-siklikta-pembenar-galeri-hamilelikhazirligi-2158446/",
    # 1151
    "http://www.hd315.gov.cn/beian/view.asp?bianhao=010202001021500016",
    # 1152
    "http://www.t-online.de/spiele/id_76510004/imperial-island-2-und-mehr-download-spiele-kostenlos-herunterladen-bei-t-online-de.html",
    # 1153
    "http://aws.amazon.com/resources/gartner-2015-mq-learn-more/?trkCampaign=global_2015_ar_gartner_mq&trk=ha_ar_gartner_mq_1041",
    # 1154
    "http://eastday.com/",
    # 1155
    "http://art.china.com/zhuanti/",
    # 1156
    "http://www.answers.com/Q/FAQ/388",
    # 1157
    "http://www.dmm.com/lod/rod/",
    # 1158
    "http://www.spiegel.de/forum/sport/bericht-von-anti-doping-kaempfern-korruption-gehoert-jetzt-offiziell-zur-leichtathletik-thread-406561-1.html",
    # 1159
    "http://cctv.cntv.cn/lm/daodeguancha/index.shtml",
    # 1160
    "http://www.yodobashi.com/%E3%83%A9%E3%82%A4%E3%82%BB%E3%83%B3%E3%82%B9%E3%82%BD%E3%83%95%E3%83%88/ct/59001_500000000000000201/",
    # 1161
    "http://www.mama.cn/z/293/",
    # 1162
    "http://uae.souq.com/ae-en/printer-or-scanner-or-printer-and-scanner-accessories/printers-192%7Cscanners-89%7Cprinter-and-scanner-accessories-85/a-t/s/?rpp=48&amp;sortby=",
    # 1163
    "http://www.liputan6.com/tag/bandara-hasanuddin",
    # 1164
    "http://shop.nordstrom.com/c/sale-beauty?dept=8000001&origin=topnav",
    # 1165
    "http://yangsheng.gmw.cn/2016-01/14/content_18483900.htm",
    # 1166
    "http://apk.angeeks.com",
    # 1167
    "http://www.chip.de/bestenlisten/Bestenliste-Externe-Festplatten-3-5-Zoll--index/index/id/372/",
    # 1168
    "http://gouk.about.com",
    # 1169
    "http://www.yodobashi.com/",
    # 1170
    "https://www.onlinesbi.com/",
    # 1171
    "http://stackoverflow.com/users/875317/b-clay-shannon",
    # 1172
    "http://www.1905.com/mdb/film/2088579/",
    # 1173
    "http://www.profitmagazine-digital.com/profitmagazine_open/OWSE2015?pg=1",
    # 1174
    "http://www.google.co.kr/",
    # 1175
    "http://bet365.com/",
    # 1176
    "http://book.sohu.com/s2015/wikou/",
    # 1177
    "http://uae.souq.com/ae-en/smart-watch/watches-490%7Cmobile-phone-accessories-26%7Csmart-watches-511%7Cmobile-phones-33%7Cfitness-technology-498/new/a-t-c/s/?page=1",
    # 1178
    "http://www.snapdeal.com/products/stationery-school-supplies?sort=plrty",
    # 1179
    "http://amazon.de/Bresser-Funkwetterstation-Temeo-schwarz-Version/dp/B00LGIFEE2",
    # 1180
    "http://www.engadget.com/advertise",
    # 1181
    "http://www.dailymail.co.uk/tvshowbiz/article-3399160/Celebrity-Big-Brother-s-Tiffany-Pollard-struggles-reach-boiling-point-tries-reform-ways-house.html",
    # 1182
    "http://news.sohu.com/s2016/dianji-1790/index.shtml",
    # 1183
    "http://feedly.com/",
    # 1184
    "http://en.savefrom.net/faq.php",
    # 1185
    "https://www.facebook.com/?_rdr",
    # 1186
    "http://tag.babytree.com/",
    # 1187
    "http://daily.urdupoint.com/livenews/2016-01-14/news-572224.html",
    # 1188
    "http://www.salesforce.com/platform/products/force/?d=70130000000f27v",
    # 1189
    "http://plus.girlspic.jp/",
    # 1190
    "http://car.bitauto.com/xinejishuangmenjiaopaoche/",
    # 1191
    "https://www.etsy.com/c/bags-and-purses/luggage-and-travel/luggage-tags?ref=catnav-2938",
    # 1192
    "http://car.bitauto.com/hanmajiachangban/",
    # 1193
    "http://power.yesky.com/c/3780_15905.shtml",
    # 1194
    "http://lifehacker.com/journey-is-a-journal-app-with-photo-support-and-calenda-1752893314",
    # 1195
    "http://detail.zol.com.cn/air-condition/mitsubshi/",
    # 1196
    "http://www.espncricinfo.com/south-africa-v-england-2015-16/content/story/962147.html",
    # 1197
    "https://www.taboola.com/resources",
    # 1198
    "https://ca.auctions.godaddy.com/trppricing.aspx",
    # 1199
    "http://entertainment.kompas.com",
    # 1200
    "http://www.buzzfeed.com/post?id=4123032",
    # 1201
    "https://www.dropbox.com/",
    # 1202
    "https://produkte.web.de/verivox/strom/",
    # 1203
    "https://www.mint.com/",
    # 1204
    "http://politics.caijing.com.cn/20160115/4054434.shtml",
    # 1205
    "http://ppomppu.co.kr/zboard/view.php?id=car&no=489967",
    # 1206
    "http://www.amazon.co.uk/b/?node=8670626031&ref=ve_track_rw_footer",
    # 1207
    "http://shutterstock.com/",
    # 1208
    "https://watsons.world.tmall.com//watsons.tmall.com/category-1141958377.htm?search=y&parentCatId=1122785379&parentCatName=%C3%C0%D7%B1%B9%A4%BE%DF&catName=%C7%FC%B3%BC%CA%CF%B9%A4%BE%DF",
    # 1209
    "http://www.marca.com/olimpismo.html",
    # 1210
    "http://www.chinadaily.com.cn/world/middle_east.html",
    # 1211
    "http://www.aliexpress.com/category/200002295/led-panel-lights.html",
    # 1212
    "http://www.engadget.com/about/editors/nathan-ingraham",
    # 1213
    "https://play.google.com/store/apps/details?id=com.globalegrow.app.gearbest",
    # 1214
    "http://amazon.com/gp/bestsellers/electronics/281052",
    # 1215
    "http://amazon.ca/",
    # 1216
    "https://www.bukalapak.com/",
    # 1217
    "http://www.olx.in/",
    # 1218
    "http://photo.gmw.cn/2016-01/04/content_18342869.htm",
    # 1219
    "http://amazon.de/",
    # 1220
    "http://www.cnn.com/",
    # 1221
    "https://www.capitalone.com/",
    # 1222
    "http://www.hp.com/",
    # 1223
    "http://photobucket.com/auth/twitter/start?callback_type=login&display=popup&mobile=",
    # 1224
    "http://www.dailymotion.com/ca-en",
    # 1225
    "http://www.asos.com/infopages/pgeshiptocountry.aspx?CTARef=HP|gen|middle|freeship",
    # 1226
    "http://extratorrent.cc/category/101/Naruto+Torrents.html",
    # 1227
    "http://uae.souq.com/ae-en/",
    # 1228
    "http://www.nicovideo.jp/",
    # 1229
    "https://www.youtube.com/",
    # 1230
    "http://www.milliyet.com.tr/ask-yeniden-38-yeni-bolum-gundem-2178176/",
    # 1231
    "http://mst.zol.com.cn/563/5635847.html",
    # 1232
    "http://weather.yahoo.co.jp/weather/",
    # 1233
    "http://goo.ne.jp/",
    # 1234
    "http://military.china.com.cn/node_7207693.htm",
    # 1235
    "http://www.google.com.tr/",
    # 1236
    "http://vimeo.com/ondemand/bunnythemovie",
    # 1237
    "http://sports.news.naver.com/videoCenter/index.nhn?uCategory=kbasketball&category=&listType=total&date=20160114&gameId=&teamCode=&playerId=&keyword=&id=171963&page=1",
    # 1238
    "http://ettoday.net/",
    # 1239
    "http://wsj.com/",
    # 1240
    "http://www.cnet.com/topics/tablets/how-to/",
    # 1241
    "http://www.reimageplus.com/",
    # 1242
    "http://sp.oshiete.goo.ne.jp/",
    # 1243
    "https://www.mystart.com/",
    # 1244
    "http://car.bitauto.com/jincouxingche/",
    # 1245
    "http://channel.jd.com/food.html",
    # 1246
    "http://amazon.de/Gardena-3101-20-cs-Rechenbesen-43-breit/dp/B0001E3VFQ",
    # 1247
    "https://commons.era.nih.gov/commons/",
    # 1248
    "http://www.amazon.in/Fastrack-Watches/b?ie=UTF8&node=4371849031",
    # 1249
    "http://www.macys.com/catalog/index.ognc?CategoryID=28001&cm_sp=intl_hdr-_-flytrackingbreadcrumb-_-28001_wear-to-work_COL1",
    # 1250
    "http://www.asd.tv/",
    # 1251
    "http://www.twitch.tv/",
    # 1252
    "http://jx.ifeng.com/a/20160114/4192621_0.shtml",
    # 1253
    "http://www.ebay.in/cln/sukaina_7389/Lap-it-up/266105110013",
    # 1254
    "http://bbs.lady8844.com/thread-1744166-1-1.html",
    # 1255
    "http://www.kinopoisk.ru/",
    # 1256
    "http://mobile.zol.com.cn/549/5496564.html",
    # 1257
    "http://ent.cntv.cn/special/zgmgqz/",
    # 1258
    "https://www.wikimedia.org//species.wikimedia.org/",
    # 1259
    "http://bbs.yaolan.com/",
    # 1260
    "http://www.wp.pl/",
    # 1261
    "http://sports.sina.com.cn/g/laliga/2016-01-14/doc-ifxnrahr8292867.shtml",
    # 1262
    "http://city.china.com/pic/11146172/20160114/21138608.html",
    # 1263
    "http://culture.gmw.cn/2016-01/14/content_18487603.htm",
    # 1264
    "http://gfycat.com/",
    # 1265
    "http://shop.nordstrom.com/c/bucket-bags?dept=8000001&origin=topnav",
    # 1266
    "http://oshiete.goo.ne.jp/qa/9153610.html",
    # 1267
    "http://so.lianmeng.360.cn/",
    # 1268
    "http://www.snapdeal.com/products/lifestyle-watches",
    # 1269
    "http://www.lady8844.com/",
    # 1270
    "http://www.google.com.pk/intl/en/ads/",
    # 1271
    "http://man.39.net/a/160112/4756532.html",
    # 1272
    "http://www.google.cl/",
    # 1273
    "http://www.amazon.cn/careers",
    # 1274
    "http://tv.yesky.com/276/99912776.shtml",
    # 1275
    "http://www.google.fr/",
    # 1276
    "http://fk.39.net/lc/",
    # 1277
    "http://i.baike.com/myRole.do?action=apply",
    # 1278
    "http://store.steampowered.com/",
    # 1279
    "http://cafeyte.about.com",
    # 1280
    "http://www.goodreads.com/",
    # 1281
    "http://onedio.com/haber/88-oscar-adaylari-aciklandi-mustang-yabanci-dilde-en-iyi-film-dalinda-aday--659045",
    # 1282
    "http://auto.sina.com.cn/service/2016-01-13/detail-ifxnkkux1265305.shtml?c=spr_web_sina_cnxh_auto_t0002",
    # 1283
    "http://www.ebay.com.au/",
    # 1284
    "http://www.libero.it/",
    # 1285
    "http://www.liveinternet.ru/",
    # 1286
    "http://www.ifeng.com/",
    # 1287
    "http://uae.souq.com/ae-en/lighting-or-lamps-or-chandeliers/garden-lighting-122%7Chome-decor-137%7Clamps---and---lightings-503/koopman%7Cbaby-zoo%7Cnsgt%7Cevidea/a-t-7/s/?sortby=cp_desc&page=2",
    # 1288
    "http://menshair.about.com",
    # 1289
    "http://www.goal.com/",
    # 1290
    "http://www.google.az/",
    # 1291
    "http://www.huffingtonpost.ca/news/home-decor-canada",
    # 1292
    "https://www.shopify.ca/",
    # 1293
    "https://www.whatsapp.com/press/",
    # 1294
    "http://www.dailymail.co.uk/news/article-3399833/Hatton-Garden-masterminds-caught-police-talking-raid.html",
    # 1295
    "http://amazon.co.uk/gp/bestsellers/electronics/560836",
    # 1296
    "http://ask.zol.com.cn/q/1556394.html",
    # 1297
    "http://www.snapdeal.com/products/food-noodles-soups-pasta",
    # 1298
    "http://military.china.com/",
    # 1299
    "http://very8879576.pixnet.net/blog/post/424682411",
    # 1300
    "http://sourceforge.net/",
    # 1301
    "http://cm.39.net/a/160113/4756490.html",
    # 1302
    "http://www.nytimes.com/content/help/rights/sale/terms-of-sale.html",
    # 1303
    "http://www.olx.in/item/eleven-months-old-balckberry-q5-for-seven-thousand-only-ID11r57p.html",
    # 1304
    "http://abbotsford.craigslist.ca/",
    # 1305
    "http://www.bloomberg.com/",
    # 1306
    "http://combate.globo.com/",
    # 1307
    "http://amazon.es/cookiesypublicidadeninternet",
    # 1308
    "http://www.impress.co.jp/",
    # 1309
    "http://www.google.be/",
    # 1310
    "http://www.booking.com/index.bg.html?bb_ltbi=0;sb_price_type=total&;lang=bg",
    # 1311
    "http://www.webmd.com/click?url=http://www.emedicinehealth.com/script/main/hp.asp",
    # 1312
    "http://adf.ly/",
    # 1313
    "http://www.adobe.com/",
    # 1314
    "http://car.bitauto.com/changanxiaoka/",
    # 1315
    "http://cctv.cntv.cn/lm/xinwendiaocha/index.shtml",
    # 1316
    "http://www.elpais.com/especial/clasificacion-colegios-madrid/",
    # 1317
    "http://www.t-online.de/wirtschaft/unternehmen/id_76644348/wirtschaft-aufsichtsratschef-mirow-hsh-nordbank-ist-eine-wettbewerbsfaehige-bank.html",
    # 1318
    "https://www.spotify.com/ca-en/",
    # 1319
    "http://detail.zol.com.cn/cell_phone/index1100891.shtml",
    # 1320
    "https://www.quora.com/",
    # 1321
    "http://redir.xuite.net/redir/xuite/www/index/log/daFunShowP^http://photo.xuite.net/_pic/ichiro0910/19743330/1111339391.jpg/redir",
    # 1322
    "https://ca.yahoo.com/?p=us",
    # 1323
    "https://www.facebook.com/",
    # 1324
    "http://www.milliyet.com.tr/mola-galeri-detay/misir-piramitlerinin-en-ilginc-9-ozelligi---/715/",
    # 1325
    "https://instagram.com/jabongindia/",
    # 1326
    "http://detail.zol.com.cn/digital_camera_index/subcate15_657_list_1.html",
    # 1327
    "http://www.dailymail.co.uk/video/news/video-1229387/Khloe-Kardashian-strips-raunchy-photo-shoot.html",
    # 1328
    "http://bbs.lady8844.com/zt/gkk14/",
    # 1329
    "http://news.nicovideo.jp/watch/nw1986410?news_ref=nicotop_topics_soft",
    # 1330
    "http://customer.xfinity.com/help-and-support",
    # 1331
    "http://amazon.it/",
    # 1332
    "http://vid.me/",
    # 1333
    "http://www.hatena.ne.jp/",
    # 1334
    "http://activity.bilibili.com",
    # 1335
    "http://www.ameba.jp/",
    # 1336
    "http://www.hurriyet.com.tr/yoldurumu/istanbul/",
    # 1337
    "http://yuedu.163.com/book_reader/f42523f43ba34722b2cf64ec99e9dd9d_4/e9bae95f834349b1a1041b24dc1c980f_4?utm_campaign=163ad&utm_source=163home&utm_medium=tab_0_3_6",
    # 1338
    "http://arte.about.com",
    # 1339
    "http://finance.oeeee.com/html/201601/12/356584.html",
    # 1340
    "http://www.mercadolivre.com.br/",
    # 1341
    "https://pinpoint.microsoft.com/en-ca",
    # 1342
    "http://www.facebook.com/dialog/share?app_id=132746074315&display=popup&href=http%3A%2F%2Fwww.engadget.com%2F2015%2F10%2F08%2Fnasa-finds-that-pluto-has-blue-skies-and-surface-water-ice%2F",
    # 1343
    "http://www.naukri.com/tieups/tieups.php?othersrcp=17636",
    # 1344
    "http://www.lenovo.com//shop.lenovo.com/ca/en/landingpage/announcements/",
    # 1345
    "http://www.fandango.com/",
    # 1346
    "http://agency.reuters.com",
    # 1347
    "http://www.alibaba.com/",
    # 1348
    "http://iservice.ltn.com.tw/Service/english/english.php?engno=931351&day=2015-11-11",
    # 1349
    "http://www.tudou.com/albumplay/TpIXNUU7Z5s/qD26a3lr7Fw.html",
    # 1350
    "http://sh.eastday.com/m/20160114/u1ai9179812.html",
    # 1351
    "http://www.hurriyet.com.tr/rusya-sultanahmet-saldirisiyla-baglantili-o-ismi-acikladi-haydar-suleymanov-40040530",
    # 1352
    "http://news.xywy.com/news/jrzd/20131211/733051.html",
    # 1353
    "http://www.bild.de/news/standards/nikolaus-blome/zu-frueh-fuer-grenz-schliessung-44155912.bild.html",
    # 1354
    "http://www.yaolan.com/zhishi/ertongjinshi/",
    # 1355
    "https://chaseonline.chase.com/",
    # 1356
    "https://developer.vimeo.com",
    # 1357
    "http://uae.souq.com/ae-en/hasbro/toys-24%7Cbaby-toys-and-accessories-335/hasbro/new/a-t-7-c/s/?sortby=ir_desc&page=1",
    # 1358
    "http://www.chip.de/preisvergleich/438425/LG-Electronics-49UF7787.html",
    # 1359
    "https://www.wellsfargo.com/goals-going-to-college/",
    # 1360
    "http://www.yesky.com/sitemap.shtml",
    # 1361
    "http://collection.sina.com.cn/yjjj/2016-01-14/doc-ifxnqriy2842198.shtml",
    # 1362
    "http://www.independent.co.uk/",
    # 1363
    "https://www.sogou.com/",
    # 1364
    "https://www.seznam.cz/",
    # 1365
    "https://www.linkedin.com/",
    # 1366
    "https://www.etsy.com/c/toys-and-games/toys/baby-and-toddler-toys?ref=catnav-2941",
    # 1367
    "http://lo.ameba.jp/v1/OrcVXglfogniYXHRWOEJ",
    # 1368
    "http://passport.china.com/jsp/user/findpassword.jsp",
    # 1369
    "http://www.dailymail.co.uk/tvshowbiz/article-3396305/Casey-Batchelor-showcases-legs-breasts-high-fashion-photoshoot.html",
    # 1370
    "http://www.slideshare.net/",
    # 1371
    "http://www.outbrain.com/",
    # 1372
    "http://www.ign.com/boards",
    # 1373
    "http://news.livedoor.com/topics/detail/11062813/",
    # 1374
    "http://conservativetribune.com/feds-schools-protect-students/",
    # 1375
    "http://www.microsoft.com/surface/en-ca/support/browse/surface-2?category=getting-started",
    # 1376
    "http://wp.tv",
    # 1377
    "http://www.lenovo.com/ca/en/",
    # 1378
    "http://esporte.uol.com.br/futebol/times/fluminense/",
    # 1379
    "http://www.microsoft.com/en-ca/",
    # 1380
    "http://www.bjcankao.com/",
    # 1381
    "http://www.163.com/",
    # 1382
    "http://store.steampowered.com/tag/en/Photo%20Editing/?snr=1_4_4__12",
    # 1383
    "http://www.pixnet.net",
    # 1384
    "http://www.sears.com/clothing-shoes-jewelry-shoes/b-1325051825",
    # 1385
    "http://ypk.39.net/yaopin/jsjnfmyy/jisulei/7bc1e.html",
    # 1386
    "http://www.ebay.co.uk/sch/Manicure-and-Pedicure/47945/bn_552182/i.html",
    # 1387
    "http://www.dailymail.co.uk/tvshowbiz/article-3396065/Shia-LaBeouf-girlfriend-three-years-Mia-Goth-nearly-identical-grey-sweatsuits.html",
    # 1388
    "http://shop.nordstrom.com/c/housewarming-gifts?dept=8000001&origin=topnav",
    # 1389
    "http://fxn.ws/1Ro7HfP",
    # 1390
    "http://rd.nicovideo.jp/cc/nicotop_blomaga/mediaarlist",
    # 1391
    "http://news.xywy.com/news/jrzd/20140113/733212.html",
    # 1392
    "http://www.cheyisou.com/",
    # 1393
    "http://amazon.ca/Dell-13-3-inch-Ultrabook-Computer-Processor/dp/B00RY4X8A4",
    # 1394
    "http://car.auto.caijing.com.cn/xuanchegongju/?p=5-8",
    # 1395
    "http://baby.39.net/yeqz/",
    # 1396
    "http://www.babytree.com/rd/rd.php?refcode=bbox1017syl&sid=bbox1017syl&url=http://babybox.babytree.com/",
    # 1397
    "http://www.olx.in/posting/",
    # 1398
    "http://ent.china.com/star/news/11052670/20160114/21137801.html",
    # 1399
    "http://detail.zol.com.cn/gpswatch/smartq/",
    # 1400
    "http://www.ebay.it",
    # 1401
    "http://s.kouclo.com/search.php?c=1902,DIY%E9%A5%B0%E5%93%81%E9%85%8D%E4%BB%B6",
    # 1402
    "https://hootsuite.com/",
    # 1403
    "http://www.ebay.de/cln/inner-circle-outlet/Naked-NO-it-s-just-NUDE/264988527014",
    # 1404
    "http://plus.baike.com/ihangkonghangtian",
    # 1405
    "https://www.etsy.com/c/craft-supplies-and-tools/fiber-and-textile-art-supplies/knitting-and-crocheting?ref=catnav-562",
    # 1406
    "http://kompas.com/",
    # 1407
    "http://www.ce.cn/cysc/",
    # 1408
    "http://car.bitauto.com/kaidilake/",
    # 1409
    "http://yyk.39.net/doctors/gaoxueya/",
    # 1410
    "http://auto.china.com/zhuanzai/hangye/11162373/20160114/21138859.html",
    # 1411
    "http://www.aol.ca/?r=www.aol.com",
    # 1412
    "http://blogs.wsj.com/japanrealtime/",
    # 1413
    "http://www.yapo.cl/",
    # 1414
    "http://ent.qq.com/a/20160114/019261.htm",
    # 1415
    "http://www.zillow.com/browse/homes/ky/",
    # 1416
    "http://sn.ifeng.com/zixun/jinrishanxi/detail_2016_01/14/4740220_0.shtml",
    # 1417
    "http://www.buzzfeed.com/",
    # 1418
    "http://photo.cntv.cn/index.shtml",
    # 1419
    "http://fitness.39.net/special/fms/",
    # 1420
    "http://shop.nordstrom.com/c/rag-bone?dept=8000001&origin=topnav",
    # 1421
    "http://www.snapdeal.com/products/mobiles-power-banks/?q=Mah_s:5001-7000^%207001-8000^%208001-9000",
    # 1422
    "http://www.teepr.com/category/%e6%b8%ac%e9%a9%97/",
    # 1423
    "http://tv.tudou.com/hanju/",
    # 1424
    "http://www.google.nl/chrome/browser/?hl=nl&brand=CHNG&utm_source=nl-hpp&utm_medium=hpp&utm_campaign=nl",
    # 1425
    "http://www.wsj.com/articles/how-the-indonesia-terror-attack-unfolded-1452788046",
    # 1426
    "http://www.bbc.com/guidance/",
    # 1427
    "http://www.kohls.com/catalog/clearance-toys.jsp?CN=4294736457+4294720971&cc=toys-TN2.0-S-clearancetoys",
    # 1428
    "http://ypk.39.net/zcy/qry/zcy-1.shtml",
    # 1429
    "http://kouclo.com/",
    # 1430
    "http://edmonton.craigslist.ca/search/sks",
    # 1431
    "http://wp.tv/i,przelomowe-wyniki-badan-wloskich-uczonych,mid,1857150,cid,4051,klip.html",
    # 1432
    "http://themeforest.net/category/muse-templates/corporate",
    # 1433
    "https://kat.cr/search/the%20revenant/",
    # 1434
    "http://sports.sina.com.cn/g/laliga/2016-01-14/doc-ifxnqriy2876302.shtml",
    # 1435
    "https://www.sway.com?WT.mc_id=O16_BingHP&utm_source=O16Bing&utm_medium=Nav&utm_campaign=HP",
    # 1436
    "https://www.wikimedia.org/",
    # 1437
    "http://www.jabong.com/beauty/",
    # 1438
    "http://en.savefrom.net/",
    # 1439
    "http://www.reuters.com/article/us-usa-coal-idUSKCN0US2WB20160114",
    # 1440
    "http://www.sf49ers.com/",
    # 1441
    "http://www.rediff.com/",
    # 1442
    "http://www.amazon.in/Fragrances/b?ie=UTF8&node=1374298031",
    # 1443
    "http://tradeadexchange.com/",
    # 1444
    "http://shutterstock.com/pic-54411157/stock-vector.html",
    # 1445
    "http://www.google.co.th/",
    # 1446
    "http://ppomppu.co.kr/zboard/view.php?id=mobile_gallery&no=47133",
    # 1447
    "http://www.google.com.au/",
    # 1448
    "http://www.kohls.com/catalog/powered-riding-toys-outdoor-play-toys-toys.jsp?CN=4294719493+4294719494+4294719592&cc=toys-TN2.0-S-poweredriding",
    # 1449
    "http://www.nyaa.se/?page=download&tid=774814",
    # 1450
    "http://maps.google.com.sa/maps?hl=ar&tab=wl",
    # 1451
    "http://www.enet.com.cn/instrument",
    # 1452
    "http://www.tudou.com/",
    # 1453
    "http://teleshow.wp.pl/wiadomosc.html?wid=18095151&title=Bilety-na-Kraftwerk-juz-w-sprzedazy&tpl=3",
    # 1454
    "http://publictransport.about.com",
    # 1455
    "http://www.xda-developers.com/",
    # 1456
    "http://gzly.cnnic.cn/gzly/index_new.jsp",
    # 1457
    "http://www.tmall.com/wow/chaoshi/act/tmcskhfc-lf",
    # 1458
    "http://dory.kr/2182",
    # 1459
    "http://en.gameforge.com/games/gamedetails/bitefight",
    # 1460
    "http://www.google.co.il/intl/iw/about.html",
    # 1461
    "http://product.yesky.com/gshijie/bizhi/362/70434862.shtml",
    # 1462
    "http://www.retailmenot.com/",
    # 1463
    "http://www.ettoday.net/news/focus/%E7%B6%B2%E6%90%9C/",
    # 1464
    "http://finance.sina.com.cn/stock/jsy/2016-01-14/doc-ifxnqriy2875826.shtml",
    # 1465
    "http://www.booking.com/destinationfinder/cities/it/rome.html?dsf_source=2&",
    # 1466
    "http://www.stumbleupon.com/",
    # 1467
    "http://www.fedex.com/ky/",
    # 1468
    "http://www.cnet.com/videos/cnet-news/",
    # 1469
    "http://japanpost.jp/locate/b15071301/index.php?tu=jpbank",
    # 1470
    "http://shutterstock.com/pic-233671087/stock-photo-budapest-hungary-nov-illustrative-editorial-photo-of-credit-cards-with-touch-free-paypass.html",
    # 1471
    "https://careers.americanexpress.com/?intlink=US-Homepage-Career-NOJS",
    # 1472
    "http://onedio.com/",
    # 1473
    "http://www.google.it/",
    # 1474
    "http://www.snapdeal.com/products/furniture-bedroom/filters/Type_s~Double%20Beds",
    # 1475
    "http://ppomppu.co.kr/",
    # 1476
    "https://ca.godaddy.com/",
    # 1477
    "http://www.hroot.com/default/index.html",
    # 1478
    "https://twitter.com/privacy",
    # 1479
    "http://baidu.com/",
    # 1480
    "http://bbs.hupu.com/15227696.html",
    # 1481
    "http://amazon.com/",
    # 1482
    "http://www.qulishi.com/",
    # 1483
    "http://www.sears.com/search=tech%20toys",
    # 1484
    "http://maps.yandex.ru",
    # 1485
    "http://www.tudou.com/home/weibusi/",
    # 1486
    "http://redir.xuite.net/redir/xuite/www/index/log/photoBlock^http://yo.xuite.net/info/edition_detail.php?id=58",
    # 1487
    "http://www.indiatimes.com/aboutus/",
    # 1488
    "http://community.newegg.com/",
    # 1489
    "http://jbk.39.net/jiancha/fbys/",
    # 1490
    "http://travel.kompas.com/hotel-story",
    # 1491
    "http://www.google.hu/",
    # 1492
    "http://amazon.de/Canon-Digitalkamera-Megapixel-ZoomPlus-LCD-Display/dp/B00RYV9P3Q",
    # 1493
    "http://sports.sina.com.cn/g/championsleague/",
    # 1494
    "http://vimeo.com/",
    # 1495
    "http://mailpec.libero.it/?o=hp",
    # 1496
    "https://eksisozluk.com/basliklar/kanal/oyun",
    # 1497
    "http://ettoday.net/news/20160114/630711.htm",
    # 1498
    "http://www.dailymail.co.uk/video/news/video-1234977/Family-perform-amazing-festive-dance-routine-Justin-Bieber.html",
    # 1499
    "http://www.appying.com/",
    # 1500
    "http://www.huffingtonpost.com/news/world-elections-2012/",
    # 1501
    "http://ent.china.com/star/news/11052670/20160114/21138724.html",
    # 1502
    "http://detail.zol.com.cn/369/368535/param.shtml",
    # 1503
    "http://rutracker.org/forum/index.php",
    # 1504
    "http://avito.ru/rossiya/ptitsy",
    # 1505
    "http://jn.house.ifeng.com/column/loupankong/qiuyinong",
    # 1506
    "https://mail.ru",
    # 1507
    "http://video.sina.com.cn/m/201512310544265_65165305.html",
    # 1508
    "http://www.att.com",
    # 1509
    "http://businessinsider.com/",
    # 1510
    "http://www.google.it/imghp?hl=it&tab=wi",
    # 1511
    "https://www.facebook.com/amazonwebservices?nc1=f_so_fb",
    # 1512
    "http://www.livedoor.com/",
    # 1513
    "https://eksisozluk.com/uzay-caginda-kagida-basilmis-kitap-okuyan-tip--5014601?a=nice",
    # 1514
    "http://product.yesky.com/product/862/862340/price.shtml",
    # 1515
    "http://customer.xfinity.com/overview",
    # 1516
    "https://mura.goo.ne.jp/",
    # 1517
    "http://www.taoche.com/qida/",
    # 1518
    "https://www.exoclick.com/",
    # 1519
    "http://blogfa.com/",
    # 1520
    "http://www.livedoor.com/",
    # 1521
    "http://www.intuit.com//global.intuit.com/choose-country.jsp",
    # 1522
    "http://www.addthis.com/",
    # 1523
    "http://espn.go.com/",
    # 1524
    "http://q.mama.cn/topic/24117274/",
    # 1525
    "http://www.ebay.in/sch/Portable-Audio-Video-/15052/i.html?_udlo=&_sop=12&_from=R40%7CR40%7CR40&_nkw=&_udhi=",
    # 1526
    "http://www.icicibank.com/Personal-Banking/account-deposit/iwish/index.page?",
    # 1527
    "http://www.imdb.com/title/tt1594972?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2381712442&pf_rd_r=1JY4J1T5VXD1VBEY3CS8&pf_rd_s=right-3&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_otw_t2",
    # 1528
    "http://www.weebly.com/",
    # 1529
    "http://web.de/",
    # 1530
    "http://go.com/",
    # 1531
    "http://user.gearbest.com/my-orders.html",
    # 1532
    "http://theguardian.com/",
    # 1533
    "https://www.airbnb.com/",
    # 1534
    "http://gotexas.about.com",
    # 1535
    "http://www.espncricinfo.com/bangladesh/content/team/25.html",
    # 1536
    "http://www.bbc.co.uk/programmes/p03ffzrw",
    # 1537
    "http://foodnetwork.com/healthy/packages/healthy-every-week.html",
    # 1538
    "http://www.clevelandbrowns.com/?icampaign=nflcom-footer-clublogos-CLE",
    # 1539
    "http://jbk.39.net/zizhen?bw=%E8%87%80%E9%83%A8",
    # 1540
    "http://www.milliyet.com.tr/konut/",
    # 1541
    "http://yandex.ru//www.yandex.ru/all",
    # 1542
    "https://adidas.world.tmall.com//adidas.tmall.com/p/rose6.htm?scene=taobao_shop",
    # 1543
    "http://www.enet.com.cn/hospital",
    # 1544
    "http://blog.milliyet.com.tr/ekranin-cicegi-burnunda-yenileri-/Blog/?BlogNo=519678&ref=milliyet_anasayfa",
    # 1545
    "http://z.xywy.com/jiahaozhuanjia.htm",
    # 1546
    "http://xunlei.com/",
    # 1547
    "https://www.kickstarter.com/",
    # 1548
    "http://plus.google.com/+NDTV/posts?pfrom=home-footer2015",
    # 1549
    "http://cctv5.cntv.cn/",
    # 1550
    "http://game.china.com/maoerduo/manzhan/news/11152946/20160114/21140492.html",
    # 1551
    "http://www.popads.net/blog",
    # 1552
    "http://www.bettermoneyhabits.com",
    # 1553
    "http://www.skype.com/en/",
    # 1554
    "http://en.gameforge.com/user/search",
    # 1555
    "http://redir.xuite.net/redir/xuite/www/index/log/photoBlock^http://photo.xuite.net/pzkw3489/19735668/24.jpg",
    # 1556
    "http://en.gameforge.com/home/index",
    # 1557
    "http://r.mail.ru/clb1406988/agent.mail.ru/?from=odnoklassniki",
    # 1558
    "http://www.google.cn/",
    # 1559
    "http://www.asos.com/asos-as-seen-on-screen/cat/pgehtml.aspx?cid=18967",
    # 1560
    "http://travel.detik.com/indeksfokus/1273/resolusi-traveling-2016/berita",
    # 1561
    "http://dictionary.reference.com/browse/dignified",
    # 1562
    "http://www.snapdeal.com/products/men-apparel-jeans",
    # 1563
    "https://aws.amazon.com/codecommit/?nc2=h_l3_dm",
    # 1564
    "http://www.kohls.com/catalog/bath-toys-bath-baby-gear.jsp?CN=4294719283+4294719613+4294719566&cc=toys-TN2.0-S-bathtoys",
    # 1565
    "https://www.groupon.com/coupons/stores/barnesandnoble",
    # 1566
    "http://services.amazon.co.uk/services/sponsored-products/how-it-works.html/ref=AMZfooter_UK_SP?ld=AMZfooterUKsp",
    # 1567
    "http://nk.39.net/a/160111/4756072.html",
    # 1568
    "http://product.yesky.com/product/862/862264/",
    # 1569
    "http://dcdv.zol.com.cn/topic/4859123.html",
    # 1570
    "http://car.bitauto.com/yingfeinidiqx56/",
    # 1571
    "http://hechi.bitauto.com/",
    # 1572
    "http://www.adventuresbydisney.com/?CMP=AFC-DPFY13Q1DIENT1376D",
    # 1573
    "http://www.kaskus.co.id/forum/671/?ref=homelanding&med=forum_categories",
    # 1574
    "http://www.kohls.com/catalog/womens-evening-pumps-heels-shoes.jsp?CN=4294720878+4294737256+4294719627+4294719777&cc=shoes-TN2.0-S-WomensEvening",
    # 1575
    "http://home.focus.cn/news/2016-01-06/10634257.html",
    # 1576
    "http://t.co/",
    # 1577
    "http://amazon.co.uk/Sony-DSCHX60-Digital-Compact-Optical/dp/B00IGL9PSS",
    # 1578
    "http://stackoverflow.com/questions/34801430/is-there-an-online-host-for-r-that-allows-it-to-work-continuously",
    # 1579
    "http://www.kinopoisk.ru/name/26537/",
    # 1580
    "http://www.kaskus.co.id/forum/13/?ref=homelanding&med=forum_categories",
    # 1581
    "http://www.buzzfeed.com/dashboard/nathanwpyle/how-empathy-takes-us-out-on-a-limb",
    # 1582
    "http://zt.xywy.com/rczy/",
    # 1583
    "http://edmonton.craigslist.ca//www.craigslist.org/about/help/",
    # 1584
    "http://www.tudou.com/programs/view/-KTYjmHaZME/",
    # 1585
    "http://www.alibaba.com/Rubber-Plastics_p80",
    # 1586
    "http://esf.focus.cn/search/",
    # 1587
    "http://www.samsung.com/ca/home/",
    # 1588
    "http://netflix.com/",
    # 1589
    "http://my.ebay.in/wishlistsearch/",
    # 1590
    "http://www.eastdaybar.com/",
    # 1591
    "http://car.bitauto.com/kuncheng/",
    # 1592
    "http://www.51.la/",
    # 1593
    "http://www.quantcast.com/p-4b4gl_1fWISuU",
    # 1594
    "http://bbs.lady8844.com/thread-1461595-1-1.html",
    # 1595
    "http://weibo.com/login.php",
    # 1596
    "http://fortune.goo.ne.jp/destiny/aries.html",
    # 1597
    "http://www.urdupoint.com/books/baab/novel/aas-paas-hai-khuda-115-desc",
    # 1598
    "http://amazon.it/Sony-Fotocamera-Obiettivo-Intercambiabile-Megapixel/dp/B00HH8A60C",
    # 1599
    "http://www.shopclues.com/wholesale/super-deals-of-wholesale/fashion-307.html",
    # 1600
    "http://www.shopclues.com/car-and-bike-accessories/car-accessories/car-interiors-and-comfort/car-perfumes-and-freshners.html",
    # 1601
    "http://videojuegos.about.com",
    # 1602
    "https://www.chase.com/",
    # 1603
    "https://www.etsy.com/c/craft-supplies-and-tools/patterns-and-tutorials/sewing-and-needlecraft/needlepoint?ref=catnav-562",
    # 1604
    "https://plus.google.com/u/0/+%D0%A0%D0%91%D0%9A/posts",
    # 1605
    "http://www.bilibili.com/",
    # 1606
    "http://gizmodo.com//kinja.com/katharinetrendacosta",
    # 1607
    "http://www.intuit.com/",
    # 1608
    "http://adplxmd.com/",
    # 1609
    "http://www.kohls.com/catalog/lc-lauren-conrad-shoes.jsp?CN=4294873305+4294719777&cc=shoes-TN2.0-S-LCLaurenConrad",
    # 1610
    "http://amazon.ca/FIT-20-5200-32-Pound-Dumbbell-Rack/dp/B00B4RVYPS",
    # 1611
    "http://www.tudou.com/home/discoveryvideo/",
    # 1612
    "https://www.whatsapp.com/dl/",
    # 1613
    "http://conservativetribune.com/powerball-jackpot-do-not-do/",
    # 1614
    "http://114.1688.com/newbie/course/36.htm",
    # 1615
    "http://club.xywy.com/doc_card/63691392",
    # 1616
    "https://watsons.world.tmall.com//watsons.tmall.com/category-1135919138.htm?search=y&parentCatId=1122785379&parentCatName=%C3%C0%D7%B1%B9%A4%BE%DF&catName=%BB%AF%D7%B1%C3%DE%B0%F4",
    # 1617
    "https://www262.americanexpress.com/business-card-application/mgm/200002-CCSG?inav=footer_refer_friend",
    # 1618
    "http://www.webmd.com/alzheimers/features/mind-diet-alzheimers-disease",
    # 1619
    "http://www.washingtonpost.com",
    # 1620
    "http://news.ifeng.com/a/20160114/47070310_0.shtml",
    # 1621
    "http://www.nike.com/th/th_th/",
    # 1622
    "http://www.ebay.co.uk/sch/Home-Audio-HiFi-Separates/14969/bn_1838773/i.html",
    # 1623
    "http://www.douyutv.com/411433",
    # 1624
    "http://fc2.com/",
    # 1625
    "http://www.mama.cn/ask/jingxuan/1365/",
    # 1626
    "http://jbk.39.net/zhengzhuang/syx/",
    # 1627
    "http://www.amazon.in/",
    # 1628
    "http://huabao.qzone.qq.com/",
    # 1629
    "https://www.whatsapp.com/",
    # 1630
    "http://car.bitauto.com/volvo/",
    # 1631
    "http://amazon.co.jp/",
    # 1632
    "http://www.asos.com/women/marketplace-edits/cat/pgehtml.aspx?cid=19024&via=top",
    # 1633
    "http://bola.liputan6.com/kategori/jadwal-live-streaming-bola",
    # 1634
    "http://kinogo.co/",
    # 1635
    "http://www.ebay.co.uk/sch/Vehicle-Parts-Accessories-/131090/i.html",
    # 1636
    "http://mamibox.yaolan.com/",
    # 1637
    "http://espn.go.com/mens-college-basketball/insider/story/_/id/14568141/keys-michigan-state-spartans-iowa-hawkeyes-matchup",
    # 1638
    "http://www.dailymail.co.uk/tvshowbiz/article-3398926/Jonathan-Rhys-Meyers-picture-health-shows-eccentric-style-oversized-hooded-jacket-outing-fianc-e-Mara-Lane.html",
    # 1639
    "http://www.yodobashi.com/ec/feature/174116_000000000000024018/",
    # 1640
    "http://salesforce.com/se/",
    # 1641
    "http://www.dmm.com/digital/cinema/",
    # 1642
    "http://www.yelp.pl/sf",
    # 1643
    "http://www.yaolan.com/zhishi/pailuanhoutongfang/",
    # 1644
    "http://www.cunan.com/",
    # 1645
    "http://www.sabah.de/turkiyeye-arac-goturebilmek",
    # 1646
    "http://shop.nordstrom.com/c/handbags-accessories?dept=8000001&origin=topnav",
    # 1647
    "https://www.reddit.com/",
    # 1648
    "http://www.gamefaqs.com/pc/699808-the-witcher-3-wild-hunt",
    # 1649
    "http://www.olx.in/furniture/categories/",
    # 1650
    "http://www.yelp.cl/",
    # 1651
    "http://www.independent.co.uk/extras/indybest/gadgets-tech/christmas-2015-streaming-box-apple-tv-google-chromecast-amazon-fire-roku-sky-now-tv-a6773821.html",
    # 1652
    "http://www.ebay.de",
    # 1653
    "http://gshow.globo.com/especial-blog/gshow-troll/1.html",
    # 1654
    "https://twitter.com/wunderground",
    # 1655
    "http://www.espncricinfo.com/ci/content/video_audio/index.html?genre=16",
    # 1656
    "https://archive.org/details/knittingreferencelibrary",
    # 1657
    "http://www.fedex.com/",
    # 1658
    "http://welcome.deviantart.com",
    # 1659
    "http://www.google.com.ar/",
    # 1660
    "http://www.google.co.il/",
    # 1661
    "http://www.varzesh3.com/contact",
    # 1662
    "http://www.baike.com/wiki/%E5%90%88%E8%82%A5%E7%8E%B0%E4%BB%A3%E5%A6%87%E4%BA%A7%E5%8C%BB%E9%99%A2?prd=shouye_qiyebaike",
    # 1663
    "https://www.usps.com/",
    # 1664
    "http://travel.163.com/outdoor/",
    # 1665
    "http://www.accuweather.com/en/weather-news",
    # 1666
    "http://s.kouclo.com/search.php?q=%E9%9D%A2%E9%83%A8%E6%8A%A4%E8%82%A4",
    # 1667
    "http://redir.xuite.net/redir/xuite/www/index/log/photoBlock^http://photo.xuite.net/whoami866/19703529/26.jpg",
    # 1668
    "http://baile.about.com",
    # 1669
    "http://araba.milliyet.com.tr/ilan-detay/1971-Anadol-A1/3655253",
    # 1670
    "http://www.cnet.com/forums/computer-newbies/",
    # 1671
    "http://bj.focus.cn/egoufang/",
    # 1672
    "http://www.zol.com.cn/",
    # 1673
    "http://www.cs.com.cn/",
    # 1674
    "https://online.wellsfargo.com/signon?serviceType=makeTransfer&loginMode=jukePassword&LOB=CONS",
    # 1675
    "https://medium.com/top-stories",
    # 1676
    "http://www.asos.com/men/a-to-z-of-brands/asos-collection/cat/pgecategory.aspx?cid=3159&ctaref=mw%7cnav%7casos&via=top",
    # 1677
    "http://flickr.com/signup",
    # 1678
    "https://www.popads.net/privacy-policy.html",
    # 1679
    "http://www.bitauto.com/zhuanti/8/bbspopularthemes/",
    # 1680
    "http://www.google.co.kr/history/optout?hl=ko",
    # 1681
    "http://www.naukri.com/",
    # 1682
    "https://flirchi.com/",
    # 1683
    "http://tnb.39.net/snxty/160113/4757579.html",
    # 1684
    "http://gshow.globo.com/Estilo/",
    # 1685
    "http://windows.microsoft.com/en-ca/windows/security-essentials-download",
    # 1686
    "https://www.etsy.com/c/electronics-and-accessories/gadgets?ref=catnav-2961",
    # 1687
    "http://yyk.39.net/doctors/erke/",
    # 1688
    "http://www.ask.com/",
    # 1689
    "http://www.homedepot.com/b/Bath/N-5yc1vZbzb3",
    # 1690
    "http://www.sears.com/toys-games-dolls-accessories/b-1020112",
    # 1691
    "http://www.engadget.com/",
    # 1692
    "http://car.bitauto.com/oulang-3561/",
    # 1693
    "https://watsons.world.tmall.com//watsons.tmall.com/category-727952755.htm?search=y&parentCatId=423860678&parentCatName=%CB%F9%D3%D0%C6%B7%C5%C6+ALL+Brands&catName=%C7%A7%C8%A4",
    # 1694
    "http://estaticos.marca.com/rss/futbol_1adivision.xml",
    # 1695
    "http://www.msn.com/en-ca/",
    # 1696
    "http://www.ebay-kleinanzeigen.de/stadt/nuernberg/",
    # 1697
    "http://www.washingtonpost.com/business/capital-business/",
    # 1698
    "http://edu.gmw.cn/2016-01/14/content_18489728.htm",
    # 1699
    "http://d.1905.com/weibo/7486312",
    # 1700
    "http://tv.liputan6.com/kategori/liputan6-petang",
    # 1701
    "https://www.linkedin.com/directory/people-l/",
    # 1702
    "http://www.shopclues.com/gourmet-and-daily-needs/gifting-2/flowers-en.html",
    # 1703
    "http://www.news.cn/health/",
    # 1704
    "https://www.etsy.com/c/home-and-living/lighting/lamps?ref=catnav-891",
    # 1705
    "http://www.google.gr/",
    # 1706
    "http://www.tj.xinhuanet.com/",
    # 1707
    "http://www.dailymail.co.uk/tvshowbiz/article-3396295/Kesha-dons-lace-boots-acting-gig-New-Orleans-set-Bad-Moms.html",
    # 1708
    "http://www.google.nl/",
    # 1709
    "http://wp.tv/i,w-czarnobylu-powstaje-olbrzymia-konstrukcja,mid,1858203,cid,4051,klip.html",
    # 1710
    "http://saltlakecity.about.com",
    # 1711
    "http://intl.ce.cn/specials/zxgjzh/201601/14/t20160114_8266304.shtml",
    # 1712
    "https://watsons.world.tmall.com//watsons.tmall.com/category-1122785356.htm?search=y&parentCatId=1122785334&parentCatName=%C3%C0%B7%F4&catName=T%C7%F8%BB%A4%C0%ED",
    # 1713
    "http://aws.amazon.com",
    # 1714
    "http://www.tudou.com/albumplay/KuNbGZ5Vy-g/1YoDDJyl9jk.html",
    # 1715
    "http://kouclo.com/specialty/cityitem/48",
    # 1716
    "http://slickdeals.net/coupons/office-depot",
    # 1717
    "http://www.quikr.com/",
    # 1718
    "http://ask.39.net/",
    # 1719
    "http://www.goodreads.com/author/show/1069006.C_S_Lewis",
    # 1720
    "http://www.sears.com/clothing-shoes-jewelry-shoes/b-1325051825?offer=All%20Items%20On%20Sale&filterList=offer&subCatView=true&searsTab=true",
    # 1721
    "http://sberbank.ru/ru/person/bank_cards/debet/universal",
    # 1722
    "http://www.sears.com/clothing-shoes-jewelry-shoes/b-1325051825?sbf=clearance",
    # 1723
    "http://www.reuters.com/",
    # 1724
    "http://finance.huanqiu.com/guijinshu/2016-01/8378084.html",
    # 1725
    "http://sourceforge.net/projects/exo/files/latest/download?source=frontpage&position=1",
    # 1726
    "http://www.csdn.net/",
    # 1727
    "http://amazon.fr/gp/help/customer/display.html?ie=UTF8&nodeId=548566",
    # 1728
    "http://travel.rakuten.co.jp/coupon/?scid=wi_grp_gmx_trv_ich_top_grptabcpn",
    # 1729
    "http://themeforest.net/",
    # 1730
    "http://allrecipes.com/",
    # 1731
    "http://bbs.zol.com.cn/sjbbs/d1795_7457.html",
    # 1732
    "http://s.kouclo.com/search.php?c=2297,%E9%85%B8%E5%A5%B6%E6%9C%BA",
    # 1733
    "http://soundcloud.com/",
    # 1734
    "http://www.iqiyi.com/a_19rrhbec7d.html",
    # 1735
    "http://www.youboy.com/",
    # 1736
    "http://www.dailymotion.com/ClevverMovies",
    # 1737
    "http://www.dailymail.co.uk/tvshowbiz/article-3396876/Ravishing-red-Jennifer-Connelly-dazzles-shimmering-crimson-gown-UNICEF-Ball-Beverly-Hills.html",
    # 1738
    "http://jx.sina.com.cn/",
    # 1739
    "http://www.dailymail.co.uk/home/index.html",
    # 1740
    "http://www.ebay-kleinanzeigen.de/s-familie-kind-baby/c17",
    # 1741
    "https://www.etsy.com/c/craft-supplies-and-tools/patterns-and-tutorials/painting?ref=catnav-562",
    # 1742
    "http://www.goo.ne.jp/renew2015/",
    # 1743
    "http://www.tistory.com/",
    # 1744
    "http://putlocker.is/",
    # 1745
    "http://globoesporte.globo.com/futebol/futebol-internacional/",
    # 1746
    "http://www.braininitiative.nih.gov/",
    # 1747
    "http://www.macys.com/catalog/index.ognc?CategoryID=58936&cm_sp=intl_hdr-_-flytrackingbreadcrumb-_-58936_shower-curtains-%26-accessories_COL2",
    # 1748
    "http://tag.lady8844.com/388490/",
    # 1749
    "http://baby.about.com",
    # 1750
    "http://www.google.pl/preferences?hl=pl",
    # 1751
    "http://card.17ok.com/news/1046/2016/0111/2510336.html",
    # 1752
    "http://stars.udn.com/stars/search",
    # 1753
    "http://www.globo.com/",
    # 1754
    "http://www.twitch.tv/directory",
    # 1755
    "http://www.nike.com/",
    # 1756
    "http://www.tianjimedia.com/zxns/",
    # 1757
    "http://car.bitauto.com/62s/",
    # 1758
    "http://www.accuweather.com/en/ca/canada-weather",
    # 1759
    "http://news.xinhuanet.com/politics/2015-12/08/c_1117386101.htm",
    # 1760
    "http://ppomppu.co.kr/zboard/view.php?id=help&no=1108902",
    # 1761
    "http://www.flipkart.com/camera-accessories/tripods/pr?sid=jek,6l2,ce6",
    # 1762
    "http://www.kohls.com/catalog/mens-big-tall-pants-bottoms-clothing.jsp?CN=4294723349+4294737980+4294719806+4294719807+4294719810&N=4294723349+4294737980+4294719454+4294719806+4294719807+4294719810&cc=mens-TN2.0-S-btjeanspants",
    # 1763
    "http://baby.jd.com",
    # 1764
    "http://www.hqpp.com.cn/",
    # 1765
    "http://www.dell.com/hr/en/gen/df.aspx?refid=df&s=gen&~ck=cr",
    # 1766
    "http://travel.163.com/16/0113/16/BD7N5L2J00063KE8.html",
    # 1767
    "http://uae.souq.com/ae-en/huawei-honor-4x-dual-sim-8gb-4g-gold-8752158/i/",
    # 1768
    "http://www.bing.com/",
    # 1769
    "http://www.douyutv.com/directory/game/qmxx",
    # 1770
    "http://www.youku.com/",
    # 1771
    "http://www.nfl.com/news/story/0ap3000000613876/article/coaching-tracker-chip-kelly-lands-with-49ers",
    # 1772
    "http://www.nih.gov/institutes-nih/nih-office-director",
    # 1773
    "http://www.iqiyi.com/v_19rrl62m7o.html?list=19rrobegja",
    # 1774
    "http://www.kaskus.co.id/forum/278/?ref=homelanding&med=forum_categories",
    # 1775
    "http://uae.souq.com/ae-en/philips-hair-curler-hp8602-03-6734014/i/",
    # 1776
    "http://www.iqiyi.com/a_19rrhbzro9.html",
    # 1777
    "http://redir.xuite.net/redir/xuite/www/index/log/photoBlock^http://photo.xuite.net/photo/18946584/1304.jpg",
    # 1778
    "http://17ok.com/",
    # 1779
    "http://www.sahibinden.com/",
    # 1780
    "http://jck.39.net/jiancha/huaxue/ydfmw/9c2f9.html",
    # 1781
    "http://www.ce.cn/xwzx/",
    # 1782
    "http://book.naver.com",
    # 1783
    "http://slide.ent.sina.com.cn/?cate=304",
    # 1784
    "http://shop.nordstrom.com/c/mens-tshirts?dept=8000001&origin=topnav",
    # 1785
    "https://games.mail.ru/pc/news/r/v_fallout_4_dobavili_zimu_i_drugie_novosti_dnja/?from=informer",
    # 1786
    "http://amazon.it/Brooks-Brothers-Saxxon-Cardigan-Biella/dp/B00YJ3120G",
    # 1787
    "http://amazon.com/Nikon-COOLPIX-Digital-Optical-Built-In/dp/B00T85PH2Y",
    # 1788
    "http://www.oeeee.com/",
    # 1789
    "http://www.cnkang.com",
    # 1790
    "http://stackoverflow.com//photo.stackexchange.com",
    # 1791
    "http://sympatia.onet.pl/?utm_source=onet.pl&utm_medium=banner&utm_campaign=ikona",
    # 1792
    "http://www.google.fi/history/optout?hl=fi",
    # 1793
    "http://www.telegraph.co.uk/technology/news/12098412/Robot-doctor-app-raises-25m-to-predict-future-of-your-health.html",
    # 1794
    "https://www.office.com/",
    # 1795
    "http://s.kouclo.com/search.php?c=2046,%E7%9A%AE%E8%A1%A3",
    # 1796
    "http://bbs.hupu.com/15245440.html",
    # 1797
    "http://www.washingtonpost.com/realestate/",
    # 1798
    "http://us.sourcing.alibaba.com/rfq/request/post_buy_request.htm?tracelog=header_action_popup_rfq&source=header",
    # 1799
    "http://qiyuan.youth.cn/lysy/201601/t20160106_7495029.htm",
    # 1800
    "http://uae.souq.com/ae-en/lg-tv-32-inch-led-32lf520-9467547/i/",
    # 1801
    "http://www.iqiyi.com/v_19rrifknmw.html?list=19rrobir2y",
    # 1802
    "http://avito.ru//www.avito.ru/vladimirskaya_oblast",
    # 1803
    "https://watsons.world.tmall.com//watsons.tmall.com/category.htm?spm=a1z10.1-b.w5003-7287744525.8.Z5LPID&orderType=hotsell_desc&viewType=grid&keyword=%BB%E1%D4%B1%BF%A8&lowPrice=&highPrice=&scene=taobao_shop",
    # 1804
    "http://www.4shared.com/",
    # 1805
    "http://www.icicibank.com/",
    # 1806
    "https://aws.amazon.com/documentation/lambda/?icmpid=docs_menu",
    # 1807
    "http://mil.huanqiu.com/world/2016-01/8377751.html",
    # 1808
    "http://legal.gmw.cn/node_9017.htm",
    # 1809
    "http://club.news.sohu.com/minjian/thread/3rpop3zcjfs",
    # 1810
    "http://health.goo.ne.jp/news/3364",
    # 1811
    "http://www.nytimes.com/content/help/site/ie9-support.html",
    # 1812
    "http://store.steampowered.com/app/346110/?snr=1_4_4__104",
    # 1813
    "https://mega.nz/",
    # 1814
    "http://ettoday.net/news/20160113/629528.htm",
    # 1815
    "http://www.usatoday.com/story/news/politics/2016/01/14/paul-ryans-short-list-what-could-get-done-year/78784910/",
    # 1816
    "http://www.goodreads.com/book/show/33917.The_Namesake",
    # 1817
    "http://sports.sina.com.cn/basketball/nba/2016-01-14/doc-ifxnqrkc6371445.shtml",
    # 1818
    "http://www.xe.com/travel-expenses-calculator/",
    # 1819
    "http://utorrent.uptodown.com",
    # 1820
    "http://www.espncricinfo.com/",
    # 1821
    "https://www.tmall.com/",
    # 1822
    "http://car.bitauto.com/c3bijiasuo/",
    # 1823
    "http://amazon.com/TurboTax-Business-Federal-Preparation-Software/dp/B01637RHBI",
    # 1824
    "https://www.popads.net/",
    # 1825
    "http://www.buzzfeed.com/kelseydarragh/questions-gay-people-have-for-bisexual-people",
    # 1826
    "http://www.snapdeal.com/product/plancess-crash-course-for-jee/621918711416",
    # 1827
    "http://www.google.ca/?gfe_rd=cr&ei=ciuuvpy3g4_t8we21be4cq",
    # 1828
    "http://www.washingtonpost.com/technology/",
    # 1829
    "http://www.yaolan.com/zhishi/ertongyiwaishanghai/",
    # 1830
    "https://www.fiverr.com/",
    # 1831
    "http://uae.souq.com/ae-en/toys/stuffed-toys%7Cstuffed-animals%7Cpuppets,-stuffed-animals---and---soft-toys/a-1446/l/?rpp=48&amp;sortby=",
    # 1832
    "http://coccoc.com/",
    # 1833
    "http://www.shopclues.com/sports-and-outdoors/fitness-en/fitness-equipment-5.html",
    # 1834
    "http://www.bbc.com/privacy/cookies/international/",
    # 1835
    "http://rock.about.com",
    # 1836
    "http://gmw.cn/",
    # 1837
    "http://www.xinhuanet.com/video/xinhuaradio/index.htm",
    # 1838
    "http://www.bananarepublic.com/products/index.jsp",
    # 1839
    "http://www.marca.com/futbol/europa-league.html",
    # 1840
    "http://ce.cn/",
    # 1841
    "https://www.lowes.ca/",
    # 1842
    "http://allegro.pl/",
    # 1843
    "http://ebates.com/coupons/amazon/index.htm?navigation_id=22864",
    # 1844
    "http://home.mcafee.com/store/total-protection",
    # 1845
    "http://www.chargers.com/?icampaign=nflcom-footer-clublogos-SD",
    # 1846
    "http://bbs.oeeee.com/photoview-fid-104-tid-17674833-onid-1.html",
    # 1847
    "http://uae.souq.com/ae-en/citrus/perfumes---and---fragrances-478/a-t/s/?rpp=48&amp;sortby=",
    # 1848
    "http://onedio.com/turkiye/egitim-haberleri",
    # 1849
    "http://www.amazon.in/Nova-Compact-NH-1202-1000-Watt-Elegant/dp/B015Z3AVVO",
    # 1850
    "http://lifehacker.com//kinja.com/HeatherYH",
    # 1851
    "http://www.mama.cn/z/1123/",
    # 1852
    "http://manhua.163.com/source/4514342859170124258",
    # 1853
    "http://news.eastday.com/s/20160115/u1a9180567.html",
    # 1854
    "http://jck.39.net/3/jianchazuhe/53/dc87c.html",
    # 1855
    "http://www.bitauto.com/jingzhou/",
    # 1856
    "http://on.aol.ca/channel/relationships",
    # 1857
    "http://nerf.about.com",
    # 1858
    "http://www.macys.com/catalog/index.ognc?CategoryID=70963&cm_sp=intl_hdr-_-flytrackingbreadcrumb-_-70963_extra-25%25-40%25-off-clearance_COL4",
    # 1859
    "https://www.wix.com/my-account/settings",
    # 1860
    "https://www.att.com/",
    # 1861
    "http://www.ikea.com/ca/en/store/burlington",
    # 1862
    "https://retail.onlinesbi.com/personal/faq.html",
    # 1863
    "http://so.iqiyi.com",
    # 1864
    "http://www.ebay-kleinanzeigen.de/",
    # 1865
    "http://www.jd.com/",
    # 1866
    "http://product.auto.163.com/series/15101.html",
    # 1867
    "http://themeforest.net/item/phases-of-the-moon/10305388",
    # 1868
    "http://www.mama.cn/ask/jingxuan/1295/",
    # 1869
    "https://github.com/",
    # 1870
    "http://stackoverflow.com/users/5712410/marko-avlija%c5%a1",
    # 1871
    "http://www.google.ca/?gfe_rd=cr&ei=2yquvtzvc6xp8ge_vrcidw",
    # 1872
    "http://www.nyaa.se/?page=download&tid=774772",
    # 1873
    "http://shopping.rediff.com/categories/sports-shoes/cat-9130",
    # 1874
    "https://www.etsy.com/c/weddings/gifts-and-mementos/guest-books?ref=catnav-1633",
    # 1875
    "http://amazon.de/Star-Wars-Complete-Saga-Blu-ray/dp/B011T11T8A",
    # 1876
    "http://www.tianya.cn",
    # 1877
    "http://www.nfl.com/",
    # 1878
    "http://badoo.com/",
    # 1879
    "http://www.buzzfeed.com/dashboard/ellievhall/more-like-hog-farts-am-i-right",
    # 1880
    "http://www.ebay.in/",
    # 1881
    "http://vhouse.163.com/16/0111/13/BD26U44300294MCG.html",
    # 1882
    "http://www.china.com.cn/",
    # 1883
    "http://avito.ru//www.avito.ru/mariy_el",
    # 1884
    "http://www.asos.com/women/magazine/cat/pgehtml.aspx?cid=20209&via=top",
    # 1885
    "http://www.zillow.com/",
    # 1886
    "https://www.icloud.com/",
    # 1887
    "http://biznes.onet.pl/wiadomosci/transport/koleje-mazowieckie-maja-nowy-tabor-pierwszy-taki-polski-pociag/rz8cbe",
    # 1888
    "http://www.hm.com/ca/",
    # 1889
    "http://www.spiegel.de/",
    # 1890
    "https://cprodx.att.com/apiserver/igate_web_dlom/logOut.do?style=relogin&returnurl=https://www.att.com/shopservlets/landing?redirectUrl=/olam/logout.olamexecute",
    # 1891
    "http://www.nytimes.com/2016/01/14/opinion/stop-wasting-americas-hydropower-potential.html",
    # 1892
    "http://www.chinadaily.com.cn/food/",
    # 1893
    "https://accounts.google.com/servicelogin?service=blogger&hl=en_gb&passive=1209600&continue=https://www.blogger.com/home",
    # 1894
    "http://z.xywy.com/zhuanye-shenjingneike.htm",
    # 1895
    "http://jbk.39.net/ykfwzy/151130/4734778.html?rel=sytp",
    # 1896
    "http://slickdeals.net/localdeals/las-vegas/",
    # 1897
    "http://www.sabah.com.tr/astroloji/?currentBurc=11",
    # 1898
    "http://kobieta.onet.pl",
    # 1899
    "http://www.babytree.com/learn/specialtopic/xiaoernaojishui",
    # 1900
    "http://iservice.ltn.com.tw/Service/english/english.php?engno=934344&day=2015-11-22",
    # 1901
    "https://creative.adobe.com/plans?promoid=KLXMK",
    # 1902
    "https://www.zendesk.com/",
    # 1903
    "http://www.opselect.com/ad_feedback/pages/survey.php?src=101",
    # 1904
    "http://www.huffingtonpost.ca/news/worst-dressed/",
    # 1905
    "http://www.alibaba.com/catalogs/products/CID8012",
    # 1906
    "http://club.china.com/baijiaping/juhe/blkx",
    # 1907
    "http://www.buzzfeed.com/post?id=4124329",
    # 1908
    "http://www.kohls.com/catalog/jennifer-lopez-bed-bath.jsp?CN=4294874717+4294719803&N=4294719803+4294874717&cc=bed_bath-TN2.0-S-jenniferlopez",
    # 1909
    "http://get-support.softonic.com",
    # 1910
    "http://world.taobao.com",
    # 1911
    "http://www.ndtv.com/",
    # 1912
    "https://www.etsy.com/c/vintage/jewelry/jewelry-sets?ref=catnav-2963",
    # 1913
    "http://www.xda-developers.com/android-based-smart-glass-round-up-whats-new-at-ces-2016/",
    # 1914
    "http://www.ppomppu.co.kr/books/index.php",
    # 1915
    "http://www.aliexpress.com/category/200214011/sports-watches.html",
    # 1916
    "http://www.kohls.com/catalog/womens-clothing.jsp?CN=4294720878+4294719810&N=4294720878+4294719810+3000079534&icid=hpmf|mfs2",
    # 1917
    "http://www.tudou.com/listplay/KFcX61yS55A/Q7lMVUPGWis.html",
    # 1918
    "http://www.google.ro/",
    # 1919
    "http://www.hulu.com/",
    # 1920
    "http://www.scienceplus2ch.com/archives/5167627.html",
    # 1921
    "http://shuma.jd.com/",
    # 1922
    "http://money.cnn.com/media/",
    # 1923
    "http://www.dell.com/ng/en/gen/df.aspx?refid=df&s=gen&~ck=cr",
    # 1924
    "https://www.lowes.ca/outdoor/snow-removal/?linkloc=promo_HP_hpfc",
    # 1925
    "http://magazine.caijing.com.cn/20160111/4051040.shtml",
    # 1926
    "https://www.wikipedia.org/",
    # 1927
    "http://flickr.com//mobile.yahoo.com/flickr",
    # 1928
    "http://bbs.hupu.com/15197668.html",
    # 1929
    "http://wunderground.com/download/index.asp",
    # 1930
    "http://www.accuweather.com/en/ca/vancouver/v5y/daily-weather-forecast/53286",
    # 1931
    "http://v.17173.com/specials/Show_20151218/?vid=sohusy_db",
    # 1932
    "http://www.macys.com/shop/search?keyword=adidas&cm_sp=intl_hdr-_-flytrackingbreadcrumb-_-adidas_COL3",
    # 1933
    "https://www.oracle.com/downloads/index.html",
    # 1934
    "http://yyk.39.net/hospital/25776_lab.html",
    # 1935
    "http://www.sabah.com.tr/yasam/2016/01/14/nufus-cuzdani-tarih-oldu",
    # 1936
    "http://www.kohls.com/catalog/patio-furniture.jsp?CN=4294709993+4294687129&cc=furniture-TN2.0-S-PatioFurniture",
    # 1937
    "http://abc.go.com/",
    # 1938
    "http://www.microsoft.com/surface/en-ca?ocid=OCTEVENT_MSCOM",
    # 1939
    "http://bollywood.about.com",
    # 1940
    "http://mall.360.com/shop/item?item_id=55839af858d4a63a41000024&utm_source=guding_360guanwang _sybanner01_0804&utm_medium=inside",
    # 1941
    "http://tech.163.com/16/0114/19/BDAJSMHU000915BF.html",
    # 1942
    "http://www.webmd.com/sex-relationships/default.htm",
    # 1943
    "http://redir.xuite.net/redir/xuite/www/index/log/photoBlock^http://photo.xuite.net/photo/19333626/223.jpg",
    # 1944
    "http://vietnamese.china.com",
    # 1945
    "https://ca.yahoo.com",
    # 1946
    "http://www.google.com.hk/",
    # 1947
    "http://www.rbc.ru/",
    # 1948
    "http://voice.hupu.com/soccer/1991108.html",
    # 1949
    "http://jianfei.39.net/forum-93-1.html",
    # 1950
    "http://mailchimp.com/about/mcsv/",
    # 1951
    "http://cq.house.ifeng.com/sale/search/50007/_/_/0_0_0_275_0_0_0_0_0_0_0_0_0_0.shtml?keyword=_",
    # 1952
    "http://finance.ce.cn/rolling/201601/14/t20160114_8260894.shtml",
    # 1953
    "http://steamcommunity.com/",
    # 1954
    "http://torrentz.eu/",
    # 1955
    "http://mashable.com/privacy/",
    # 1956
    "http://car.bitauto.com/shanghaihuizhong/",
    # 1957
    "http://yyk.39.net/doctors/feiyan/",
    # 1958
    "http://www.uol.com.br/",
    # 1959
    "http://moto.onet.pl/aktualnosci/genesis-g90-pierwszy-model-nowej-marki-detroit-2016/f6sk7s",
    # 1960
    "http://jr.ifeng.com/"
] # urls = [ ... ]
