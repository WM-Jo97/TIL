>  PJT 작성 시 주의!
> 
> * 절대로 코드만 복붙하지 않는다.
> * 후기는 적어도 3줄은 씁시다!
> * 교수님이 안 볼 것 같지만 다 뜯어 봅니다.
> * 제출 당일 23:59분 내로 제출 합시다!
> * readme 없으면 일주일간 박제할 예정입니다. 
>   * 물론 readme 작성도 결국 해주셔야 합니다. 

# 

# PJT 01

### 이번 pjt 를 통해 배운 내용

* WEB이라는 신기한 세계를 알게 되었습니다.

* 반응형 웹을 직접사용해볼 수 있었습니다.

## 01_nav_footer.html

* 요구 사항 :  Navigation Bar
  
  1. Bootstrap Navbar Component를 참고합니다.
  
  2. 스크롤을 하더라도 항상 화면 상단에 고정되어 있습니다.
  
  3. 로고 이미지는 제공된 logo.png를 사용합니다.
  
  4. 로고 이미지는 하이퍼링크 역할도 가능하며 클릭 시 02_home.html로 이동해야 합니다.
  
  5. 내비게이션 메뉴 중 Home, Community는 하이퍼링크 역할도 가능하며 클릭 시 각각
     02_home.html, 03_community.html로 이동해야 합니다.
  
  6. 내비게이션 메뉴 중 Login은 클릭 시 Bootstrap Modal Component가 나타납니다.
     • Modal Component 내부에는 HTML form 요소를 배치합니다.
  
  7. Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록 합니다.
     
     • Footer
     
     1. 스크롤을 하더라도 항상 화면 하단에 고정되어 있습니다.
     2. Footer에 작성된 내용은 수직·수평 가운데 정렬되어 있습니다.

* 결과 : 
  
  ![](C:\Users\saffy\ssafy8\PJT\03_pjt\result\PJT1.PNG)

          ![](C:\Users\saffy\ssafy8\PJT\03_pjt\result\pjt1-1.PNG)

* 문제 접근 방법 및 코드 설명
  
  ```python
  <div class="modal" id="login_modal" tabindex="-1" aria-labelledby="login_moralLabel" aria-hidden="true" data-bs-backdrop="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="login_moralLabel">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row my-1">
              Email address
            </div>
            <div class="row mt-2 mb-0">
              <input type="text">
            </div>
            <div class="row mt-0 mb-2">
              <p class="text-secondary">We'll never share your e-mail wuth anyone else</p>
            </div>
            <div class="row my-1">
              Password
            </div>
            <div class="row my-1">
              <input type="text">
            </div>
            <div class="row my-1">
              <div class="col-1"><input type="checkbox" name="Check me out"></div>
              <div class="col-11 px-0 mx-0">Check me out</div> 
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Submit</button>
          </div>
        </div>
      </div>
    </div>
    <!-- 모달 -->
    <!-- 네비바 -->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top">
      <div class="container-fluid">
        <div class="logo">
          <a class="navbar-brand" href="./02_home.html">
            <img class="" src="./images/logo.png" alt="" width="100%">
          </a>
        </div>
        <button class="navbar-toggler outline-white" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse ms-4" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <a class="ps-2 text-white nav-link active" aria-current="page" href="./02_home.html">Home</a>
            <a class="ps-2 text-white-50 nav-link" href="./03_community.html">Community</a>
            <a class="ps-2 text-white-50 nav-link" href="#login_modal" data-bs-toggle="modal">Login</a>
          </div>
        </div>
      </div>
    </nav>
    <!-- 네비바 -->
    <!-- conbox -->
    <section>
    </section>
  
    <footer class="d-flex justify-content-center my-3 py-3 border-top fixed-bottom">
      Web-bootstrap PJT. by Hongjun
    </footer>
  ```

* 이 문제에서 어려웠던점
  
  * 모달부분이 어려웠습니다. 특히 모달이 배경색 뒤로 가서 클릭이 안먹는 상태였는데 다행히 모달 코드의 위치를 바꾸니 정상 작동했습니다.
  
  * Navbar를 단순히 복사하는 것이 아니라 필요한 부분과 필요없는 부분을 적절히 위치시키는게 어려웠습니다.

* 내가 생각하는 이 문제의 포인트
  
  * 단순히 bootstrap에서 코드를 복사해서 사용하는 것이 아니라 코드가 어떤것을 의미하는지 제대로 알아야 필요한 부분만 사용할 수 있을 것 같습니다.
  
  * 모달을 켜는 스위치코드의 개념을 이해해야할 것 같습니다.

## 

## 02_home.html

- 요구 사항 :• 01_nav_footer.html에서 작성한 Navigation bar & Modal & Footer 코드를
  적절한 위치에 사용합니다.
  
  • Header
  
  1. Bootstrap Carousel Component로 구성합니다.
  2. 이미지는 최소 3장 이상 사용하며 자동으로 전환됩니다.
  
  Section
  
  1. Section 내부의 개별 요소(article)들은 Bootstrap Card Component로 구성합니다.
     • 이미지, 제목, 설명을 포함합니다.
     • 이미지는 제공된 영화 포스터 이미지를 사용합니다.
  2. 개별 요소들은 좌우 일정한 간격을 가집니다. (간격은 자유롭게 설정 가능)
  3. Viewport의 가로 크기가 576px 미만일 경우 한 행에 1개씩 표시됩니다.
  4. Viewport의 가로 크기가 576px 이상일 경우 한 행에 2개 이상 표시됩니다. 
     (자유롭게 설정 가능)
  5. Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록
     합니다.

- 결과 :
  
  ![](C:\Users\saffy\ssafy8\PJT\03_pjt\result\pjt1-2.PNG)
  
  ![](C:\Users\saffy\ssafy8\PJT\03_pjt\result\pjt1-3.PNG)

- 문제 접근 방법 및 코드 설명
  
  ```python
  <body>
  <!-- 01_nav_footer에서 완성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다. -->
   <!-- 모달 -->
   <div class="modal" id="login_modal" tabindex="-1" aria-labelledby="login_moralLabel" aria-hidden="true" data-bs-backdrop="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="login_moralLabel">Modal title</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row my-1">
            Email address
          </div>
          <div class="row mt-2 mb-0">
            <input type="text">
          </div>
          <div class="row mt-0 mb-2">
            <p class="text-secondary">We'll never share your e-mail wuth anyone else</p>
          </div>
          <div class="row my-1">
            Password
          </div>
          <div class="row my-1">
            <input type="text">
          </div>
          <div class="row my-1">
            <div class="col-1"><input type="checkbox" name="Check me out"></div>
            <div class="col-11 px-0 mx-0">Check me out</div> 
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Submit</button>
        </div>
      </div>
    </div>
  </div>
  <!-- 모달 -->
  <!-- 네비바 -->
  <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top">
    <div class="container-fluid">
      <div class="logo">
        <a class="navbar-brand" href="./02_home.html">
          <img class="" src="./images/logo.png" alt="" width="100%">
        </a>
      </div>
      <button class="navbar-toggler outline-white" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse ms-4" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="ps-2 text-white nav-link active" aria-current="page" href="./02_home.html">Home</a>
          <a class="ps-2 text-white-50 nav-link" href="./03_community.html">Community</a>
          <a class="ps-2 text-white-50 nav-link" href="#login_modal" data-bs-toggle="modal">Login</a>
        </div>
      </div>
    </div>
  </nav>
  <!-- 네비바 -->
  <!-- 02_home.html -->
  <header>
    <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="./images/header1.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="./images/header2.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="./images/header3.jpg" class="d-block w-100" alt="...">
        </div>
      </div>
    </div>
  </header>
  <div class="d-flex justify-content-center my-3">
    <h1>Boxoffice</h1>
  </div>
  <div class="container">
    <section class="row">
      <article class="col-12 col-sm-4 my-2">
        <div class="card" style="width: 100%;">
          <img src="./images/movie1.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
      </article>
      <article class="col-12 col-sm-4 my-2">
        <div class="card" style="width: 100%;">
          <img src="./images/movie2.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
      </article>
      <article class="col-12 col-sm-4 my-2">
        <div class="card" style="width: 100%;">
          <img src="./images/movie3.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
      </article>
      <article class="col-12 col-sm-4 my-2">
        <div class="card" style="width: 100%;">
          <img src="./images/movie4.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
      </article>
      <article class="col-12 col-sm-4 my-2">
        <div class="card" style="width: 100%;">
          <img src="./images/movie5.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
      </article>
      <article class="col-12 col-sm-4 my-2">
        <div class="card" style="width: 100%;">
          <img src="./images/movie6.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
      </article>
    </section>
  </div>
  
  <footer class="d-flex justify-content-center my-3 py-3 border-top">
    Web-bootstrap PJT. by Hongjun
  </footer>
  ```

- 이 문제에서 어려웠던점
  
  - 그리드를 이용해 화면 크기에 따라 그리드의 column을 변화시키는 부분

- 내가 생각하는 이 문제의 포인트
  
  - 그리드를 잘 짜면 쉽게 해결이 가능하지만 처음부터 레이아웃 구성을 잘못하게되면 문제가 더 어려워질 것 같습니다.
  - 사진간 간격을 띄울때 마진, 패딩등을 이해하고 사용해야합니다.

## 03_community.html

- 요구 사항 :Aside (게시판 목록)
  
  1. HTML aside 요소로 이루어져 있습니다.
  2. Bootstrap List group Component로 구성합니다.
  3. 내부의 각 항목은 클릭이 가능한 하이퍼링크이지만, URL은 별도로 없습니다.
  4. Viewport의 가로 크기가 992px 미만일 경우
     HTML main 요소 영역 전체만큼의 너비를 가집니다.
  5. Viewport의 가로 크기가 992px 이상일 경우
     HTML main 요소 영역 기준으로 좌측 1/6 만큼의 너비를 가집니다.
  6. Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여
     일치하도록 합니다. 

- Section (게시판)
  
  1. 게시판은 HTML section 요소로 이루어져 있습니다.
  
  2. 게시판은 Viewport의 가로 크기에 따라 전혀 다른 요소를 표시합니다.
     • Viewport의 가로 크기가 992px 미만일 경우
     게시판은 HTML article 요소의 집합으로 표시되며,
     HTML main 요소 영역 전체만큼의 너비를 가집니다.
     • Viewport의 가로 크기가 992px 이상일 경우
     게시판은 Bootstrap Tables Content로 구성되며, 
     HTML main 요소 영역 기준으로 우측 5/6 만큼의 너비를 가집니다.
     
     • Pagination
     
     1. Bootstrap Pagination Component로 구성합니다.
     2. 게시판 하단에 위치하며 너비는 자유롭게 설정합니다.
     3. 자신의 영역 안에서 수평 중앙 정렬되어 있습니다.
     4. 내부의 각 항목은 클릭이 가능한 하이퍼링크이지만, URL은 별도로 없습니다.
  
  결과:
  
  ![](C:\Users\saffy\ssafy8\PJT\03_pjt\result\3-1.PNG)
  
  ![](C:\Users\saffy\ssafy8\PJT\03_pjt\result\3-2.PNG)

- 문제 접근 방법 및 코드 설명
  
  ```python
  <style>
    @media (max-width:992px ) { 
      .table_res{
        display: none;
      } }
  
    @media (min-width:992px ) { 
      .table_res{
        display: block;
      } }
  
    @media (max-width:992px ) { 
      .board_res{
        display: block;
      } }
  
    @media (min-width:992px ) { 
      .board_res{
        display: none;
      } }      
  </style>
  </head>
  <body>
  <!-- 01_nav_footer에서 작성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다. -->
    <!-- 모달 -->
    <div class="modal" id="login_modal" tabindex="-1" aria-labelledby="login_moralLabel" aria-hidden="true" data-bs-backdrop="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="login_moralLabel">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row my-1">
              Email address
            </div>
            <div class="row mt-2 mb-0">
              <input type="text">
            </div>
            <div class="row mt-0 mb-2">
              <p class="text-secondary">We'll never share your e-mail wuth anyone else</p>
            </div>
            <div class="row my-1">
              Password
            </div>
            <div class="row my-1">
              <input type="text">
            </div>
            <div class="row my-1">
              <div class="col-1"><input type="checkbox" name="Check me out"></div>
              <div class="col-11 px-0 mx-0">Check me out</div> 
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Submit</button>
          </div>
        </div>
      </div>
    </div>
    <!-- 모달 -->
    <!-- 네비바 -->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top">
      <div class="container-fluid">
        <div class="logo">
          <a class="navbar-brand" href="./02_home.html">
            <img class="" src="./images/logo.png" alt="" width="100%">
          </a>
        </div>
        <button class="navbar-toggler outline-white" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse ms-4" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <a class="ps-2 text-white nav-link active" aria-current="page" href="./02_home.html">Home</a>
            <a class="ps-2 text-white-50 nav-link" href="./03_community.html">Community</a>
            <a class="ps-2 text-white-50 nav-link" href="#login_modal" data-bs-toggle="modal">Login</a>
          </div>
        </div>
      </div>
    </nav>
    <!-- 네비바 -->
  <!-- 03_community.html -->
  <main>
    <h1 class="my-3 pt-1 ms-4">Community</h1>
    <!-- Aside - 게시판 목록 -->
    <div class="container">
      <div class="row">  
        <aside class="col-lg-2">
          <ul class="list-group ">
            <li class="list-group-item"><a class="text-decoration-none" href="">Boxoffice</a></li>
            <li class="list-group-item"><a class="text-decoration-none" href="">Movies</a></li>
            <li class="list-group-item"><a class="text-decoration-none" href="">Genres</a></li>
            <li class="list-group-item"><a class="text-decoration-none" href="">Actors</a></li>
          </ul>
        </aside>
  
        <!-- Section - 게시판 -->
        <div class="col-lg-10">
          <section class=>
            <div class="table_res">
              <table class="table table-striped">
                <thead class="table-dark">
                  <tr>
                    <th scope="col">영화 제목</th>
                    <th scope="col">글 제목</th>
                    <th scope="col">작성자</th>
                    <th scope="col">작성 시간</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <th scope="row">Great Movie title</th>
                    <td>Best Movie Ever</td>
                    <td>user</td>
                    <td>1minutes ago</td>
                  </tr>
                  <tr>
                    <th scope="row">Great Movie title</th>
                    <td>Movie Test</td>
                    <td>user</td>
                    <td>1minutes ago</td>
                  </tr>
                  <tr>
                    <th scope="row">Great Movie title</th>
                    <td>Movie Test</td>
                    <td>user</td>
                    <td>1minutes ago</td>
                  </tr>
                  <tr>
                    <th scope="row">Great Movie title</th>
                    <td>Movie Test</td>
                    <td>user</td>
                    <td>1minutes ago</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="board_res mt-3 py-2">
              <article class="border-top py-2">
                <h2>Best Movie Ever</h2>
                <h4>Great Movie Title</h4>
                <p>user</p>
                <p>1 minute ago</p>
              </article>
              <article class="border-top py-2">
                <h2>Movie Test</h2>
                <h4>Great Movie Title</h4>
                <p>user</p>
                <p>1 minute ago</p>
              </article>
              <article class="border-top py-2">
                <h2>Movie Test</h2>
                <h4>Great Movie Title</h4>
                <p>user</p>
                <p>1 minute ago</p>
              </article>
            </div>
          </section>
        </div>
      </div>
      <div class="row d-flex justify-content-center">
        <nav aria-label="Page navigation example">
          <ul class="pagination d-flex justify-content-center">
            <li class="page-item"><a class="page-link" href="#">Previous</a></li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>
      </div>  
    </div>
  ```
  
  </main>
  
  <footer class="d-flex justify-content-center my-3 py-3 border-top">
      Web-bootstrap PJT. by Hongjun
    </footer>

- 이 문제에서 어려웠던점
  - 미디어쿼리 사용법을 잘 몰라서 그 부분이 가장 어려웠습니다.
  - 반응형으로 2개의 요소를 동시에 움직이는 부분이 어려웠습니다.
- 내가 생각하는 이 문제의 포인트
  - 반응형 웹이라고해서 어렵게 생각했는데 2개의 화면 중 상황에 맞게 한가지 화면을 보여주는 것에 불과하다는 것을 알게 되었습니다. 이 부분을 알게되면 조금 더 쉽게 문제에 접근할 수 있을 것 같습니다.
  - 2개의 row로 나누는 것이 아니라 1개의 row로 나누고 wrap을 이용해서 2줄로 사용하다가 화면 크기에 따라 1 줄로 사용하는 부분이 포인트인 것 같습니다.



## 4. 선택과제 : 인스타그램 COPY



- 요구 사항 : 최대한 비슷하게 웹 페이지 복사
  
  
  - 결과 : 
    
    ![](C:\Users\saffy\ssafy8\PJT\03_pjt\result\4-1.PNG)
    
    
    
    
    
    
    - 문제 접근 방법 및 코드 설명
      
      ```python
      <body class="bg-light">
          <nav class="navbar navbar-expand-lg bg-white border-bottom">
              <div class="container-fluid d-flex justify-content-between">
                <a class="navbar-brand ct" href="#">
                  <img class="wn" src="./images/insta.svg" alt="">
                </a>
                <form class="d-flex" role="search">
                  <input class="form-control me-2" type="search" placeholder="검색" aria-label="Search">
                </form>
                <form>
                  <button class="btn btn-primary btn-outline-white" type="submit">로그인</button>
                  <button class="btn btn-white text-primary" type="submit">가입하기</button>
                </form>
                </div>
              </div>
          </nav>
      
          <div id="profile" class="container mt-4">
              <div class="row">
                  <div class="col-4 d-flex justify-content-center ms-4">
                      <div class="img_circle">
                          <img src="./images/oooo.png" alt="" class="rounded-circle" width="100%" height="100%"> 
                      </div>
                  </div>
                  <div class="col-7 ms-0 my-4">
                      <h3>Lanscape_0.00^</h3>
                      <div class="d-flex my-2">
                          <div class="me-4 my-2">게시물 425</div> 
                          <div class="mx-4 my-2">팔로워 512</div>
                          <div class="mx-4 my-2">팔로우 266</div>
                      </div>
                      <p>각종 산, 강 사진 찍습니다.</p>
                  </div>
              </div>
              <div class="row d-flex mt-3 mx-3 px-4">
                  <div class="col-1 img_circle_under m-3 px-2 text-center">
                      <div>
                          <img src="./images/movie6.jpg" alt="" class="rounded-circle" height="80px" width="80px">
                          <p class="m-2">1223</p>                    
                      </div>
                  </div>
                  <div class="col-1 img_circle_under m-3 px-2 text-center">
                      <div class="">
                          <img src="./images/movie4.jpg" alt="" class="rounded-circle" height="80px" width="80px">
                          <p class="m-2">1223</p>
                      </div>
                  </div>
                  <div class="col-1 img_circle_under m-3 px-2 text-center">
                      <div class=""> 
                          <img src="./images/movie3.jpg" alt="" class="rounded-circle" height="80px" width="80px">
                      <p class="m-2">1223</p>                    
                      </div>
                  </div>
              </div>
          </div>
          <section class="border-top mx-2">
              <dev class="container-fluid d-flex justify-content-center">
                  <button class="ms-5 my-2 btn btn-light">게시물</button>
                  <button class="ms-5 my-2 btn btn-light">릴스</button>
                  <button class="ms-5 my-2 btn btn-light">동영상</button>
                  <button class="ms-5 my-2 btn btn-light">태그됨</button>
              </dev>
          </section>
          <section class="container">
              <div class="row">
                  <div class="col-4">
                      <div class="img_con overflow-hidden">
                          <img src="./images/movie1.jpg" alt="" width="100%">
                      </div>
                  </div>
                  <div class="col-4">
                      <div class="img_con overflow-hidden">
                          <img src="./images/movie2.jpg" alt="" width="100%">
                      </div>                
                  </div>
                  <div class="col-4">
                      <div class="img_con overflow-hidden">
                          <img src="./images/movie3.jpg" alt="" width="100%">
                      </div>                
                  </div>
              </div>
      
          </section>
      
      
      
        <footer class="d-flex justify-content-center my-3 py-3 border-top">
          Web-bootstrap PJT. by Hongjun
        </footer>

``````

```

```

```



이 문제에서 어려웠던점

- 힌트가 되는 설명 없이 그림만 보고 비슷하게 만든다는 부분이 어려웠습니다.

- 내가 생각하는 이 문제의 포인트
  
  - 웹의 시작과 끝은 그리드를 활용한 레이아웃을 만드는 것인 것 같습니다. 그리드를 더 열심히 공부해서 더 익숙해져야겠습니다.
  - 사진을 원형으로 만들때 rounded-circle 이라는 bootstrap 을 사용할 수 도 있지만 css 로는 만드는 것이 생각보다 쉽지 않았습니다.

-----

....

# 후기

* 웹은 내용 자체는 어려운 개념은 없지만 실제로 실행이 안되는 경우가 많아서 당황스러웠습니다.
* 웹 부분이 생각보다 재미있어서 즐겁게 공부할 수 있었습니다. 벌써 끝나서 조금 아쉽습니다 ㅠㅠ
* 시간이 짧아서 과목평가에 대한 준비가 부족한데 집에서 열심히 복습해야겠습니다.
