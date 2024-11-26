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
<script src="{base_url}/src/script/script.js"></script>
</html>"""

PROD = f"""
<!doctype html>
<html lang="en">
<meta http-equiv="refresh" content="15">
<head>
<title>Sandbix - Spotify Widget</title>
</head>
<body id="prod">{{body}}</body>
<script src="{base_url}/src/script/script.js"></script>
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

HEADER = f"""<div class="header">
    <a href="{base_url}/">
        <div class="header-left">
            <div class="header-title body-text">
                Spotify<span class="bold-text">Widget</span>
            </div>
        </div>
    </a>
    <a href="{base_url}/about">
        <div class="header-right">
            <div class="header-about bold-text body-text">
                About
            </div>
        </div>
    </a>
</div>"""

MAIN = f"""{HEADER}
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
                    Your widget URL
                </div>
                <div class="token-item small-text rounded">
                    Copy this address and paste it in a new <span class="bold-text">Browser Source</span> in OBS.
                    <div class="main-item-box rounded">
                        <div id="copy-html" class="main-item-box-text">
                            {base_url}/current-song/{{token}}
                        </div>
                        <div id="button-html" class="main-item-box-button rounded" onClick="copy('copy-html', 'button-html', 'main-item-box-button rounded');">
                            <img class="main-item-box-image" src="{base_url}/src/img/copy.png" alt="copy.png"/>
                        </div>
                    </div>
                    You can choose your favorite design and add the CSS code inside the <span class="bold-text">Custom CSS</span> field.
                </div>
            </div>
            <div class="main-tuto">
                <div class="tuto-title bold-text body-text">
                    How to use SpotifyWidget
                </div>
                <div class="tuto-item small-text rounded">
                    If you'd like to interact with the data, you can get the <span class="bold-text">JSON output</span>
                    on this url.
                    <div class="main-item-box rounded">
                        <div id="copy-json" class="main-item-box-text">
                            {base_url}/current-song/{{token}}/json
                        </div>
                        <div id="button-json" class="main-item-box-button rounded" onClick="copy('copy-json', 'button-json', 'main-item-box-button rounded');">
                            <img class="main-item-box-image" src="{base_url}/src/img/copy.png" alt="copy.png"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="main-gallery">
            <div class="gallery-item one rounded">
                <div class="gallery-widget rounded">
                    <div class="frame">
                        <iframe src="{base_url}/examples/iframe/{{gallery_1_id}}"></iframe>
                    </div>
                </div>
                <div class="gallery-bar">
                    <div class="bar-title bold-text body-text">
                        {{gallery_1_name}}
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
                        {{gallery_2_name}}
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
                        {{gallery_3_name}}
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
                        {{gallery_4_name}}
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
                        {{gallery_5_name}}
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
                        {{gallery_6_name}}
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
</div>
<script src="{base_url}/src/script/copy.js"></script>"""

EXAMPLE = f"""{HEADER}
<div class="main-zoom rounded">
    <div class="zoom-widget">
        <div class="zoom-frame frame rounded">
            <iframe src="{base_url}/examples/iframe/{{index}}"></iframe>
        </div>
    </div>
    <div class="zoom-bar">
        <div class="zoom-bar-text bold-text body-text">
            Copy this CSS and paste it in your OBS source, in the <span class="white-text">custom CSS</span> field
        </div>
        <div id="button-css" class="zoom-bar-button bold-text rounded" onClick="copy('copy-css', 'button-css', 'zoom-bar-button-clicked bold-text rounded');">
            Copy
        </div>
    </div>
    <div id="copy-css" class="zoom-text small-text rounded">
        {{css}}
    </div>
</div>
<script src="{base_url}/src/script/copy.js"></script>"""

SONG = f"""<div id="song">
    <div class="album-container">
        <img class="album" src="{{album}}"/>
    </div>
    <div class="info-container">
        <div class="name-container"><p class="name">{{name}}</p></div>
        <div class="separator-container"><p class="separator">-</p></div>
        <div class="artists-container"><p class="artists">{{artists}}</p></div>
    </div>
</div>"""