from db.db_models import db, Dates, Requests
from werkzeug.datastructures import MultiDict


class MessagesEnum:
    does_not_exist = "does not exist"
    already_exists = "already exists"
    success = "success"
    # result = "result"


def calendar_request_get(form: MultiDict):
    day = form.get('day')
    month = form.get('month')
    if len(month) == 1:
        month = '0' + month
    year = form.get('year')
    print(day, month, year)
    date = Dates.query.filter_by(date=(str(day) + '.' + str(month) + '.' + str(year))).first()
    if date:
        req = Requests.query.filter_by(id_dates=date.id).all()
        res = []
        for r in req:
            res.append({'user': r.user, 'time': r.time, 'pers_data': r.pers_data, 'comment': r.comment})
        print(res)
        return {MessagesEnum.success: True, "requests": res}
    return {MessagesEnum.success: False}


def calendar_request_set(form: MultiDict):
    full_date_time = form.get('date').split(' ')
    print(full_date_time)
    date = Dates.query.filter_by(date=full_date_time[0]).first()
    if not date:
        date = Dates(date=full_date_time[0])
        db.session.add(date)
        db.session.commit()
    print(date.id)
    # date = Dates.query.filter_by(date=full_date_time[0]).first()
    req = Requests.query.filter_by(id_dates=date.id, user=form.get('user'), time=full_date_time[1]).first()
    if req:
        return {"result": MessagesEnum.already_exists}
    req = Requests(user=form.get('user'), time=full_date_time[1], pers_data=form.get('link'),
                   comment=form.get('comment'), id_dates=date.id)
    db.session.add(req)
    db.session.commit()
    return {"result": MessagesEnum.success}
