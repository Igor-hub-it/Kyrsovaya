function draw_requests(data) {
    let tmp = ''
    if (data.success) {
        for (let i = 0; i < data.requests.length; ++i) {
            tmp += '<div class="request_1 req">';
            tmp += '<div class="top_of_req">\n' +
                '<div class="name">\n' +
                'Пользователь: '+ data.requests[i].user +'\n' +
                '</div>\n' +
                '<div class="date_to_go">\n' +
                'Поедет в аэропорт: ' + data.requests[i].time +'\n' +
                '</div>\n' +
                '<div class="user_vklink">\n' +
                'Страница Вк: ' + data.requests[i].pers_data + '\n' +
                '</div>\n' +
                '</div>\n' +
                '<div class="comment"> Комментарий: ' + data.requests[i].comment + '\n' +
                '</div>\n' +
                '</div>\n';
        }
    } else {
         tmp = '<div class="nothingtext"> В этот день пока нет заявок </div>';
    }
    document.getElementById("requests").innerHTML = tmp;
}