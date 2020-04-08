from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '57812a6cb7675f5b5316b69a72f856da'

posts = [
    {
        'author': 'Corey',
        'title': 'Bolg post1',
        'content': 'Fist',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Corey',
        'title': 'Bolg post2',
        'content': 'second',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='about')
    #title 의 text가 탭 이름으로 노출됨

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have ben logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            
    return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
    app.run(debug=True)