import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,hashlibimport base64import HTMLParserimport osfrom resources.libs.modules import satoolsaddon_id        = 'plugin.video.streamarmy'AddonTitle      = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))dialog          = xbmcgui.Dialog()dp              = xbmcgui.DialogProgress()def SCRAPE_DOCS_CATS(url):    link = satools.open_url(url)    match = re.compile('<li.+?href="(.+?)".+?>(.+?)</a.+?li>').findall(link)    for url2, title in match:        if url2.find('categ') != -1:            new = url + url2            satools.addDir("[COLOR silver]" + title + "[/COLOR]",new,53,icon,fanarts,'')            def SCRAPE_DOCS_CONTENT(name,url,iconimage):    link2 = satools.open_url(url).replace('&#8217;',"'")    information = re.compile('<div class="post-thumbnail".+?<a href="(.+?)".+?src="(.+?)".+?alt="(.+?)"', re.DOTALL).findall(link2)    for url,thumbnail,name in information:        link3 = satools.open_url(url)        videolink = re.compile('<div class=\'video\'><iframe width=".+?" height=".+?" src="(.+?)"').findall(link3)        for ids in videolink:            try:                reallinks = ids.split("/embed/")[1]                endlink = "plugin://plugin.video.youtube/play/?video_id=" + reallinks                satools.addLink("[COLOR silver]" + name.title() + "[/COLOR]",endlink,7,thumbnail,fanarts,'')            except: pass    try:        np = re.compile('<link rel="next" href="(.+?)" />', re.DOTALL).findall(link2)[0]        satools.addDir("[COLOR red]Next Page -->[/COLOR]",np,52,icon,fanarts,'')    except: pass