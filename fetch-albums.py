# Import relevant packages from the Google Data Python client library
import gdata.photos.service
import gdata.media
import gdata.geo

# User-specific data
user_id = '100382636415340600164'
ignored_albums = ('5716491723391976337', '5706446377771654129',
                  '5688661881733842001', '5668520065107350593',
                  '5625206640295281457', '5625205598890785729')

# Create a connection to the Picasa Web Albums service
gd_client = gdata.photos.service.PhotosService()
gd_client.source = 'org-harishnarayanan-album-fetcher'

# Request a list of albums for a given user
albums = gd_client.GetUserFeed(user=user_id)

# Go through the albums and ...
for album in albums.entry:
    if album.gphoto_id.text not in ignored_albums:
        print('%s' % album.title.text)
        print('<hr />')
        print('<br />')
        photo_query = '/data/feed/api/user/%s/albumid/%s?kind=photo'
        photos = gd_client.GetFeed(photo_query % (user_id,
                                                  album.gphoto_id.text))
        for photo in photos.entry:
            print('	          <a href="%s" title="%s"><img class="thumbnail-photo" src="%s" alt="%s" /></a>' % (photo.content.src, album.title.text, photo.media.thumbnail[0].url, photo.title.text))

        print('<br />')

#print '<table>'



#for album in albums.entry:
#    print '<tr>'

#    print 'Album: %s (%s)' % (album.title.text, album.numphotos.text)

#    photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (user_id, album.gphoto_id.text))
#    for photo in photos.entry:
#        print '<td>'
#        print '<a href="%s"><img src="%s" /></a>' % ( photo.media.thumbnail[0].url, photo.content.src )
#        print '</td>'
#    print '</tr>'

  #   tags = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s/photoid/%s?kind=tag' % (album.gphoto_id.text, photo.gphoto_id.text))
  #   for tag in tags.entry:
  #     print '    Tag:', tag.title.text

  #   comments = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s/photoid/%s?kind=comment' % (album.gphoto_id.text, photo.gphoto_id.text))
  #   for comment in comments.entry:
  #     print '    Comment:', comment.content.text

#print '</table>'
