# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).

# 회원
class User:
    # private: 자신의 클래스에서만 접근 가능
    # 1. 외부에서 접근하지 말자!
    # 2. 외부에서 접근할 때 꼭 메소드로 접근하자!

    # private: 자신의 클래스에서만 접근 가능(접근을 제어한다)
    # 앞에다가 언더바 두번 붙이면 private
    # 안 붙이면 퍼블릭
    __user_number = 0

    # 번호, 아이디, 비밀번호, 이름
    def __init__(self, user_id, user_password, user_name):
        # 번호는 자동으로 1씩 증가한다.
        User.__user_number += 1
        self.user_number = User.__user_number
        self.user_id = user_id
        self.user_password = user_password
        self.user_name = user_name

        @staticmethod
        def get_number():
            return User.__user_number

        @classmethod
        def set_admin(cls, **kwargs):
            kwargs['user_id'] = 'admin_' + kwargs['user_id']
            return cls(**kwargs)

    user = User('hds', '1234', '한동석')
    print(user.user_id)

    admin = User.set_admin(user_id='hds', user_password='1234', user_name='한동석')
    print(admin.user_id)

    print(User.get_number())

# staticmethod는 퍼블릭이라 가져다 쓸 수 있게 됨
# 다른 언어에서 파이썬에 있는 걸 접근하기 위해서는 메소드밖에 접근안됨
# 프라이빗을 붙인이유는 다른 곳에서 쓰려구
# 프라이빗을 하면 스테틱메소드로 빼줌(수정하지 말고 가져다가 쓰라는 것)

# 프라이빗 쓰는 이유 2가지
# 1.외부에서 접근하지 말자!
# 2. 외부에서 접근할 때 꼭 메소드로 접근하자!