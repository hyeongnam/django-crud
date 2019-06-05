from django.db import models

# Create your models here.
class Board(models.Model):  # 상속
    # id 는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True)

    # 클래스 변수 => DB의 필드를 나타냄
    # CharField함수는 max_length가 필수요소임
    title = models.CharField(max_length=10)
    # 글자수가 많으면 TextField를 쓰면 된다.
    content = models.TextField()
    # 생성할때만 사용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 인스턴스 출력 형식을 결정
    def __str__(self):
        return f'{self.id}번째 글 - {self.title} : {self.content}'