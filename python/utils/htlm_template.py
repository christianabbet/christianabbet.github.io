
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
                        <span class="icon solid fa-utensils" style="margin-right:16px"></span><span class="title"> Back to menu</span>
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

def get_html_article(style: int, img: str, title: str, npers: int, time_prep: str, time_bake: str, url: str):
    
    article = """
        <article class="style{0}">
        <span class="image">
            <img src="{1}" alt="" />
        </span>
        <a href="{6}">
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
    """.format(style, img, title, npers, time_prep, time_bake, url)
    
    return article

    

def get_html_recipe(url_back: str, title_back: str):
    
    index = """
        <!DOCTYPE HTML>
        <html>
        <head>
            <title>Generic - Phantom by HTML5 UP</title>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
            <link rel="stylesheet" href="../../../assets/css/main.css" />
            <noscript><link rel="stylesheet" href="../../../assets/css/noscript.css" /></noscript>
        </head>
        <body class="is-preload">
        <!-- Wrapper -->
        <div id="wrapper">

            <!-- Header -->
            <header id="header">
                <div class="inner">

                    <!-- Logo -->
                    <a href="{0}" class="logo">
                        <span class="icon solid fa-utensils" style="margin-right:16px"></span><span class="title">Back to {1}</span>
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
                    <li><a href="../../../index.html">Home</a></li>
                    <li><a href="../../../cooking.html">Cooking</a></li>
                </ul>
            </nav>

            <!-- Main -->
            <div id="main">
                <div class="inner">
                    <h1>Vegetable Lasagna</h1>
                    <div class="box alt">
                        <div class="row gtr-uniform">
                            <div class="col-12"><span class="image fit"><img src="../../../images/cooking/veggie/vegetable_lasagna.jpg" alt="" /></span></div>
                        </div>
                    </div>
                    <section>
                        <p style="text-align: center">
                            <span class="icon solid fa-users"></span>
                            <span style="display:inline-block; width: 4px;"></span> 4
                            <span style="display:inline-block; width: 32px;"></span>
                            <span class="icon solid fa-clock"></span>
                            <span style="display:inline-block; width: 4px;"></span> 1h
                            <span style="display:inline-block; width: 32px;"></span>
                            <span class="icon solid fa-fire"></span>
                            <span style="display:inline-block; width: 4px;"></span> 40 min
                        </p>
                    </section>
                    <section>
                        <h2>Ingredients</h2>
                        <h3>Bechamel sauce</h3>
                        <div class="table-wrapper">
                            <table>
                                <colgroup>
                                    <col span="1" style="width: 20%;">
                                    <col span="1" style="width: 80%;">
                                </colgroup>

                                <thead>
                                <tr>
                                    <th>Quantity</th>
                                    <th>Name</th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr>
                                    <td>500 ml</td>
                                    <td>Milk</td>
                                </tr>
                                <tr>
                                    <td>45 g</td>
                                    <td>BUtter</td>
                                </tr>
                                <tr>
                                    <td>45 g</td>
                                    <td>Flour</td>
                                </tr>
                                </tbody>
                            </table>
                        </div>

                        <h3>Lasagna</h3>
                        <div class="table-wrapper">
                            <table>
                                <colgroup>
                                    <col span="1" style="width: 20%;">
                                    <col span="1" style="width: 80%;">
                                </colgroup>

                                <thead>
                                <tr>
                                    <th>Quantity</th>
                                    <th>Name</th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr>
                                    <td>200 g</td>
                                    <td>Squash</td>
                                </tr>
                                <tr>
                                    <td>125 g</td>
                                    <td>Parmesan</td>
                                </tr>
                                <tr>
                                    <td>125 ml</td>
                                    <td>Vegetable stock</td>
                                </tr>
                                <tr>
                                    <td>3</td>
                                    <td>Carrots</td>
                                </tr>
                                <tr>
                                    <td>2</td>
                                    <td>Zucchini</td>
                                </tr>
                                <tr>
                                    <td>1</td>
                                    <td>Onion</td>
                                </tr>
                                <tr>
                                    <td>1</td>
                                    <td>Garlic clove</td>
                                </tr>
                                <tr>
                                    <td>-</td>
                                    <td>Lasagna noodles</td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </section>
                    <section>
                        <hr />
                        <h2>Step 1</h2>
                        In a large bowl, microwave butter during 1 minute. Slowly add flour while stirring.
                        <hr />
                        <h2>Step 2</h2>
                        Bring to a boil milk and allow to cool for a moment. Pour milk in the bowl while stirring. Season.
                        <hr />
                        <h2>Step 3</h2>
                        Microwave again for 1 minute. Preheat oven at 150°C.
                        <hr />
                        <h2>Step 4</h2>
                        Dice and sauté vegetables until slightly golden.
                        <hr />
                        <h2>Step 5</h2>
                        During the last stage add stock and stir. Let reduce.
                        <hr />
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
                            <li><a href="mailto:christian.abbet@epfl.ch" class="icon solid style2 fa-envelope"><span class="label">Email</span></a></li>
                        </ul>
                    </section>
                    <ul class="copyright">
                        <li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
                    </ul>
                </div>
            </footer>

        </div>

        <!-- Scripts -->
        <script src="../../../assets/js/jquery.min.js"></script>
        <script src="../../../assets/js/browser.min.js"></script>
        <script src="../../../assets/js/breakpoints.min.js"></script>
        <script src="../../../assets/js/util.js"></script>
        <script src="../../../assets/js/main.js"></script>

        </body>
        </html>
    """.format(url_back, title_back)
    return index