from flask import Blueprint,render_template,request
from flaskblog.models import Post,User

main= Blueprint('main',__name__)


@main.route("/")
@main.route("/home")
def home():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
 



@main.route("/list_user")
#@login_required
def list_user():
    page=request.args.get('page',1,type=int)
    users=User.query.paginate(page=page,per_page=5)
    return render_template('list_user.html', users=users)
