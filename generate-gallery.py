# Import base libraries
import os

# Import relevant packages from the Google Data Python client library
import gdata.photos.service
import gdata.media
import gdata.geo

# Albums on Google+ have the following form:
# https://plus.google.com/photos/[user_id]/albums/[album_id]
#
# So change the following to reflect the albums you want, giving
# them appropriate slugs. I've left some some of my albums in as a
# sample.
user_id = '100382636415340600164'
album_slugs = {
    '5840443431763834657': 'save-the-date',
    '5783207452453609937': 'varun-anjana-wedding',
    '5781964989109220945': 'little-red-balloon',
    }

# If it doesn't exist already, create a folder to store the output
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read boilerplate header and footer files
header_file = open('gallery-header.html', 'r')
header = header_file.read()
footer_file = open('gallery-footer.html', 'r')
footer = footer_file.read()

# Create a connection to the Picasa Web Albums service
gd_client = gdata.photos.service.PhotosService()
gd_client.source = 'org-harishnarayanan-album-fetcher'

# Request a list of albums for a given user
albums = gd_client.GetUserFeed(user=user_id)

# For each required album, create a unique output folder and drop the
# generated gallery code into it
for album in albums.entry:

    # Extract the ID of the album
    album_id = album.gphoto_id.text

    # Check if it is within the list of useful albums, and if so,
    # extract a manually-defined slug
    if album_id in album_slugs.keys():
        album_slug = album_slugs[album_id]
    else:
        continue

    # Create the output folder and file
    if not os.path.exists(os.path.join(output_dir, album_slug)):
        os.makedirs(os.path.join(output_dir, album_slug))
    output_file = open(os.path.join(output_dir, album_slug,
    'index.html'), 'w+')

    output_file.write(header.replace('insert_title_here', album.title.text).replace('insert_nav_here', album.name.text))
    photo_query = '/data/feed/api/user/%s/albumid/%s?kind=photo&imgmax=900&thumbsize=120'
    photos = gd_client.GetFeed(photo_query % (user_id, album_id))
    for photo in photos.entry:
        output_file.write('	          <a href="%s" title=""><img class="thumbnail-photo" src="%s" alt="%s" /></a>\n' % (photo.content.src, photo.media.thumbnail[0].url, photo.title.text))
    output_file.write(footer)
    output_file.close()

# Close header and footer files
header_file.close()
footer_file.close()
