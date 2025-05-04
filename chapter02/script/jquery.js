$('#post-url').val("새 글 입니다.");

let url = $('#post-url').val();
console.log(url)

$('#post-url').hide();
$('#post-url').show();



$('.card-columns').append("추가 텍스트");

let button = `<button class='btn btn-primary'>추가 버튼</button>`
$('.card-columns').append(button)

let img_url = 'https://cdn.vox-cdn.com/thumbor/Pkmq1nm3skO0-j693JTMd7RL0Zk=/0x0:2012x1341/1200x800/filters:focal(0x0:2012x1341)/cdn.vox-cdn.com/uploads/chorus_image/image/47070706/google2.0.0.jpg';
let link_url = 'https://google.com/';
let title = '제목 - 구글';
let desc = '구글에 대한 설명이 여기에 들어간다.';
let comment = '여기는 개인적인 코멘트가 들어간다.';


let temp_html = `<div>
                    <img class='card-img-top' src='${img_url}' alt='Card image cap'>
                    <div class='card-body'>
                        <a href='${link_url}' class='card-title'>${title}</a>
                        <p class='card-text'>${desc}</p>
                        <p class='card-text comment'>${comment}</p>
                    </div>
                </div>`;

$('.card-columns').append(temp_html);





