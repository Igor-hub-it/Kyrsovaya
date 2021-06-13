const MONTH_NAME=[
    'Январь', 'Февраль', 'Март', 'Апрель',
    'Май', 'Июнь', 'Июль', 'Август',
    'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
];

const DAY_NAME=[
    'ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС'
];

const CALENDAR_ID='calendar';

let selectedDate = {
    'Day' : null,
    'Month' : new Date().getMonth(),
    'Year' : new Date().getFullYear()
};

function selectDate(day, month, year) {
    selectedDate = {
        'Day' : day,
        'Month' : month,
        'Year' : year
    };
    drawCalendar(month,year);
}

function countMonth(month) {
    if (month === -1) {
        return 11;
    }
    if (month === 12) {
        return 0;
    }
    return month;
}

function countYear(month, year) {
    if (month === -1) {
        return year - 1;
    }
    if (month === 12) {
        return year + 1;
    }
    return year;
}

function drawCalendar(month,year) {
    let months = [countMonth(month - 1), countMonth(month + 1)];
    let years = [countYear(month - 1, year), countYear(month + 1, year)]

    let tmp='';

    tmp += '<div class="mounth">\n' +
        '<div class="prev_mounth" ' +
        'onclick="drawCalendar(' + months[0] + ', ' + years[0] +')">' +
        '&#171;' +
        '</div>\n' +
        '<div class="cur_mounth">' + MONTH_NAME[month] + '</div>\n' +
        '<div class="next_mounth" ' +
        'onclick="drawCalendar(' + months[1] + ', ' + years[1] + ')">' +
        '&#187;' +
        '</div>\n' +
        '</div>\n';

    tmp += '<div class="weeks_days">\n' +
        '<div class="name_weeks">\n';
    for (let i = 1; i < 3; ++i) {
        tmp += '<div class="week'+ (i) +' col-lg-3 col-lg-2">\n' +
            '<div class="inner">\n';
        for (let j = 0; j < 7; ++j) {
            tmp += '<div class="day_name">\n' +
                DAY_NAME[j]+'\n' +
                '</div>\n';
        }
        tmp += '</div>\n';
        tmp += '</div>\n';
    }

    tmp += '<div class="week3 col-lg-3">\n' +
            '<div class="inner">\n';
    for (let j = 0; j < 7; ++j) {
            tmp += '<div class="day_name">\n' +
                DAY_NAME[j]+'\n' +
                '</div>\n';
    }
    tmp += '</div>\n';
    tmp += '</div>\n';

    let totalDays = 32 - new Date(year, (month), 32).getDate();
    let totalDaysPrevMonth = 32 - new Date(year, (month - 1), 32).getDate();
    let start_day = new Date(year, (month), 1).getDay();
    // start on Sunday, change num
    if (start_day === 0) {
        start_day = 7;
    }
    --start_day;

    let day = 0;
    let index = 0;
    let dayNextMonth = 0;

    tmp += '<div id="days">';
    for (let i = 1; i < 7; ++i) {
        tmp += '<div class="colomn'+ i +' col-lg-3 col-lg-2">\n' +
            '<div class="inner">\n';
        for (let j = 0; j < 7; ++j) {
            let num_day;
            if (index < start_day) {
                num_day = totalDaysPrevMonth - (start_day - index - 1);
            } else if (index >= totalDays + start_day) {
                num_day = ++dayNextMonth;
            } else {
                num_day = ++day;
            }
            tmp += '<div class="day">' + num_day + '</div>\n';
            ++index;
        }
        tmp += '</div>\n';
        tmp += '</div>\n';
    }
    tmp += '</div>\n';
    document.getElementById(CALENDAR_ID).innerHTML=tmp;
}

drawCalendar(selectedDate.Month, selectedDate.Year);