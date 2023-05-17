# Sad Toys - Sample of Pelican Page-Centered Site
This project is a sample Pelican site which is page-centered; instead of article-centered, that is blog.
The generated site can be seen at [https://muranamihdk.github.io/sad-toys/](https://muranamihdk.github.io/sad-toys/).

## How to make the page-centered site by Pelican
<p><a href="http://docs.getpelican.com/">Pelican</a> is a static site generator written in Python. It has two main types of content: the article and the page. The article is a blog post. The page is a non-chronological content and usually written as a part of the site in advance, e.g. like “About” or “Contact” pages.</p>
<p>Pelican is mainly intended for an article-centered site, that is a blog. Its default settings and themes are suitable for the blogs. If you want to make a page-centered site instead of a blog, you must change some settings and customize templates of your theme.</p>
<p>(This tutorial is written based on Pelican 3.6.3.) </p>
<h3>1. Make a source directory be page-centered</h3>
<p>[Before changes (default)]</p>
<pre>yourproject/
    ├── content/
    │   └──  pages/
    │       ├── yourpage.md
    │       └──  ...
    └── output/
          └──  pages/
              ├── yourpage.html
              └──  ...</pre>
<p>To make a source directory be page-centered, add the following two lines in the pelicanconf.py:</p>
<pre><code class="python">PAGE_PATHS = ['']
ARTICLE_PATHS = ['articles']
</code></pre>
<p>[After changes]</p>
<pre>yourproject/
    ├── content/
    │   ├── yourpage.md
    │   └──  ...
    └── output/
          ├── yourpage.html
          └──  ...</pre>
<p>You can put page sources in <i>content</i> directory instead of <i>content/pages</i> directory.<br />You can use your favorite name for articles directory instead of "articles".</p>
<p>If you want to make blog posts in addition to pages, add the following lines in pelicanconf.py:</p>
<pre><code class="python">PAGE_PATHS = ['']
ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
TAG_URL = 'articles/tag/{slug}.html'
TAG_SAVE_AS = 'articles/tag/{slug}.html'
CATEGORY_URL = 'articles/category/{slug}.html'
CATEGORY_SAVE_AS = 'articles/category/{slug}.html'
AUTHOR_URL = 'articles/author/{slug}.html'
AUTHOR_SAVE_AS = 'articles/author/{slug}.html'
(...etc.)
</code></pre>
<p>In publishconf.py (if you need RSS output):</p>
<pre><code class="python">FEED_ALL_ATOM = 'articles/feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'articles/feeds/%s.atom.xml'
</code></pre>
<p>[After changes]</p>
<pre>yourproject/
    ├── content/
    │   ├── yourpage.md
    │   ├──  ...
    │   └──  articles/
    │       └──  yourblogpost.md
    └── output/
          ├── yourpage.html
          ├──  ...
          └── articles/
              ├── yourblogpost.html
              ├── tag/
              ├── category/
              ├── author/
              └── feeds/</pre>
<h3>2. Make a source directory structure be kept in html output</h3>
<p>[Before changes (default)]</p>
<pre>yourproject/
    ├── content/
    │   ├── yourpage1.md
    │   └── dir1/
    │       ├── yourpage2.md
    │       └──  dir2/
    │           └── yourpage3.md
    └── output/
          ├── yourpage1.html
          ├── yourpage2.html
          └── yourpage3.html</pre>
<p>To make a source directory structure be kept in html output, add the following lines in pelicanconf.py:</p>
<pre><code class="python">PATH_METADATA = '(?P.*)\..*'
PAGE_SAVE_AS = '{path_no_ext}.html'
PAGE_URL = '{path_no_ext}.html'
</code></pre>
<p>[After changes]</p>
<pre>yourproject/
    ├── content/
    │   ├── yourpage1.md
    │   └── dir1/
    │       ├── yourpage2.md
    │       └──  dir2/
    │           └── yourpage3.md
    └── output/
           ├── yourpage1.html
           └── dir1/
               ├── yourpage2.html
               └──  dir2/
                   └── yourpage3.html</pre>
<p>You can keep the hierarchic structure in html output as in <i>content</i> directory.<br />ref. <a href="https://github.com/getpelican/pelican/issues/686">https://github.com/getpelican/pelican/issues/686</a></p>
<p> </p>
<h3>3. Make blog related files be not generated</h3>
<p>[Before changes (default)]</p>
<pre>yourproject/
    ├── content/
    │   └── yourpage.md
    └── output/
          ├── yourpage.html
          ├── index.html
          ├── tags.html
          ├── categories.html
          ├── authors.html
          └── archives.html</pre>
<p>To make blog related files be not generated, add the following lines in pelicanconf.py:</p>
<pre><code class="python">DIRECT_TEMPLATES = []
</code></pre>
<p>[After changes]</p>
<pre>yourproject/
    ├── content/
    │   └── yourpage.md
    └── output/
          └── yourpage.html</pre>
<p>Blog related filles (index.html, tags.html, categories.html, authors.html, archives.html) are not generated.<br /><em>But you must write your "index.html" file yourself instead</em>.</p>
<p>If you want to make blog posts in addition to pages and need blog related files, add the following lines in pelicanconf.py:</p>
<pre><code class="python">DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives']
INDEX_SAVE_AS = 'articles/index.html'
TAGS_SAVE_AS = 'articles/tags.html'
CATEGORIES_SAVE_AS = 'articles/categories.html'
AUTHORS_SAVE_AS = 'articles/authors.html'
ARCHIVES_SAVE_AS = 'articles/archives.html'
</code></pre>
<p>[After changes]</p>
<pre>yourproject/
    ├── content/
    │   ├── yourpage.md
    │   └── articles/
    │       └── yourblogpost.md
    └── output/
          ├── yourpage.html
          └── articles/
              ├── yourblogpost.html
              ├── index.html
              ├── tags.html
              ├── categories.html
              ├── authors.html
              └── archives.html</pre>
<p> </p>
<h3>4. Make pages and categories be not displayed on the global menu of the template</h3>
<p>In pelicanconf.py:</p>
<pre><code class="python">DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
</code></pre>
<p>You must write the global menu yourself instead. In default template, you can this by writing MENUITEMS setting.</p>
<p>In pelicanconf.py:</p>
<pre><code class="python">MENUITEMS = [('Menu1', 'dir1/index.html'), ('Menu2', 'dir2/index.html'), ('Contact', 'contact.html'), ('About', 'about.html')]
</code></pre>
<h3>5. Assign custom templates on a per-page basis (if you need)</h3>
<p>In source file's metadata:</p>
<pre><code class="python">Template: template_name
</code></pre>
<p>If you use reST format, in source file's metadata:</p>
<pre><code class="python">:template: template_name
</code></pre>
<p>You must make your theme contains the relevant template file (e.g. template_name.html).</p>
<p>ref. <a href="http://docs.getpelican.com/en/3.6.3/faq.html#how-do-i-assign-custom-templates-on-a-per-page-basis">http://docs.getpelican.com/en/3.6.3/faq.html#how-do-i-assign-custom-templates-on-a-per-page-basis</a></p>
