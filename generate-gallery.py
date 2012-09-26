# Import base libraries
import os

# Import relevant packages from the Google Data Python client library
import gdata.photos.service
import gdata.media
import gdata.geo

# User-specific data
user_id = '100382636415340600164'
ignored_albums = ('5716491723391976337', '5706446377771654129',
                  '5688661881733842001', '5668520065107350593',
                  '5625206640295281457', '5625205598890785729')

# Create a folder to store the output
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a connection to the Picasa Web Albums service
gd_client = gdata.photos.service.PhotosService()
gd_client.source = 'org-harishnarayanan-album-fetcher'

# Request a list of albums for a given user
albums = gd_client.GetUserFeed(user=user_id)

# For each unignored album, generate the gallery code and drop it in a
# separate folder
for album in albums.entry:
    album_id = album.gphoto_id.text
    if album_id not in ignored_albums:
        if not os.path.exists(os.path.join(output_dir, album_id)):
            os.makedirs(os.path.join(output_dir, album_id))
        output_file = open(os.path.join(output_dir, album_id, 'index.html'), 'w+')
        output_file.write('%s' % album.title.text)
        output_file.write('<hr />')
        output_file.write('<br />')
        photo_query = '/data/feed/api/user/%s/albumid/%s?kind=photo'
        photos = gd_client.GetFeed(photo_query % (user_id, album_id))
        for photo in photos.entry:
            output_file.write('	          <a href="%s" title="%s"><img class="thumbnail-photo" src="%s" alt="%s" /></a>' % (photo.content.src, album.title.text, photo.media.thumbnail[0].url, photo.title.text))

        output_file.close()
