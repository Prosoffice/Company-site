from flask_wtf import Form
from wtforms import StringField, TextAreaField, IntegerField, FieldList, FormField, PasswordField, BooleanField, FileField
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileAllowed






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