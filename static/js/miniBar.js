$(function () {
    $('.mini-bar li').hover(function () {
        $(this).addClass('on');
        $(this).find('span').css({'left': '-80px', 'visibility': 'visible'});
    }, function () {
        $(this).removeClass('on');
        $(this).find('span').css({'left': '0px', 'visibility': 'hidden'});
    });
    $('.mini-bar li.miItem').each(function (index) {
        $(this).click(function () {
            $('#lf-view').css({'left': '0'});
            var miDiv = $('.mini-ni').eq(index);
            $(this).find('span').css({'left': '0px', 'visibility': 'hidden'});
            if (miDiv.is(':hidden')) {
                $('#miniBus').animate({right: '0'});
                $(this).addClass('select').siblings().removeClass('select');
                miDiv.show();
                $('.mini-ni').eq(index).siblings().hide();

            } else {
                $('#miniBus').animate({right: '-270px'});
                miDiv.hide();
                $(this).removeClass('select');
            }
        })
    });
    $('.mini-close').click(function () {
        $('#miniBus').animate({right: '-270px'}, 'fast');
        $('.mini-bar li').removeClass('select');
    });
    var callTop = $('.mini-barlist ul').position().top - $('.callItem').position().top - 18;
    $('#lf-view').css('top', callTop);
    $('.callItem').click(function () {
        $('#mini-idea').hide();
        $('#lf-view').animate({left: '-405'});
    });
    $('#viewClose').click(function () {
        $('#lf-view').css({'left': '0'});
    });
    $('#lf-view dfn').click(function () {
        $('#lf-view dfn').removeClass('on')
        $(this).addClass('on');
    })
})

// 用户注册
var yz = /\S{6,}/;
var m = /^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$/;

function regcheck() {
    var mob = reg.mobile.value;//手机号
    var ver = reg.verify.value;//验证码
    var name = reg.realname.value;//姓名
    var gen = reg.gender.value;//性别
    var pass = reg.password.value;//密码
    var pass2 = reg.password2.value;//确认密码
    var carid = form.carid.value;
    var carstatus = form.carstatus.value;
    var url = '/users/register/';
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    if (mob == '') {
        alert("手机号不能为空");
        reg.mobile.focus();
        return false;
    }
    if (!m.exec(mob)) {
        alert("手机号格式不正确");
        reg.mobile.focus();
        return false;
    }
    if (ver == '') {
        alert("验证码不能为空");
        reg.verify.focus();
        return false;
    }
    if (pass == '') {
        alert("密码不能为空");
        reg.password.focus();
        return false;
    }
    if (!yz.exec(pass)) {
        alert("密码格式不正确");
        reg.password.focus();
        return false;
    }
    if (pass != pass2) {
        alert("两次输入密码不一致");
        reg.password2.focus();
        return false;
    }

    $.ajax({
        type: "POST",
        url: url,
        data: {
            username: mob,
            mobile: mob,
            password: pass,
            password2: pass2,
            verify: ver,
            realname: name,
            gender: gen,
            carid: carid,
            carstatus: carstatus,
            "csrfmiddlewaretoken": csrfToken
        },
        dataType: "json",
        success: function (data) {
            if (data.status == "2") {
                alert("注册成功,请登录");
                $('#popBox').fadeOut();
            }
            if (data.status == "1") {
                alert("验证码错误");
                return false;
            }
            if (data.status == "3") {
                alert("该用户已经注册，请登录");
                return false;
            }
        }
    });
    return false;
}

// 找回密码
function findPassword() {
    var mob = find_pwd.mobile.value;//手机号
    var ver = find_pwd.verify.value;//验证码
    var pass = find_pwd.password.value;//密码
    var pass2 = find_pwd.password2.value;//确认密码
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    var url = '/users/findpassword/';
    if (!mob) {
        alert("手机号不能为空");
        reg.mobile.focus();
        return false;
    }
    if (!m.exec(mob)) {
        alert("手机号格式不正确");
        reg.mobile.focus();
        return false;
    }
    if (!ver) {
        alert("验证码不能为空");
        reg.verify.focus();
        return false;
    }
    if (!pass) {
        alert("密码不能为空");
        reg.password.focus();
        return false;
    }
    if (!yz.exec(pass)) {
        alert("密码格式不正确");
        reg.password.focus();
        return false;
    }
    if (pass != pass2) {
        alert("两次输入密码不一致");
        reg.password2.focus();
        return false;
    }

    $.ajax({
        type: "POST",
        url: url,
        data: {
            mobile: mob,
            password: pass,
            verify: ver,
            "csrfmiddlewaretoken": csrfToken
        },
        dataType: "json",
        success: function (data) {
            if (data.code == "2") {
                alert("操作成功,请登录");
                $('#popBox').fadeIn();
            }
            if (data.code == "1") {
                alert("验证码错误");
                return false;
            }
        }
    });
    return false;

}


//用户登录验证
function check() {
    var user = form.username.value;
    var pass = form.password.value;
    var check = form.checkbox.value;
    var carid = form.carid.value;
    var carstatus = form.carstatus.value;
    var url = '/users/login/';
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    if (user == '') {
        alert("登录名不能为空");
        form.username.focus();
        return false;
    }
    if (!m.exec(user)) {
        alert("手机号格式不正确");
        return false;
    }
    if (pass == '') {
        alert("密码不能为空");
        form.password.focus();
        return false;
    }
    $.ajax({
        type: "POST",
        url: url,
        data: {
            username: user,
            password: pass,
            checkbox: check,
            carid: carid,
            carstatus: carstatus,
            "csrfmiddlewaretoken": csrfToken
        },
        dataType: "json",
        success: function (data) {
            if (data.status == "success") {
                if (data.result = "2") {
                    window.location.reload();
                }
                if (data.carstatus == "collection") {
                    collection(data.carid);
                    window.location.reload();
                }
                if (data.carstatus == "order") {
                    addorder(data.carid)
                    window.location.reload();
                }

            }
            else {
                if (data.result == "1") {
                    alert("密码错误,请重新输入!")
                }
                if (data.result == "3") {
                    alert("用户未注册,请先注册")
                }
            }

        }
    });
    return false;
}


// 私人定制需求提交
function cleckform(user) {

    var brandname = dForm.makeid.value;
    var carseries = dForm.modeid.value;
    var years = dForm.years.value;
    var dprice = dForm.dprice.value;
    var hprice = dForm.hprice.value;
    var buytime = dForm.buytime.value;
    var content = dForm.content.value;
    var url = "/oper/srdz/";
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();

    if (brandname == "") {
        alert("品牌不能为空");
        return false;
    }
    if (carseries == "") {
        alert("车系不能为空");
        return false;
    }
    if (dprice == '' || hprice == '') {
        alert("价格不能为空");
        return false;
    }
    if (dprice >= hprice) {
        alert("最低预算不能高于最最高预算");
        return false;
    }
    if (buytime == "") {
        alert("请选择计划购买时间");
        return false;
    }

    $.ajax({
        type: "POST",
        url: url,
        data: {
            user: user,
            brandname: brandname,
            carseries: carseries,
            years: years,
            dprice: dprice,
            hprice: hprice,
            buytime: buytime,
            content: content,
            "csrfmiddlewaretoken": csrfToken
            //mobile: mobile,
            //verify: verify,
            //ckmobile: remember,

        },
        dataType: "json",
        success: function (data) {
            // alert(data);
            if (data.status == "success") {
                alert('您的需求提交成功，我们将尽快处理');
                window.location.reload();
            } else {
                alert('提交出错');

            }
        }
    });
    return false;
}

// 我要卖车
function sellCar(user) {
    var brand_name = forms.makeid.value;
    var car_series = forms.modeid.value;
    var car_type = forms.styleid.value;
    var buytime = forms.buytime.value;
    var lichen = forms.mile.value;
    var url = '/oper/sellcar/';
    var csrf_token = $('[name="csrfmiddlewaretoken"]').val();
    if (!brand_name) {
        alert('品牌不能为空');
        return false;
    }
    if (!car_series) {
        alert('品牌不能为空');
        return false;
    }
    if (!car_type) {
        alert('品牌不能为空');
        return false;
    }
    if (!buytime) {
        alert('品牌不能为空');
        return false;
    }
    if (!lichen) {
        alert('品牌不能为空');
        return false;
    }
    // 验证里程
    reg = /\d{1,2}/;
    if (reg.test(lichen)) {
        if (lichen < 0 || lichen > 100) {
            alert("里程范围为0-100");
            return false;
        }
    }else{
        alert("请输入0-100的数字");
        return false;
    }

    $.ajax({
        type: 'POST',
        url: url,
        dataType:'json',
        data:{
            user:user, brand_name: brand_name, car_series: car_series,
            car_type: car_type, buytime: buytime, lichen: lichen,
             "csrfmiddlewaretoken": csrf_token
        },
        success:function (data) {
            if (data.status == "success"){
                alert("信息提交成功，我们将尽快处理");
                window.location.reload()
            }else{
                alert("提交失败");
                return false;
            }
        }

    });
    return false;
}


//发送手机验证码
$('.send_code').click(function () {
    var url = '/users/verifycode/';
    var mobile = $('#mobile').val();
    var m = /^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$/;
    var send_type = $(this).attr('id');
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    if (!m.exec(mobile)) {
        alert("手机号格式不正确");
        $('#mobile').focus();
        return false;
    }
    $.ajax({
        type: "POST",
        url: url,
        data: {mobile: mobile, send_type: send_type, "csrfmiddlewaretoken": csrfToken},
        dataType: "json",
        success: function (data) {
            if (data.status == '2') {
                alert('发送成功');
                $('#send').html('<a class="send_code right">已发送</a>');
            } else if (data.status == '1') {
                // 发送失败
                alert(data.msg)
            } else if (data.status == '3') {
                // 已注册
                alert(data.msg)
            } else if (data.status == '4') {
                // 未注册
                alert(data.msg)
            }
        }
    });
    return false;
})

// 用户留言
function Lmessage() {
    var content = leaveMess.bankAuthSrc.value;
    var mobile = leaveMess.mobile.value;
    var url = '/corp/leavemsg/';
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    if (content == '') {
        alert("请输入您的留言");
        leaveMess.bankAuthSrc.focus();
        return false;
    }
    if (mobile == '') {
        alert("手机号码不能为空");
        leaveMess.mobile.focus();
        return false;
    }
    var m = /^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/;
    if (!m.exec(mobile)) {
        alert("手机号格式不正确");
        leaveMess.mobile.focus();
        return false;
    }

    $.ajax({
        type: "POST",
        url: url,
        data: {
            content: content, mobile: mobile, "csrfmiddlewaretoken": csrfToken
        },
        dataType: "json",
        success: function (data) {
            if (data.code == '2') {
                alert('留言成功');
                window.location.reload();
            } else {
                alert('留言失败');
            }
        }
    });
    return false;
}


BizQQWPA.addCustom({aty: '0', a: '0', nameAccount: 4000337777, selector: 'BizQQWPA'});

