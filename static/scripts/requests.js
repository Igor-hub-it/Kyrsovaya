function calendarRequest(day, month, year) {
    const request = new XMLHttpRequest();
    request.open('CALENDAR', '/');
    request.onload = () => {
        const data = JSON.parse(request.responseText);
        draw_requests(data);
    }
    const data = new FormData();
    data.append('day', String(day))
    data.append('month', String(month))
    data.append('year', String(year))
    request.send(data);
}


function reqWindowRequest(in_data) {
    const request = new XMLHttpRequest();
    request.open('CREATE_REQ', '/');
    request.onload = () => {
        const data = JSON.parse(request.responseText);
        if (data.result === "success") {
            alert("Успешно добавлено");
        } else {
            alert("У вас уже есть заявка на это время.");
        }
    }
    const data = new FormData();
    data.append('user', in_data.user)
    data.append('date', in_data.date)
    data.append('time', in_data.time)
    data.append('comment', in_data.comment)
    data.append('link', in_data.link)
    request.send(data);
}