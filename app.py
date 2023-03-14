from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)
JWTManager(app)

app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_SECRET_KEY"] = "Nathan04"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=30)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=1)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Nathan04@localhost:3306/karkadb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

Migrate(app, db)

from models.course import Course
from models.chapter import Chapter
from models.lesson import Lesson
from models.topic import Topic
from models.content import Content
from models.mapping_models.course_level import CourseLevel
from models.mapping_models.level_chapter import LevelChapter
from models.mapping_models.chapter_lesson import ChapterLesson
from models.mapping_models.lesson_topic import LessonTopic 
from models.mapping_models.topic_content import TopicContent

from routes.roleRouts import router
from routes.userRoutes import userBlueprint
from routes.authRoutes import authBlueprint
app.register_blueprint(router, url_prefix ='/admin')   
app.register_blueprint(userBlueprint, url_prefix = '/admin/users') 
app.register_blueprint(authBlueprint, url_prefix = '/auth/user')