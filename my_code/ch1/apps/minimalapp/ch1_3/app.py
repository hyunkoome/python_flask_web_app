from flask import (
    Flask,
    current_app,
    flash,
    g,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from email_validator import EmailNotValidError, validate_email
import logging, os
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message

app = Flask(__name__)

# SECRET_KEY를 추가한다
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"

# 로그 레벨을 설정한다
app.logger.setLevel(logging.DEBUG)

# if log print
app.logger.critical("fatal error")
app.logger.error("error")
app.logger.warning("warning")
app.logger.info("info")
app.logger.debug("debug")

# 리다이렉트를 중단하지 않도록 한다
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# Mail 클래스의 컨피그를 추가한다
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

# DebugToolbarExtension에 애플리케이션을 세트한다
toolbar = DebugToolbarExtension(app)

# flask-mail 확장을 등록한다
mail = Mail(app)

@app.route("/")
def index():
    return "Hello, Flask, Hyunkoo"

@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    # return f"Hello, {name}"
    return "Hello, {}".format(name)

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

with app.test_request_context():
    # /
    print(url_for("index"))

    # /hello/world
    print(url_for("hello-endpoint", name="world"))

    # /name/Hyunkoo?page=1
    print(url_for("show_name", name="Hyunkoo", page="1"))

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # get values from form
        username = request.form['username']
        email = request.form['email']
        description = request.form['description']

        # 입력 체크
        is_valid = True
        if not username:
            flash("사용자명은 필수입니다")
            is_valid = False

        if not email:
            flash("메일 주소는 필수입니다")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("메일 주소의 형식으로 입력해 주세요")
            is_valid = False

        if not description:
            flash("문의 내용은 필수입니다")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        # send email
        send_email(
            email,
            "문의 감사합니다.",
            "contact_mail",
            username=username,
            description=description,
        )

        # 문의 완료 엔드포인트로 리다이렉트한다
        flash("문의 내용은 메일로 송신했습니다. 문의해 주셔서 감사합니다.")

        # contact 엔드포인트로 리다이렉트한다
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")

def send_email(to, subject, template, **kwargs):
    """메일을 송신하는 함수"""
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)