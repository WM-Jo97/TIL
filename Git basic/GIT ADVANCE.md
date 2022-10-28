git 작업 되돌리기

1. working diretory 작업 단계
2. Staging Area 단계
3. Repogitory 단계

Working Directory
- git restore
- 워킹 디렉토리에서 수정한 파일을 수정 전(직전 커밋)으로 되돌리기
- 이미 버젼 관리가 되고있는 파일만 되돌리기 가능
- git restore을 통해 되돌리면 해당 내용을 복원할 수 없음
- 명령어 : git restore {파일 이름}

    임시 보관 : git stash

Staging Area
- root-commit 여부에 따라 두가지 명령어로 나뉨
- root- commit 없는 경우 : git rm --cached
- root- commit 있는 경우 : git restore --staged

    git rm --cached
    (--cached가 없으면 파일 삭제)
    => git 관리되고 있는 file을 더이상 관리하고 싶지 않을때

    git restore --staged
    => 한개 이상의 커밋이 있는 경우


Repogitory 단계에서 수정
- git commit --amend
  - 커밋을 완료한 파일을 Staging Area로 되돌리기
  - 상황별로 2가지 기능으로 나뉨
    - Staging Area에 새로 올라온 내용 없으면 -> 직전 커밋 메세지만 수정
    - 올라온 내용이 있으면 -> 직전 커밋 덮어쓰기
  이전 커밋은 수정하여 새로운 커밋으로 변경 => 이전 커밋은 히스토리에도 남지 않음


git reset
    프로젝트를 특정 커밋(버젼) 상태로 되돌림
    특정 커밋으로 되돌아갔을때 해당 커밋 이후로 쌓았던 커밋들은 모두 사라짐

    git reset [옵션] {커밋 id}
        옵션은 soft, mixed, hard
        --soft => 해당 커밋으로 되돌아가고, 되돌아간 커밋 이후의 파일들은 Staging Area로 돌려놓음

        --mixed => 해당 커밋으로 되돌아가고 되돌아간 커밋 이후의 파을들은 working directory로 돌려놓음 (옵션 설정 안하면 mixed)

        --hard => 해당 커밋으로 되돌아가고 되돌아간 커밋 이후 파일은 모두 working directory에서 삭제

git reflog 
 -> reset 하기 전의 과거 커밋 내역을 모두 조회 가능
 이후 해당 커밋으로 리셋하면 hard 옵션으로 삭제된 파일도 복구 가능

git revert {커밋id}
 -> 커밋을 취소하는 명령어, 
    reset은 커밋 내역을 삭제, revert는 새로운 커밋을 생성
    revert는 github를 통해 협업할 때, 커밋 내역의 차이로 인한 충돌 방지 기능

    문법적 차이
        -> git resest 5sd2f42 : 5sd2f42 라는 커밋으로 되돌린다
        -> git revert 5sd2f42 : 5sd2f42 라는 커밋 한개를 취소한다.
            (5sd2f42 커밋이 취소되었다는 내용의 새로운 커밋을 생성)

git branch
    브랜치는 여래갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와줌

    장점 : 독립 공간을 형성하기 떄문에 원본은 안전

조회 : git branch : 로컬 저장소의 브랜치 목록 확인 , 
       git branch -r 원격 저장소의 브랜치 목록 확인

생성 : git branch {브랜치 이름}
       git branch {브랜치 이름} {커밋id} 특정 커밋 시점에 브랜치 생성

삭제 : git branch -d {브랜치 이름} (병합된 브랜치만 삭제 가능)
       git branch -D {브랜치 이름} (강제 삭제)

git switch {브랜치 이름} : 다른 브랜치로 이동
git switch -c {브랜치 이름} : 브랜치를 생성 및 이동
git switch -c {브랜치 이름} {커밋 id} : 특정 커밋 기준 브랜치 생성 및 이동


git merge
분기된 브랜치를 하나로 합치는 명령어
    git merge {합칠 브랜치 이름}

    메인 브랜치로 스위치 한 후 merge 해야 함
    (원본으로 스위치 한 후 브랜치를 merge 해야 브랜치가 마스터에 합쳐짐)

Merge Conflict
    두 브랜치에서 같은 부분을 수정한 경우
    git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못하여 충돌이 발생
    보통 같은 파일의 같은 부분을 수정했을 때 자주 발생


GIT WORKHOW
    Branch 와 원격 저장소를 이용해 협업을 하는 두가지 방법
    1. 원격 저장소 소유권이 있는 경우 -> Shared repository model
    2. 원격 저장소 소유권이 없는 경우 -> Fork 

    원격 저장소가 자신의 소유이거나 콜라보레이터로 등록되어 있는 경우
    master 브랜치에 직접 개발하는 것이 아니라, 기능별로 브랜치를 따로 만들어 개발
    PULL REQUEST를 사용하여 팀원 간 변경 내용에 대한 소통 진행