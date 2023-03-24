from django.db import models

# Create your models here.
# 모델 : 데이터베이스를 SQL없이 다루려고 모델을 사용
# => 데이터를 객체화해서 다루겠다.
## 모델 = 테이블 (exel의 한 시트와 같다)
#  모델의 필드 = 테이블의 column (exel의 열: A, B열 등)
#  인스턴스 = 테이블의 레코드 (엑셀의 행)
#  필드의 값(인스턴스의 필드 값) = 데이터 값 (엑셀의 셀에 있는 값)

class Bookmark(models.Model):    # 모델명 첫글자는 대문자. () 안은 상속받는 클래스
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름 : "+self.site_name+", 주소 : "+self.url

# 필드의 종류가 결정하는 것
#  1. 데이터베이스의 column 종류
#  2. 제약 사항( 몇 글자까지, 한글 사용 여부 등)
#  3. Form에 대한 규정('전화번호는 숫자만 넣으세요' 등)

## 모델이 완성되는 과정
# 1. 모델을 만든 것: 데이터베이스에 넣을 데이터를 설계한 단계.
# 2. makemigrations : 모델의 변경내용을 추적해서 기록하는 역할.
# 3. migration : 설계한 내용을 데이터베이스에 반영(테이블 생성). 이후 데이터베이스에 적용함