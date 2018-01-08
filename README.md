# showerbasket

[![CircleCI](https://circleci.com/gh/showerbugs/showerbasket.svg?style=svg)](https://circleci.com/gh/showerbugs/showerbasket) [![codecov](https://codecov.io/gh/showerbugs/showerbasket/branch/master/graph/badge.svg)](https://codecov.io/gh/showerbugs/showerbasket)

showerbasket은 코쟁이들이 생업에 집중하는 사이에, coinone의 코인들을 basket 투자 방식으로 관리해 자산을 증식시켜주는 고마운 녀석입니다.

## How to use

이 프로젝트는 `python 3.6.3`에서 개발하고 있습니다.

`config.py.template`를 `config.py`로 복사해 api 서버 접근을 위한 변수를 설정합니다.

```sh
$ cp config.py.template config.py
```

```py
# Insert your coinone personal api access token and secret key
COINONE_API_SERVER = 'https://api.coinone.co.kr'
PERSONAL_API_ACCESS_TOKEN = <YOUR_TOKEN>
PERSONAL_API_SECRET_KEY = <YOUR_KEY>
```

pip를 통해 패키지를 설치하고 테스트를 구동합니다.

```sh
$ pip install -r requirements.txt
$ pytest
```