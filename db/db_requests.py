from db.db_models import db, Dates, Requests, User
from werkzeug.datastructures import MultiDict
from hashlib import sha3_512


def conv_password(password):
    salt = "924728_PEGASUS_d_r34"
    password = salt + password
    return sha3_512(str(password).encode('utf-8')).hexdigest()


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
    date = Dates.query.filter_by(date=(str(year) + '-' + str(month) + '-' + str(day))).first()
    if date:
        req = Requests.query.filter_by(id_dates=date.id).all()
        res = []
        for r in req:
            res.append({'user': r.user, 'time': r.time, 'pers_data': r.pers_data, 'comment': r.comment})
        print(res)
        return {MessagesEnum.success: True, "requests": res}
    return {MessagesEnum.success: False}


def calendar_request_set(form: MultiDict):
    date = form.get('date')
    time = form.get('time')
    print(date, time)
    date_row = Dates.query.filter_by(date=date).first()
    if not date_row:
        date_row = Dates(date=date)
        db.session.add(date_row)
        db.session.commit()
    print(date_row.id)
    # date = Dates.query.filter_by(date=full_date_time[0]).first()
    req = Requests.query.filter_by(id_dates=date_row.id, user=form.get('user'), time=time).first()
    if req:
        return {"result": MessagesEnum.already_exists}
    req = Requests(user=form.get('user'), time=time, pers_data=form.get('link'),
                   comment=form.get('comment'), id_dates=date_row.id)
    db.session.add(req)
    db.session.commit()
    return {"result": MessagesEnum.success}


# noinspection PyArgumentList
def user_add(username: str, password: str, vk_link: str):
    new_user = User.query.filter_by(user=username).first()
    if new_user:
        return MessagesEnum.already_exists
    password = conv_password(password)
    new_user = User(user=username, password=password, pers_data=vk_link)
    db.session.add(new_user)
    db.session.commit()
    return MessagesEnum.success


def user_get(username: str, password: str):
    user = User.query.filter_by(user=username).first()
    if user:
        if user.password == conv_password(password):
            return user
    return None


def user_list_of_request(username: str):
    requests = Requests.query.filter_by(user=username).all()
    date_time = []
    for req in requests:
        date = Dates.query.filter_by(id=req.id_dates).first()
        date_time.append(date.date)
