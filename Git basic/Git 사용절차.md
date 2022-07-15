# Git 기초 사용법

Git으로 프로젝트를 관리하려면

== Git init == 명령어를 이용해야함

Git init을 입력하면
Working directory, Staging area, Repository 가 생성됨

    Working Directory : 작업하는 디렉토리 (폴더) 공간
    Staging Area : 중간 확인하는 공간
    Repository : commit 이 저장되는 공간

------

### Commit 하기 절차
-----
    git status ==> 현재 상태 확인
    git add . ==> 현재 폴더 내 모든 파일을 올림
    git commit -m "커밋 메세지"  <-- 커밋하기
    git status --> 커밋 되었는지 확인

-------
### Git diff

    git diff 코드 6자리 코드 6자리

### Git log --oneline
-------
    
    git log를 한줄로 간략히 표시
-----
### Remote Repository VS local Repository
-----
    local => 컴퓨터 내 저장소
    Remote => git hub와 같은 서버에 저장


### Repository 생성
    Github 에서 생성하고 URL 주소가 곧 레포주소
    별명으로는 대부분 origin 사용

#### Git remote add origin(레포별명) 레포주소
-----
    Repo 주소=(control + c , shift + insert)

    git remote add origin 레포주소
    -> 올라갔는지 확인 : git remote -v

    git push 레포별명 브렌치명(master)

### Git에 올린 파일 내려받기
-----
    git clone 레포주소

### 기준 버젼은 GitHub!
------
    기준을 맞춘 상황에서 + or - 해야함
    --> conflict 상황 발생 가능

    올리는 것 (Github를 업데이트) : PUSH
    받는 것 (Local 환경을 업데이트): PULL

    git pull origin master --> 최신버전을 다운
    일치를 시킨 후에 수정해야 함.

    Remote를 연결한 상태라면 항상 pull을 가장 먼저 해야 함.

    이후에 새로운 내용을 작성했다면
    add -> commit -> push 과정으로 진행

### Clone 과 Pull 의 차이점
    --> 클론은 복제 (.git도 함께 복제)
    -> Pull은 remote repository에 있는 버젼과 동일한 버전으로 다운받는 기능

    -> Clone은 최초 받을때만 사용, 이후로는 push와 pull만 사용