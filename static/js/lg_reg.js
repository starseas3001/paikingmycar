$(function () {
    $('.p-tab a').each(function (index) {
        $(this).click(function () {
            $(this).addClass('on').siblings().removeClass('on');
            $('.p-dl').eq(index).show().siblings().hide();
        })
    });
    //登录按钮
    $('.b-login').click(function () {
        var idd = $(this).attr('id');
        if (idd) {
            var strs = idd.split("_");
                $('.orderstatus').val(strs[0]);
                $('.ordercarid').val(strs[1]);

        } else {
            $('.ordercarid').val('');
        }
        $('#popBox').fadeIn();
        $('.p-tab a:first').addClass('on').siblings().removeClass('on');
        $('.p-dl:first').show().siblings().hide();
    })
    //退出按钮
    $('#b-tuichu').click(function () {
        alert('退出成功');
        window.location.reload();
    })
    $('#b-regist').click(function () {
        $('#popBox').fadeIn();
        $('.p-tab a:last').addClass('on').siblings().removeClass('on');
        $('.p-dl:last').show().siblings().hide();
    })

    $('#popBox').click(function () {
        $('#popBox').fadeOut();
    });
    $('.popCont').click(function (e) {
        e.stopPropagation();
    });
    /*$('.closed').click(function(){
        $('#popBox').fadeOut();
    });*/
    /*$('.send_phone').click(function(){
        $('#popBoxYzm').fadeIn();
    });*/
    $('.p_closed').click(function () {
        $('#popBox').fadeOut();
    });
    $('.closed').click(function () {
        $('#popBoxYzm').fadeOut();
    });
    $('#Carduibi li').hover(function () {
        $(this).toggleClass('hover')
    });
    jQuery(".mini-gotop").click("click", function () {
        jQuery('html, body').stop().animate({scrollTop: 0}, 800);
    });
    $('.wx1').hover(function () {
        $('.wmImg').removeClass('hide')
    }, function () {
        $('.wmImg').addClass('hide')
    })
    $('#deletealldb').click(function () {
        var balancecar = $.cookie('flamingo.compare.car');
        if (balancecar) {
            strs = balancecar.split("_");
            for (var i = 0; i < strs.length; i++) {
                if (strs[i]) {
                    var sss = strs[i].substr(2);
                    $('.balance_' + sss).text('加入对比');
                    $('.Cardd_' + sss).hide();
                }
            }
        }
        $.cookie('flamingo.compare.car', '', {expires: 1, path: '/'});
        $('#Dbnumber').text(0);
        $('.shopping').click();
    });
});

// function closeDuibi(checkid) {
//     balance(checkid);
//     $(this).parent('li').hide();
// }

// // 对比
// function balance(checkid) {
//     var balancecar = $.cookie('flamingo.compare.car');
//
//     if (balancecar) {
//         strs = balancecar.split("_");
//
//         var len = strs.length - 2;
//         if (balancecar.indexOf('id' + checkid + '_') >= 0) {//取消对比
//             balancecar = balancecar.replace('id' + checkid + '_', '');
//             $.cookie('flamingo.compare.car', balancecar, {expires: 1, path: '/'});
//             $('.balance_' + checkid).text('加入对比');
//             $('#Dbnumber').text(len - 1);
//             $('.Cardd_' + checkid).hide();
//             if (len <= 1) {
//                 $('.shopping').click();
//             }
//
//         } else {//加入对比
//             strs = balancecar.split("_");
//             if (len >= 4) {
//                 $('#Dbnumber').text(len);
//                 alert('最多只能对比4个');
//             } else {
//                 $('#Dbnumber').text(len + 1);
//                 $.cookie('flamingo.compare.car', balancecar + 'id' + checkid + '_', {expires: 1, path: '/'});
//                 $('.balance_' + checkid).text('取消对比');
//                 var v = $('.CarValue_' + checkid).val();
//                 var v = eval("(" + v + ")");
//                 var h = ' <li class="clearfix Cardd_' + checkid + '">';
//                 h += '	<a href="' + v.url + '"><img src="' + v.img + '" class="left" width="80" /></a>';
//                 h += '	<h3><a href="' + v.url + '">' + v.title + '</a></h3>';
//                 h += '	<div class="mi_a clearfix">';
//                 h += '		<strong class="left">￥' + v.price + '万元</strong>';
//                 h += '		<a href="javascript:void(0)" onclick="balance(\'' + v.id + '\')" class="right mini-tocar">取消对比</a>';
//                 h += '<input type="hidden" class="CarValue_' + v.id + '" value="{img:\'' + v.img + '\',id:\'' + v.id + '\',price:\'' + v.price + '\',status:\'取消对比\',title:\'' + v.title + '\',url:\'' + v.url + '\'}" />';
//                 h += '	</div>';
//                 h += '	<a class="mini-m-close" onclick="closeDuibi(\'' + v.id + '\')"></a>';
//                 h += '</li>';
//                 $("#Carduibi ul").append(h);
//                 $('.Cardd_' + checkid).hover(function () {
//                     $(this).toggleClass('hover')
//                 });
//                 if ($("#shopping").is(":hidden")) {
//                     $('.shopping').click();
//                 }
//
//             }
//         }
//     } else {//加入对比
//         $('#Dbnumber').text(1);
//         $.cookie('flamingo.compare.car', '_id' + checkid + '_', {expires: 1, path: '/'});
//         $('.balance_' + checkid).text('取消对比');
//
//         var v = $('.CarValue_' + checkid).val();
//         var v = eval("(" + v + ")");
//         var h = ' <li class="clearfix Cardd_' + checkid + '">';
//         h += '	<a href="' + v.url + '"><img src="' + v.img + '" class="left" width="80" /></a>';
//         h += '	<h3><a href="' + v.url + '">' + v.title + '</a></h3>';
//         h += '	<div class="mi_a clearfix">';
//         h += '		<strong class="left">￥' + v.price + '万元</strong>';
//         h += '		<a href="javascript:void(0)" onclick="balance(\'' + v.id + '\')" class="right mini-tocar">取消对比</a>';
//         h += '<input type="hidden" class="CarValue_' + v.id + '" value="{img:\'' + v.img + '\',id:\'' + v.id + '\',price:\'' + v.price + '\',status:\'取消对比\',title:\'' + v.title + '\',url:\'' + v.url + '\'}" />';
//         h += '	</div>';
//         h += '	<a class="mini-m-close" onclick="closeDuibi(\'' + v.id + '\')"></a>';
//         h += '</li>';
//         $("#Carduibi ul").append(h);
//         $('.Cardd_' + checkid).hover(function () {
//             $(this).toggleClass('hover')
//         });
//         if ($("#shopping").is(":hidden")) {
//             $('.shopping').click();
//         }
//
//     }
// }
//
// // 侧边栏显示对比
// function compare(carid) {
//     $.cookie(carid, carid)
//
//     if ($("#shopping").is(":hidden")) {
//         $('.shopping').click();
//     }
//
// }



//收藏&取消收藏
function collection(carid) {
    var url = '/oper/fav/';

    $.ajax({
        type: "GET",
        url: url,
        data: {carid: carid},
        dataType: "json",
        success: function (data) {
            if (data.code == 1) {
                $('#collection_' + carid).text('已收藏');
                var v = $('.CarValue_' + carid).val();
                var v = eval("(" + v + ")");
                var h = ' <li class="clearfix" id="id_' + v.id + '">';
                h += '	<a href="' + v.url + '"><img src="' + v.img + '" class="left" width="80" /></a>';
                h += '	<h3><a href="' + v.url + '">' + v.title + '</a></h3>';
                h += '	<div class="mi_a clearfix">';
                h += '		<strong class="left">￥' + v.price + '万元</strong>';
                h += '		<a href="javascript:void(0)" onclick="collection(\'' + v.id + '\')" class="right mini-tocar">' + v.status + '</a>';
                h += '	</div>';
                h += '<input type="hidden" class="CarValue_' + v.id + '" value="{img:\'' + v.img + '\',id:\'' + v.id + '\',price:\'' + v.price + '\',status:\'' + v.status + '\',title:\'' + v.title + '\',url:\'' + v.url + '\'}" />';
                h += '	<a class="mini-m-close"></a>';
                h += '</li>';

                $("#shoucang ul").append(h);
            }
            if (data.code == 2) {
                $('#collection_' + carid).text("收藏");
                // 右侧小框内、个人中心都移除收藏
                $('li[id="id_' + carid + '"]').remove();
            }
            if (data.code == 3) {
                alert("收藏失败")
            }
        }
    });
    return false;
}


//侧边栏显示收藏
function userfavcar(userid) {
    var url = '/oper/getfavcar/';
    $.ajax({
        type: "GET",
        url: url,
        data: {userid: userid},
        dataType: "json",
        success: function (data) {
            // 显示收藏
            if (data.code == "2") {
                $('div[id="shoucang"] ul li').remove();
                $.each(data.all_cars, function (index, value) {
                    var v = value;
                    //写入html
                    var h = ' <li class="clearfix" id="id_' + v.id + '">';
                    h += '	<a href="/cars/maichineshow/' + v.id + '"><img src="/media/' + v.image + '" class="left" width="80" /></a>';
                    h += '	<h3><a href="/cars/maichineshow/' + v.id + '">' + v.series + v.kuanhao + v.displacement + v.gear_box + v.version + '</a></h3>';
                    h += '	<div class="mi_a clearfix">';
                    h += '		<strong class="left">￥' + v.price + '万元</strong>';
                    h += '		<a href="javascript:void(0)" onclick="collection(\'' + v.id + '\')" class="right mini-tocar">取消收藏</a>';
                    h += '	</div>';
                    h += '	<a class="mini-m-close"></a>';
                    h += '</li>';
                    $("#shoucang ul").append(h);
                })
            }
            // 没有收藏
            if (data.code == "0") {
                $('div[id="shoucang"] ul li').remove();
                $("#shoucang ul").append("<li>暂无收藏</li>");
            }
            // 登录
            if (data.code == '1') {
                $('#popBox').fadeIn();
            }
        }
    });
}


// 侧边栏显示订单
function userorder(userid){
    var url = '/oper/getorder/';
    $.ajax({
        type: "GET",
        url: url,
        data: {userid: userid},
        dataType: "json",
        success: function (data) {
            // 显示订单
            if (data.code == "2") {
                $('div[id="user_order"] ul li').remove();
                $.each(data.all_cars, function (index, value) {
                    var v = value;
                    //写入html
                    var h = ' <li class="clearfix" id="id_' + v.id + '">';
                    h += '	<a href="/cars/maichineshow/' + v.id + '"><img src="/media/' + v.image + '" class="left" width="80" /></a>';
                    h += '	<h3><a href="/cars/maichineshow/' + v.id + '">' + v.series + v.kuanhao + v.displacement + v.gear_box + v.version + '</a></h3>';
                    h += '	<div class="mi_a clearfix">';
                    h += '		<strong class="left">￥' + v.price + '万元</strong>';
                    h += '		<a href="/users/cars/"  class="right mini-tocar">查看订单</a>';
                    h += '	</div>';
                    h += '	<a class="mini-m-close"></a>';
                    h += '</li>';
                    $("#user_order ul").append(h);
                })
            }
            // 没有订单
            if (data.code == "0") {
                $('div[id="user_order"] ul li').remove();
                $("#user_order ul").append("<li>暂无订单</li>");
            }
            // 登录
            if (data.code == '1') {
                $('#popBox').fadeIn();
            }
        }
    });

}

// 添加&删除订单
function addorder(carid) {
    var url = "/oper/addorder/";
    $.ajax({
        type: "GET",
        url: url,
        data: {carid: carid},
        dataType: "json",
        success: function (data) {

            if (data.code == 1) {
                //alert("添加订单成功！");
                $("#order_" + carid).text("已预订");
            }
            if (data.code == 2) {
                alert("已取消订单");
                $("#order_" + carid).text("立即抢订");

                // 删除页面上显示的订单
                $('li[id="user_order_' + carid + '"]').remove();

            }
            if (data.code == 3) {
                alert("预订失败");
            }
        }
    })

}

function yudingtongkuan(carId) {
    var url = '/Concern/yudingtongkuan';
    $.ajax({
        type: "POST",
        url: url,
        data: {carId: carId},
        dataType: "json",
        success: function (data) {
            alert(data.msg);
        }
    });
    return false;
}


// 搜索栏车系品牌关联显示
$("#Smakeid").change(function () {
    var brand = $(this).val();
    var brands = brand.split('-');
    var brandkey = brands[0];
    var brandname = brands[1];
    var url = "/oper/getcarseries/";
    //选择品牌后添加到搜索框后面
    $('#car_brand').remove();
    $('#sou_suo_lan').append('<p class="left" id="car_brand" style="width:auto;" onclick="delNode()">&nbsp;' + brandkey + ' ' + brandname + '<span class="close right"></span></p>');

    $.ajax({
        type: "POST",
        url: url,
        data: {brandname: brandname},
        dataType: "json",
        success: function (data) {
            if (data.status == "success") {
                var v = eval("(" + data.car_series + ")");
                $("#Smodeid").empty();
                $.each(v, function (index, value) {
                    var series_name = value.fields.series_name;
                    $("#Smodeid").append('<option value="' + series_name + '">' + series_name + '</option>');

                    //把第一个添加到搜索栏后，后面可以更改
                    if (index == 0) {
                        $('#sou_suo_lan').append('<p class="left" id="car_series" style="width:auto;" onclick="delNode()">&nbsp;' + series_name + '<span class="close right"></span></p>');
                    }
                })
            }
            else {
                window.location.reload()
            }

        }
    })
});


//汽车列表页面私人定制栏车系品牌关联显示
$("#Smakeid2").change(function () {
    var brandname = $(this).val();
    var url = "/oper/getcarseries/";
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type: "POST",
        url: url,
        data: {brandname: brandname, "csrfmiddlewaretoken": csrfToken},
        dataType: "json",
        success: function (data) {
            if (data.status == "success") {
                var v = eval("(" + data.car_series + ")");
                $("#Smodeid2").empty();
                $.each(v, function (index, value) {
                    var series_name = value.fields.series_name;
                    $("#Smodeid2").append('<option value="' + series_name + '">' + series_name + '</option>');
                })
            }
            else {
                window.location.reload()
            }
        }

    })
});

//私人定制页面车系品牌关联显示
$("#Smakei").change(function () {
    var brandname = $(this).val();
    var url = "/oper/getcarseries/";
    $.ajax({
        type: "POST",
        url: url,
        data: {brandname: brandname},
        dataType: "json",
        success: function (data) {
            if (data.status == "success") {
                var v = eval("(" + data.car_series + ")");
                $("#Smodeid2").empty();
                $.each(v, function (index, value) {
                    var series_name = value.fields.series_name;
                    $("#Smodeid2").append('<option value="' + series_name + '">' + series_name + '</option>');
                })
            }
            else {
                window.location.reload()
            }
        }

    })
});

// 提示登录
$("#alert_login").change(function () {
    $('#popBox').fadeIn();
});
$("#btn_login").click(function () {
    $('#popBox').fadeIn();
});
// 私人定制页面登录
$("#srdz_login").click(function () {
    $('#popBox').fadeIn();
});

// 我要卖车页面登录
$("#sell_login").click(function () {
    $('#popBox').fadeIn();
});

//我要卖车页面车系品牌关联显示
$("#select car-select").change(function () {
    var brandname = $(this).val();
    var url = "/oper/getcarseries/";
    $.ajax({
        type: "POST",
        url: url,
        data: {brandname: brandname},
        dataType: "json",
        success: function (data) {
            if (data.status == "success") {
                var v = eval("(" + data.car_series + ")");
                $("#Smodeid2").empty();
                $.each(v, function (index, value) {
                    var series_name = value.fields.series_name;
                    $("#Smodeid2").append('<option value="' + series_name + '">' + series_name + '</option>');
                })
            }
            else {
                window.location.reload()
            }
        }

    })
});



// 用户最近浏览
function currentBrowse(userid) {
    var url = "/oper/userbrowse/";
    $.ajax({
        type: "GET",
        url: url,
        data: {userid: userid},
        dataType: "json",
        success: function (data) {
            // 显示浏览记录
            if (data.code == "2") {
                $('div[id="Liulan"] ul li').remove();
                $.each(data.all_cars, function (index, value) {
                    var v = value;
                    //写入html
                    var h = ' <li class="clearfix" id="browse_' + v.id + '">';
                    h += '	<a href="/cars/maichineshow/' + v.id + '"><img src="/media/' + v.image + '" class="left" width="80" /></a>';
                    h += '	<h3><a href="/cars/maichineshow/' + v.id + '">' + v.series + v.kuanhao + v.displacement + v.gear_box + v.version + '</a></h3>';
                    h += '	<div class="mi_a clearfix">';
                    h += '		<strong class="left">￥' + v.price + '万元</strong>';
                    h += '		<a href="javascript:void(0)" onclick="delBrowse(\'' + v.id + '\')" class="right mini-tocar">删除记录</a>';
                    h += '	</div>';
                    h += '<input type="hidden" class="CarValue_' + v.id + '" value="{img:\'' + v.image + '\',id:\'' + v.id + '\',price:\'' + v.price + '\',status:\'删除记录\',title:\'' + v.series + v.kuanhao + v.displacement + v.gear_box + v.version + '\',url:\'/cars/maichineshow/' + v.id + '\'}" />';
                    h += '	<a class="mini-m-close"></a>';
                    h += '</li>';
                    $("#Liulan ul").append(h);
                })
            }

            // 没有收藏
            if (data.code == "0") {
                $('div[id="Liulan"] ul li').remove();
                $("#Liulan ul").append("<li>暂无浏览记录</li>");
            }

            // 登录
            if (data.code == '1') {
                $('#popBox').fadeIn();
            }
        }
    })
}

// 删除浏览记录
function delBrowse(carid) {
    // ('li[id="id_' + carid + '"]').remove();
    // $('#browse'+carid).remove()
    $('li[id="browse_' + carid + '"]').remove()
}

// 修改用户信息
function checkpost() {
    var mobile = editM.mobile.value;//手机号码
    var realname = editM.realname.value;//姓名
    var gender = editM.gender.value;//性别
    var email = editM.email.value;//邮箱
    var Yemail = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/; //邮箱验证
    var url = '/users/updatemsg/';
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    if (realname == "") {
        alert("姓名不能为空");
        return false;
    }
    if (realname.length > 10) {
        alert("姓名要不得大于10个字符");
        editM.realname.focus();
        return false;
    }
    if (!Yemail.exec(email) && email != '') {
        alert("邮箱格式不正确");
        editM.email.focus();
        return false;
    }
    $.ajax({
        type: "POST",
        url: url,
        data: {mobile: mobile, realname: realname, gender: gender, email: email, "csrfmiddlewaretoken": csrfToken},
        dataType: "json",
        success: function (data) {
            if (data.code == "2") {
                alert("修改信息成功");
                window.location.reload()
            } else {
                alert("修改信息失败");
                window.location.reload()
            }
        }
    });
    return false;
}


function checkPasspost() {

    var password = editP.password.value;//密码
    var password2 = editP.password2.value;//密码
    var Ypass = /\S{6,16}/;//密码验证
    var url = '/users/updatepwd/';
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    if (password == "") {
        alert("不能为空");

        return false;
    }
    if (!password2) {
        alert("请重复输入新密码");

        return false;
    }
    if (password != password2) {
        alert("两次新密码输入不一致");

        return false;
    }
    if (!Ypass.exec(password)) {
        alert("密码格式不正确，必须以字母开头的6-16 字母，数字");

        return false;
    }
    $.ajax({
        type: "POST",
        url: url,
        data: {password: password, password2: password2, "csrfmiddlewaretoken": csrfToken},
        dataType: "json",
        success: function (data) {
            if (data.code == "2") {
                alert("密码修改成功");
                window.location.href = "/";
            } else {
                alert("密码修改失败");
                window.location.href = "/";
            }
        }
    });
    return false;
}

//修改密码
function updatePwd() {
    var password = editP.password.value;//密码
    var password2 = editP.password2.value;//密码
    var Ypass = /\S{6,16}/;//密码验证
    var url = '/users/updatepwd/';
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    if (!password) {
        alert("不能为空");
        return false;
    }
    if (!password2) {
        alert("请重复输入新密码");
        return false;
    }
    if (password != password2) {
        alert("两次新密码输入不一致");
        return false;
    }
    if (!Ypass.exec(password)) {
        alert("密码格式不正确，必须以字母开头的6-16 字母，数字");
        return false;
    }
    $.ajax({
        type: "POST",
        url: url,
        dataType: "json",
        data: {password: password, "csrfmiddlewaretoken": csrfToken},
        success: function (data) {
            if (data.code == '1') {
                alert('修密码失败');
            } else {
                alert('修改密码成功');
                window.location.reload()
            }
        }
    });
    return false
}