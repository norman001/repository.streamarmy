import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,hashlibimport base64import HTMLParserimport osfrom resources.libs.modules import satoolsaddon_id        = 'plugin.video.streamarmy'AddonTitle      = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))dialog          = xbmcgui.Dialog()dp              = xbmcgui.DialogProgress()def SCRAPE_3D_DOCS(url):    link = satools.open_url(url)    match = re.compile('<div id="peliculas">(.+?)</div>').findall(link)    for links in match:        title = re.compile ('alt="(.+?)"').findall(links)[0]        url1 = re.compile ('<a href="(.+?)"').findall(links)[0].replace(' ', '%20')        icon2 = re.compile ('<img src="(.+?)"').findall(links)[0]        url = 'http://www.documentarymania.com/' + url1        icon = 'http://www.documentarymania.com' + icon2        satools.addDir("[COLOR silver]" + title + "[/COLOR]",url,55,icon,fanarts,'')            try:        np = re.compile ('<td class="table">.+?<a href=\"([^"]*)\"> ></a>').findall(link)[0]        nextpage = 'http://www.documentarymania.com' + np        np = 'http://i.imgur.com/B4r7zDm.png'        satools.addDir("[COLOR red]Next Page[/COLOR]",nextpage,54,np,fanart)    except:pass    def SCRAPE_3D_DOCS_LINKS(name,url,iconimage):    link = satools.open_url(url)    match = re.compile ('<div id="myElement">(.+?)</script>').findall(link)[0]    grab = re.compile ('{(.+?)}').findall(match)    for links in grab:        try:            title = re.compile ('label: "(.+?)"').findall(links)[0]            url = re.compile ('"(.+?)"').findall(links)[0]            if '.mp4' in url:                satools.addLink(title,url,7,iconimage,fanart)        except:pass