import gdata.photos.service
import gdata.media
import gdata.geo

gd_client = gdata.photos.service.PhotosService()
gd_client.source = 'org-harishnarayanan-album-fetcher'
user_name = 'hnarayanan'
google_plus_user_id = '100382636415340600164'


albums = gd_client.GetUserFeed(user=user_name)

#print '<table>'

for album in albums.entry:
#    print '<tr>'

#    print 'Album: %s (%s)' % (album.title.text, album.numphotos.text)

    photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (google_plus_user_id, album.gphoto_id.text))
    for photo in photos.entry:
#        print '<td>'
        print '<a href="%s"><img src="%s" /></a>' % ( photo.media.thumbnail[0].url, photo.content.src )
#        print '</td>'
#    print '</tr>'

  #   tags = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s/photoid/%s?kind=tag' % (album.gphoto_id.text, photo.gphoto_id.text))
  #   for tag in tags.entry:
  #     print '    Tag:', tag.title.text

  #   comments = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s/photoid/%s?kind=comment' % (album.gphoto_id.text, photo.gphoto_id.text))
  #   for comment in comments.entry:
  #     print '    Comment:', comment.content.text

#print '</table>'
