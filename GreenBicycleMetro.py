from flask import (
    Flask,
    render_template,
    render_template_string,
    redirect)
from datetime import datetime
import random

app = Flask("GreenBicycle-Metro")

STATIONS = {
    "Ga Bến Thành": {
        "bikes": 35,
        "image": "benthanh.jpg"
    },
    "Ga Nhà hát Thành phố": {
        "bikes": 30,
        "image": "nhahat.jpg"
    },
    "Ga Ba Son": {
        "bikes": 25,
        "image": "bason.jpg"
    },
    "Ga Công viên Văn Thánh": {
        "bikes": 10,
        "image": "vanthanh.jpg"
    },
    "Ga Tân Cảng": {
        "bikes": 25,
        "image": "tancang.jpg"
    },
    "Ga Thảo Điền": {
        "bikes": 15,
        "image": "thaodien.jpg"
    },
    "Ga An Phú": {
        "bikes": 15,
        "image": "anphu.jpg"
    },
    "Ga Rạch Chiếc": {
        "bikes": 15,
        "image": "rachchiec.jpg"
    },
    "Ga Phước Long": {
        "bikes": 15,
        "image": "phuoclong.jpg"
    },
    "Ga Bình Thái": {
        "bikes": 15,
        "image": "binhthai.jpg"
    },
    "Ga Thủ Đức": {
        "bikes": 15,
        "image": "thuduc.jpg"
    },
    "Ga Khu Công nghệ cao": {
        "bikes": 30,
        "image": "khucnghecao.jpg"
    },
    "Ga Đại học Quốc gia": {
        "bikes": 35,
        "image": "dhquocgia.jpg"
    },
    "Ga Bến xe Suối Tiên": {
        "bikes": 20,
        "image": "suoitien.jpg"
    }
}

STATION_NAMES = {

    "Ga Bến Thành": [
        "Ga Metro Bến Thành",
        "Công viên Tao Đàn",
        "Ngã năm Cống Quỳnh",
        "Trường Đại học Văn Lang CS1"
    ],

    "Ga Nhà hát Thành phố": [
        "Ga Metro Nhà hát Thành phố",
        "Nhà thờ Đức Bà",
        "Bảo tàng Chứng tích Chiến tranh",
        "Bến Bạch Đằng"
    ],

    "Ga Ba Son": [
        "Ga Metro Ba Son",
        "Khu đô thị mới Thủ Thiêm",
        "Thảo Càm Viên",
        "Vòng xoay Điện Biên Phủ"
    ],

    "Ga Công viên Văn Thánh": [
        "Ga Metro công viên Văn Thánh",
        "Khu du lịch Văn Thánh",
        "Ngã tư Hàng Xanh",
        "Đại học HUTECH"
    ],

    "Ga Tân Cảng": [
        "Ga Metro Tân Cảng",
        "Vinhomes Tân Cảng",
        "Trường Đại Học Giao Thông Vận Tải TPHCM CS1",
        "Cư xá Thanh Đa"
    ],

    "Ga Thảo Điền": [
        "Ga Metro Thảo Điền",
        "Khu biệt thự Thảo Điền",
        "Trường Đại Học Giao Thông Vận Tải TPHCM CS2",
        "Vòng xoay Lương Định Của"
    ],

    "Ga An Phú": [
        "Ga Metro An Phú",
        "Khu đô thị An Phú",
        "Estella Place",
        "Khu đô thị An Phú An Khánh"
    ],

    "Ga Rạch Chiếc": [
        "Ga Metro Rạch Chiếc",
        "Chung cư The Vista",
        "Chung cư Imperia An Phú",
        "The Global City"
    ],

    "Ga Phước Long": [
        "Ga Metro Phước Long",
        "Cảng Phước Long",
        "Cao Đẳng Kinh Tế Đối Ngoại TPHCM",
        "Chợ Phước Bình"
    ],

    "Ga Bình Thái": [
        "Ga Metro Bình Thái",
        "Cảng Phúc Long",
        "Cao Đẳng Công Thương TPHCM",
        "Đình Phong Phú"
    ],

    "Ga Thủ Đức": [
        "Ga Metro Thủ Đức",
        "Vincom Thủ Đức",
        "Chợ Thủ Đức",
        "Phân hiệu Trường Đại học GTVT tại TPHCM"
    ],

    "Ga Khu Công nghệ cao": [
        "Ga Metro Khu Công nghệ cao",
        "FPT Software",
        "Trường Đại học FPT TPHCM",
        "Khu chế xuất Linh Trung"
    ],

    "Ga Đại học Quốc gia": [
        "Ga Metro Đại học Quốc gia",
        "Trường Đại học Nông Lâm TPHCM",
        "Nhà Văn hóa Sinh viên TPHCM",
        "Trung tâm Nghiên cứu Tiên Tiến"
    ],

    "Ga Bến xe Suối Tiên": [
        "Ga Metro Bến xe Suối Tiên",
        "Chợ Bình An",
        "Du lịch Sinh thái Bình Châu",
        "Cầu Đồng Nai"
    ]
}

STATION_DESC = {

    "Ga Bến Thành": [
        "Phía trên Ga Metro",
        "Cổng chính công viên Tao Đàn",
        "Cổng chính chợ Thái Bình",
        "Kế bên cổng chính trường"
    ],

    "Ga Nhà hát Thành phố": [
        "Phía trên ga Metro",
        "Kế bên mặt chính nhà thờ",
        "Cổng chính bảo tàng",
        "Phía trước cổng chính"
    ],

    "Ga Ba Son": [
        "Phía trên ga Metro",
        "Chân cầu Ba Son phía Thủ Đức",
        "Cổng chính Thảo Cầm Viên",
        "Chân cầu Điện Biên Phủ phía đường Nguyễn Bỉnh Khiêm"
    ],

    "Ga Công viên Văn Thánh": [
        "Phía trên ga Metro",
        "Cổng chính khu du lịch Văn Thánh",
        "Ngay vòng xoay phía đường Xô Viết Nghệ Tĩnh",
        "Cổng chính Đại học HUTECH"
    ],

    "Ga Tân Cảng": [
        "Phía dưới ga Metro",
        "Ngay chân Landmark 81",
        "Cổng chính trường UTH CS1",
        "Chân cầu kinh phía đường Xô Viết Nghệ Tĩnh"
    ],

    "Ga Thảo Điền": [
        "Phía dưới ga Metro",
        "Cổng chính khu biệt thự cao cấp Thảo Điền 2",
        "Cổng chính trường UTH CS2",
        "Đầu đường Quốc Hương"
    ],

    "Ga An Phú": [
        "Phía dưới ga Metro",
        "Cổng chính khu dân cư An Phú đường Lotus Rd",
        "Trước trung tâm Estella Placei",
        "Kế bên bệnh viện quốc tế CARMEL"
    ],

    "Ga Rạch Chiếc": [
        "Phía dưới ga Metro",
        "Trước cổng tòa Tower 5 đường Giang Văn Minh",
        "Trước cổng chính chung cư đường Lồ Bắc",
        "Ngay vòng xoay trung tâm đường Liên Phường với D3"
    ],

    "Ga Phước Long": [
        "Phía dưới ga Metro",
        "Ngay ngã 3 đầu đường số 1 với nhà máy điện",
        "Cổng chính trường trên đường Đại Lộ 3",
        "Kế bên cổng chính chợ Phước Bình"
    ],

    "Ga Bình Thái": [
        "Phía dưới ga Metro",
        "Đường số 1 phía trước đường vào cảng",
        "Cổng chính trường trên đường Tăng Nhơn Phú",
        "Xa lộ Hà Nội"
    ],

    "Ga Thủ Đức": [
        "Phía dưới ga Metro",
        "Kế bên cổng chính Vincom Thủ Đức",
        "Ngay vòng xoay đầu chợ",
        "Cổng chính trường trên đường Lê Văn Việt"
    ],

    "Ga Khu Công nghệ cao": [
        "Phía dưới ga Metro",
        "Cổng chính FPT Software",
        "Cổng chính trường trên đường D1",
        "Kế bên điểm đón khách tuyến cố định"
    ],

    "Ga Đại học Quốc gia": [
        "Phía dưới ga Metro",
        "Cổng chính trường Đại học Nông Lâm",
        "Cổng chính nhà Văn hóa Sinh viên TPHCM",
        "Cổng chính trung tâm Nghiên cứu Tiên Tiến"
    ],

    "Ga Bến xe Suối Tiên": [
        "Phía dưới ga Metro",
        "Kế bên cổng chính chợ Bình An",
        "Cổng chính du lịch Sinh thái Thủy Châu",
        "Dưới chân cầu phía TPHCM"
    ]
}

IMAGE_PREFIX = {
    "Ga Bến Thành": "bt",
    "Ga Nhà hát Thành phố": "nh",
    "Ga Ba Son": "bs",
    "Ga Công viên Văn Thánh": "vt",
    "Ga Tân Cảng": "tc",
    "Ga Thảo Điền": "td",
    "Ga An Phú": "ap",
    "Ga Rạch Chiếc": "rc",
    "Ga Phước Long": "pl",
    "Ga Bình Thái": "bth",
    "Ga Thủ Đức": "thuduc",
    "Ga Khu Công nghệ cao": "cnc",
    "Ga Đại học Quốc gia": "dhqg",
    "Ga Bến xe Suối Tiên": "st"
}

bike_stations = []
station_id = 1

for metro_name, metro_info in STATIONS.items():

    bikes_per_station = metro_info["bikes"] // 4

    for index in range(4):

        bike_stations.append(
            {
            "id": station_id,
            "metro": metro_name,
            "name": STATION_NAMES[metro_name][index],
            "desc": STATION_DESC[metro_name][index],
            "bikes": bikes_per_station,
            "image": f"{IMAGE_PREFIX[metro_name]}_{index + 1}.jpg"
            }
        )

        station_id += 1


current_total = sum(station["bikes"] for station in bike_stations)

while current_total < 300:
    random.choice(bike_stations)["bikes"] += 1
    current_total += 1


rent_info = None
available_bikes = list(range(1, 301))

def get_period():

    current_hour = datetime.now().hour

    if 5 <= current_hour < 9:
        return "Cao điểm sáng"

    if 16 <= current_hour < 19:
        return "Cao điểm chiều"

    return "🕒 Bình thường"


def adjust_bikes():

    period = get_period()

    morning_stations = {
        "Ga Thủ Đức",
        "Ga Khu Công nghệ cao",
        "Ga Đại học Quốc gia",
        "Ga Bến xe Suối Tiên"
    }

    afternoon_stations = {
        "Ga Bến Thành",
        "Ga Nhà hát Thành phố",
        "Ga Ba Son"
    }

    for station in bike_stations:

        if (
            period == "Cao điểm sáng"
            and station["metro"] in morning_stations
        ):
            station["bikes"] += 2

        elif (
            period == "Cao điểm chiều"
            and station["metro"] in afternoon_stations
        ):
            station["bikes"] += 2


METRO_HTML = """

<!DOCTYPE html>
<html>

<head>

<title>Green Bicycle - Metro</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
}

body::before{
    content:"";
    position:fixed;
    inset:0;

    background:
        url('{{ url_for("static", filename="images/metro_nen2.jpg") }}')
        center/cover no-repeat;

    filter:blur(5px);
    opacity:.5;

    z-index:-1;
}

a{
    text-decoration:none;
}

.title{
    display:flex;
    align-items:center;
    justify-content:center;

    width:fit-content;

    margin:20px auto;
    padding:15px 35px;

    border:3px solid rgba(255,255,255,.8);
    border-radius:20px;

    background:rgba(0,0,0,.25);
    backdrop-filter:blur(10px);

    color:#fff;

    font-size:70px;
    font-weight:700;
}

.title img{
    height:1em;
    width:auto;
    margin-right:15px;
}

.dashboard{
    display:flex;
    justify-content:center;
    gap:20px;

    margin-bottom:40px;
}

.stat-card{
    width:180px;

    padding:20px;

    border-radius:20px;

    background:rgba(255,255,255,.15);
    backdrop-filter:blur(12px);

    color:#fff;
    text-align:center;

    font-size:70px;
    font-weight:700;

    box-shadow:
        0 5px 20px rgba(0,0,0,.2);
}

.stat-card span{
    display:block;

    margin-top:10px;

    font-size:28px;
}

.metro-card{
    width:85%;
    margin:auto;

    overflow:hidden;

    border-radius:25px;
    border:2px solid rgba(255,255,255,.6);

    background:#fff;
    backdrop-filter:blur(10px);

    box-shadow:
        0 15px 40px rgba(0,0,0,.25),
        0 5px 15px rgba(0,0,0,.15);

    transition:
        transform .25s ease,
        box-shadow .25s ease;
}

.metro-card:hover{
    transform:translateY(-5px);

    box-shadow:
        0 20px 40px rgba(0,0,0,.4);
}

.metro-image{
    width:100%;
    height:750px;

    display:block;

    object-fit:cover;

    filter:
        contrast(1.05)
        saturate(1.1);
}

.metro-info{
    padding:25px 25px 40px;

    text-align:center;
    color:#fff;

    background:
        linear-gradient(
            180deg,
            #35c85a,
            #28a745
        );
}

.metro-info h2{
    font-size:60px;
    letter-spacing:1px;

    text-shadow:
        0 3px 8px rgba(0,0,0,.25);
}

.metro-info p{
    margin:10px 0;
    font-size:45px;
}

.menu-btn{
    position:fixed;

    top:20px;
    right:20px;

    width:70px;
    height:70px;

    display:flex;
    justify-content:center;
    align-items:center;

    border-radius:18px;

    background:rgba(40,167,69,.95);
    backdrop-filter:blur(20px);

    color:#fff;
    font-size:42px;

    cursor:pointer;
    z-index:1000;

    box-shadow:
        0 8px 20px rgba(0,0,0,.2);
}

.side-menu{
    position:fixed;

    top:0;
    right:-350px;

    width:300px;
    height:100vh;

    background:#28a745;

    padding-top:100px;

    transition:right .3s ease;

    z-index:999;
}

.side-menu a{
    display:block;

    padding:20px 30px;

    color:#fff;

    font-size:30px;
    font-weight:700;
}

.side-menu a:hover{
    background:rgba(255,255,255,.15);
}

.service-box,
.intro-box{
    display:none;

    position:fixed;

    top:100px;
    left:20px;

    width:650px;

    padding:35px;

    border-radius:25px;

    background:#fff;

    box-shadow:
        0 15px 40px rgba(0,0,0,.25);

    z-index:1001;
}

.service-box{
    color:#333;
}

.service-box h3,
.intro-box h3{
    margin-bottom:25px;

    color:#28a745;

    text-align:center;

    font-size:42px;
    font-weight:700;
}

.service-box table{
    width:100%;

    border-collapse:collapse;
}

.service-box th{
    padding:18px;

    background:#28a745;

    color:#fff;

    font-size:28px;
}

.service-box td{
    padding:18px;

    font-size:26px;

    border-bottom:
        1px solid #ddd;
}

.service-box tr:nth-child(even){
    background:#f8f8f8;
}

.intro-box p{
    color:#444;

    font-size:28px;

    line-height:1.8;
}

.footer{
    position:fixed;

    left:0;
    right:0;
    bottom:15px;

    text-align:center;

    color:#fff;

    font-size:22px;
    font-weight:700;

    text-shadow:
        0 2px 10px rgba(0,0,0,.5);
}

#splash-screen{
    position:fixed;
    inset:0;

    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;

    background:
    linear-gradient(
        rgba(255,255,255,.95),
        rgba(255,255,255,.95)
    ),
    url('/static/images/metro_nen2.jpg');

    background-size:cover;
    background-position:center;

    z-index:99999;

    transition:opacity .5s;
}

.splash-logo{
    width:220px;
    animation:logoAnim 1.5s ease;
}

.splash-title{
    margin-top:20px;

    color:#28a745;

    font-size:42px;
    font-weight:800;

    text-align:center;
}

.splash-loading{
    margin-top:40px;

    width:60px;
    height:60px;

    border:8px solid #ddd;
    border-top:8px solid #28a745;

    border-radius:50%;

    animation:spin 1s linear infinite;
}

@keyframes spin{
    100%{
        transform:rotate(360deg);
    }
}

@keyframes logoAnim{
    0%{
        opacity:0;
        transform:scale(.5);
    }

    100%{
        opacity:1;
        transform:scale(1);
    }
}

</style>

</head>

<body>

<div id="splash-screen">

    <img
    src="{{ url_for('static', filename='images/logo.png') }}"
    class="splash-logo">

    <div class="splash-title">
        Green Bicycle - Metro
    </div>

    <div class="splash-loading"></div>

</div>

    <div class="loader"></div>
</div>

<div class="title">
    <img
        src="{{ url_for('static', filename='images/logo.png') }}"
        alt="Logo"
    >
    Green Bicycle - Metro
</div>

<div class="dashboard">

    <div class="stat-card">
        🚉
        <span>14 Ga</span>
    </div>

    <div class="stat-card">
        📍
        <span>56 Trạm</span>
    </div>

    <div class="stat-card">
        🚲
        <span>300 Xe</span>
    </div>

</div>

<a href="/metro/1">

    <div class="metro-card">

        <img
            class="metro-image"
            src="{{ url_for('static', filename='images/metro_nen1.jpg') }}"
            alt="Metro Line 1"
        >

        <div class="metro-info">
            <p>METRO SỐ 1</p>
            <p>Bến Thành - Suối Tiên</p>
        </div>

    </div>

</a>

<div
    class="menu-btn"
    onclick="toggleMenu()"
>
    ☰
</div>

<div
    id="sideMenu"
    class="side-menu"
>

    <a href="/">Trang chủ</a>

    <a
        href="#"
        onclick="toggleService(); return false;"
    >
        Gói dịch vụ
    </a>

    <a
        href="#"
        onclick="toggleIntro(); return false;"
    >
        Giới thiệu
    </a>

</div>

<div
    id="serviceBox"
    class="service-box"
>

    <h3>Gói dịch vụ Green Bicycle - Metro</h3>

    <table>

        <tr>
            <th>Gói dịch vụ</th>
            <th>Mức phí</th>
        </tr>

        <tr>
            <td>Vé ngày</td>
            <td>30.000 đồng</td>
        </tr>

        <tr>
            <td>Vé tháng sinh viên</td>
            <td>99.000 đồng/tháng</td>
        </tr>

        <tr>
            <td>Vé tháng người lao động</td>
            <td>199.000 đồng/tháng</td>
        </tr>

    </table>

</div>

<div
    id="introBox"
    class="intro-box"
>

    <h3>Giới thiệu Green Bicycle- Metro</h3>

    <p>
        Green Bicycle - Metro là ứng dụng mô phỏng hệ thống xe đạp công cộng
        thông minh kết nối với tuyến Metro số 1 (Bến Thành - Suối Tiên),
        được thực hiện bởi nhóm sinh viên Trường Đại học Giao thông Vận tải
        TP. Hồ Chí Minh trong học phần Hệ thống Giao thông Thông minh (ITS).
    </p>

</div>

<div class="footer">
    Green Bicycle - Metro © 2026
</div>

<script>

const sideMenu =
    document.getElementById("sideMenu");

const serviceBox =
    document.getElementById("serviceBox");

const introBox =
    document.getElementById("introBox");

function toggleMenu() {

    sideMenu.style.right =
        sideMenu.style.right === "0px"
            ? "-350px"
            : "0px";
}

function toggleService() {

    introBox.style.display = "none";

    serviceBox.style.display =
        serviceBox.style.display === "block"
            ? "none"
            : "block";
}

function toggleIntro() {

    serviceBox.style.display = "none";

    introBox.style.display =
        introBox.style.display === "block"
            ? "none"
            : "block";
}

</script>

<script>

window.addEventListener("load", function(){

    setTimeout(function(){

        let splash =
        document.getElementById(
            "splash-screen"
        );

        splash.style.opacity = "0";

        setTimeout(function(){

            splash.remove();

        },500);

    },2500);

});

</script>

</body>

</html>
"""


GA_HTML = """

<!DOCTYPE html>
<html>

<head>

<title>Danh sách ga</title>

<style>

body{
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    margin:0;
    padding:15px;

    min-height:100vh;

    position:relative;
}

body::before{
    content:"";

    position:fixed;

    top:0;
    left:0;
    right:0;
    bottom:0;

    background-image:url('{{ url_for("static", filename="images/metro_nen2.jpg") }}');

    background-size:cover;
    background-position:center;

    filter:blur(6px);

    opacity:.15;

    z-index:-1;
}

.grid{
    display:grid;

    grid-template-columns:1fr 1fr;

    gap:18px;
}

.card{
    aspect-ratio:1/1;

    border-radius:22px;

    overflow:hidden;

    position:relative;

    background-size:cover;
    background-position:center;

    box-shadow:
        0 10px 25px rgba(0,0,0,.18);

    transition:all .25s ease;
}

.card:hover{
    transform:translateY(-6px);

    box-shadow:
        0 18px 35px rgba(0,0,0,.25);
}

.card:active{
    transform:scale(.97);
}

.home-btn{
    width:calc(100% - 90px);
    height:95px;

    margin:auto;
    margin-bottom:20px;

    display:flex;
    align-items:center;
    justify-content:center;

    gap:15px;

    border:none;
    border-radius:18px;

    background:rgba(255,255,255,.35);

    backdrop-filter:blur(15px);
    -webkit-backdrop-filter:blur(15px);

    border:2px solid rgba(255,255,255,.4);

    box-shadow:
        0 8px 25px rgba(0,0,0,.15);

    color:#28a745;

    font-size:55px;
    font-weight:650;

    cursor:pointer;

    -webkit-text-stroke:1px #1f7a35;

    text-shadow:
        0 2px 8px rgba(0,0,0,.15);
}

.btn-logo{
    height:75px;
    width:auto;
}

.page-title{
    font-size:50px;
    font-weight:800;

    color:#28a745;

    margin:0 0 15px 0;

    padding:5px;

    background:rgba(255,255,255,.7);

    backdrop-filter:blur(10px);

    border-radius:15px;

    display:inline-block;
}

.sub-title{
    background:rgba(255,255,255,.75);

    backdrop-filter:blur(10px);

    padding:15px 20px;

    margin:0 0 20px 0;

    border-radius:15px;

    color:#555;

    font-size:28px;
}

a{
    text-decoration:none;
    color:black;
}

.menu-btn{
    position:fixed;

    top:20px;
    right:20px;

    font-size:50px;

    color:white;

    background:rgba(40,167,69,.95);

    backdrop-filter:blur(20px);

    cursor:pointer;

    z-index:1000;
}

.side-menu{
    position:fixed;

    top:0;
    right:-350px;

    width:300px;
    height:100%;

    background:#28a745;

    padding-top:100px;

    transition:.3s;

    z-index:999;
}

.side-menu a{
    display:block;

    padding:20px 30px;

    color:white;

    font-size:30px;
    font-weight:700;

    text-decoration:none;
}

.side-menu a:hover{
    background:rgba(255,255,255,.15);
}
.service-box{
    display:none;

    position:fixed;

    top:100px;
    left:20px;

    width:650px;

    background:white;

    padding:35px;

    border-radius:25px;

    box-shadow:
        0 15px 40px rgba(0,0,0,.25);

    color:#333;

    z-index:1001;
}

.service-box h3{
    font-size:42px;
    color:#28a745;

    margin-bottom:25px;

    text-align:center;
}

.service-box table{
    width:100%;

    border-collapse:collapse;
}

.service-box th{
    background:#28a745;

    color:white;

    font-size:28px;

    padding:18px;
}

.service-box td{
    font-size:26px;

    padding:18px;

    border-bottom:1px solid #ddd;
}

.service-box tr:nth-child(even){
    background:#f8f8f8;
}

.intro-box{
    display:none;

    position:fixed;

    top:100px;
    left:20px;

    width:650px;

    background:white;

    padding:35px;

    border-radius:25px;

    box-shadow:
        0 15px 40px rgba(0,0,0,.25);

    z-index:1001;
}

.intro-box h3{
    font-size:42px;

    color:#28a745;

    text-align:center;

    margin-bottom:25px;
}

.intro-box p{
    font-size:28px;

    line-height:1.8;

    color:#444;
}


</style>

</head>

<body>

<button
    class="home-btn"
    onclick="window.location.href='/'">

    <img
        src="{{ url_for('static', filename='images/logo.png') }}"
        class="btn-logo">

    Green Bicycle - Metro

</button>

<h2 class="page-title">
    🚉 Ga Metro
</h2>

<p class="sub-title">
    Chọn ga để xem các trạm xe đạp xung quanh
</p>

<div class="grid">

{% for ga, info in stations.items() %}

<a href="/ga/{{ga}}">

    <div
        class="card"
        style="background-image:url('{{ url_for('static', filename='images/' + info.image) }}');">

        <div
            style="
                position:absolute;
                bottom:0;
                left:0;
                right:0;
                background:#28a745;
                color:white;
                padding:12px;
                text-align:center;
            ">

            <h3
                style="
                    margin:0;
                    font-size:40px;
                    font-weight:700;
                ">
                {{ga}}
            </h3>

            <p
                style="
                    margin:5px 0 0;
                    font-size:30px;
                ">
                4 trạm hoạt động
            </p>

        </div>

    </div>

</a>

{% endfor %}

</div>

<div class="menu-btn" onclick="toggleMenu()">
    ☰
</div>

<div id="sideMenu" class="side-menu">

    <a href="/">Trang chủ</a>

    <a href="#" onclick="toggleService(); return false;">
        Gói dịch vụ
    </a>

    <a href="#" onclick="toggleIntro(); return false;">
        Giới thiệu
    </a>

</div>

<div id="serviceBox" class="service-box">

    <h3>Gói dịch vụ Green Bicycle - Metro</h3>

    <table>

        <tr>
            <th>Gói dịch vụ</th>
            <th>Mức phí</th>
        </tr>

        <tr>
            <td>Vé ngày</td>
            <td>30.000 đồng</td>
        </tr>

        <tr>
            <td>Vé tháng sinh viên</td>
            <td>99.000 đồng/tháng</td>
        </tr>

        <tr>
            <td>Vé tháng người lao động</td>
            <td>199.000 đồng/tháng</td>
        </tr>

    </table>

</div>

<div id="introBox" class="intro-box">

    <h3>ℹ️ Giới thiệu Green Bicycle - Metro</h3>

    <p>
        Green Bicycle - Metro là ứng dụng mô phỏng hệ thống xe đạp công cộng thông minh kết nối tuyến Metro số 1 (Bến Thành - Suối Tiên), được thực hiện bởi nhóm sinh viên Trường Đại học Giao thông Vận tải TP. Hồ Chí Minh trong học phần Hệ thống Giao thông Thông minh (ITS).
    </p>

</div>

<script>

function toggleMenu() {
    const menu = document.getElementById("sideMenu");

    menu.style.right =
        menu.style.right === "0px"
            ? "-350px"
            : "0px";
}

function toggleService() {
    document.getElementById("introBox").style.display = "none";

    const box = document.getElementById("serviceBox");

    box.style.display =
        box.style.display === "block"
            ? "none"
            : "block";
}

function toggleIntro() {
    document.getElementById("serviceBox").style.display = "none";

    const box = document.getElementById("introBox");

    box.style.display =
        box.style.display === "block"
            ? "none"
            : "block";
}

</script>

</body>

</html>

"""


STOP_HTML = """

<!DOCTYPE html>
<html>

<head>

<title>{{ga_name}}</title>

<style>
body{
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    margin:0;
    padding:15px;

    min-height:100vh;

    position:relative;
}

body::before{
    content:"";

    position:fixed;

    top:0;
    left:0;
    right:0;
    bottom:0;

    background-image:
        url('{{ url_for("static", filename="images/metro_nen2.jpg") }}');

    background-size:cover;
    background-position:center;

    filter:blur(6px);

    opacity:.15;

    z-index:-1;
}

.grid{
    display:grid;

    grid-template-columns:1fr 1fr;

    gap:18px;
}

.card{
    background:rgba(255,255,255,.92);

    border-radius:22px;

    overflow:hidden;

    border:1px solid rgba(255,255,255,.8);

    box-shadow:
        0 12px 30px rgba(0,0,0,.15);

    transition:all .25s ease;
}

.card:hover{
    transform:translateY(-6px);

    box-shadow:
        0 18px 35px rgba(0,0,0,.25);
}

.card:active{
    transform:scale(.97);
}

.home-btn{
    width:calc(100% - 90px);
    height:95px;

    margin:auto;
    margin-bottom:20px;

    display:flex;
    align-items:center;
    justify-content:center;

    gap:15px;

    border:none;
    border-radius:18px;

    background:rgba(255,255,255,.35);

    backdrop-filter:blur(15px);
    -webkit-backdrop-filter:blur(15px);

    border:2px solid rgba(255,255,255,.4);

    box-shadow:
        0 8px 25px rgba(0,0,0,.15);

    color:#28a745;

    font-size:55px;
    font-weight:650;

    cursor:pointer;

    -webkit-text-stroke:1px #1f7a35;

    text-shadow:
        0 2px 8px rgba(0,0,0,.15);
}

.btn-logo{
    height:75px;
    width:auto;
}

.page-title{
    font-size:50px;
    font-weight:800;

    color:#28a745;

    margin:0 0 15px 0;

    padding:5px;

    background:rgba(255,255,255,.7);

    backdrop-filter:blur(10px);

    border-radius:15px;

    display:inline-block;
}

.sub-title{
    background:rgba(255,255,255,.75);

    backdrop-filter:blur(10px);

    padding:15px 20px;

    margin:0 0 20px 0;

    border-radius:15px;

    color:#555;

    font-size:28px;
}

.station-name{
    display:flex;
    align-items:center;
    justify-content:center;

    padding:15px 10px 5px 10px;

    text-align:center;

    color:#28a745;

    font-size:32px;
    font-weight:800;

    line-height:1.2;

    min-height:auto;
    margin:0;
}

.station-desc{

    margin-top:20;
    margin-bottom:20px;

    padding:0 10px 10px 10px;

    text-align:center;

    color:#555;

    font-size:25px;
    font-weight:400;

    line-height:1;
}

.bike-count{
    height:50px;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:24px;
    font-weight:700;
}

.menu-btn{
    position:fixed;

    top:20px;
    right:20px;

    color:white;

    font-size:50px;

    background:rgba(40,167,69,.95);

    backdrop-filter:blur(20px);

    cursor:pointer;

    z-index:1000;
}

.side-menu{
    position:fixed;

    top:0;
    right:-350px;

    width:300px;
    height:100%;

    background:#28a745;

    padding-top:100px;

    transition:.3s;

    z-index:999;
}

.side-menu a{
    display:block;

    padding:20px 30px;

    color:white;

    text-decoration:none;

    font-size:30px;
    font-weight:700;
}

.side-menu a:hover{
    background:rgba(255,255,255,.15);
}

button{
    width:100%;
    height:70px;

    border:none;
    border-radius:15px;

    background:
        linear-gradient(
            180deg,
            #2ecb56,
            #28a745
        );

    color:white;

    font-size:35px;
    font-weight:800;

    cursor:pointer;

    box-shadow:
        0 8px 20px rgba(40,167,69,.35);

    transition:.25s;
}

button:hover{
    transform:translateY(-3px);
}

.card img{
    width:100%;

    height:300px;

    object-fit:cover;
    object-position:center;

    border-radius:16px;

    display:block;

    margin-bottom:10px;
}

.service-box{
    display:none;

    position:fixed;

    top:100px;
    left:20px;

    width:650px;

    padding:35px;

    background:white;

    border-radius:25px;

    color:#333;

    box-shadow:
        0 15px 40px rgba(0,0,0,.25);

    z-index:1001;
}

.service-box h3{
    margin-bottom:25px;

    color:#28a745;

    text-align:center;

    font-size:42px;
}

.service-box table{
    width:100%;

    border-collapse:collapse;
}

.service-box th{
    padding:18px;

    background:#28a745;

    color:white;

    font-size:28px;
}

.service-box td{
    padding:18px;

    border-bottom:1px solid #ddd;

    font-size:26px;
}

.service-box tr:nth-child(even){
    background:#f8f8f8;
}

.intro-box{
    display:none;

    position:fixed;

    top:100px;
    left:20px;

    width:650px;

    padding:35px;

    background:white;

    border-radius:25px;

    box-shadow:
        0 15px 40px rgba(0,0,0,.25);

    z-index:1001;
}

.intro-box h3{
    margin-bottom:25px;

    color:#28a745;

    text-align:center;

    font-size:42px;
}

.intro-box p{
    color:#444;

    font-size:28px;

    line-height:1.8;
}

</style>

</head>
<body>

<button
    class="home-btn"
    onclick="window.location.href='/'">

    <img
        src="{{ url_for('static', filename='images/logo.png') }}"
        class="btn-logo">

    Green Bicycle - Metro

</button>

<h2 class="page-title">
    🚉 {{ ga_name }}
</h2>

<p class="sub-title">
    Chọn trạm thuê xe gần nhất
</p>

<div class="grid">

    {% for station in stations %}

    <div class="card">

        <h3 class="station-name">
            {{ station.name }}
        </h3>

        <p class="station-desc">
        📍 {{station.desc}}
        </p>

        <img
            src="{{ url_for('static', filename='images/' + station.image) }}">

        <p class="bike-count">
            🚲 Xe khả dụng: {{ station.bikes }}
        </p>

        <a href="/rent/{{ station.id }}">
            <button class="rent-btn">
            THUÊ XE
            </button>
        </a>

    </div>

    {% endfor %}

</div>

<div
    class="menu-btn"
    onclick="toggleMenu()">

    ☰

</div>

<div
    id="sideMenu"
    class="side-menu">

    <a href="/">Trang chủ</a>

    <a
        href="#"
        onclick="toggleService(); return false;">

        Gói dịch vụ

    </a>

    <a
        href="#"
        onclick="toggleIntro(); return false;">

        Giới thiệu

    </a>

</div>

<div
    id="serviceBox"
    class="service-box">

    <h3>
        Gói dịch vụ Green Bicycle - Metro
    </h3>

    <table>

        <tr>
            <th>Gói dịch vụ</th>
            <th>Mức phí</th>
        </tr>

        <tr>
            <td>Vé ngày</td>
            <td>30.000 đồng</td>
        </tr>

        <tr>
            <td>Vé tháng sinh viên</td>
            <td>99.000 đồng/tháng</td>
        </tr>

        <tr>
            <td>Vé tháng người lao động</td>
            <td>199.000 đồng/tháng</td>
        </tr>

    </table>

</div>

<div
    id="introBox"
    class="intro-box">

    <h3>
        Giới thiệu Green Bicycle - Metro
    </h3>

    <p>
        Green Bicycle - Metro là ứng dụng mô phỏng hệ thống xe đạp công cộng thông minh kết nối với tuyến Metro số 1 (Bến Thành - Suối Tiên), được thực hiện bởi nhóm sinh viên Trường Đại học Giao thông Vận tải TP. Hồ Chí Minh trong học phần Hệ thống Giao thông Thông minh (ITS).
    </p>

    <p>
        Dự án được xây dựng dựa trên đề tài nghiên cứu và thiết kế giải pháp điều phối xe đạp công cộng thông minh kết nối 14 ga Metro số 1.
    </p>

    <p>
        Thành viên nhóm:
        <br>• Lê Trọng Phát
        <br>• Nguyễn Đào Nguyên
        <br>• Võ Tấn Phát
        <br>• Huỳnh Hướng
        <br>• Phạm Gia Huy
    </p>

</div>

<script>

function toggleMenu() {

    const menu =
        document.getElementById("sideMenu");

    if (menu.style.right === "0px") {
        menu.style.right = "-350px";
    } else {
        menu.style.right = "0px";
    }

}

function toggleService() {

    document.getElementById("introBox").style.display =
        "none";

    const box =
        document.getElementById("serviceBox");

    if (box.style.display === "block") {
        box.style.display = "none";
    } else {
        box.style.display = "block";
    }

}

function toggleIntro() {

    document.getElementById("serviceBox").style.display =
        "none";

    const box =
        document.getElementById("introBox");

    if (box.style.display === "block") {
        box.style.display = "none";
    } else {
        box.style.display = "block";
    }

}

</script>

</body>

</html>

"""


QR_HTML = """

<!DOCTYPE html>
<html>

<head>
<title>Quét mã mở khóa</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    min-height:100vh;

    display:flex;
    justify-content:center;
    align-items:center;

    background:
        linear-gradient(
            rgba(0,0,0,.35),
            rgba(0,0,0,.35)
        ),
        url('{{ url_for("static", filename="images/metro_nen2.jpg") }}');

    background-size:cover;
    background-position:center;
}

.box{
    width:600px;

    background:rgba(255,255,255,.92);

    border-radius:40px;

    padding:50px 40px;

    text-align:center;

    backdrop-filter:blur(15px);

    box-shadow:
        0 20px 50px rgba(0,0,0,.25);
}

.title{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:15px;

    color:#28a745;

    font-size:60px;
    font-weight:700;
}

.title-logo{
    height:100px;
    width:auto;
}

.metro{
    margin:15px 0 8px;

    color:#28a745;

    font-size:48px;
    font-weight:800;
}

.station{
    margin:15px 0;

    color:#666;

    font-size:35px;
    font-weight:700;
}

.note{
    margin-top:15px;

    color:#666;

    font-size:26px;
    line-height:1.4;
}

.qr-scanner{
    position:relative;

    width:100%;
    height:500px;

    margin:10px 0 25px;

    border-radius:25px;

    overflow:hidden;

    background:rgba(40,167,69,.05);
}

.corner{
    position:absolute;

    width:60px;
    height:60px;

    border:8px solid #28a745;
}

.tl{
    top:15px;
    left:15px;

    border-right:none;
    border-bottom:none;
}

.tr{
    top:15px;
    right:15px;

    border-left:none;
    border-bottom:none;
}

.bl{
    bottom:15px;
    left:15px;

    border-right:none;
    border-top:none;
}

.br{
    bottom:15px;
    right:15px;

    border-left:none;
    border-top:none;
}

.scan-line{
    position:absolute;

    left:30px;
    right:30px;

    height:5px;

    background:#28a745;

    box-shadow:
        0 0 12px #28a745,
        0 0 25px #28a745;

    animation:scan 4s linear infinite;
}

@keyframes scan{
    0%{
        top:50px;
    }

    100%{
        top:400px;
    }
}

.qr-text{
    position:absolute;

    top:50%;
    left:50%;

    transform:translate(-50%,-50%);

    width:80%;

    color:#888;

    font-size:28px;
    font-weight:700;

    line-height:1.4;
}

.scan-btn{
    width:100%;
    height:90px;

    border:none;
    border-radius:18px;

    background:
        linear-gradient(
            180deg,
            #39c953,
            #28a745
        );

    color:white;

    font-size:42px;
    font-weight:800;

    cursor:pointer;

    box-shadow:
        0 8px 20px rgba(40,167,69,.35);

    transition:.2s;
}

.scan-btn:hover{
    transform:translateY(-2px);
}

.scan-btn:active{
    transform:scale(.97);
}

</style>

</head>

<body>

    <div class="box">

        <div class="title">

            <img
                src="{{ url_for('static', filename='images/logo.png') }}"
                class="title-logo"
            >

            Green Bicycle - Metro

        </div>

        <div class="metro">
            {{ station.metro }}
        </div>

        <div class="station">
            {{ station.name }}
        </div>

        <div class="qr-scanner">

            <div class="corner tl"></div>
            <div class="corner tr"></div>
            <div class="corner bl"></div>
            <div class="corner br"></div>

            <div class="scan-line"></div>

            <div class="qr-text">
                Đưa mã QR vào đây
            </div>

        </div>

        <div class="note">
            Đưa mã QR trên xe đạp vào khung quét
        </div>

        <div
            id="scan-result"
            style="
                margin-top:100px;
                font-size:100px;
                font-weight:bold;
                color:#28a745;
            "
        >
        </div>

        <button
            class="scan-btn"
            type="button"
            onclick="window.location.href='/confirm_rent/{{ station.id }}'"
        >
            ĐÃ QUÉT QR
        </button>

    </div>

</body>

</html>

"""


LOADING_HTML = """

<!DOCTYPE html>
<html>

<head>

<title>Mở khóa xe</title>

<meta http-equiv="refresh" content="3;url=/status">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    height:100vh;

    display:flex;
    justify-content:center;
    align-items:center;

    background:
        linear-gradient(
            rgba(0,0,0,.4),
            rgba(0,0,0,.4)
        ),
        url('{{ url_for("static", filename="images/metro_nen2.jpg") }}');

    background-size:cover;
    background-position:center;
}

.box{
    width:70%;

    background:rgba(255,255,255,.9);

    padding:50px;

    border-radius:40px;

    text-align:center;

    box-shadow:
        0 35px 45px rgba(0,0,0,.25);
}

.title{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:15px;

    color:#28a745;

    font-size:60px;
    font-weight:700;
}

.title-logo{
    height:100px;
    width:auto;
}

.success-text{
    margin-top:30px;

    color:#28a745;

    font-size:50px;
    font-weight:700;
}

.subtitle{
    margin-top:25px;

    color:#444;

    font-size:40px;
}

.loader{
    width:80px;
    height:80px;

    margin:40px auto;

    border:12px solid #ddd;
    border-top:12px solid #28a745;
    border-radius:50%;

    animation:spin 1s linear infinite;
}

.note{
    color:#666;
    font-size:30px;
}

@keyframes spin{
    100%{
        transform:rotate(360deg);
    }
}

</style>

</head>

<body>

    <div class="box">

        <div class="title">

            <img
                src="{{ url_for('static', filename='images/logo.png') }}"
                class="title-logo"
            >

            Green Bicycle - Metro

        </div>

        <div class="success-text">
            Quét mã thành công
        </div>

        <div class="subtitle">
            Đang mở khóa xe...
        </div>

        <div class="loader"></div>

        <div class="note">
            Vui lòng chờ trong giây lát
        </div>

    </div>

</body>

</html>

"""


STATUS_HTML = """

<!DOCTYPE html>
<html>

<head>

<title>Đang sử dụng xe</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    height:100vh;

    display:flex;
    justify-content:center;
    align-items:center;

    background:
        linear-gradient(
            rgba(0,0,0,.45),
            rgba(0,0,0,.45)
        ),
        url('{{ url_for("static", filename="images/metro_nen2.jpg") }}');

    background-size:cover;
    background-position:center;
}

.box{
    width:80%;
    height:50%;

    background:rgba(255,255,255,.9);

    padding:50px;

    border-radius:40px;

    text-align:center;

    box-shadow:
        0 35px 45px rgba(0,0,0,.25);
}

.title{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:15px;

    color:#28a745;

    font-size:50px;
    font-weight:800;
}

.title-logo{
    height:100px;
    width:auto;
}

.metro{
    margin-top:15px;

    color:#28a745;

    font-size:50px;
    font-weight:800;
}

.station{
    margin-top:8px;
    margin-bottom:20px;

    color:#666;

    font-size:40px;
    font-weight:700;
}

.info{
    background:
        linear-gradient(
            180deg,
            #32c44d,
            #28a745
        );

    padding:22px 25px;

    border-radius:20px;

    text-align:left;
}

.info p{
    margin:12px 0;

    color:white;

    font-size:40px;
    font-weight:600;
}

.timer{
    margin:25px 0;

    color:#28a745;

    font-size:50px;
    font-weight:800;

    text-shadow:
        0 0 10px rgba(40,167,69,.35);
}

.return-btn{
    width:100%;
    height:80px;

    border:none;
    border-radius:18px;

    background:
        linear-gradient(
            180deg,
            #39c953,
            #28a745
        );

    color:white;

    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    font-size:60px;
    font-weight:800;

    box-shadow:
        0 8px 20px rgba(40,167,69,.35);

    transition:.2s;
}

.return-btn:active{
    transform:scale(.97);
}

</style>

</head>

<body>

    <div class="box">

        <div class="title">

            <img
                src="{{ url_for('static', filename='images/logo.png') }}"
                class="title-logo"
            >

            Green Bicycle - Metro

        </div>

        <div class="metro">
            {{ rent.metro }}
        </div>

        <div class="station">
            {{ rent.station }}
        </div>

        <div class="info">

            <p>🚲 Xe số: {{ rent.bike_code }}</p>

            <p>🟢 Xe đang được sử dụng</p>

            <p>📅 Bắt đầu: {{ rent.date }}</p>

            <p>🕒 Thời gian: {{ rent.start }}</p>

        </div>

        <div id="timer" class="timer">
            00:00:00
        </div>

        <button
            class="return-btn"
            onclick="window.location.href='/return_bike'"
        >
            TRẢ XE
        </button>

    </div>

<script>

const start = new Date("{{ start_time_js }}");

function updateTimer() {

    const now = new Date();

    const diff =
        Math.floor((now - start) / 1000);

    const h = Math.floor(diff / 3600);
    const m = Math.floor((diff % 3600) / 60);
    const s = diff % 60;

    document.getElementById("timer").innerHTML =
        String(h).padStart(2, "0") + ":" +
        String(m).padStart(2, "0") + ":" +
        String(s).padStart(2, "0");
}

setInterval(updateTimer, 1000);
updateTimer();

</script>

</body>

</html>

"""


PAY_QR_HTML = """

<!DOCTYPE html>
<html>

<head>

<title>Thanh toán chuyến đi</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    min-height:100vh;

    display:flex;
    justify-content:center;
    align-items:center;

    background:
        linear-gradient(
            rgba(0,0,0,.45),
            rgba(0,0,0,.45)
        ),
        url('{{ url_for("static", filename="images/metro_nen2.jpg") }}');

    background-size:cover;
    background-position:center;
}

.box{
    width:90%;

    padding:40px;

    border-radius:35px;

    background:rgba(255,255,255,.88);

    backdrop-filter:blur(12px);
    -webkit-backdrop-filter:blur(12px);

    box-shadow:
        0 15px 40px rgba(0,0,0,.25);
}

.title{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:15px;

    margin-bottom:25px;

    color:#28a745;

    font-size:50px;
    font-weight:800;

    text-align:center;

    text-shadow:
        0 2px 8px rgba(0,0,0,.08);
}

.title-logo{
    height:100px;
    width:auto;
}

.info{
    padding:25px;

    border-radius:20px;

    margin-bottom:25px;

    color:white;

    background:
        linear-gradient(
            180deg,
            #35c84f,
            #28a745
        );

    box-shadow:
        0 8px 20px rgba(40,167,69,.35);
}

.info p{
    display:flex;
    align-items:center;
    gap:12px;

    margin:14px 0;

    font-size:40px;
    font-weight:650;
}

.amount{
    margin-bottom:25px;

    color:#28a745;

    font-size:60px;
    font-weight:900;

    text-align:center;

    text-shadow:
        0 3px 10px rgba(40,167,69,.2);
}

.qr-box{
    width:260px;
    height:260px;

    margin:25px auto;

    display:flex;
    align-items:center;
    justify-content:center;

    background:white;

    border:4px solid #28a745;
    border-radius:20px;

    box-shadow:
        0 8px 20px rgba(40,167,69,.15);
}

.qr-box img{
    width:220px;
    height:220px;

    object-fit:contain;
}

.note{
    margin-bottom:30px;

    color:#666;

    font-size:24px;
    line-height:1.5;

    text-align:center;
}

.pay-btn{
    width:100%;
    height:80px;

    border:none;
    border-radius:18px;

    background:
        linear-gradient(
            180deg,
            #39c953,
            #28a745
        );

    color:white;

    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    font-size:50px;
    font-weight:800;

    box-shadow:
        0 8px 20px rgba(40,167,69,.35);

    transition:.2s;

    cursor:pointer;
}

.pay-btn:active{
    transform:scale(.97);
}

</style>

</head>

<body>

<div class="box">

    <div class="title">

        <img
            src="{{ url_for('static', filename='images/logo.png') }}"
            class="title-logo"
        >

        Green Bicycle - Metro

    </div>

    <div class="title">
        Thanh toán chuyến đi
    </div>

    <div class="info">

        <p>🚲 Mã xe: {{ bike_code }}</p>

        <p>🚉 Ga bắt đầu: {{ start_metro }}</p>

        <p>📅 Ngày: {{ start_date }}</p>

        <p>🕒 Thời gian: {{ start_time }}</p>

        <p>🏁 Ga kết thúc: {{ end_metro }}</p>

        <p>📅 Ngày: {{ end_date }}</p>

        <p>🕒 Thời gian: {{ end_time }}</p>

    </div>

    <div class="title">
        Số tiền cần thanh toán
    </div>

    <div class="amount">
        {{ cost }} VNĐ
    </div>

    <div class="qr-box">

        <img
            src="{{ url_for('static', filename='images/qr_demo.jpg') }}"
        >

    </div>

    <div class="note">
        Vui lòng quét mã QR bằng ứng dụng ngân hàng hoặc ví điện tử để hoàn tất thanh toán.
    </div>

    <button
        class="pay-btn"
        onclick="window.location.href='/payment_success'"
    >
        ĐÃ THANH TOÁN
    </button>

</div>

</body>

</html>

"""


END_HTML = """

<!DOCTYPE html>
<html>

<head>

<title>Hoàn tất chuyến đi</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    min-height:100vh;

    display:flex;
    justify-content:center;
    align-items:center;

    background:
        linear-gradient(
            rgba(0,0,0,.45),
            rgba(0,0,0,.45)
        ),
        url('{{ url_for("static", filename="images/metro_nen2.jpg") }}');

    background-size:cover;
    background-position:center;
}

.box{
    width:90%;
    max-width:700px;

    padding:50px;

    text-align:center;

    border-radius:40px;

    background:rgba(255,255,255,.9);

    box-shadow:
        0 35px 45px rgba(0,0,0,.25);
}

.title{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:15px;

    margin-bottom:20px;

    color:#28a745;

    font-size:50px;
    font-weight:800;

    text-align:center;
}

.title-logo{
    height:100px;
    width:auto;
}

.subtitle{
    margin-bottom:25px;

    color:#666;

    font-size:30px;
    font-weight:500;
}

.summary{
    padding:25px;

    text-align:left;

    border-radius:22px;

    color:white;

    background:
        linear-gradient(
            180deg,
            #39c953,
            #28a745
        );

    box-shadow:
        0 8px 20px rgba(40,167,69,.35);
}

.summary p{
    margin:14px 0;

    font-size:35px;
}

.summary h1{
    margin-top:10px;

    color:white;

    font-size:50px;
    font-weight:800;

    text-align:center;
}

.cost{
    text-align:center;
}

.cost div{
    margin-top:30px;
    margin-bottom:25px;

    color:#28a745;

    font-size:50px;
    font-weight:800;
}

.home-btn{
    width:100%;
    height:80px;

    margin-top:25px;
    margin-bottom:25px;

    border:none;
    border-radius:18px;

    background:
        linear-gradient(
            180deg,
            #39c953,
            #28a745
        );

    color:white;

    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    font-size:38px;
    font-weight:800;

    box-shadow:
        0 8px 20px rgba(40,167,69,.35);

    transition:.2s;

    cursor:pointer;
}

.home-btn:active{
    transform:scale(.97);
}

.footer{
    margin-top:10px;

    color:#888;

    font-size:30px;

    text-align:center;
}

</style>

</head>

<body>

<div class="box">

    <div class="title">

        <img
            src="{{ url_for('static', filename='images/logo.png') }}"
            class="title-logo"
        >

        Green Bicycle - Metro

    </div>

    <div class="title">
        Hoàn tất chuyến đi
    </div>

    <div class="subtitle">
        Cảm ơn bạn đã sử dụng Green Bicycle - Metro
    </div>

    <div class="summary">

        <p>🚲 Dịch vụ: Green Bicycle - Metro</p>

        <p>⏱️ Thời gian sử dụng: {{ minutes }} phút</p>

        <p>📅 Ngày: {{ today }}</p>

        <p>💰 Tổng thanh toán</p>

        <h1>{{ cost }} VNĐ</h1>

    </div>

    <div class="cost">

        <div>
            Trả xe thành công
        </div>

    </div>

    <a href="/">

        <button class="home-btn">
            VỀ TRANG CHỦ
        </button>

    </a>

    <div class="footer">
        Chúc bạn một ngày tốt lành
    </div>

</div>

</body>

</html>

"""


@app.route("/metro/<int:metro_id>")
def metro_stations(metro_id):

    return render_template_string(
        GA_HTML,
        stations=STATIONS
    )


@app.route("/ga/<ga_name>")
def show_stops(ga_name):

    stops = [
        station
        for station in bike_stations
        if station["metro"] == ga_name
    ]

    return render_template_string(
        STOP_HTML,
        stations=stops,
        ga_name=ga_name
    )


@app.route("/rent/<int:station_id>")
def rent(station_id):

    station = next(
        (
            item
            for item in bike_stations
            if item["id"] == station_id
        ),
        None
    )

    return render_template_string(
        QR_HTML,
        station=station
    )


@app.route("/unlock_bike/<int:station_id>")
def unlock_bike(station_id):

    return render_template(
        "unlock_success.html",
        station_id=station_id
    )


@app.route("/confirm_rent/<int:station_id>")
def confirm_rent(station_id):

    global rent_info

    station = next(
        (
            item
            for item in bike_stations
            if item["id"] == station_id
        ),
        None
    )

    if station and station["bikes"] > 0:

        station["bikes"] -= 1

        bike_id = random.choice(
            available_bikes
        )

        available_bikes.remove(
            bike_id
        )

        now = datetime.now()

        rent_info = {
            "bike_id": bike_id,
            "bike_code": f"GBM-{bike_id:03d}",
            "metro": station["metro"],
            "station": station["name"],
            "start_time": now,
            "start": now.strftime("%H:%M:%S"),
            "date": now.strftime("%d/%m/%Y")
        }

        return render_template_string(
            LOADING_HTML
        )

    return redirect("/metro")


@app.route("/status")
def status():

    if rent_info is None:
        return redirect("/")

    return render_template_string(
        STATUS_HTML,
        rent=rent_info,
        start_time_js=rent_info["start_time"].isoformat()
    )


@app.route("/return_bike")
def return_bike():

    global rent_info
    global available_bikes

    if rent_info is None:
        return redirect("/")

    minutes = max(
        1,
        int(
            (
                datetime.now()
                - rent_info["start_time"]
            ).seconds / 60
        )
    )

    if minutes <= 30:

        cost = 5000

    elif minutes <= 60:

        cost = 10000

    else:

        extra_blocks = (
            (minutes - 60) // 30
        ) + 1

        cost = (
            10000
            + extra_blocks * 3000
        )

    return render_template_string(
        PAY_QR_HTML,
        bike_code=rent_info["bike_code"],
        start_metro=rent_info["metro"],
        start_time=rent_info["start"],
        start_date=rent_info["start_time"].strftime(
            "%d/%m/%Y"
        ),
        end_metro=rent_info["metro"],
        end_time=datetime.now().strftime(
            "%H:%M:%S"
        ),
        end_date=datetime.now().strftime(
            "%d/%m/%Y"
        ),
        cost=cost
    )


@app.route("/payment_success")
def payment_success():

    global rent_info
    global available_bikes

    if rent_info is None:
        return redirect("/")

    minutes = max(
        1,
        int(
            (
                datetime.now()
                - rent_info["start_time"]
            ).seconds / 60
        )
    )

    if minutes <= 30:

        cost = 5000

    elif minutes <= 60:

        cost = 10000

    else:

        extra_blocks = (
            (minutes - 60) // 30
        ) + 1

        cost = (
            10000
            + extra_blocks * 3000
        )

    available_bikes.append(
        rent_info["bike_id"]
    )

    rent_info = None

    return render_template_string(
        END_HTML,
        minutes=minutes,
        cost=cost,
        today=datetime.now().strftime(
            "%d/%m/%Y %H:%M"
        )
    )


@app.route("/")
def home():

    return redirect("/metro")


@app.route("/metro")
def metro():

    adjust_bikes()

    metros = [
        {
            "id": 1,
            "name": "Metro số 1",
            "stations": 14
        }
    ]

    return render_template_string(
        METRO_HTML,
        metros=metros,
        period=get_period()
    )


if __name__ == "__main__":
    app.run(debug=True)