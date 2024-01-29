
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

    

def get_html_recipe(
    url_back: str, 
    title_back: str, 
    title: str, 
    url_image: str,
    npers: str,
    time_prep: str,
    time_bake: str,
    ingredient_tables: str,
    steps: str,
    ):
                    
    index = """
        <!DOCTYPE HTML>
        <html>
        <head>
            <title>Cooking</title>
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
                    <h1>{2}</h1>
                    <div class="box alt">
                        <div class="row gtr-uniform">
                            <div class="col-12"><span class="image fit"><img src="{3}" alt="" /></span></div>
                        </div>
                    </div>
                    <section>
                        <p style="text-align: center">
                            <span class="icon solid fa-users"></span>
                            <span style="display:inline-block; width: 4px;"></span> {4}
                            <span style="display:inline-block; width: 32px;"></span>
                            <span class="icon solid fa-clock"></span>
                            <span style="display:inline-block; width: 4px;"></span> {5}
                            <span style="display:inline-block; width: 32px;"></span>
                            <span class="icon solid fa-fire"></span>
                            <span style="display:inline-block; width: 4px;"></span> {6}
                        </p>
                    </section>
                    <section>
                        <h2>Ingredients</h2>
                        {7}
                    </section>
                    <section>
                        <hr />
                        {8}
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
    """.format(url_back, title_back, title, url_image, npers, time_prep, time_bake, ingredient_tables, steps)
    
    return index



def get_html_ingredient(title: str, ingredients: list):
    
    
    # Create rows
    str_rows = []
    for row in ingredients:
        str_row = get_html_ingredient_row(amount=row["amount"] + " " + row["unit"], name=row["name"])
        str_rows.append(str_row)
    
    ingredients_table = "\n".join(str_rows)
    table = """
        <h3>{0}</h3>
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
                {1}
                </tbody>
            </table>
        </div>
    """.format(title, ingredients_table)
    
    return table


def get_html_ingredient_row(amount: str, name: str):
        
    row = """
        <tr>
            <td>{0}</td>
            <td>{1}</td>
        </tr>
    """.format(amount, name)
    
    return row


def get_html_step_row(id_step: int, step: str):
    
    row = """
        <h2>Step {0}</h2>
        {1}
        <hr />
    """.format(str(id_step), step)
    
    return row
    
    