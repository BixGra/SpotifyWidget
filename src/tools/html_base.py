from src.tools.settings import base_url


BASE = f"""
<!doctype html>
<html lang="en">
<meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet"/>
<link href="{base_url}/src/style/style.css" media="screen" rel="stylesheet" type="text/css"/>
<title>Sandbix - Spotify Widget</title>
</head>
<body>{{body}}</body>
</html>"""

IFRAME = f"""
<!doctype html>
<html lang="en">
<meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
<head>
<link href="{base_url}/src/style/style{{style}}.css" media="screen" rel="stylesheet" type="text/css"/>
<title>Sandbix - Spotify Widget</title>
</head>
<body id="prod" style="background-color: #161616;">{{body}}</body>
</html>"""

PROD = f"""
<!doctype html>
<html lang="en">
<meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="30">
<head>
<title>Sandbix - Spotify Widget</title>
</head>
<body id="prod">{{body}}</body>
</html>"""

CONNECT = f"""<div class="main-connect">
    <div class="connect-title-1 body-text">
        Spotify<span class="bold-text">Widget</span>
    </div>
    <div class="connect-title-2 bold-text h1-text">
        Get started with us
    </div>
    <div class="connect-title-3 small-text">
        Complete this easy step to gain access
    </div>
    <a href="{base_url}/connect">
        <div class="connect-button bold-text rounded">
            Connect to Spotify
        </div>
    </a>
</div>"""

MAIN = f"""<div class="header">
    <div class="header-left">
        <div class="header-title body-text">
            Spotify<span class="bold-text">Widget</span>
        </div>
    </div>
    <div class="header-right">
        <div class="header-about bold-text body-text">
            About
        </div>
    </div>
</div>
<div class="main">
    <div class="main-top">
        <div class="main-title bold-text h1-text">
            Find inspiration and customize your <span class="white-text">Spotify widget</span>
        </div>
        <div class="main-subtitle small-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </div>
    </div>
    <div class="main-bottom">
        <div class="main-info rounded">
            <div class="main-token">
                <div class="token-title bold-text body-text">
                    Your token
                </div>
                <div class="token-item small-text rounded">
                    {{token}}
                </div>
            </div>
            <div class="main-tuto">
                <div class="tuto-title bold-text body-text">
                    How to use SpotifyWidget
                </div>
                <div class="tuto-item small-text rounded">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
                </div>
            </div>
        </div>
        <div class="main-gallery">
            <div class="gallery-item one rounded">
                <div class="gallery-widget rounded">
                    <div class="frame">
                        <iframe height="20%" width="90%" src="{base_url}/examples/iframe/{{gallery_1_id}}"></iframe>
                    </div>
                </div>
                <div class="gallery-bar">
                    <div class="bar-title bold-text body-text">
                        This is the widget name
                    </div>
                    <a href="{base_url}/examples/{{gallery_1_id}}">
                        <div class="bar-button rounded">
                            <img class="button-arrow arrow-1" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                            <img class="button-arrow arrow-2" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                        </div>
                    </a>
                </div>
            </div>
            <div class="gallery-item two rounded">
                <div class="gallery-widget rounded">
                    <div class="frame">
                        <iframe src="{base_url}/examples/iframe/{{gallery_2_id}}"></iframe>
                    </div>
                </div>
                <div class="gallery-bar">
                    <div class="bar-title bold-text body-text">
                        This is the widget name
                    </div>
                    <a href="{base_url}/examples/{{gallery_2_id}}">
                        <div class="bar-button rounded">
                            <img class="button-arrow arrow-1" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                            <img class="button-arrow arrow-2" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                        </div>
                    </a>
                </div>
            </div>
            <div class="gallery-item three rounded">
                <div class="gallery-widget rounded">
                    <div class="frame">
                        <iframe src="{base_url}/examples/iframe/{{gallery_3_id}}"></iframe>
                    </div>
                </div>
                <div class="gallery-bar">
                    <div class="bar-title bold-text body-text">
                        This is the widget name
                    </div>
                    <a href="{base_url}/examples/{{gallery_3_id}}">
                        <div class="bar-button rounded">
                            <img class="button-arrow arrow-1" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                            <img class="button-arrow arrow-2" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                        </div>
                    </a>
                </div>
            </div>
            <div class="gallery-item four rounded">
                <div class="gallery-widget rounded">
                    <div class="frame">
                        <iframe src="{base_url}/examples/iframe/{{gallery_4_id}}"></iframe>
                    </div>
                </div>
                <div class="gallery-bar">
                    <div class="bar-title bold-text body-text">
                        This is the widget name
                    </div>
                    <a href="{base_url}/examples/{{gallery_4_id}}">
                        <div class="bar-button rounded">
                            <img class="button-arrow arrow-1" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                            <img class="button-arrow arrow-2" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                        </div>
                    </a>
                </div>
            </div>
            <div class="gallery-item five rounded">
                <div class="gallery-widget rounded">
                    <div class="frame">
                        <iframe src="{base_url}/examples/iframe/{{gallery_5_id}}"></iframe>
                    </div>
                </div>
                <div class="gallery-bar">
                    <div class="bar-title bold-text body-text">
                        This is the widget name
                    </div>
                    <a href="{base_url}/examples/{{gallery_5_id}}">
                        <div class="bar-button rounded">
                            <img class="button-arrow arrow-1" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                            <img class="button-arrow arrow-2" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                        </div>
                    </a>
                </div>
            </div>
            <div class="gallery-item six rounded">
                <div class="gallery-widget rounded">
                    <div class="frame">
                        <iframe src="{base_url}/examples/iframe/{{gallery_6_id}}"></iframe>
                    </div>
                </div>
                <div class="gallery-bar">
                    <div class="bar-title bold-text body-text">
                        This is the widget name
                    </div>
                    <a href="{base_url}/examples/{{gallery_6_id}}">
                        <div class="bar-button rounded">
                            <img class="button-arrow arrow-1" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                            <img class="button-arrow arrow-2" src="{base_url}/src/img/arrow.png" alt="arrow.png"/>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>"""

ZOOM = f"""
<div class="header">
    <div class="header-left">
        <div class="header-title body-text">
            Spotify<span class="bold-text">Widget</span>
        </div>
    </div>
    <div class="header-right">
        <div class="header-about bold-text body-text">
            About
        </div>
    </div>
</div>
<div class="main-zoom rounded">
    <div class="zoom-widget">
        <div class="zoom-frame frame rounded">
            {{widget}}
        </div>
    </div>
    <div class="zoom-bar">
        <div class="zoom-bar-text bold-text body-text">
            Copy this CSS and paste it in your OBS source, in the <span class="white-text">custom CSS</span> field
        </div>
        <div class="zoom-bar-button bold-text rounded">
            Copy
        </div>
    </div>
    <div class="zoom-text small-text rounded">
        {{css}}
    </div>
</div>
"""

SONG = f"""<div id="song">
    <div class="item-image">
        <img class="image-1" src="{{image}}"/>
    </div>
    <div class="item-1"><p class="text-1">{{text_1}}</p></div>
    <div class="item-sep"><p class="text-sep">-</p></div>
    <div class="item-2"><p class="text-2">{{text_2}}</p></div>
</div>
"""