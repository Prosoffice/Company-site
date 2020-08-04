import os
import functools
import urllib.request
from uuid import uuid4

import uuid
from PIL import Image
from flask import Flask, render_template, redirect, session, request, url_for, Response, Markup, flash, abort, jsonify, \
    make_response, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_wtf.file import FileAllowed
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache

from flask_wtf import Form, FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FieldList, FormField, PasswordField, BooleanField, \
    FileField, ext
from wtforms.validators import InputRequired, Length
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect



ADMIN_PASSWORD = 'secret'
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'

csrf = CSRFProtect(app)

oembed_providers = bootstrap_basic(OEmbedCache())

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

import models


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'models': models}


@login.user_loader
def load_staff(id):
    return models.Staff.query.get(int(id))


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = ContactForm()
        return render_template("index.html", form=form)
    else:
        contact_form = ContactForm()

        name = contact_form.name.data
        job_title = contact_form.job_title.data
        business_name = contact_form.business_name.data
        email = contact_form.email.data
        subject = contact_form.subject.data
        message = contact_form.message.data

        new_contact = models.Contacts(name=name, job_title=job_title, business_name=business_name, email=email,
                                      subject=subject, message=message)
        models.Contacts.save(new_contact)
        flash("Your message has been sent. Thank you!")
        return redirect("/#contact")




@app.route("/services")
def services():
    return redirect("/#services")


@app.route("/contact")
def contact():
    return redirect("/#contact")


class ContactForm(Form):
    name = StringField('Name', validators=[InputRequired()], render_kw={'placeholder': 'Frank Lewis'})
    job_title = StringField('Job title', validators=[InputRequired()], render_kw={'placeholder': 'Managing Director'})
    business_name = StringField('Business name', validators=[InputRequired()], render_kw={'placeholder': 'Nestle Inc'})
    email = StringField('Email', validators=[InputRequired()], render_kw={'placeholder': 'franklewis@nestle.com'})
    subject = StringField('Project type', validators=[InputRequired()],
                          render_kw={'placeholder': 'Customer Management Platform'})
    message = TextAreaField('Project description', validators=[InputRequired()],
                            render_kw={'placeholder': 'I/We need a ...', 'class': 'form-control', 'rows': 5})


class PostForm(Form):
    title = StringField('Title', validators=[InputRequired(), Length(min=1, max=50)])
    subtitle = StringField('Subtitle', validators=[InputRequired(), Length(min=1, max=50)])
    content = TextAreaField('Say something', validators=[InputRequired(), Length(min=1, max=500000)],
                            render_kw={'class': 'form-control', 'id': "mytextarea"})
    category = StringField('Category')
    featured_image = FileField('Featured image', validators=[InputRequired(), FileAllowed(['jpg', 'png', 'gif'],
                                                                                          'We only accept JPG, PNG or GIF files')])


class CommentForm(Form):
    name = StringField('Name')
    email = StringField('Email')
    website = StringField('Website')
    body = TextAreaField('Comment', validators=[InputRequired(), Length(min=1, max=50000)],
                         render_kw={'class': 'form-control', 'rows': 10})


class LoginForm(Form):
    username = StringField('Username', validators=[InputRequired()], render_kw={'placeholder': 'Username'})
    password = PasswordField('Password', validators=[InputRequired()], render_kw={'placeholder': 'Password'})
    remember_me = BooleanField('Remember me')


class SkillForm(Form):
    language = StringField('Language', validators=[InputRequired()], render_kw={'placeholder': 'HTML'})
    efficiency = IntegerField('Efficiency (%)', validators=[InputRequired()], render_kw={'placeholder': '50', 'type': 'number'})


class ExpertiseForm(Form):
    title = StringField('Title', validators=[InputRequired(),Length(min=2, max=50)] , render_kw={'placeholder':'Front End Dev'})
    ex_details = TextAreaField('Details', validators=[InputRequired(),Length(min=1, max=180)], render_kw={'placeholder':'Tell us more'})


class ExperienceForm(Form):
    e_year = StringField('Year', render_kw={'placeholder': '2010-2012'}, validators=[InputRequired()])
    e_role = StringField('Role', render_kw={'placeholder': 'CEO'}, validators=[InputRequired()])
    e_company = StringField('Company', render_kw={'placeholder': 'Apple'}, validators=[InputRequired()])
    e_details = TextAreaField('Details', render_kw={'placeholder': 'What is the company all about?'}, validators=[InputRequired()])


class EducationForm(Form):
    a_year = StringField('Year', render_kw={'placeholder': '2014-2019'}, validators=[InputRequired()])
    school = StringField('School', render_kw={'placeholder': 'Federal University Of Tech. Owerri'}, validators=[InputRequired()])
    degree = StringField('Degree', render_kw={'placeholder': 'Bachelor of Technology'}, validators=[InputRequired()])
    location = StringField('Location', render_kw={'placeholder': 'Owerri, South-Eastern Nigeria'}, validators=[InputRequired()])
    a_details = TextAreaField('Details', validators=[InputRequired()])


class ProjectsForm(Form):
    url = StringField('Project Url', render_kw={'placeholder':'talktailor.com'})
    image = FileField('Featured Image', render_kw={'placeholder':'Screen shot of homepage'}, validators=[FileAllowed(['jpg', 'png', 'gif'],
                                                                                          'We only accept JPG, PNG or GIF files')])
    nam = StringField('Project Name',render_kw={'placeholder':'GreenVest'})
    date = StringField('Date',render_kw={'placeholder':'19 Sep. 2019'})


class PortfolioForm(Form):
    display_name = StringField('Name', validators=[InputRequired(), Length(min=1, max=50)], render_kw={"placeholder": "Full Name"})
    role = StringField('Role', validators=[InputRequired()], render_kw={"placeholder": "Software Engineer | G.Boy"})
    c_location = StringField('Location', validators=[InputRequired()], render_kw={'placeholder': 'Aba, Nigeria'})
    phone = StringField('Phone', validators=[InputRequired()], render_kw={'placeholder': '+2348000000000'})
    email = StringField('Email', validators=[InputRequired()], render_kw={'placeholder': 'heineken@usolutions.com'})
    about_me = TextAreaField('About me', validators=[InputRequired()],
                             render_kw={'placeholder': 'Considerable amount of content here'})
    expertise = FieldList(FormField(ExpertiseForm), min_entries=2, max_entries=12)
    skill = FieldList(FormField(SkillForm), min_entries=1, max_entries=12)
    experience = FieldList(FormField(ExperienceForm), min_entries=1, max_entries=10)
    education = FieldList(FormField(EducationForm), min_entries=1, max_entries=10)
    projects = FieldList(FormField(ProjectsForm), min_entries=1, max_entries=10)
    facebook = StringField('Facebook', render_kw={'placeholder': 'facebook.com/mikky'})
    linkedin = StringField('Linkedin', render_kw={'placeholder': 'linkedin.com/chinenye'})
    twitter = StringField('Twitter', render_kw={'placeholder': 'twitter.com/ocv'})
    instagram = StringField('Instagram', render_kw={'placeholder': 'instagram.com/ocv'})


@app.route("/staff", methods=["GET", "POST"])
def login():
    """Log user in"""
    db.session.rollback()
    if current_user.is_authenticated:
        return redirect(url_for('edit'))
    form = LoginForm()
    if form.validate_on_submit():
        staff = models.Staff.query.filter_by(username=form.username.data).first_or_404(
            description='No staff with that username')
        if staff is None or staff.password != form.password.data:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(staff, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('edit')
        return redirect(next_page)
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect('/')


@app.route("/edit", methods=['GET', 'POST'])
@login_required
def edit():
    def add_to_database():
        portfolio = models.Portfolio(
            staff_id=id,
            basic={'display_name': form.display_name.data, 'c_location': form.c_location.data,
                   'phone': form.phone.data,
                   'email': form.email.data,
                   'role': form.role.data, 'about_me': form.about_me.data},
            expertise={'data': form.expertise.data},
            skill={'data': form.skill.data},
            experience={'data': form.experience.data},
            education={'data': form.education.data},
            projects={'data': form.projects.data},
            social={'facebook': form.facebook.data, 'linkedin': form.linkedin.data, 'twitter': form.twitter.data,
                    'instagram': form.instagram.data}
        )

        db.session.add(portfolio)
        db.session.commit()
        print("Portfolio added, staff id={}".format(models.Portfolio.staff_id))
        return redirect(url_for('edit'))

    def update_database_entry():
        update = models.Portfolio.query.get(id)
        print('here')
        update.basic = {'display_name': form.display_name.data, 'c_location': form.c_location.data,
                        'phone': form.phone.data,
                        'email': form.email.data, 'role': form.role.data, 'about_me': form.about_me.data}
        print('done basic')
        update.expertise = {'data': form.expertise.data}
        print('done expertise')
        update.skill = {'data': form.skill.data}
        print('done skill')
        update.experience = {'data': form.experience.data}
        print('done experience')
        update.education = {'data': form.education.data}
        print('done education')
        update.projects = {'data': form.projects.data}
        print('done projects')
        update.social = {'facebook': form.facebook.data, 'linkedin': form.linkedin.data,
                         'twitter': form.twitter.data,
                         'instagram': form.instagram.data}
        print('done social')

        db.session.merge(update)
        print('merged')
        db.session.commit()
        print('commited....about to return redirect to /edit')
        return redirect(url_for('edit'))

    id = current_user.id
    form = PortfolioForm()
    username = current_user.username

    if form.validate_on_submit():

        for i in form.projects:
            if i.image.data:
                f = i.image.data
                image_id = str(uuid.uuid4())
                file_name = image_id + '.png'
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
                Image.open(f).save(file_path)
                i.image.data = image_id

        all_data = models.Portfolio.query.all()
        serialized_data = [data.serialize() for data in all_data]

        # If database is empty just add directly cos it wont return id already exist if db is empty
        if not serialized_data:
            try:
                add_to_database()
                flash("Your portfolio has been successfully added/updated")
                return redirect('/edit')
            except Exception as e:
                return str(e)

        # If the database is not empty check if id is there, if not add to database
        elif serialized_data:
            present = False
            for i in serialized_data:
                if id in i.values():
                    present = True
                    break

            if not present:
                try:
                    add_to_database()
                    flash("Your portfolio has been successfully added/updated")
                    return redirect('/edit')
                except Exception as e:
                    return str(e)

            # If control gets here then the id already exist so just update
            else:
                try:
                    print("first")
                    update_database_entry()
                    print("second")
                    print("Porfolio updated, staff id={}".format(id))
                    flash("Your portfolio has been successfully added/updated")
                    return redirect('/edit')
                except Exception as e:
                    print("i am here")
                    return str(e)

    all_data = models.Portfolio.query.all()
    serialized_data = [data.serialize() for data in all_data]
    valid_id = False
    for i in serialized_data:
        if current_user.id in i.values():
            valid_id = True
            break
        else:
            print("No")

    if valid_id:
        staff_port = models.Portfolio.query.filter_by(staff_id=id).first()
        form.display_name.data = staff_port.basic.get('display_name')
        form.role.data = staff_port.basic.get('role')
        form.c_location.data = staff_port.basic.get('c_location')
        form.phone.data = staff_port.basic.get('phone')
        form.email.data = staff_port.basic.get('email')
        form.about_me.data = staff_port.basic.get('about_me')
        form.facebook.data = staff_port.social.get('facebook')
        form.instagram.data = staff_port.social.get('instagram')
        form.twitter.data = staff_port.social.get('twitter')
        form.linkedin.data = staff_port.social.get('linkedin')
    return render_template('edit.html', form=form, name=username, staff_id=current_user.id)


@app.route('/profile/<staff_id>', methods=['GET', 'POST'])
@login_required
def profile(staff_id):
    db.session.rollback()
    all_post = models.Entry.query.filter_by(staff_id=staff_id).all()
    return render_template('profile.html', posts=all_post, staff_id=current_user.id)


@app.route("/about")
def about():
    form = ContactForm()
    return render_template('about.html', form=form)


@app.route("/projects")
def projects():
    form = ContactForm()
    return render_template("projects.html", form=form)


@app.route("/portfolio/<staff_id>")
def portfolio(staff_id):
    port_base = models.Portfolio.query.all()
    serialized_data = [data.serialize() for data in port_base]

    # Search the Database and ensure the Staff username input exist

    port_found = False

    for port_row in serialized_data:
        if int(staff_id) in port_row.values():
            port_found = True
            break

    if port_found:
        staff_portfolio_row = models.Portfolio.query.filter_by(staff_id=staff_id).first()
        port = staff_portfolio_row

        baba = (port.expertise.get('data'))
    

        single = False
        multi = False
        case2 = []
        case3 = []

        if len(baba) == 1:
            single = True
        elif len(baba) > 1:
            multi = True
            next = False
            for i in range(len(baba)):
                if i == 0:
                    case2.append(baba[i])
                    next = True
                else:
                    if next:
                        case3.append(baba[i])
                        next = False
                        continue
                    else:
                        case2.append(baba[i])
                        next = True
                        continue


        skills = (port.skill.get('data'))

        s_single = False
        s_multi = False
        case4 = []
        case5 = []

        if len(skills) == 1:
            s_single = True

        elif len(skills) > 1:
            s_multi = True
            nex = False
            for i in range(len(skills)):
                if i == 0:
                    case4.append(skills[i])
                    nex = True
                else:
                    if nex:
                        case5.append(skills[i])
                        nex = False
                        continue
                    else:
                        case4.append(skills[i])
                        nex = True
                        continue


        return render_template('pportfolio.html', port=port, single=single,multi=multi, s_single=s_single, s_multi=s_multi, case4=case4, case5=case5, case2=case2, case3=case3, staff_id=int(staff_id))
    else:
        return ('Sorry, this staff no longer work with us... GUY GO FILL YOUR PORTFOLIO NAH!')


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        image_id = None

        if form.featured_image.data:
            f = form.featured_image.data
            image_id = str(uuid.uuid4())
            file_name = image_id + '.png'
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
            Image.open(f).save(file_path)


        duplicate_title = False
        all_post = models.Entry.query.all()
        serialized_data = [data.serialize() for data in all_post]
        for i in serialized_data:
            if form.title.data == i['title']:
                duplicate_title = True
                break

        if duplicate_title:
            return 'Sorry, This Post title has already been used. Kindly use another'

        post = models.Entry(title=form.title.data, subtitle=form.subtitle.data, content=form.content.data,
                            author=current_user, featured_image=image_id, category=form.category.data)
        models.Entry.save(post)
        flash('Your post is now live!')
        return redirect(url_for('create'))
    return render_template("test.html", form=form, legend='New Post', submit='Publish', staff_id=current_user.id)


@csrf.exempt
@app.route('/imageuploader', methods=['POST'])
@login_required
def imageuploader():
    file = request.files.get('file')
    if file:

        filename = file.filename.lower()
        img_fullpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        Image.open(file).save(img_fullpath)
        return jsonify({'location': filename})
    flash("Image couldn`t be uploaded")
    return redirect(url_for('uploaded_file'))


@app.route('/blog')
def blog():
    form = ContactForm()
    page = request.args.get('page', 1, type=int)
    posts = models.Entry.query.order_by(models.Entry.timestamp.desc()).paginate(page, app.config['POST_PER_PAGE'],
                                                                                False)
    next_url = url_for('blog', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('blog', page=posts.prev_num) if posts.has_prev else None

    categories = models.Entry.query.with_entities(models.Entry.category).all()
    return render_template('blog.html', posts=posts.items, next_url=next_url, prev_url=prev_url, categories=categories,
                           form=form)


@app.route('/blog/<slug>/', methods=['GET', 'POST'])
def detail(slug):
    comment_form = CommentForm()
    form = ContactForm()
    if request.method == 'GET':
        db.session.rollback()
        selected_post = models.Entry.query.filter_by(slug=slug).first_or_404(description='Post does not exist')
        comments = selected_post.comments
        list_of_comments = [i for i in comments]
        no_of_comments = (len(list_of_comments))
        categories = models.Entry.query.with_entities(models.Entry.category).all()
        return render_template('blog-post.html', post=selected_post, comment_form=comment_form, form=form, slug=slug, comments=comments,
                               no_of_comments=no_of_comments, categories=categories)
    else:
        selected_post = models.Entry.query.filter_by(slug=slug).first()

        if comment_form.validate_on_submit():
            comment = models.Comment(body=comment_form.body.data, name=comment_form.name.data, email=comment_form.email.data,
                                     article=selected_post, website=comment_form.website.data)
            models.Comment.save(comment)
            flash("Your comment has been added to the post", "success")
            return redirect(url_for('detail', slug=slug))


@app.route('/blog/<slug>/update', methods=['GET', 'POST'])
@login_required
def update(slug):
    post = models.Entry.query.filter_by(slug=slug).first()
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        image_id = None

        if form.featured_image.data:
            f = form.featured_image.data
            image_id = str(uuid.uuid4())
            file_name = image_id + '.png'
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
            Image.open(f).save(file_path)

        post.featured_image = image_id
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.content = form.content.data
        post.category = form.category.data

        db.session.merge(post)
        db.session.commit()
        flash("Your post has been updated :)")
        return redirect(url_for('update', slug=slug))

    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.category.data = post.category
        form.subtitle.data = post.subtitle
    return render_template("blog_form.html", form=form, legend='Update Post', submit='Update', staff_id=current_user.id)


@app.route('/blog/<slug>/delete')
@login_required
def delete(slug):
    post = models.Entry.query.filter_by(slug=slug).first()
    return render_template('comingsoon.html', post=post, staff_id=current_user.id)


@app.route('/projects/<project_id>', methods=['GET', 'POST'])
def project_detail(project_id):
    project_id = project_id
    form = ContactForm()
    return render_template('projects-details.html', form=form, project_id=project_id)


@app.route('/blog/announcements')
def announcements():
    flash('Coming soon')
    return redirect('/blog')


if __name__ == '__main__':
    app.run()
