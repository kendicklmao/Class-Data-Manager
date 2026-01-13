#database
id_student = "1003"
id_teacher = "1004"
students = [{ #danh sách sinh viên
    "id": "25021000",
    "name": "Ngô Đại Lâm",
    "major": "Khoa Học Máy Tính",
    "class": "CS-5",
    "dob": "03/20/2030",
    "hometown": "Thanh Hóa",
    "score": (10.0, 10.0, 10.0, 10.0),
    "overall": 10.0,
}, {
    "id": "25021001",
    "name": "Phạm Viết Long",
    "major": "Khoa Học Máy Tính",
    "class": "CS-5",
    "dob": "04/01/1945",
    "hometown": "Đồng Nai",
    "score": (10.0, 10.0, 10.0, 10.0),
    "overall": 10.0,
}, {
    "id": "25021002",
    "name": "Trịnh Minh Khánh",
    "major": "Khoa Học Máy Tính",
    "class": "CS-5",
    "dob": "02/01/2023",
    "hometown": "Cà Mau",
    "score": (10.0, 10.0, 10.0, 10.0),
    "overall": 10.0,
}]

teachers = [{ #danh sách giáo viên
    "id_teacher": "1000",
    "id": "UET.MAT1050",
    "name": "Phạm Hoàng Hiệp",
    "subject": "Giải Tích 1",
    "class": ["CS-5"],
    "degree": "Giáo Sư",
}, {
    "id_teacher": "1001",
    "id": "UET.MAT1053",
    "name": "Đinh Sĩ Tiệp",
    "subject": "Đại Số Tuyến Tính",
    "class": ["CS-5"],
    "degree": "Tiến Sĩ",
}, {
    "id_teacher": "1002",
    "id": "UET.COM1050",
    "name": "Lê Nguyên Khôi",
    "subject": "Tư Duy Tính Toán",
    "class": ["CS-5"],
    "degree": "Tiến Sĩ",
}, {
    "id_teacher": "1003",
    "id": "POL1001",
    "name": "Nguyễn Thị Thu Hương",
    "subject": "Tư Tưởng Hồ Chí Minh",
    "class": ["CS-5"],
    "degree": "Không có thông tin",
}]

subjects = {
    "Giải Tích 1": "UET.MAT1050",
    "Đại Số Tuyến Tính": "UET.MAT1053",
    "Tư Duy Tính Toán": "UET.COM1050",
    "Tư Tưởng Hồ Chí Minh": "POL1001",
    "Triết Học Mác Lênin": "PHI1006",
    "Kinh Tế Chính Trị Mác Lênin": "PEC1008", 
    "Lịch Sử Đảng Cộng Sản Việt Nam": "HIS1001", 
    "Chủ Nghĩa Xã Hội Khoa Học": "PHI1002",
    "Tiếng Anh B1": "FLF1107",
    "Nhập Môn Công Nghệ Số Và Ứng Dụng Trí Tuệ Nhân Tạo": "VNU1001",
    "Nhà Nước Pháp Luật Đại Cương": "THL1057",
    "Giải Tích 2": "UET.MAT1051",
    "Vật Lý Đại Cương 1": "UET.PHY1095",
    "Vật Lý Đại Cương 2": "UET.PHY1096",
    "Xác Suất Thống Kê": "UET.MAT1052",
    "Toán Học Rời Rạc": "UET.MAT1057",
    "Cấu Trúc Dữ Liệu Và Giải Thuật": "UET.CS1058",
}

provinces = [
    "an giang",
    "bà rịa - vũng tàu",
    "bắc giang",
    "bắc kạn",
    "bạc liêu",
    "bắc ninh",
    "bến tre",
    "bình định",
    "bình dương",
    "bình phước",
    "bình thuận",
    "cà mau",
    "cần thơ",
    "cao bằng",
    "đà nẵng",
    "đắk lắk",
    "đắk nông",
    "điện biên",
    "đồng nai",
    "đồng tháp",
    "gia lai",
    "hà giang",
    "hà nam",
    "hà nội",
    "hà tĩnh",
    "hải dương",
    "hải phòng",
    "hậu giang",
    "hòa bình",
    "hưng yên",
    "khánh hòa",
    "kiên giang",
    "kon tum",
    "lai châu",
    "lâm đồng",
    "lạng sơn",
    "lào cai",
    "long an",
    "nam định",
    "nghệ an",
    "ninh bình",
    "ninh thuận",
    "phú thọ",
    "phú yên",
    "quảng bình",
    "quảng nam",
    "quảng ngãi",
    "quảng ninh",
    "quảng trị",
    "sóc trăng",
    "sơn la",
    "tây ninh",
    "thái bình",
    "thái nguyên",
    "thanh hóa",
    "thừa thiên huế",
    "tiền giang",
    "thành phố hồ chí minh",
    "trà vinh",
    "tuyên quang",
    "vĩnh long",
    "vĩnh phúc",
    "yên bái"
]

majors = [
    "Công Nghệ Thông Tin",
    "Hệ Thống Thông Tin",
    "Mạng Máy Tính Và Truyền Thông Dữ Liệu",
    "Khoa Học Máy Tính"
]

classes = {
    "IT-1": "Công Nghệ Thông Tin",
    "IT-2": "Công Nghệ Thông Tin",
    "IT-3": "Công Nghệ Thông Tin",
    "IT-4": "Công Nghệ Thông Tin",
    "IT-5": "Công Nghệ Thông Tin",
    "IT-6": "Công Nghệ Thông Tin",
    "IT-7": "Công Nghệ Thông Tin",
    "IS-1": "Hệ Thống Thông Tin",
    "IS-2": "Hệ Thống Thông Tin",
    "IS-3": "Hệ Thống Thông Tin",
    "IS-4": "Hệ Thống Thông Tin",
    "IS-5": "Hệ Thống Thông Tin",
    "CN-1": "Mạng Máy Tính Và Truyền Thông Dữ Liệu",
    "CN-2": "Mạng Máy Tính Và Truyền Thông Dữ Liệu",
    "CS-1": "Khoa Học Máy Tính",
    "CS-2": "Khoa Học Máy Tính",
    "CS-3": "Khoa Học Máy Tính",
    "CS-4": "Khoa Học Máy Tính",
    "CS-5": "Khoa Học Máy Tính",
    "CS-6": "Khoa Học Máy Tính",
    "CS-7": "Khoa Học Máy Tính",
}

list_id_students = [
    "25021000",
    "25021001",
    "25021002"
]

list_id_teachers = [
    "1000",
    "1001",
    "1002",
    "1003"
]

degrees = [
    "cử nhân",
    "thạc sĩ",
    "tiến sĩ",
    "phó giáo sư",
    "giáo sư"
]

#các chức năng
def display_id_students() -> None:#xuất danh sách mã sinh viên
    for i in list_id_students:
        print(i)
    return

def display_id_teachers() -> None:#xuất danh sách mã giảng viên
    for i in list_id_teachers:
        print(i)

def isletter(s:str) -> bool:#Kiểm tra nếu 1 xâu toàn là chữ và dấu cách
    if (len(s) == 0):
        return False
    for ch in s:
        if ch.isalpha():
            continue
        if ch == " ":
            continue
        return False
    return True

def naming(s:str) -> str:#chuẩn hóa tên riêng
    tmp = ""
    Len = len(s)
    for i in range(0, Len):
        if (i == 0):
            tmp += s[i].upper()
        elif (s[i - 1] == " "):
            tmp += s[i].upper()
        else:
            tmp += s[i]
    return tmp

def dobing(s:str) -> bool:#chuẩn hóa ngày sinh
    if ("0" <= s[0] <= "9" and "0" <= s[1] <= "9" and s[2] == "/" and "0" <= s[3] <= "9" and "0" <= s[4] <= "9" and s[5] == "/" and "0" <= s[6] <= "9" and "0" <= s[7] <= "9" and "0" <= s[8] <= "9" and "0" <= s[9] <= "9"):
        return True
    return False

def search_student_id() -> None:#tìm kiếm sinh viên theo id
    while True:
        print()
        sid = input("Nhập mã sinh viên cần tìm: ").strip()
        if (sid.isdigit() == True):
            if (sid in list_id_students):
                stu = students[int(sid) - 25021000]
                print("Mã sinh viên:", stu['id'], "\nHọ và tên:", stu['name'],"\nNgành:", stu['major'], "\nLớp:", stu['class'], "\nNgày sinh:", stu['dob'], "\nQuê quán:", stu['hometown'], "\nĐiểm:", *stu['score'], "\nTổng kết:", stu['overall'])
                return
            else:
                print()
                print("Hệ thống: Sinh viên không tồn tại hãy kiểm tra lại danh sách sinh viên")
                display_id_students()
        else:
            print()
            print("Hệ thống: Mã sinh viên chỉ có số")

def display_all() -> None:#hiển thị tất cả sinh viên
    check = False
    for stu in students:
        if (stu["id"] != "0"):
            check = True
            print("Mã sinh viên:", stu['id'], "\nHọ và tên:", stu['name'],"\nNgành:", stu['major'], "\nLớp:", stu['class'], "\nNgày sinh:", stu['dob'], "\nQuê quán:", stu['hometown'], "\nĐiểm:", *stu['score'], "\nTổng kết:", stu['overall'])    
            print()
    if (check == False):
        print()
        print("hệ thống: Không tìm thấy sinh viên nào")
    return

def nhuan(dob:str) -> bool:#kiểm tra năm nhuận
    if (int(dob) % 400 == 0 or (int(dob) % 4 == 0 and int(dob) % 100 != 0)):
        return True
    return False

def add() -> None:#thêm sinh viên mới
    while True:
        global id_student
        sid = "2502" + id_student
        print()
        Class = input("Nhập lớp của sinh viên: ").strip().upper()
        if (Class in classes):
            while True:
                try:
                    print()
                    score = tuple(map(float,input("Nhập điểm tổng kết của 4 môn sinh viên đang học theo thang 10 (Giải tích, Tư duy tính toán, Đại số tuyến tính, Tư tưởng Hồ Chí Minh) phân tách bởi dấu cách: ").split()))
                    if (len(score) == 4):
                        check = True
                        for i in score:
                            if (i < 0 or i > 10):
                                print()
                                print("Hệ thống: Điểm phải nằm trong thang 10")
                                check = False
                                break
                        if (check == True):
                            while True:
                                print()
                                name = input("Nhập họ và tên: ").strip().lower()
                                if (isletter(name) == False):
                                    print()
                                    print("hệ thống: Tên chỉ bao gồm các kí tự alphabet và có độ dài lớn hơn 0")
                                else:
                                    while True:
                                        check_date = True
                                        print()
                                        dob = input("Nhập ngày tháng năm sinh (ví dụ: mm/dd/yyyy): ").strip()
                                        if (len(dob) < 10 or len(dob) > 10):
                                            print()
                                            print("Hệ thống: Hãy nhập lại ngày tháng năm sinh theo đúng cú pháp")
                                        elif (dobing(dob) == True):
                                            if (dob[0:2] == "01"):
                                                if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                                    print()
                                                    print("Hệ thống: Tháng 1 chỉ có ngày 01 đến 31")
                                                    check_date = False
                                            elif (dob[0:2] == "02"):
                                                if (nhuan(dob[6:10]) == True):
                                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 29):
                                                        print()
                                                        print("Hệ thống: Tháng 2 chỉ có ngày 01 đến 29")
                                                        check_date = False
                                                else:
                                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 28):
                                                        print()
                                                        print("Hệ thống: Tháng 2 chỉ có ngày 01 đến 28")
                                                        check_date = False
                                            elif (dob[0:2] == "03"):
                                                if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                                    print()
                                                    print("Hệ thống: Tháng 3 chỉ có ngày 01 đến 31")
                                                    check_date = False
                                            elif (dob[0:2] == "04"):
                                                if (int(dob[3:5]) < 1 or int(dob[3:5]) > 30):
                                                    print()
                                                    print("hệ thống: Tháng 4 chỉ có ngày 01 đến 30")
                                                    check_date = False
                                            elif (dob[0:2] == "05"):
                                                if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                                    print()
                                                    print("Hệ thống: Tháng 5 chỉ có ngày 01 đến 31")
                                                    check_date = False
                                            elif (dob[0:2] == "06"):
                                                if (int(dob[3:5]) < 1 or int(dob[3:5]) > 30):
                                                    print()
                                                    print("Hệ thống: Tháng 6 chỉ có ngày 01 đến 30")
                                                    check_date = False
                                            elif (dob[0:2] == "07"):
                                                if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                                    print()
                                                    print("Hệ thống: Tháng 7 chỉ có ngày 01 đến 31")
                                                    check_date = False
                                            elif (dob[0:2] == "08"):
                                                if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                                    print()
                                                    print("Hệ thống: Tháng 8 chỉ có ngày 01 đến 31")
                                                    check_date = False
                                            elif (dob[0:2] == "09"):
                                                if (int(dob[3:5]) < 1 or int(dob[3:5]) > 30):
                                                    print()
                                                    print("Hệ thống: Tháng 9 chỉ có ngày 01 đến 30")
                                                    check_date = False
                                            elif (dob[0:2] == "10"):
                                                if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                                    print()
                                                    print("Hệ thống: Tháng 10 chỉ có ngày 01 đến 31")
                                                    check_date = False
                                            elif (dob[0:2] == "11"):
                                                if (int(dob[3:5]) < 1 or int(dob[3:5]) > 30):
                                                    print()
                                                    print("Hệ thống: Tháng 11 chỉ có ngày 01 đến 30")
                                                    check_date = False
                                            elif (dob[0:2] == "12"):
                                                if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                                    print()
                                                    print("Hệ thốngTháng 12 chỉ có ngày 01 đến 31")
                                                    check_date = False
                                            else:
                                                print()
                                                print("Hệ thống: Chỉ có tháng 01 đến tháng 12")
                                                check_date = False
                                            if (check_date == True):
                                                while True:
                                                    print()
                                                    hometown = input("Nhập quê quán: ").strip().lower()
                                                    if (hometown not in provinces):
                                                        print()
                                                        print("Hệ thống: Tỉnh/Thành phố không hợp lệ")
                                                    else:                                              
                                                        overall = round(sum(score) / 4, 1)
                                                        name = naming(name)
                                                        hometown = naming(hometown)
                                                        new_student = {
                                                            "id": sid,
                                                            "name": name,
                                                            "major": classes[Class],
                                                            "class": Class,
                                                            "dob": dob,
                                                            "hometown": hometown,
                                                            "score": score,
                                                            "overall": overall,
                                                        }
                                                        students.append(new_student)
                                                        list_id_students.append(sid)
                                                        print()
                                                        print("Mã sinh viên:", "2502" + id_student)
                                                        print("Họ và tên:", name)
                                                        print("Ngành:", classes[Class])
                                                        print("Lớp:", Class)
                                                        print("Ngày sinh:", dob)
                                                        print("Quê quán:", hometown)
                                                        print("Điểm:", *score)
                                                        print("Điểm tổng kết:", overall)
                                                        id_student = str(int(id_student) + 1)
                                                        return
                                        else:
                                            print()
                                            print("Hệ thống: Hãy nhập ngày sinh đúng cú pháp")
                    else:
                        print()
                        print("Hệ thống: Phải nhập đủ 4 điểm")                                  
                except:
                    print()
                    print("Hệ thống: Điểm phải là số thực")
        else:
            print()
            print("Hệ thống: Lớp không tồn tại hãy xem lại danh sách lớp trước khi thử lại")
            display_all_classes()

def update() -> None:#cập nhật thông tin sinh viên theo id
    while True:
        print()
        sid = input("Nhập mã sinh viên cần cập nhật: ").strip() 
        if (sid.isdigit() == True):
            if (sid in list_id_students):                            
                stu = students[int(sid) - 25021000]
                while True:
                    print("                                                 0. Về màn hình chính")
                    print("                                                 1. Họ và tên")
                    print("                                                 2. Quê quán")
                    print("                                                 3. Điểm")
                    print("                                                 4. Lớp")
                    print("                                                 5. Ngày sinh")
                    choice = input("Nhập thông tin muốn sửa từ 0 đến 5: ").strip()
                    if (choice == "1"):
                        while True:
                            print()
                            name = input("Nhập tên muốn sửa: ").strip().lower()
                            if (isletter(name) == False):
                                print()
                                print("Hệ thống: Tên chỉ bao gồm các kí tự alphabet và có độ dài lớn hơn 0")
                            else:
                                name = naming(name)
                                stu["name"] = name
                                print("Đã thành công!")
                                break
                    elif (choice == "2"):
                        while True:
                            print()
                            hometown = input("Nhập quê quán muốn sửa: ").strip().lower()
                            if (hometown not in provinces):
                                print()
                                print("hệ thống: Tỉnh/Thành phố không hợp lệ")
                            else: 
                                stu["hometown"] = naming(hometown)
                                print("Đã thành công!")
                                break                     
                    elif (choice == "3"):
                        while True:
                            try:
                                print()
                                score = tuple(map(float, input("Nhập bảng điểm mới: ").split()))
                                if (len(score) == 4):
                                    check = True
                                    for i in score:
                                        if (i < 0 or i > 10):
                                            print()
                                            print("Hệ thống: Điểm phải nằm trong thang 10")
                                            check = False
                                            break
                                    if (check == True):
                                        stu["score"] = score
                                        stu["overall"] = sum(score) / 4
                                        print("Đã thành công!")
                                        break
                                else:
                                    print()
                                    print("Hệ thống: Phải nhập đủ 4 điểm")
                            except:
                                print()
                                print("Hệ thống: Điểm phải là số thực")
                    elif (choice == "5"):
                        while True:
                            check_date = True
                            print()
                            dob = input("Nhập ngày tháng năm sinh (ví dụ: mm/dd/yyyy): ").strip()
                            if (len(dob) < 10 or len(dob) > 10):
                                print()
                                print("Hệ thống: Hãy nhập lại ngày tháng năm sinh theo đúng cú pháp")
                            elif (dobing(dob) == True):
                                if (dob[0:2] == "01"):
                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                        print()
                                        print("Hệ thống: Tháng 1 chỉ có ngày 01 đến 31")
                                        check_date = False
                                elif (dob[0:2] == "02"):
                                    if (nhuan(dob[6:10]) == False):
                                        if (int(dob[3:5]) < 1 or int(dob[3:5]) > 28):
                                            print()
                                            print("Hệt thống: Tháng 2 chỉ có ngày 01 đến 28")
                                            check_date = False
                                    else:
                                        if (int(dob[3:5]) < 1 or int(dob[3:5]) > 29):
                                            print()
                                            print("Hệ thống: Tháng 2 chỉ có ngày 01 đến 29")
                                            check_date = False
                                elif (dob[0:2] == "03"):
                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                        print()
                                        print("Hệ thống: Tháng 3 chỉ có ngày 01 đến 31")
                                        check_date = False
                                elif (dob[0:2] == "04"):
                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 30):
                                        print()
                                        print("Hệ thống: Tháng 4 chỉ có ngày 01 đến 30")
                                        check_date = False
                                elif (dob[0:2] == "05"):
                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                        print()
                                        print("Hệ thống: Tháng 5 chỉ có ngày 01 đến 31")
                                        check_date = False
                                elif (dob[0:2] == "06"):
                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 30):
                                        print()
                                        print("Hệ thống: Tháng 6 chỉ có ngày 01 đến 30")
                                        check_date = False
                                elif (dob[0:2] == "07"):
                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                        print()
                                        print("Hệ thống: Tháng 7 chỉ có ngày 01 đến 31")
                                        check_date = False
                                elif (dob[0:2] == "08"):
                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                        print()
                                        print("Hệ thống: Tháng 8 chỉ có ngày 01 đến 31")
                                        check_date = False
                                elif (dob[0:2] == "09"):
                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 30):
                                        print()
                                        print("Hệ thống: Tháng 9 chỉ có ngày 01 đến 30")
                                        check_date = False
                                elif (dob[0:2] == "10"):
                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                        print()
                                        print("Hệ thống: Tháng 10 chỉ có ngày 01 đến 31")
                                        check_date = False
                                elif (dob[0:2] == "11"):
                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 30):
                                        print()
                                        print("Hệ thống: Tháng 11 chỉ có ngày 01 đến 30")
                                        check_date = False
                                elif (dob[0:2] == "12"):
                                    if (int(dob[3:5]) < 1 or int(dob[3:5]) > 31):
                                        print()
                                        print("Hệ thống: Tháng 12 chỉ có ngày 01 đến 31")
                                        check_date = False
                                else:
                                    print()
                                    print("Hệ thống: Chỉ có tháng 01 đến tháng 12")
                                    check_date = False
                            else:
                                print()
                                print("Hệ thống: Hãy nhập ngày sinh đúng cú pháp")
                            if (check_date == True):
                                print("Đã thành công")
                                stu["dob"] = dob
                                break
                    elif (choice == "4"):
                        while True:
                            print()
                            Class = input("Nhập lớp của sinh viên: ").strip().upper()
                            if (Class not in classes):
                                print()
                                print("Hệ thống: Lớp không tồn tại hãy xem lại danh sách lớp trước khi thử lại")
                                display_all_classes()
                            else:
                                stu["class"] = Class
                                stu["major"] = classes[Class]
                                print("Đã thành công!")
                                break
                    elif (choice == "0"):
                        return
                    else:
                        print()
                        print("Hệ thống: chỉ nhập số từ 0 đến 5")
            else:
                print()
                print("Hệ thống: Không tìm thấy sinh viên hãy xem lại danh sách mã sinh viên")
                display_id_students()
        else:
            print()
            print("Hệ thống: Mã sinh viên chỉ chứa số")

def search_student_hometown() -> None:#tìm sinh viên theo quê quán
    while True:
        check = False
        print()
        hometown = input("Nhập quê quán của sinh viên: ").strip().lower()
        if (hometown in provinces):
            for stu in students:
                if (stu["id"] != "0"):
                    if stu["hometown"].lower() == hometown.lower():
                        print("Mã sinh viên:", stu['id'], "\nHọ và tên:", stu['name'],"\nNgành:", stu['major'], "\nLớp:", stu['class'], "\nNgày sinh:", stu['dob'], "\nQuê quán:", stu['hometown'], "\nĐiểm:", *stu['score'], "\nTổng kết:", stu['overall'])
                        check = True
                        print()
            if (check == False):
                print()
                print(f"Không tìm thấy sinh viên có quê quán: {naming(hometown)}")
            return
        else:
            print()
            print("Hệ thống: Tỉnh không tồn tại")

def phan_loai_sinh_vien() -> None:#thêm vào danh sách sinh viên theo học lực
    kem, yeu, trungbinh, kha, gioi, xuatsac = [], [], [], [], [], []
    for stu in students:
        if (stu["id"] != "0"):
            if 0 <= stu["overall"] < 4.0:
                kem.append(stu)
            elif 4.0 <= stu["overall"] < 5.0:
                yeu.append(stu)
            elif 5.0 <= stu["overall"] < 7.0:
                trungbinh.append(stu)
            elif 7.0 <= stu["overall"] < 8:
                kha.append(stu)
            elif 8.0 <= stu["overall"] < 9.0:
                gioi.append(stu)
            else:
                xuatsac.append(stu)
    while True:
        print()
        hoc_luc = input("Nhập học lực của sinh viên muốn liệt kê (kém, yếu, trung bình, khá, giỏi, xuất sắc): ").strip().lower()
        if (hoc_luc == "kém"):
            if (len(kem) == 0):
                print("Không có sinh viên nào học lực kém")
            else:
                for stu in kem:
                    print("Mã sinh viên:", stu['id'], "\nHọ và tên:", stu['name'],"\nNgành:", stu['major'], "\nLớp:", stu['class'], "\nNgày sinh:", stu['dob'], "\nQuê quán:", stu['hometown'], "\nĐiểm:", *stu['score'], "\nTổng kết:", stu['overall'])
                    print()
            return
        elif (hoc_luc == "yếu"):
            if (len(yeu) == 0):
                print("Không có sinh viên nào học lực yếu")
            else:
                for stu in yeu:
                    print("Mã sinh viên:", stu['id'], "\nHọ và tên:", stu['name'],"\nNgành:", stu['major'], "\nLớp:", stu['class'], "\nNgày sinh:", stu['dob'], "\nQuê quán:", stu['hometown'], "\nĐiểm:", *stu['score'], "\nTổng kết:", stu['overall'])
                    print()
            return
        elif (hoc_luc == "trung bình"):
            if (len(trungbinh) == 0):
                print("Không có sinh viên nào học lực trung bình")
            else:
                for stu in trungbinh:
                    print("Mã sinh viên:", stu['id'], "\nHọ và tên:", stu['name'],"\nNgành:", stu['major'], "\nLớp:", stu['class'], "\nNgày sinh:", stu['dob'], "\nQuê quán:", stu['hometown'], "\nĐiểm:", *stu['score'], "\nTổng kết:", stu['overall'])   
                    print()
            return
        elif (hoc_luc == "khá"):
            if (len(kha) == 0):
                print("Không có sinh viên nào học lực khá")
            else:
                for stu in kha:
                    print("Mã sinh viên:", stu['id'], "\nHọ và tên:", stu['name'],"\nNgành:", stu['major'], "\nLớp:", stu['class'], "\nNgày sinh:", stu['dob'], "\nQuê quán:", stu['hometown'], "\nĐiểm:", *stu['score'], "\nTổng kết:", stu['overall'])
                    print()
            return
        elif (hoc_luc == "giỏi"):
            if (len(gioi) == 0):
                print("Không có sinh viên nào học lực giỏi")
            else:
                for stu in gioi:
                    print("Mã sinh viên:", stu['id'], "\nHọ và tên:", stu['name'],"\nNgành:", stu['major'], "\nLớp:", stu['class'], "\nNgày sinh:", stu['dob'], "\nQuê quán:", stu['hometown'], "\nĐiểm:", *stu['score'], "\nTổng kết:", stu['overall']) 
                    print()
            return
        elif (hoc_luc == "xuất sắc"):
            if (len(xuatsac) == 0):
                print("Không có sinh viên nào học lực xuất sắc")
            else:
                for stu in xuatsac:
                    print("Mã sinh viên:", stu['id'], "\nHọ và tên:", stu['name'],"\nNgành:", stu['major'], "\nLớp:", stu['class'], "\nNgày sinh:", stu['dob'], "\nQuê quán:", stu['hometown'], "\nĐiểm:", *stu['score'], "\nTổng kết:", stu['overall'])
                    print()
            return
        else:
            print()
            print("Hệ thống: Hãy nhập đúng cú pháp")

def search_student_major() -> None:#tìm kiếm sinh viên theo ngành
    while True:
        check = False
        print()
        major = input("Nhập ngành của sinh viên: ").strip().lower()
        if (naming(major) in majors):
            for stu in students:
                if (stu["id"] != "0"):
                    if stu["major"].lower() == major.lower():
                        print("Mã sinh viên:", stu['id'], "\nHọ và tên:", stu['name'],"\nNgành:", stu['major'], "\nLớp:", stu['class'], "\nNgày sinh:", stu['dob'], "\nQuê quán:", stu['hometown'], "\nĐiểm:", *stu['score'], "\nTổng kết:", stu['overall'])
                        check = True
                        print()
            if (check == False):
                print()
                print(f"Không tìm thấy sinh viên khoa: {naming(major)}")
            return
        else:
            print()
            print("Hệ thống:Ngành không tồn tại hãy kiểm tra lại danh sách ngành")
            display_all_majors()

def search_student_class() -> None:#tìm kiếm sinh viên theo lớp
    while True:
        check = False
        print()
        Class = input("Nhập lớp của sinh viên: ").strip().upper()
        if (Class in classes):
            for stu in students:
                if (stu["id"] != "0"):
                    if stu["class"].lower() == Class.lower():
                        print("Mã sinh viên:", stu['id'], "\nHọ và tên:", stu['name'],"\nNgành:", stu['major'], "\nLớp:", stu['class'], "\nNgày sinh:", stu['dob'], "\nQuê quán:", stu['hometown'], "\nĐiểm:", *stu['score'], "\nTổng kết:", stu['overall'])
                        check = True
                        print()
            if (check == False):
                print(f"Không tìm thấy sinh viên lớp: {Class}")
            return
        else:
            print()
            print("Hệ thống: Lớp không tồn tại hãy kiểm tra lại danh sách lớp")
            display_all_classes()

def search_score() -> None:#tra cứu điểm sinh viên theo id
    while True:
        print()
        sid = input("Nhập mã sinh viên cần tra cứu: ").strip()
        if (sid.isdigit() == True):
            if (sid in list_id_students):
                stu = students[int(sid) - 25021000]
                print(stu["name"])
                print(f"Tư tưởng Hồ Chí Minh: {stu['score'][0]}")
                print(f"Tư duy tính toán: {stu['score'][1]}")
                print(f"Giải tích 1: {stu['score'][2]}")
                print(f"Đại số tuyến tính: {stu['score'][3]}")
                return
            else:
                print()
                print("Hệ thống: Không tìm thấy sinh viên hãy kiểm tra lại danh sách mã sinh viên")
                display_id_students()
        else:
            print()
            print("Hệ thống: Mã sinh viên chỉ chứa số")

def search_course() -> None:#tra cứu học phần của sinh viên theo tên học phần
    while True:
        print()
        sid = input("Nhập mã sinh viên cần tra cứu: ").strip()
        if (sid.isdigit() == True):
            if (sid in list_id_students):
                while True:
                    print()
                    course = input("Nhập tên học phần: ").strip().lower()
                    stu = students[int(sid) - 25021000]
                    check = False
                    if (naming(course) in subjects):
                        for tea in teachers:
                            if (tea["subject"].lower() == course and stu["class"] in tea["class"]):
                                check = True
                                print("Mã học phần:", tea['id'], "\nHọ và tên:", tea['name'], "\nTrình độ:", tea['degree'], "\nHọc phần:", tea['subject'], "\nLớp:", stu['class']   )
                        if (check == False):
                            print("sinh viên chưa đăng kí học phần")
                        return
                    else:
                        print()
                        print("Hệ thống: Nhập sai tên học phần hãy kiểm tra lại danh sách học phần và thử lại")
                        display_all_subjects()
            else:
                print()
                print("Hệ thống: Không tìm thấy sinh viên hãy xem lại danh sách mã sinh viên")
                display_id_students()
        else:
            print()
            print("Hệ thống: Mã sinh viên chỉ chứa số")

def update_teacher() -> None:#sửa thông tin giảng viên
    while True:
        print()
        id = input("Nhập mã giảng viên: ")
        if (id.isdigit() == True):
            if (id in list_id_teachers):
                while True:
                        print("                                                     0. Quay về màn hình chính")
                        print("                                                     1. Sửa thông tin lớp giảng dạy")
                        print("                                                     2. Sửa thông tin cá nhân")
                        choice = input("Nhập thông tin muốn sửa từ 0 đến 2: ")
                        if (choice == "1"):
                            while True:
                                print("                                                     0. Quay về")
                                print("                                                     1. Thêm lớp")
                                print("                                                     2. Xóa lớp")                    
                                choice_general = input("Chọn chức năng từ 0 đến 2: ")
                                if (choice_general == "1"):
                                    tea = teachers[int(id) - 1000]
                                    while True:   
                                        print() 
                                        Class = input("Nhập lớp muốn thêm: ").upper().strip()
                                        if (Class in classes):
                                            tea["class"].append(Class)
                                            print("Đã thành công!")
                                            break
                                        else:
                                            print()
                                            print("Hệ thống: Lớp không tồn tại hãy xem lại danh sách lớp trước khi thử lại")
                                            display_all_classes()
                                elif (choice_general == "2"):
                                    while True:
                                        tea = teachers[int(id) - 1000]
                                        print()
                                        Class = input("Nhập lớp muốn xóa: ").upper().strip()
                                        if (Class in classes):
                                            if (Class in tea["class"]):
                                                tea["class"].remove(Class)
                                                print("Đã thành công!")
                                                break
                                            else:
                                                print()
                                                print("Hệ thống: Giảng viên không dạy lớp này")
                                        else:
                                            print()
                                            print("Hệ thống: Lớp không tồn tại hãy xem lại danh sách lớp trước khi thử lại")
                                            display_all_classes()
                                elif (choice_general == "0"):
                                    break
                                else:
                                    print()
                                    print("Hệ thống: Hãy nhập số từ 0 đến 2")
                        elif (choice == "2"):
                            while True:
                                print("                                                     0. Quay về")
                                print("                                                     1. Họ và tên")
                                print("                                                     2. Học phần")
                                print("                                                     3. Học vấn")
                                choice_personal = input("Nhập thông tin muốn sửa từ 0 đến 3: ")
                                if (choice_personal == "1"):
                                    tea = teachers[int(id) - 1000]
                                    while True:
                                        print()
                                        name = input("Nhập họ tên muốn sửa: ").strip().lower()
                                        if (isletter(name) == True):
                                            name = naming(name)
                                            tea["name"] = name
                                            print("Đã thành công!")
                                            break
                                        else:
                                            print()
                                            print("Hệ thống: Tên chỉ chứa kí tự alphabet và có độ dài lớn hơn 0")
                                elif (choice_personal == "2"):
                                    while True:
                                        tea = teachers[int(id) - 1000]
                                        print()
                                        subject = input("Nhập học phần muốn sửa: ").strip().lower()
                                        if (naming(subject) in subjects):
                                            tea["subject"] = naming(subject)
                                            print("Đã thành công")
                                            break
                                        else:
                                            print()
                                            print("Hệ thống: Không tìm thấy học phần hãy xem lại danh sách học phần trước khi thử lại")
                                            display_all_subjects()
                                elif (choice_personal == "3"):
                                    tea = teachers[int(id) - 1000]
                                    while True:
                                        print()
                                        degree = input("Nhập trình độ học vấn muốn sửa (cử nhân, thạc sĩ, tiến sĩ, phó giáo sư, giáo sư): ").strip().lower()
                                        if (degree in degrees):
                                            tea["degree"] = naming(degree)
                                            print("Đã thành công!")
                                            break
                                        else:
                                            print()
                                            print("Hệ thống: Không có trình độ học vấn này")
                                elif (choice_personal == "0"):
                                    break
                                else:
                                    print()
                                    print("Hệ thống: Hãy nhập số từ 0 đến 3")
                        elif (choice == "0"):
                            return
                        else:
                            print()
                            print("Hệ thống: Hãy nhập số từ 0 đến 2")
            else:
                print()
                print("Hệ thống: Mã giảng viên không tồn tại hãy xem lại danh sách mã giảng viên")
                display_id_teachers()
        else:
            print()
            print("Hệ thống: Mã giảng viên chỉ chứa số")

def display_all_teachers() -> None:#in ra danh sách giảng viên
    check = False
    for tea in teachers:
        if (tea["id_teacher"] != "0"):
            check = True
            print("Mã học phần:", tea['id'], "\nMã giảng viên:", tea['id_teacher'], "\nHọ và tên:", tea['name'], "\nTrình độ:", tea['degree'], "\nHọc phần:", tea['subject'], "\nLớp:", *tea["class"])
            print()
    if (check == False):
        print("Không tìm thấy giảng viên nào")
    return

def add_teacher() -> None:#thêm giảng viên mới
    global id_teacher
    id = id_teacher
    while True:
        print()
        name = input("Nhập họ và tên giảng viên: ").strip().lower()
        if (isletter(name) == False):
            print()
            print("Hệ thống: Tên chỉ chứa kí tự alphabet và có độ dài lớn hơn 0")
        else:
            while True:
                print()
                subject = input("Nhập tên môn học: ").strip().lower()
                if (naming(subject) not in subjects):
                    print()
                    print("Hệ thống: Không tìm thấy học phần hãy xem lại danh sách học phần trước khi thử lại")
                    display_all_subjects()
                else:
                    while True:
                        check = True
                        print()
                        Class = list(map(str, input("Nhập lớp giảng dạy: ").upper().split())) 
                        Class = list(set(Class))
                        for i in Class:
                            if (len(i) != 4 or i not in classes):
                                print()
                                print("Hệ thống: Lớp không tồn tại hãy xem lại danh sách lớp trước khi thử lại")
                                check = False
                                display_all_classes()
                        if (check == True):
                            while True:
                                print()
                                degree = input("Trình độ học vấn (cử nhân, thạc sĩ, tiến sĩ, phó giáo sư, giáo sư): ").strip().lower()
                                if (degree not in degrees):
                                    print()
                                    print("Hệ thống: Không tồn tại trình độ học vấn này")
                                else:
                                    id_subject = subjects[str(naming(subject))]
                                    name = naming(name)
                                    subject = naming(subject)
                                    degree = naming(degree)
                                    new_teacher = {
                                        "id_teacher": id,
                                        "id": id_subject,
                                        "name": name,
                                        "subject": subject,
                                        "class": Class,
                                        "degree": degree,
                                    }
                                    teachers.append(new_teacher)
                                    list_id_teachers.append(id_teacher)
                                    print()
                                    print("Mã giảng viên:", id_teacher)
                                    print("Mã học phần:", id_subject)
                                    print("Học phần:", subject)
                                    print("Lớp:", *Class)
                                    print("Trình độ:", degree)
                                    id_teacher = str(int(id_teacher) + 1)
                                    return
                                
def display_all_subjects() -> None:#hiển thị danh sách học phần
    for k, v in subjects.items():
        print(k, ":", v)
    return

def display_all_majors() ->None:#hiển thị danh sách ngành
    for major in majors:
        print(major)
    return

def display_all_classes() -> None:#hiển thị danh sách lớp
    for k, v in classes.items():
        print(k, ":", v)
    return

def remove_student() -> None:#xóa hồ sơ sinh viên
    while True:
        print()
        sid = input("Nhập mã sinh viên cần xóa: ").strip()
        if (sid.isdigit() == True):
            if (sid in list_id_students):
                stu = students[int(sid) - 25021000]
                while True:
                    print("                                                     Bạn có chắc muốn xóa sinh viên này không?")
                    print("Thông tin sinh viên bạn muốn xóa")
                    print("Mã sinh viên:", stu["id"], "\nHọ và tên:", stu["name"], "\nNgành:", stu["major"], "\nLớp:", stu["class"], "\nNgày sinh:", stu["dob"], "\nQuê quán:", stu["hometown"], "\nĐiểm:", *stu["score"], "\nTổng kết:", stu["overall"])
                    print("                                                     1. Có")
                    print("                                                     2. Không")
                    choice = input("Nhập lựa chọn từ 1 đến 2: ").strip()
                    if (choice == "1"):
                        students[int(sid) - 25021000] = {"id": "0"}
                        list_id_students.remove(sid)
                        print("Đã thành công!")
                        return
                    elif (choice == "2"):
                        return
                    else:
                        print()
                        print("Hệ thống: Hãy nhập số 1 hoặc 2")
            else:
                print()
                print("Hệ thống: Mã sinh viên không tồn tại hãy kiểm tra lại danh sách mã sinh viên")
                display_id_students()
        else:
            print()
            print("Hệ thống: Mã sinh viên chỉ chứa số")
        
def remove_teacher() -> None:#xóa hồ sơ giảng viên
    while True:
        print()
        id = input("Nhập mã giảng viên cần xóa: ").strip()
        if (id.isdigit() == True):
            if (id in list_id_teachers):
                tea = teachers[int(id) - 1000]
                while True:
                    print("                                                     Bạn có chắc muốn xóa giảng viên này?")
                    print("Thông tin giảng viên bạn muốn xóa")
                    print("Mã giảng viên:", tea["id_teacher"], "\nMã học phần:", tea["id"], "\nHọ và tên:", tea["name"], "\nHọc phần:", tea["subject"], "\nLớp:", *tea["class"], "\nHọc vấn:", tea["degree"])
                    print("                                                     1. Có")
                    print("                                                     2. Không")
                    choice = input("Nhập lựa chọn từ 1 đến 2: ")
                    if (choice == "1"):
                        teachers[int(id) - 1000] = {"id_teacher": "0"}
                        list_id_teachers.remove(id)
                        print("Đã thành công!")
                        return
                    elif (choice == "2"):
                        return
                    else:
                        print()
                        print("Hệ thống: Hãy nhập số từ 1 đến 2")
            else:
                print()
                print("Hệ thống: Mã giảng viên không tồn tại hãy xem lại danh sách mã giảng viên")
                display_id_teachers()
        else:
            print()
            print("Hệ thống: Mã giảng viên chỉ chứa số")

#chương trình chính
print("                                                      CLASS DATA MANAGER APP")
print("                                                                         By: Ngô Đại Lâm, Phạm Viết Long and Trịnh Minh Khánh")
while True:
    print()
    print("Hệ thống: Bạn là người dùng mới hay đã quen sử dụng nếu là mới sử dụng tôi sẽ in cho bạn xem tất cả danh sách mà bạn sẽ cần trong quá trình sử dụng")
    print("1. Tôi mới sử dụng")
    print("2. Tôi đã sử dụng quen")
    choice_check = input("Nhập lựa chọn 1 hoặc 2: ").strip()
    if (choice_check == "1"):
        print()
        print("Danh sách sinh viên")
        display_all()
        print("Danh sách giảng viên")
        display_all_teachers()
        print("Danh sách học phần")
        display_all_subjects()
        print()
        print("Danh sách ngành")
        display_all_majors()
        print()
        print("Danh sách lớp")
        display_all_classes()
        print()
        break
    elif (choice_check == "2"):
        break
    else:
        print()
        print("Hệ thống: Hãy nhập số 1 hoặc 2")

while True:
    print("                                                     0. Tắt chương trình")
    print("                                                     1. Thêm sinh viên")
    print("                                                     2. Tìm sinh viên")
    print("                                                     3. Hiển thị danh sách sinh viên")
    print("                                                     4. Cập nhật thông tin sinh viên")
    print("                                                     5. Liệt kê sinh viên theo học lực")
    print("                                                     6. Tra cứu điểm sinh viên")
    print("                                                     7. Tra cứu học phần")
    print("                                                     8. Chỉnh sửa thông tin giảng viên")
    print("                                                     9. Hiển thị danh sách giảng viên")
    print("                                                    10. Thêm giảng viên")
    print("                                                    11. Hiển thị danh sách học phần và mã học phần")
    print("                                                    12. Hiển thị danh sách các ngành")
    print("                                                    13. Hiển thị danh sách lớp")
    print("                                                    14. Xóa hồ sơ sinh viên")
    print("                                                    15. Xóa hồ sơ giảng viên")
    print()
    choice = input("Chọn chức năng từ 0 đến 15: ").strip()
    if (choice == "1"):
        add()
    elif (choice == "2"):
        while True:
            print("                                                 0. Thoát tìm kiếm")
            print("                                                 1. Tìm sinh viên theo id")
            print("                                                 2. Tìm sinh viên theo quê quán")
            print("                                                 3. Tìm sinh viên theo ngành")
            print("                                                 4. Tìm sinh viên theo lớp")
            choice_search = input("Chọn chức năng từ 0 đến 4: ").strip()
            if (choice_search == "1"):
                search_student_id()
            elif (choice_search == "2"):
                search_student_hometown()
            elif (choice_search == "3"):
                search_student_major()
            elif (choice_search == "4"):
                search_student_class()
            elif (choice_search == "0"):
                break
            else:
                print()
                print("Hệ thống: Chỉ được nhập 1 số từ 0 đến 4")
    elif (choice == "3"):
        display_all()
    elif (choice == "4"):
        update()
    elif (choice == "5"):
        phan_loai_sinh_vien()                                       
    elif (choice == "6"):
        search_score()
    elif (choice == "7"):
        search_course()
    elif (choice == "8"):
        update_teacher()
    elif (choice == "9"):
        display_all_teachers()
    elif (choice == "10"):
        add_teacher()
    elif (choice == "0"):  
        print("                                                     Bạn có chắc chắn muốn thoát không?")
        print("                                                     1. Có")
        print("                                                     2. Không")
        choice_escape = input("Nhập lựa chọn 1 hoặc 2: ")
        if (choice_escape == "1"):
            break
        elif (choice_escape == "2"):
            ...
        else:
            print("Hãy nhập số 1 hoặc 2")
    elif (choice == "11"):
        display_all_subjects()
    elif (choice == "12"):
        display_all_majors()
    elif (choice == "13"):
        display_all_classes()
    elif (choice == "14"):
        remove_student()
    elif (choice == "15"):
        remove_teacher()
    else:
        print()
        print("Hệ thống: Chỉ được nhập 1 số từ 0 đến 15")