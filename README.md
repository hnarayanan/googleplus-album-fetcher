Fetch albums from Google+ onto your own site
============================================

(C) 2012 Harish Narayanan

Motivation
----------

Like most people, I find myself creating less and less content on my
own websites/blogs and instead choosing to use services such as
Google+ and Twitter. They're so much easier to use and encourage
immediate community feedback. Even so, I'd still like to have my
content featured on my own sites in a cohesive way.

If you're like me, read on.

What is it?
----------

Google+ Album Fetcher does exactly what its name suggests. It is a
simple script that fetches albums uploaded to Google+ and writes out
static HTML files that can be used to populate your own website.

How do you use it?
------------------

The script is quite rough and requires a bunch of fiddling around,
but in essence, you:

1. Install the Google Data (Python) client library on your
computer. If you're running OS X with MacPorts, this is as simple as:

`sudo port install py27-gdata`

2. Open the script file `generate-gallery.py` and edit `user_id` and
`album_slugs` in `generate-gallery.py` to point to yourself on Google+
and the unique IDs of the galleries you want to extract.

3. Edit the header and footer HTML in the `.html` files to suit your
own website.

4. Run

`python generate-gallery.py`

which will fetch album data from Google+ and write out static HTML to
`output/slug/index.html` (one for each album you requested) with
galleries showcasing your photographs.

How do I report bugs and request features?
------------------------------------------

Contact me via e-mail <mail@harishnarayanan.org> and I'll try to help.
