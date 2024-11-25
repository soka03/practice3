『밑바닥부터 시작하는 딥러닝 ❸』
==========================
<p>
<a href="http://www.yes24.com/Product/Goods/95343845"><img src="https://github.com/WegraLee/deep-learning-from-scratch-3/blob/master/cover.jpg" width="150" align=right></a>
</p>

[미리보기](https://preview2.hanbit.co.kr/books/jqlw/#p=1) | [알려진 오류(정오표)](https://docs.google.com/document/d/1_qHrFCrfx5zNOdslAa9rY3Vv1KECLCToHWJNhvn2jDA) | [본문 그림과 수식 이미지 모음 파일](https://github.com/WegraLee/deep-learning-from-scratch-3/raw/refs/heads/master/%EB%B0%91%EB%B0%94%EB%8B%A53%20%EA%B7%B8%EB%A6%BC%EA%B3%BC%20%EC%88%98%EC%8B%9D.zip)

## DeZero 빌드 현황

<p>
<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/dezero_logo.png" width="400px"> </p>

<p>
  <a href="https://pypi.python.org/pypi/dezero"><img
		alt="pypi"
		src="https://img.shields.io/pypi/v/dezero.svg"></a>
  <a href="https://github.com/oreilly-japan/deep-learning-from-scratch-3/blob/master/LICENSE.md"><img
		alt="MIT License"
		src="http://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="https://travis-ci.org/oreilly-japan/deep-learning-from-scratch-3"><img
		alt="Build Status"
		src="https://travis-ci.org/oreilly-japan/deep-learning-from-scratch-3.svg?branch=master"></a>
</p>

『밑바닥부터 시작하는 딥러닝 ❸』에서는 'DeZero'라는 이 책의 오리지널 딥러닝 프레임워크를 만듭니다. DeZero는 파이토치와 텐서플로 2.0 같은 현대적인 프레임워크가 채택한 동적 계산 그래프(Define-by-Run) 방식의 프레임워크입니다. 최소한의 코드로, 하지만 충분히 강력한 프레임워크를 총 5개 고지, 60단계에 걸쳐 점진적으로 완성합니다. 마지막 고지에서는 직접 만든 프레임워크 위에서 VGG16과 LSTM 같은 신경망을 돌려보기도 합니다. 이 과정에서 여러분은 다음과 같은 효과를 얻으실 수 있을 겁니다.
 
* 파이토치, 텐서플로 2.0 같은 현대적인 딥러닝 프레임워크의 동작 원리를 깨우친다.
* 현대적인 딥러닝 프레임워크를 떠받드는 기술과 사상을 들여다본다.
* 딥러닝을 한 차원 깊게 이해한다.
* ‘프레임워크’를 직접 개발해보는 경험을 쌓아, 개발자로서 한 단계 성장한다.
* 유용한 파이썬 프로그래밍 관례를 익힌다.
* 파이토치, 텐서플로 2, 체이너 같은 현대적 프레임워크의 소스 코드를 더욱 쉽게 분석하고 이해할 수 있다.

다음은 DeZero 프레임워크를 구성하는 핵심 클래스들의 관계도입니다.
<a href="https://github.com/WegraLee/deep-learning-from-scratch-3/blob/master/DeZeroClasses.pdf"><img src="https://github.com/WegraLee/deep-learning-from-scratch-3/blob/master/DeZeroClasses.png" width=1000></a>
원서에는 없는 그림으로, 공부하시는 중간에 혹은 책을 다 읽으신 후에 전체 그림을 정리해보시는 데 도움 드리고자 그려봤습니다.

또한 책 마지막 인덱스(찾아보기)에는 'DeZero API 찾아보기'를 따로 분류해놓았으니 소스 코드를 보시다가 해당 책의 설명이 궁금하실 때 활용해주세요.

더 자세한 소개 정보는 다음 문서를 참고하세요.
* *[상세 소개 및 목차](https://docs.google.com/document/d/1nJ9vhQnAnc3yW2OLFBFkv9NvKFuP0igGjgaz9ykCySo/)*

## 파일 구성

|폴더 이름 |설명                         |
|:--        |:--                          |
|[dezero](/dezero)       |DeZero의 소스 코드 |
|[examples](/examples)      |Dezero를 사용한 구현 예    |
|[steps](/steps)|각 단계의 파일（step01.py ~ step60.py）|
|[tests](/tests)|DeZero 단위 테스트|

## 요구사항
소스 코드를 실행하려면 아래의 소프트웨어가 설치되어 있어야 합니다.

- [Python 3.3 이상](https://docs.python.org/3/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

또한 선택사항으로 엔비디아 GPU에서 수행할 수 있는 기능도 제공합니다. 이 경우 다음 라이브러리가 필요합니다.

- [CuPy](https://cupy.chainer.org/) （선택사항）

## 실행 방법

steps 폴더 안의 step01.py, step02.py, ... 파일들이 각 단계에서 작성한 파일에 해당합니다. 실행하려면 프로젝트 루트에서 다음의 python 명령어를 입력합니다.

```
$ python steps/step01.py
$ python steps/step02.py
```

다음과 같이 해당 단계의 디렉터리 안에서 실행할 수도 있습니다.

```
$ cd steps
$ python step31.py
```

## 데모
[examples](/examples) 디렉터리에서 DeZero의 다른 구현 예를 찾아볼 수 있습니다.

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_tanh.png" height="175"/>](https://github.com/oreilly-japan/deep-learning-from-scratch-3/tree/tanh)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_spiral.png" height="175"/>](/examples/spiral.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_gpu.png" height="175"/>](https://colab.research.google.com/github/oreilly-japan/deep-learning-from-scratch-3/blob/master/examples/mnist_colab_gpu.ipynb)

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/gan.gif" height="175"/>](/examples/gan.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/vae.png" height="175"/>](/examples/vae.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/grad_cam.png" height="175"/>](/examples/grad_cam.py)

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/style_transfer.png" height="175"/>](/examples/style_transfer.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/pythonista.png" height="175"/>](https://github.com/oreilly-japan/deep-learning-from-scratch-3/wiki/DeZero%E3%82%92iPhone%E3%81%A7%E5%8B%95%E3%81%8B%E3%81%99)

---

## 팬픽 - 바닷속 딥러닝 어드벤처 (5부작)

<img src="https://github.com/WegraLee/deep-learning-from-scratch-5/blob/main/posters/%E1%84%87%E1%85%A1%E1%84%83%E1%85%A1%E1%86%BA%E1%84%89%E1%85%A9%E1%86%A8%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%8B%E1%85%A5%E1%84%83%E1%85%B3%E1%84%87%E1%85%A6%E1%86%AB%E1%84%8E%E1%85%A5.png?raw=true">

바닷속 세계를 배경으로, 해양 생물들이 자신의 특성과 필요에 맞는 딥러닝 기술을 개발하여 문제를 해결해 나가는 모험을 그린 연작 소설입니다. 《밑바닥부터 시작하는 딥러닝》 시리즈를 읽으신 분은 더 많은 재미를 느끼실 수 있도록 딥러닝 요소들을 곳곳에 삽입하였습니다.

각 편의 주인공과 주제는 다음과 같습니다.

1. **시야를 찾아서**: 쏨뱅이(쏨)가 **이미지 처리 기술**을 개발하여 주변 환경을 선명하게 파악
1. **상어공주**: 괭이상어 공주(꽹)가 **자연어 처리** 기술로 돌고래 왕자와의 사랑을 쟁취
1. **DeZero의 창조자**: 나뭇잎해룡(잎룡)이 **딥러닝 프레임워크**를 만들어 기술 보급과 협업 촉진
1. **제발, 가즈아!**: 가자미(가즈아)가 **심층 강화 학습**으로 먹이가 풍부한 새로운 바다 개척
1. **피쉬카소와 천재의 초상**: 유령실고기(피쉬카소)가 **이미지 생성 모델**로 바닷속 예술계 혁신

<a href="https://www.hanbit.co.kr/channel/series/series_detail_list.html?hcs_idx=34" target="_blank" rel="noopener noreferrer">소설 보러 가기</a>
