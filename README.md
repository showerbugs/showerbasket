# showerbasket

[![circleci](https://circleci.com/gh/showerbugs/showerbasket.svg?style=svg)](https://circleci.com/gh/showerbugs/showerbasket) [![codecov](https://codecov.io/gh/showerbugs/showerbasket/branch/master/graph/badge.svg)](https://codecov.io/gh/showerbugs/showerbasket)

showerbasket은 코쟁이들이 생업에 집중하는 사이에, coinone의 코인들을 basket 투자 방식으로 관리해 자산을 증식시켜주는 고마운 녀석입니다.

이 프로젝트는 파이썬 3.6으로 개발하고 있습니다.

## 설정 생성


`config/local.sed` 위치에 파일을 생성하고 민감한 설정값을 `sed` 명령의 포맷에 맞춰 입력합니다.

```sh
s|__ENV_TYPE__|local|g
s|__COINONE_ACCESS_TOKEN__|<access-token>|g
s|__COINONE_SECRET_KEY__|<secret-key>|g
```

다음 명령을 실행하면 `config/config.yml` 파일이 생성됩니다.

```sh
./generate_config.sh
```

애플리케이션이 시작되면 `config/config.yml` 파일을 읽어 객체로 변형합니다.

파이썬 모듈 안에서는 다음과 같이 설정을 사용합니다.

```py
from config import config

print(config.env.type)  # local
```

## 의존성 설치

이 프로젝트의 파이썬 의존성 패키지는 `requirements.txt`로 관리합니다.

```sh
pip install -r requirements.txt
```

## 테스트

이 프로젝트의 테스트는 `pytest`를 이용해서 작성하고 실행합니다.

```sh
pytest
```
