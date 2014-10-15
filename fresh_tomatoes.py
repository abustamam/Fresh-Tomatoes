import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="//code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <!-- Add fancyBox -->
    <link rel="stylesheet" href="fancybox/source/jquery.fancybox.css?v=2.1.5" type="text/css" media="screen" />
    <script type="text/javascript" src="fancybox/source/jquery.fancybox.pack.js?v=2.1.5"></script>

    <!-- Optionally add helpers - button, thumbnail and/or media -->
    <link rel="stylesheet" href="fancybox/source/helpers/jquery.fancybox-buttons.css?v=1.0.5" type="text/css" media="screen" />
    <script type="text/javascript" src="fancybox/source/helpers/jquery.fancybox-buttons.js?v=1.0.5"></script>
    <script type="text/javascript" src="fancybox/source/helpers/jquery.fancybox-media.js?v=1.0.6"></script>

    <link rel="stylesheet" href="fancybox/source/helpers/jquery.fancybox-thumbs.css?v=1.0.7" type="text/css" media="screen" />
    <script type="text/javascript" src="fancybox/source/helpers/jquery.fancybox-thumbs.js?v=1.0.7"></script>

    
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }

       .fancybox-nav {
            width: 60px;       
        }

        .fancybox-nav span {
            visibility: visible;
            opacity: 0.5;
        }

        .fancybox-nav:hover span {
            opacity: 1;
        }

        .fancybox-next {
            right: -60px;
        }

        .fancybox-prev {
            left: -60px;
        }

        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }

        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            padding-bottom: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        .fancybox-nav {
            width: 60px;       
        }

        .fancybox-nav span {
            visibility: visible;
            opacity: 0.5;
        }

        .fancybox-nav:hover span {
            opacity: 1;
        }

        .fancybox-next {
            right: -60px;
        }

        .fancybox-prev {
            left: -60px;
        }

        
    </style>
    <script type="text/javascript" charset="utf-8">
        $(".fancybox")
            .attr('rel', 'gallery')
            .fancybox({
                openEffect  : 'none',
                closeEffect : 'none',
                nextEffect  : 'none',
                prevEffect  : 'none',
                padding     : 0,
                margin      : [20, 60, 20, 60] // Increase left/right margin
        });
	$(".infos").fancybox({
		maxWidth	: 800,
		maxHeight	: 600,
		fitToView	: false,
		width		: '70%',
		height		: '70%',
		autoSize	: true,
		closeClick	: false,
		openEffect	: 'none',
		closeEffect	: 'none'
	});
        
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>

    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
    <footer class = "text-center">
        <p>All images and trailers are copyright of their respective owners. This website is for display purposes only. It is not meant to be used commercially. </p>
    </footer>
  </body>
</html>
'''

# A single "category" entry html template

category_content = '''
<div class="text-center">
    <h1>{title}</h1>
</div>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center">
    <img src="{poster_image_url}" width="220" height="342">
    <h3>{movie_title}</h3>
    <a role="button" href="#{trailer_youtube_id}" class="infos btn btn-warning" rel="text-gallery">More Info</a>
    <a role="button" class="trails btn btn-danger fancybox fancybox.iframe" href="//www.youtube.com/embed/{trailer_youtube_id}?autoplay=1&wmode=opaque" rel="video-gallery">Watch Trailer</a>
</div>
'''

info_content = '''

<div class="text-center" id={trailer_youtube_id} style="display:none">
    <img src="{poster_image_url}" width="330" height="513">
    <br>
    {cont}
</div>

'''

def create_movie_tiles_content(cont):
    # The HTML content for this section of the page
    content = ''
    for cat in cont:
        content += category_content.format(
            title = cat["name"]
            )
        for item in cat["content"]:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(r'(?<=v=)[^&#]+', item.trailer)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer)
            trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

            # Append the tile for the movie with its content filled in
            content += movie_tile_content.format(
                movie_title=item.title,
                poster_image_url=item.poster,
                trailer_youtube_id=trailer_youtube_id
            )
            content += info_content.format(
                cont = item.show_info(),
                trailer_youtube_id = trailer_youtube_id,
                poster_image_url=item.poster
            )
    return content



def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('index.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
