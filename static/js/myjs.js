// 组合筛选排序
// $('#saix a').click(function () {
// 	val = ($(this).text())
// })

// 汽车搜索
//首页搜索栏
function indexSearch() {
    index_keywords = $('#index_keyword').val();
    if (!index_keywords) {
        alert('请输入关键字');
        return false;
    }

    location.href = '/cars/searchresult/?top_keywords=' + index_keywords;
    return false;
}

//顶部搜索栏
function topSearch() {
    top_keywords = $('#top_keyword').val();
    if (!top_keywords) {
        alert('请输入关键字');
        return false;
    }

    location.href = '/cars/searchresult/?top_keywords=' + top_keywords;
    return false;
}

// 汽车列表页搜索
function searchCar() {
    var keyword = $('#keyword').val();
    var car_brand = $('#car_brand').text();
    var car_series = $('#car_series').text();
    var price = $('#price_range').text();
    var car_type = $('#car_type').text();
    var car_age = $('#age_range').text();
    var lichen = $('#lichen_range').text();
    var emission = $('#emission_range').text();
    var url = '/cars/searchresult/';
    if (!car_brand && !keyword) {
        alert('请选择品牌或填写关键字');
        return false;
    }
    if (emission == '国四') {
        emission = 'four';
    } else if (emission == '国五') {
        emission = 'five';
    } else {
        emission = '';
    }
    location.href = '/cars/searchresult/?keyword=' + keyword + '&car_brand=' + car_brand + '&car_series=' + car_series + '&price=' + price + '&car_type=' + car_type + '&car_age=' + car_age + '&lichen' + lichen + '&emission=' + emission
    return false;
}

// $('#tjkey').click(function () {
//     var keyword = $('#keyword').val();
//     var car_brand = $('#car_brand').text();
//     var car_series = $('#car_series').text();
//     var price = $('#price_range').text();
//     var car_type = $('#car_type').text();
//     var car_age = $('#age_range').text();
//     var lichen = $('#lichen_range').text();
//     var emission = $('#emission_range').text();
//     var url='/cars/searchresult/';
//     if (emission == '国四'){
//         emission = 'four';
//     }else if(emission == '国五'){
//         emission = 'five';
//     }else{
//         emission = '';
//     }
//     //location.href='/cars/searchresult/?keyword='+keyword+'car_brand='+car_brand+'car_series='+car_series+'price='+price+'car_type='+car_type+'car_age='+car_age+'lichen'+lichen+'emission='+emission
//     location.href="http://www.baidu.com";
//     alert('dd')
//     // $.ajax({
//     //     type: 'GET',
//     //     url: url,
//     //     data:{
//     //         search:'search', keyword: keyword, car_series: car_series,
//     //         price: price, car_type: car_type, car_age: car_age,
//     //         lichen: lichen, emission:emission, car_brand: car_brand
//     //     },
//     //     dataType:'json',
//     //     success:function (data) {
//     //         alert('dd')
//     //     }
//     //
//     // })
//
// });

//删除搜索栏后的信息
function delNode() {
    $('#sou_suo_lan p').click(function () {
        $(this).remove()
    })
}

// 点击图标品牌后添加到搜索栏
function souSuoLanCar(key, name) {
    $('#car_brand').remove();
    $('#sou_suo_lan').append('<p class="left" id="car_brand" style="width:auto;" onclick="delNode()">&nbsp;' + key + ' ' + name + '<span class="close right"></span></p>');
    $('#car_series').remove();
}

//点击车系，搜索框后面显示
$('#Smodeid').change(function () {
    var series_name = $(this).val();
    var all_node = $('#sou_suo_lan p').text();
    if (all_node.indexOf(series_name) == -1) {
        $('#car_series').remove();
        $('#sou_suo_lan').append('<p class="left" id="car_series" style="width:auto;" onclick="delNode()">&nbsp;' + series_name + '<span class="close right"></span></p>');
    }
});

//价格搜索
$('#price_select a').click(function () {
    var price = this.text;
    $('#price_range').remove();
    $('#sou_suo_lan').append('<p class="left" id="price_range" style="width:auto;" onclick="delNode()">&nbsp;' + price + '<span class="close right"></span></p>');
});

// 输入框输入价格
$('#tjprice').click(function () {
    var reg = /^[0-9]{1,5}$/;
    var min_price = $('#price_L').val() ? $('#price_L').val() : 0;
    var max_price = $('#price_R').val() ? $('#price_R').val() : 0;
    if (!reg.test(min_price) || !reg.test(max_price)) {
        alert('请输入1~5位数字');
    } else {
        if (min_price == 0 && max_price == 0) {
            alert('请输入价格');
        } else if (min_price >= max_price) {
            alert('最低价格不能大于或等于最高价格')
        } else {
            var p1 = min_price + '-' + max_price;
            $('#price_range').remove();
            $('#sou_suo_lan').append('<p class="left" id="price_range" style="width:auto;" onclick="delNode()">&nbsp;' + p1 + '万<span class="close right"></span></p>');

        }
    }
});

// 车型搜索
$('#type_select a').click(function () {
    var type = this.text;
    $('#car_type').remove();
    $('#sou_suo_lan').append('<p class="left" id="car_type" style="width:auto;" onclick="delNode()">&nbsp;' + type + '<span class="close right"></span></p>');

});

// 车龄搜索
$('#age_select a').click(function () {
    var age = this.text;
    $('#age_range').remove();
    $('#sou_suo_lan').append('<p class="left" id="age_range" style="width:auto;" onclick="delNode()">&nbsp;' + age + '<span class="close right"></span></p>');

});
// 输入框输入车龄
$('#tjcheling').click(function () {
    var reg = /^[0-9]{1,2}$/;
    var min_age = $('#cheling_L').val() ? $('#cheling_L').val() : 0;
    var max_age = $('#cheling_R').val() ? $('#cheling_R').val() : 0;
    if (!reg.test(min_age) || !reg.test(max_age)) {
        alert('请输入数字');
    } else {
        if (min_age == 0 && max_age == 0) {
            alert('请输入车龄');
        } else if (min_age >= 30 || max_age >= 30) {
            alert('车龄不能超过30年');
        }
        else if (min_age >= max_age) {
            alert('最小年龄不能大于或等于最高价格')
        } else {
            var p1 = min_age + '-' + max_age;
            $('#age_range').remove();
            $('#sou_suo_lan').append('<p class="left" id="age_range" style="width:auto;" onclick="delNode()">&nbsp;' + p1 + '年<span class="close right"></span></p>');

        }
    }
});

// 里程搜索
$('#lichen_select a').click(function () {
    var lichen = this.text;
    $('#lichen_range').remove();
    $('#sou_suo_lan').append('<p class="left" id="lichen_range" style="width:auto;" onclick="delNode()">&nbsp;' + lichen + '<span class="close right"></span></p>');

});
// 输入框输入里程
$('#tjlicheng').click(function () {
    var reg = /^[0-9]{1,3}$/;
    var min_lichen = $('#licheng_L').val() ? $('#licheng_L').val() : 0;
    var max_lichen = $('#licheng_R').val() ? $('#licheng_R').val() : 0;
    if (!reg.test(min_lichen) || !reg.test(max_lichen)) {
        alert('请输入数字');
    } else {
        if (min_lichen == 0 && max_lichen == 0) {
            alert('请输入里程');
        } else if (min_lichen >= 200 || max_lichen >= 200) {
            alert('里程不能超过200万公里');
        }
        else if (min_lichen >= max_lichen) {
            alert('最小里程不能大于或等于最高里程')
        } else {
            var p1 = min_lichen + '-' + max_lichen;
            $('#lichen_range').remove();
            $('#sou_suo_lan').append('<p class="left" id="lichen_range" style="width:auto;" onclick="delNode()">&nbsp;' + p1 + '万公里<span class="close right"></span></p>');

        }
    }
});

// 排放标准
$('#emission_sel a').click(function () {
    var emission = this.text;
    $('#emission_range').remove();
    $('#sou_suo_lan').append('<p class="left" id="emission_range" style="width:auto;" onclick="delNode()">&nbsp;' + emission + '<span class="close right"></span></p>');

});


// 热门品牌自动刷新
function hotRefresh() {
    $.ajax({
        type: 'GET',
        url: '/refresh/',
        data: {},
        dataType: 'json',
        success: function (data) {
            // 解析对象
            $('#hot_car a').remove();
            for (var i in data) {
                var car_data = data[i];
                car_data = JSON.parse(car_data);
                for (var j in car_data){
                    var car = car_data[j]['fields']['series_name'];
                    var doc = '<a href="/cars/searchresult/?top_keywords='+car+'">'+car+'</a>';
                    $('#hot_car').append(doc);
                }
            }
        }

    })
}

setTimeout('hotRefresh()', 0);
//5秒刷新一次
setInterval('hotRefresh()', 50000000);

// 支付定金
function dingjinPay(price, user, order_num, car_id){
    var url = '/users/dingjinpay/';
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type: 'POST',
        url: url,
        data:{
            price:price, user:user, order_num:order_num,
            car_id:car_id, "csrfmiddlewaretoken": csrfToken
        },
        dataType: 'json',
        success: function(data){
            if (data.status == 1){
                location.href = data.re_url;
                return false
            }
            if (data.status == 0){
                alert('支付失败');
                return false
            }
        }


    });

    return false
}
