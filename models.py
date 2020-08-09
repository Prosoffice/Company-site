from settings import db
import datetime

from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import JSON
from flask_login import UserMixin
import re




class Staff(UserMixin, db.Model):
    __tablename__ = 'staff'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False,)
    full_name = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=False)
    post = db.relationship('Entry', backref='author', lazy='dynamic')

    def __init__(self, username, password, full_name, role, image):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.role = role
        self.image = image

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'full_name': self.full_name,
            'self.role': self.role,
            'self.image': self.image,
            'post': self.post
        }

    def __repr__(self):
        return '<Staff {}>'.format(self.username)


class Portfolio(db.Model):
    __tablename__ = 'portfolio'

    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), primary_key=True)
    basic = db.Column(MutableDict.as_mutable(JSON))
    expertise = db.Column(MutableDict.as_mutable(JSON))
    skill = db.Column(MutableDict.as_mutable(JSON))
    experience = db.Column(MutableDict.as_mutable(JSON))
    education = db.Column(MutableDict.as_mutable(JSON))
    projects = db.Column(MutableDict.as_mutable(JSON))
    social = db.Column(MutableDict.as_mutable(JSON))

    def __init__(self, staff_id, basic, expertise, skill, experience, education, projects, social):
        self.staff_id = staff_id
        self.basic = basic
        self.expertise = expertise
        self.skill = skill
        self.experience = experience
        self.education = education
        self.projects = projects
        self.social = social

    def serialize(self):
        return {
            'staff_id': self.staff_id,
            'basic': self.basic,
            'expertise': self.expertise,
            'skill': self.skill,
            'experience': self.experience,
            'education': self.education,
            'projects': self.projects,
            'social': self.social
        }

    def __repr__(self):
        return '<staff_id {}>'.format(self.staff_id)


class Entry(db.Model):
    __tablename__ = 'entry'
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    slug = db.Column(db.String, unique=True)
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    content = db.Column(db.Text)
    featured_image = db.Column(db.String(36))
    category = db.Column(db.String(50))
    comments = db.relationship('Comment', backref='article', lazy='dynamic')

    def save(self, commit=True):
        if not self.slug:
            self.slug = re.sub('[^\w]+', '-', self.title.lower())
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self


    def serialize(self):
        return {
            'id': self.id,
            'slug': self.slug,
            'title': self.title,
            'subtitle': self.subtitle,
            'timestamp': self.timestamp,
            'content': self.content,
            'featured_image': self.featured_image
        }

    def __repr__(self):
        return '<Entry {}>'.format(self.title)


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    post_slug = db.Column(db.String(500), db.ForeignKey('entry.slug'))
    website = db.Column(db.String(50), nullable=True)

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def __repr__(self):
        return '<Comment {}>'.format(self.id)



class Contacts(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    job_title = db.Column(db.String(150), nullable=False)
    business_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(150), nullable=False)
    message = db.Column(db.String(150), nullable=False)

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def __repr__(self):
        return '<Contact {}>'.format(self.id)