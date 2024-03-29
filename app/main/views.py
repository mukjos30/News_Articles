
from flask import render_template
from . import main
from ..request import get_sources,get_articles

 



@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    Source=get_sources('general')
    title = 'News Sources'
    print(Source)
    return render_template('index.html',title=title,sources=Source)

@main.route('/articles/<string:id>')
def source(id):
    """
    View source page function that returns the  sources and their details
    """
    articles= get_articles(id)
    print(articles)
    return render_template('articles.html',articles=articles)
