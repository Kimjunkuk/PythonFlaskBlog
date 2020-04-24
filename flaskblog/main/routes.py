from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/experience")
def experience():
    return render_template('experience.html', title='Experience')

@main.route("/education")
def education():
    return render_template('education.html', title='Education')

@main.route("/skills")
def skills():
    return render_template('skills.html', title='Skills')

@main.route("/award")
def award():
    return render_template('award.html', title='Award')



