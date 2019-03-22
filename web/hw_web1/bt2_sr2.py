from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    
    users = {
        "huy":         {
            "name": "Nguyen Quang Huy",
            "age": 29,
            "school": "unidentifined",
            "notion":"none",
            "story":"unknown"
        },
        "tuananh": {
            "name": "Huynh Tuan Anh",
            "age": 22,
            "school": "unidentifined",
            "notion":"none",
            "story":"unknown"
        },
        "quan": {
            "name": "Nguyễn Trần Anh Quân",
            "age": 19,
            "school": "HUST",
            "notion":"boss",
            "story":"from a royal family"
        },
        "cho_thai": {
            "name": "con 1 người quyền lực",
            "age": 19,
            "school": "LU (life university)",
            "notion": "ngáo",
            "story":'''Xuất thân trong một gia đình quyền lực.(xin phép k đc tiết lộ vì vấn đề riêng tư và sự sống còn của admin)
            có 3 thế hệ cùng chung sống trg 1 ngôi nhà và đặc biệt có 1 em gái :)). Nhưng Thái k quý nó lắm. Cuộc đời đ có j đặc biệt cho đến khi thi đại học...
            Bắt nguốn từ cấp 3 Thái k ham học mà lại ham chơi và gái gú nên điều j đến cx phải đến khi kỳ thi có lẽ là lướn nhất cuộc đời Thái đã đến: Kỳ thi THPT Quốc Gia năm 2018.
            Vì chả có cái chữ mẹ j trong đầu nên việc Thái đc 9 điểm 3 môn Toán Hóa Anh là kp điều j bất ngờ. Nhưng,
            một con người quyền lực mà t đã từ chối tiết lộ ở trên đã có 1 sự tác động "nhẹ". Sự tác động đó đã biến tổng điểm của Thái vụt lên 23,2 điểm 3 môn. Chính vì vậy anh ta đường hoàng vào đh Bách Khoa mà kp mất chút trí lực nào!
            Từ giai thoại trên người đọc cx sẽ phần nào đoán đc gia thế khủng của anh ta. 
            Tôi viết những điều này mong mng ở techkids đọc đc và dẽ chừng con người này !!'''
        },
        "dat": {
            "name": "làm j có",
            "age": "đ tính đc",
            "school": "voo hox",
            "notion": "trẻ trâu",
            "story":"known boss Quân"}
    }
    if username not in users:
        return "user profile not found"
    else :
        return render_template("info.html", nguoidung=users[username])


if __name__ == '__main__':
    app.run(debug=True)
