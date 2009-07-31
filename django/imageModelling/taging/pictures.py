#!/usr/bin/python
# -*- coding: utf-8 -*-

import flickr

method = 'flickr.photos.getRecent'
#url=flickr._getURL(method)
user=flickr.people_findByUsername('enguillem')


#print "prova", method,"url",url,"user",dir(user)

fotos=flickr.photos_search(user.id,tags='dinar')
print fotos
for foto in fotos:
    print "FOTO:",foto.getURL()