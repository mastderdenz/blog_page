# Blog Project

This project is a blog platform built with **Python**, **Django** as the backend framework, and **HTML** for rendering pages, using Bootstrap for styling and layout. Below is an overview of the HTML structure used in the project.

The HTML in this blog project focuses on delivering a **responsive, user-friendly** interface, ensuring compatibility across different devices. Bootstrap components are integrated for consistent styling and layout flexibility.

## HTML Structure

#### Key Features:

-	**Semantic HTML:** HTML5 semantic elements like `<header>`, `<nav>`, `<main>`, and `<footer>` are used to improve readability and SEO.
  
-	**Navigation Bar:** A responsive navbar is implemented using Bootstrap’s navigation components. It includes links to the home page, blog posts, and user authentication (login/sign-up).

```HTML
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="{% url 'home' %}">Blog</a>
    <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
            <li class="nav-item"><a class="nav-link" href="{% url 'login' %}">Login</a></li>
            <li class="nav-item"><a class="nav-link" href="{% url 'sign-up' %}">Sign Up</a></li>
        </ul>
    </div>
</nav>
```

- **Post Display:** Blog posts are displayed in a Bootstrap card layout. Each card contains the post title, author, date, and a brief excerpt with a “read more” link.

```HTML
<div class="card my-3">
    <div class="card-body">
        <h5 class="card-title">{{ post.title }}</h5>
        <h6 class="card-subtitle mb-2 text-muted">By {{ post.author }} on {{ post.date_posted }}</h6>
        <p class="card-text">{{ post.content|slice:":200" }}...</p>
        <a href="{% url 'post-detail' post.id %}" class="btn btn-primary">Read More</a>
    </div>
</div>
```
- **Form Handling:** Forms for creating and editing posts, as well as login and signup, are rendered using Django’s built-in form system with Bootstrap styling for form controls.
```HTML
<form method="POST" action="">
    {% csrf_token %}
    <div class="form-group">
        <label for="title">Post Title</label>
        <input type="text" class="form-control" id="title" name="title" value="{{ form.title.value }}">
    </div>
    <div class="form-group">
        <label for="content">Content</label>
        <textarea class="form-control" id="content" name="content">{{ form.content.value }}</textarea>
    </div>
    <button type="submit" class="btn btn-success">Submit</button>
</form>
```
- **Authentication Pages:** Login and sign-up pages are created using Bootstrap forms, ensuring a smooth user experience across different devices.
```HTML
<form method="POST">
    {% csrf_token %}
    <div class="form-group">
        <label for="email">Email address</label>
        <input type="email" class="form-control" id="email" name="email" placeholder="Enter email">
    </div>
    <div class="form-group">
        <label for="password">Password</label>
        <input type="password" class="form-control" id="password" name="password" placeholder="Password">
    </div>
    <button type="submit" class="btn btn-primary">Login</button>
</form>
```
- **Comment Section:** Comments under blog posts are displayed using a simple list layout, with an input form for adding new comments. Each comment shows the author’s name and the date it was posted.
```HTML
<div class="comment-section">
    <h5>Comments</h5>
    <ul class="list-group">
        {% for comment in comments %}
        <li class="list-group-item">
            <strong>{{ comment.author }}</strong> - {{ comment.date_posted }}
            <p>{{ comment.content }}</p>
        </li>
        {% endfor %}
    </ul>
    <form method="POST">
        {% csrf_token %}
        <div class="form-group">
            <label for="content">Add a comment</label>
            <textarea class="form-control" id="content" name="content"></textarea>
        </div>
        <button type="submit" class="btn btn-secondary">Post Comment</button>
    </form>
</div>
```

## Python Code

The Python code in this blog project is built using Django as the web framework, leveraging its powerful features for handling backend logic, data management, and user authentication. This ensures a robust, scalable, and secure application.

#### Key Features:

1. **Flask App Configuration and Setup**  
The app is initialized in the `create_app()` function, which configures Flask, sets up the database using **SQLAlchemy**, and initializes **Flask-Login**.
```python
app = Flask(__name__)
app.config['SECRET_KEY'] = "spencer1010"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{D_B}'
db.init_app(app)
```
2. **Database Models**  
The project defines several models (`User`, `Post`, `Comment`, `Like`) using SQLAlchemy, establishing relationships between them. This structure supports data management and retrieval in the blog.
```python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(150), unique=False)
    # Relationships with posts, comments, and likes
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    likes = db.relationship('Like', backref='user', passive_deletes=True)
```

3.	**User Authentication**  
Flask-Login is integrated to manage user sessions. The login and `sign_up` routes handle user login and registration, respectively, with password hashing for security.
```python
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Handle invalid login
```
4.	**Routing and Views**  
The app uses Flask’s routing system to define various views, allowing users to interact with posts, comments, and their profiles. This setup ensures a seamless user experience throughout the blog.
```python
@ui.route("/")
@ui.route("/home")
@login_required
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)
```
5.	**Form Validation**  
Custom functions validate user input for email and password during signup and login processes, ensuring adherence to specified criteria for security and data integrity.
```python
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

## Final Image

This section highlights the completed blog platform interface, emphasizing the user experience and interaction features. It showcases the layout for posts, comments, and user interactions of the application. The design combines functionality and style, demonstrating how users can easily navigate, create posts, and engage with content, all while enjoying a seamless and appealing interface.
<img src="https://github.com/user-attachments/assets/b64e41c4-740f-44bf-be3c-973308479d18" alt="Description of first image" width="400">
<img src="https://github.com/user-attachments/assets/ab4f10bc-ebcb-41bc-b81e-22ec5f6eb2f2" alt="Description of second image" width="400">
<img src="https://github.com/user-attachments/assets/3df2e59a-a096-4b56-a163-02056e205088" alt="Description of third image" width="400">


