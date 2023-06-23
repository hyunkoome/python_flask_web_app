from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField


# 이미지 업로드 폼(버튼)
class UploadImageForm(FlaskForm):
    # 파일 업로드에 필요한 밸리데이션을 설정한다
    image = FileField(
        validators=[
            FileRequired("이미지 파일을 지정해 주세요."),
            FileAllowed(["png", "jpg", "jpeg"], "지원되지 않는 이미지 형식입니다."),
        ]
    )
    submit = SubmitField("업로드")


# 이미지 인지(감지) 폼(버튼)
class DetectorForm(FlaskForm):
    submit = SubmitField("감지")


# 이미지 삭제 폼(버튼)
class DeleteForm(FlaskForm):
    submit = SubmitField("삭제")
