
def get_html_index(title: str, articles: str):
    
    index = """
        <!DOCTYPE HTML>
        <html>
        <head>
            <title>Christian Abbet</title>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
            <link rel="stylesheet" href="../assets/css/main.css" />
            <noscript><link rel="stylesheet" href="../assets/css/noscript.css" /></noscript>
        </head>
        <body class="is-preload">
        <!-- Wrapper -->
        <div id="wrapper">

            <!-- Header -->
            <header id="header">
                <div class="inner">


                    <!-- Logo -->
                    <a href="../cooking.html" class="logo">
                        <span class="icon solid fa-carrot" style="margin-right:16px"></span><span class="title"> Cooking</span>
                    </a>


                    <!-- Nav -->
                    <nav>
                        <ul>
                            <li><a href="#menu">Menu</a></li>
                        </ul>
                    </nav>

                </div>
            </header>

        <!-- Menu -->
        <nav id="menu">
            <h2>Menu</h2>
            <ul>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../cooking.html">Cooking</a></li>
            </ul>
        </nav>

        <!-- Main -->
        <div id="main">
            <div class="inner">
                <header>
                    <h1>{0}</h1>
                    <p>Multiple recipes I tried and liked. If existing, the reference to the original website is linked. Enjoy :).</p>
                </header>
                <section class="tiles">

                    {1}

                </section>
            </div>
        </div>

        <!-- Footer -->
        <footer id="footer">
            <div class="inner">
                <section>
                    <h2>Follow</h2>
                    <ul class="icons">
                        <li><a href="https://github.com/christianabbet/" class="icon brands style2 fa-github"><span class="label">GitHub</span></a></li>
                        <li><a href="https://www.linkedin.com/in/christian-abbet-519090142/" class="icon brands style2 fa-linkedin"><span class="label">Linkedin</span></a></li>
                        <li><a href="mailto:abbet.christian@gmail.com" class="icon solid style2 fa-envelope"><span class="label">Email</span></a></li>
                    </ul>
                </section>
                <ul class="copyright">
                    <li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
                </ul>
            </div>
        </footer>

        </div>

        <!-- Scripts -->
        <script src="../assets/js/jquery.min.js"></script>
        <script src="../assets/js/browser.min.js"></script>
        <script src="../assets/js/breakpoints.min.js"></script>
        <script src="../assets/js/util.js"></script>
        <script src="../assets/js/main.js"></script>

        </body>
        </html>
    """.format(title, articles)
    return index

def get_html_article(style: int, img: str, title: str, npers: int, time_prep: str, time_bake: str):
    
    article = """
        <article class="style{0}">
        <span class="image">
            <img src="{1}" alt="" />
        </span>
        <a href="#">
            <h2>{2}</h2>
            <div class="content">
                <p>
                    <span class="icon solid fa-users"></span>
                    <span style="display:inline-block; width: 4px;"></span> <b>{3}</b>
                    <span style="display:inline-block; width: 32px;"></span>
                    <span class="icon solid fa-clock"></span>
                    <span style="display:inline-block; width: 4px;"></span> <b>{4}</b>
                    <span style="display:inline-block; width: 32px;"></span>
                    <span class="icon solid fa-fire"></span>
                    <span style="display:inline-block; width: 4px;"></span> <b>{5}</b>
                </p>
            </div>
        </a>
    </article>
    """.format(style, img, title, npers, time_prep, time_bake)
    
    return article

    