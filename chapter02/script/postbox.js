function openclose() {
    let status = $('.form').css('display');
    if (status == 'block') {
        $('.form').hide();
        $('#post-box').text('포스팅박스 열기');
    } else {
        $('.form').show();
        $('#post-box').text('포스팅박스 닫기');
    }
}