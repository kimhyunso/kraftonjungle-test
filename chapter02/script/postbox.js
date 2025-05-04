function openclose() {
    let status = $('#post-box').css('display');
    if (status == 'inline-block') {
        $('#post-box').hide();
        $('#btn-posting-box').text('포스팅박스 열기');
    } else {
        $('#post-box').show();
        $('#btn-posting-box').text('포스팅박스 닫기');
    }
}