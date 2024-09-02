class Phone:
    IMEI = None
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("1111")

class MyPhone(Phone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("2222")
        super().call_by_5g()


phone = MyPhone()
phone.call_by_5g()