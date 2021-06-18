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
