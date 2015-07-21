var fixture_ticket = $('#ticket');
var user_comments = $('#comments');
var more_info = $('#more-info');
var active_panel = fixture_ticket;
$('#for-ticket').on('click', function () {
    if (fixture_ticket.css('display') != 'block') {
        active_panel.fadeOut(function () {
            fixture_ticket.fadeIn();
            active_panel = fixture_ticket;
        });
    }
});
$('#for-comments').on('click', function () {
    if (user_comments.css('display') != 'block') {
        active_panel.fadeOut(function () {
            user_comments.fadeIn();
            active_panel = user_comments;
        });
    }
});
$('#for-more-info').on('click', function () {
    if (more_info.css('display') != 'block') {
        active_panel.fadeOut(function () {
            more_info.fadeIn();
            active_panel = more_info;
        });
    }
});
var your_comment = $('#your-comment');
$('#submit-comment').on('click', function () {
    var comment = $('<div class="comment col col-md-12"><div class="col col-md-11">' +
    '<div class="name">کاربر ثبت نامی</div><div class="date">۲۵ خرداد ۱۳۹۴، ۲:۱۱ عصر</div>' +
    '<div class="text"></div></div><div class="col col-md-1 image"></div></div>');
    comment.find('.text').text(your_comment.find('textarea').val());
    comment.find('.image').css('background-image', your_comment.find('.image').css('background-image'));
    $('#comments').append(comment);
    your_comment.find('textarea').val('');
});


var step1 = $('.bs-wizard div:first-of-type');
var step2 = $('.bs-wizard div:nth-of-type(2)');
var step3 = $('.bs-wizard div:last-of-type');

var show_times = $('#show-times');

$('#cinemas .item').on('click', function () {
    step1.removeClass('active').addClass('complete');
    setTimeout(function () {
        step2.removeClass('disabled').addClass('active');
    }, 600);
    $(this).parent().fadeOut();
    show_times.fadeIn();
});

$('.show-time').on('click', function(){
    step2.removeClass('active').addClass('complete');
    setTimeout(function () {
        step3.removeClass('disabled').addClass('active');
    }, 600);
    $(this).parent().fadeOut();
    $('#plans').fadeIn();
});